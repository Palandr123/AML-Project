import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from template import template_ilo, template_assessment
from template import template as template_topics
from functools import reduce

from peft import LoraConfig, get_peft_model


def load_model(model_id=None):
    # debug output
    print(model_id)

    # load model and tokenizer
    base_model_id = (
        "google/gemma-1.1-2b-it"
        if model_id.find("2b") != -1
        else "google/gemma-1.1-7b-it"
    )
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    model = AutoModelForCausalLM.from_pretrained(
        base_model_id, quantization_config=bnb_config, device_map="auto"
    )
    if model_id.endswith("finetuned") and model_id.find("7b") == -1:
        # Load the saved parameters
        adapted_params = torch.load("src/gemma-1.1-2b-it-finetune.pth")

        config = LoraConfig(
            r=16,
            lora_alpha=64,
            target_modules=[
                "q_proj",
                "k_proj",
                "v_proj",
                "o_proj",
                "gate_proj",
                "up_proj",
                "down_proj",
                "lm_head",
            ],
            bias="none",
            lora_dropout=0.05,  # Conventional
            task_type="CAUSAL_LM",
        )

        model = get_peft_model(model, config)

        for name, param in adapted_params.items():
            target_param = dict(model.named_parameters())[name]
            with torch.no_grad():
                target_param.copy_(param)

    tokenizer = AutoTokenizer.from_pretrained(
        base_model_id,
        padding_side="left",
        add_eos_token=True,
        add_bos_token=True,
    )
    tokenizer.pad_token = tokenizer.eos_token

    model_params = {
        "max_new_tokens": 2048,
    }

    return {'model_id': model_id, 'model': model, 'tokenizer': tokenizer, 'model_params': model_params}


def generate_syllabus_single_topic(
        model_id=None,
        model=None,
        tokenizer=None,
        model_params=None,
        prompt_str=None,
):
    chat = [
        {"role": "user", "content": prompt_str},
    ]
    # model inference
    prompt = tokenizer.apply_chat_template(
        chat, tokenize=False, add_generation_prompt=True
    )
    input_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
    generated_ids = model.generate(
        input_ids=input_ids.cuda(),
        **model_params,
    )
    response = tokenizer.decode(generated_ids[0])
    answer = response[len(prompt) :]

    return {
        "model": model_id,
        "answer": answer,
    }


def generate_prompt_str(
    field_to_generate=None,
    course_title=None,
    course_description=None
):
    if field_to_generate == "Course topics":
        prompt_base = template_topics
    elif field_to_generate == "ILO":
        prompt_base = template_ilo
    elif field_to_generate == "Final Assessment":
        prompt_base = template_assessment

    prompt_str = (
        f"{prompt_base}TITLE: {course_title}\nDESCRIPTION: {course_description}\n"
    )
    if field_to_generate == "Course topics":
        prompt_str += "COURSE_TOPICS: "
    elif field_to_generate == "ILO":
        prompt_str += "INTENDED_LEARNING_OUTCOMES: "
    elif field_to_generate == "Final Assessment":
        prompt_str += "FINAL_ASSESSMENT: "

    return prompt_str


def generate_syllabus(
        model_id=None,
        model=None,
        tokenizer=None,
        model_params=None,
        field_to_generate=None,
        course_title=None,
        course_description=None
):
    # debug output
    print(model)
    print(field_to_generate)
    print(course_title)
    print(course_description)

    generated_data = []
    if field_to_generate == "All":
        for field in ["Course topics", "ILO", "Final Assessment"]:
            prompt_str = generate_prompt_str(field, course_title, course_description)
            generated_single = generate_syllabus_single_topic(model_id, model, tokenizer, model_params, prompt_str)
            generated_single[field] = generated_single["answer"]
            del generated_single["answer"]
            generated_data.append(generated_single)
            generated_data = reduce(lambda a, b: {**a, **b}, generated_data)
    else:
        prompt_str = generate_prompt_str(field_to_generate, course_title, course_description)
        generated_data = generate_syllabus_single_topic(model_id, model, tokenizer, model_params, prompt_str)
    return generated_data

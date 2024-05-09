template = """Your task is to assist syllabus creation for the courses. You are given course title TITLE, course description DESCRIPTION and prerequisites PREREQUISITES. Generate a list of appropriate course sections and topics for each section, labeled as COURSE_TOPICS,
for the given COURSE. As a reference, you are given several examples in EXAMPLES section.

EXAMPLES:

EXAMPLE 1:
TITLE: "Machine Learning"
DESCRIPTION: "This course covers the following concepts: Machine learning paradigms; Machine Learning approaches, and algorithms."
PREREQUISITES: {
    PREREQUISITE_SUBJECTS: [
      "Data Structures and Algorithms: python, numpy, basic object-oriented concepts, memory management",
      "Mathematical Analysis I",
      "Mathematical Analysis II",
      "Analytical Geometry and Linear Algebra I",
      "Analytic Geometry And Linear Algebra II"
    ],
    "PREREQUISITE_TOPICS": []
}
COURSE_TOPICS: [
            {
            "Section": "Supervised Learning",
            "Topics within the section": [
                "Introduction to Machine Learning",
                "Derivatives and Cost Function",
                "Data Pre-processing",
                "Linear Regression",
                "Multiple Linear Regression",
                "Gradient Descent",
                "Polynomial Regression",
                "Splines",
                "Bias-varaince Tradeoff",
                "Difference between classification and regression",
                "Logistic Regression",
                "Naive Bayes",
                "Bayesian Network",
                "KNN",
                "Confusion Metrics",
                "Performance Metrics",
                "Regularization",
                "Hyperplane Based Classification",
                "Perceptron Learning Algorithm",
                "Max-Margin Classification",
                "Support Vector Machines",
                "Slack Variables",
                "Lagrangian Support Vector Machines",
                "Kernel Trick"
            ]
            },
            {
            "Section": "Decision Trees and Ensemble Methods",
            "Topics within the section": [
                "Decision Trees",
                "Bagging",
                "Boosting",
                "Random Forest",
                "Adaboost"
            ]
            },
            {
            "Section": "Unsupervised Learning",
            "Topics within the section": [
                "K-means Clustering",
                "K-means++",
                "Hierarchical Clustering",
                "DBSCAN",
                "Mean-shift"
            ]
            },
            {
            "Section": "Deep Learning",
            "Topics within the section": [
                "Artificial Neural Networks",
                "Back-propagation",
                "Convolutional Neural Networks",
                "Autoencoder",
                "Variatonal Autoencoder",
                "Generative Adversairal Networks"
            ]
            }
        ]

EXAMPLE 2:
COURSE: Fundamentals of Robot Control
DESCRIPTION: This course covers the following concepts: Introductory nonlinear control over dynamic systems with the focus on robotics; Stability, pros and cons of nonlinear control systems.
PREREQUISITES: {
    "PREREQUISITE_SUBJECTS": [
        "python,",
        "numpy library,",
        "Google Colab environment",
        "Mathematical Analysis I and CSE203 — Mathematical Analysis II]: integration and differentiation, exponentials, gradient.",
        "Analytical Geometry and Linear Algebra I",
        "Analytic Geometry And Linear Algebra II: matrix multiplication, eigenvector and eigenvalue.",
        "Differential Equations: state-space representation, homogeneous and nonhomogeneous equations, general solution of linear 1st and 2nd order ODEs, stability of solutions.",
        "Linear control theory: concepts of feedback, open- and closed-loop systems, linear controllers (PD, PID)"
    ],
    "PREREQUISITE_TOPICS": []
}
COURSE_TOPICS: [
            {
            "Section": "Motion. Kinematics. Dynamics.",
            "Topics within the section": [
                "Free body motion",
                "Manipulator position and orientation",
                "Homogeneous transformations",
                "Forward and inverse kinematics",
                "Kinetic and potential energy",
                "Euler-Lagrange equations"
            ]
            },
            {
            "Section": "Linear systems. Stability",
            "Topics within the section": [
                "State-space equations",
                "Eigenvalues and eigenvectors",
                "Phase plane analysis",
                "Energy and stability",
                "Lyapunov’s direct method",
                "Lyapunov stability analysis"
            ]
            },
            {
            "Section": "Feedback control systems",
            "Topics within the section": [
                "Feedback and building control loops",
                "Stabilization and trajectory tracking",
                "Linear regulators (P, PD, PID)"
            ]
            },
            {
            "Section": "Feedback linearization",
            "Topics within the section": [
                "Joint-space inverse dynamics of serial manipulators",
                "Stabilization and trajectory tracking problems",
                "Input-state linearization"
            ]
            },
            {
            "Section": "Robust control",
            "Topics within the section": [
                "Sliding modes in dynamic systems",
                "Robust control in scalar and matrix form",
                "Stability and tuning of robust controllers",
                "Control law smoothening."
            ]
            }
        ]

EXAMPLE 3:
COURSE: Managing Software Development
DESCRIPTION: This course covers the following concepts: People Management; Processes and Software Development Life-cycles; Planning and Controlling.
PREREQUISITES: {
    "PREREQUISITE_SUBJECTS": [
        "Understanding of Agile Processes, for example SCRUM",
        "Writing 1 page essays"
    ],
    "PREREQUISITE_TOPICS": []
}
COURSE_TOPICS: [
            {
            "Section": "People Management",
            "Topics within the section": [
                "MSD Introduction",
                "OBU Case Study Discussion",
                "Managing Technical People",
                "Team formation, Decision Making and Conflict Resolution",
                "Managing Customer Expectations",
                "MCE Case Study Discussion"
            ]
            },
            {
            "Section": "Software development processes",
            "Topics within the section": [
                "Defining and measuring processes",
                "Case Study Exercise Discussion",
                "Software Development Life-cycles",
                "Process Frameworks and How to choose"
            ]
            },
            {
            "Section": "Defining project success criteria",
            "Topics within the section": [
                "Requirements Management",
                "Case Study Exercise Discussion",
                "Requirements case study/lecture",
                "Identifying and Managing Software Risk",
                "TBQ, Threshold of Success",
                "Risk statement discussion"
            ]
            },
            {
            "Section": "Planning and controlling software development projects",
            "Topics within the section": [
                "Introduction - Planning & Controlling Software Development Projects",
                "Work Breakdown Structures",
                "Estimation Methods",
                "Activity Planning",
                "Milestone Planning",
                "Release Planning",
                "Tracking Reporting & Controlling"
            ]
            }
        ]

EXAMPLE 4:
COURSE: Empirical Methods
DESCRIPTION: This course covers the following concepts: Goal-Question-Metric approach; Experimental design; Basics of statistics.
PREREQUISITES: {
    "PREREQUISITE_SUBJECTS": [],
    "PREREQUISITE_TOPICS": []
}
COURSE_TOPICS: [
            {
                "Section": "Concept of measuring",
                "Topics within the section": [
                    "Measurement: concept, definition and fundamentals of measurement",
                    "Goal-Question-Metric approach",
                    "Representational theory of measurement",
                    "Measurement scales and functions that can be applied to scales",
                    "Experimental designs"
                ]
            },
            {
                "Section": "Fundamentals of statistics",
                "Topics within the section": [
                    "Basic concepts of probability theory",
                    "Random variable and random process",
                    "Linear regression",
                    "Correlation and convolution",
                    "Moments and moment generating functions",
                    "Law of Large Numbers",
                    "Central Limit Theorem",
                    "Hypothesis testing"
                ]
            }
        ]

EXAMPLE 5:
COURSE: Sensing, Perception & Actuation
DESCRIPTION: This course covers the following concepts: Physical principles of sensors and their limitations; Measurements, Sensor Calibration, Data and Error analysis; Development of algorithms for image processing, feature extraction and object recognition; 3D Point cloud processing and scene reconstruction; Linear Kalman Filter and Sensor Fusion.
PREREQUISITES: {
    "PREREQUISITE_SUBJECTS": [
        "Physics I (Mechanics)",
        "Physics II - Electrical Engineering",
        "Mathematical Analysis I",
        "Mathematical Analysis II",
        "Analytical Geometry and Linear Algebra I",
        "Analytic Geometry And Linear Algebra II",
        "Probability And Statistics"
    ],
    "PREREQUISITE_TOPICS": []
}
COURSE_TOPICS: [
            {
                "Section": "Intro to Sensors. Data and Error Analysis",
                "Topics within the section": [
                    "Sensors’ classification and Applications",
                    "Sensors Characteristics: Dynamic range, Accuracy, Signal & Noise ratio",
                    "Error analysis: Systematic vs Statistical Errors, Accuracy and Precision, Central Limit Theorem, 3 sigma rule, outliers",
                    "Sensor calibration. Direct and indirect measurements",
                    "Introduction to Data Analysis: Linear Regression, Least-Squares Fitting, Curve fitting, and Smoothing"
                ]
            },
            {
                "Section": "Perception",
                "Topics within the section": [
                    "Image sensors: camera matrix, characteristics. Color filters.",
                    "Pinhole camera model, lenses and distortions",
                    "Camera calibration, Intrinsic and Extrinsic matrices",
                    "Video camera: CCTV, IR & thermal imaging camera, Fish eye camera",
                    "Stereo vision: Stereosystem, Stereogeometry",
                    "Image rectification, Disparity map, 3D Point Cloud from Stereo",
                    "Point clouds processing, 3D reconstruction, Structure-from-Motion (SfM)",
                    "LIDAR: Laser rangefinders. Laser-camera systems. Airborne LIDAR",
                    "Depth, TOF, RGBD camera, MS Kinect: characteristics and calibration",
                    "SONAR. Piezocrystalls. Doppler effect. Doppler radar.",
                    "Acoustic sensor systems. Sound spectrogram",
                    "mm-RADAR, Long-Range RADAR, Short-range RADAR"
                ]
            },
            {
                "Section": "Sensor Fusion and Filtering",
                "Topics within the section": [
                    "Filtering",
                    "Linear Kalman Filter (KF)",
                    "Sensor Fusion",
                    "Linear Kalman Filter vs Extended KF",
                    "MoCap system",
                    "Multicamera system"
                ]
            },
            {
                "Section": "Actuators and Passive Sensors: GPS, IMU and Inertial Sensors",
                "Topics within the section": [
                    "GPS, differential GPS (dGPS)",
                    "Inertial sensors: IMU, accelerometers, gyroscopes",
                    "Magnetometers",
                    "Internal sensors: position, velocity, torque & force sensors, encoders",
                    "MEMS for robot applications",
                    "Actuators",
                    "Smart and Intelligent Sensors"
                ]
            }
        ]

EXAMPLE 6:
COURSE: Requirements Engineering
DESCRIPTION: This course covers the following concepts: Requirements elicitation; Requirements specification; Requirements prototyping and implementation; Requirements verification; Requirements traceability.
PREREQUISITES: {
    "PREREQUISITE_SUBJECTS": [
        "Basics of Software Development",
        "Basics of Software Testing",
        "Basics of Software design and Unified Modelling Language",
        "Basics of Software Development process",
        "Basics of Software Engineering"
    ],
    "PREREQUISITE_TOPICS": []
}
COURSE_TOPICS: [
            {
                "Section": "Requirements elicitation and documentation",
                "Topics within the section": [
                    "Foundations of requirements engineering",
                    "The world and the machine",
                    "Domain understanding and requirements elicitation",
                    "Questions for interviews",
                    "The requirements process",
                    "Use cases",
                    "Requirements specification and documentation"
                ]
            },
            {
                "Section": "Requirements prototyping and implementation",
                "Topics within the section": [
                    "Mapping use cases to object models",
                    "From use cases to user interface design",
                    "Activity diagrams",
                    "The psychopathology of everyday things",
                    "Seamless requirements",
                    "The anatomy of requirements"
                ]
            },
            {
                "Section": "Requirements verification and traceability",
                "Topics within the section": [
                    "Parameterized unit tests",
                    "Goal modelling",
                    "Scrum & User stories",
                    "Use case testing"
                ]
            }
        ]

Remember to use exact algorithms or topics names inside each section. Produce a similar json-like
answer with course title, description and generated course topics. Number of sections shoud be 3 or 4, with 4-5 topics within the section. Do not use repetetive topics names. Course topics should not overlap with PREREQUISITES.
Make sure that parentheses and bracketes match EXAMPLES provided.
Now generate the COURSE_TOPICS for the following:
"""


template_ilo = """Your task is to assist syllabus creation for the courses. You are given course title TITLE and 
course description DESCRIPTION. Generate a list of appropriate intended learning outcomes, labeled as INTENDED_LEARNING_OUTCOMES,
for the given COURSE. As a reference, you are given several examples in EXAMPLES section.

EXAMPLES:

EXAMPLE 1:
TITLE: "Machine Learning"
DESCRIPTION: "This course covers the following concepts: Machine learning paradigms; Machine Learning approaches, and algorithms."
INTENDED_LEARNING_OUTCOMES: {
    "What is the main purpose of this course?": "There is a growing business need of individuals skilled in artificial intelligence, data analytics, and machine learning. Therefore, the purpose of this course is to provide students with an intensive treatment of a cross-section of the key elements of machine learning, with an emphasis on implementing them in modern programming environments, and using them to solve real-world data science problems.",
    "ILOs defined at three levels": {
      "Level 1: What concepts should a student know/remember/explain?": [
        "Different learning paradigms",
        "A wide variety of learning approaches and algorithms",
        "Various learning settings",
        "Performance metrics",
        "Popular machine learning software tools"
      ],
      "Level 2: What basic practical skills should a student be able to perform?": [
        "Difference between different learning paradigms",
        "Difference between classification and regression",
        "Concept of learning theory (bias/variance tradeoffs and large margins etc.)",
        "Kernel methods",
        "Regularization",
        "Ensemble Learning",
        "Neural or Deep Learning"
      ],
      "Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?": [
        "Classification approaches to solve supervised learning problems",
        "Clustering approaches to solve unsupervised learning problems",
        "Ensemble learning to improve a model’s performance",
        "Regularization to improve a model’s generalization",
        "Deep learning algorithms to solve real-world problems"
      ]
    }
  }

EXAMPLE 2:
COURSE: Fundamentals of Robot Control
DESCRIPTION: This course covers the following concepts: Introductory nonlinear control over dynamic systems with the focus on robotics; Stability, pros and cons of nonlinear control systems.
INTENDED_LEARNING_OUTCOMES: {
    "What is the main purpose of this course?": "Control theory is an integral part of modern robotics, and there is a high chance that most students majoring in Robotics would face the problems of controlling a physical plant (a robot, manipulator, drone, autonomous vehicle) in their research and graduation work as well as their professional careers. Therefore, the main purpose of this course is to prepare the students for solving practical control problems by teaching the most fundamental approaches of nonlinear control used in modern robotics applications.",
    "ILOs defined at three levels": {
      "Level 1: What concepts should a student know/remember/explain?": [
        "Basic structure of differential equations describing motion of robotic manipulators,",
        "Motivation behind and the basic structure of feedback control systems,",
        "How to find control system’s error dynamics and methods to analyze it,",
        "General structure of linear controllers (P, PD, PID),",
        "Physical motivation behind Lyapunov stability analysis,",
        "Basic structure of robust control system."
      ],
      "Level 2: What basic practical skills should a student be able to perform?": [
        "Name the main sources of nonlinearities in physical systems,",
        "Explain the cons of applying PID controllers to nonlinear systems,",
        "Understand pros and cons of feedback linearization method,",
        "Name pros and cons of robust control approach,",
        "Numerically solve differential equations in MATLAB environment."
      ],
      "Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?": [
        "Know how to analyze stability of physical systems with Lyapunov direct method,",
        "Design feedback linearization systems,",
        "Synthesize robust control systems and tune them,",
        "Implement nonlinear control in MATLAB environment to simulate the behavior of multi-DOF robotic systems."
      ]
    }
  }

EXAMPLE 3:
COURSE: Managing Software Development
DESCRIPTION: This course covers the following concepts: People Management; Processes and Software Development Life-cycles; Planning and Controlling.
INTENDED_LEARNING_OUTCOMES: {
    "What is the main purpose of this course?": "CIA course serves as kick-start for the security and network engineering Masters program. Before diving into the depth of the topics, the students must know preliminary concepts related to computer networks services and applications therein. This course is designed to cover the basic services offered by the Internet including operating systems and computer architecture. The concepts from this course will be used throughout the course of whole masters. More precisely, this course will cover the basic computer architecture and assembly language programming, Domain Name Services (DNS), DNSSec, email, web, directories, and disks. This course will also cover protocols and ABNF. The theory part will strengthen the theoretical aspects of the concepts whereas the lab exercises will provide the students with the opportunity to have hands-on experience of the ideas they learnt in the lectures.",
    "ILOs defined at three levels": {
      "Level 1: What concepts should a student know/remember/explain?": [
        "Identify different Internet applications and understand their working principles from the protocols point of view",
        "Demonstrate the acquired knowledge and skills in classical internet applications including DNS, Email, and Directory services.",
        "Able to write regular expressions and context-free grammar that are essential in Internet applications and information exchange through the networks",
        "Able to partition disks and remember the booting principles as well as secure booting"
      ],
      "Level 2: What basic practical skills should a student be able to perform?": [
        "Demonstrate knowledge and skills to use web services",
        "Demonstrate the essential knowledge of disks and calculate particular locations/addresses in disks",
        "Reason about problems in the current DNS and the need to upgrade to DNSSEC and DNS over HTTPS",
        "Demonstrate the knowledge of email and other services configuration"
      ],
      "Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?": [
        "Install, Configure, update, and manage DNS services over a network",
        "Configure, maintain, and update the secure DNS over a network",
        "Update, add, and delete records in DNS",
        "Configure a secure mail server and maintain it",
        "Get hands-on experience of the afore-mentioned technologies on their own servers."
      ]
    }
  }

EXAMPLE 4:
COURSE: Empirical Methods
DESCRIPTION: This course covers the following concepts: Goal-Question-Metric approach; Experimental design; Basics of statistics.
INTENDED_LEARNING_OUTCOMES: {
    "What is the main purpose of this course?": "The main purpose of this course is to present the fundamentals of empirical methods and fundamental statistics to the future software engineers and data scientists, on one side providing the scientific fundamentals of the disciplines, and on the other anchoring the theoretical concepts on practices coming from the world of software development and engineering. As a side product, the course also refreshes the basics of statistics, providing the basis for more advanced statistical courses in the following semester(s) of study.",
    "ILOs defined at three levels": {
      "Level 1: What concepts should a student know/remember/explain?": [
        "Remember the fundamentals of statistics and probability theory",
        "Remember the basic models for experimentation and quasi-experimentation",
        "Remember the specifics and purpose of different measurement scales",
        "Distinguish between random variable and random process",
        "Explain the difference between the correlation and causation"
      ],
      "Level 2: What basic practical skills should a student be able to perform?": [
        "the value of experimentation for software engineers and data scientists",
        "the basic concepts of an hypothesis",
        "the concept of correlation",
        "the fundamental laws in statistics",
        "the concept of Goal-Question-Metric approach"
      ],
      "Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?": [
        "Apply Goal-Question-Metric approach in practice",
        "Apply the fundamental principles of experimental design",
        "Apply reduction to quasi-experimentation experimental design",
        "Apply statistics and probability theory in practice",
        "Apply hypothesis testing technique in software analysis"
      ]
    }
  }

EXAMPLE 5:
COURSE: Sensing, Perception & Actuation
DESCRIPTION: This course covers the following concepts: Physical principles of sensors and their limitations; Measurements, Sensor Calibration, Data and Error analysis; Development of algorithms for image processing, feature extraction and object recognition; 3D Point cloud processing and scene reconstruction; Linear Kalman Filter and Sensor Fusion.
INTENDED_LEARNING_OUTCOMES: {
    "What is the main purpose of this course?": "One of the most important tasks of an autonomous system of any kind is to acquire knowledge about its environment. This is done by taking measurements using various sensors and then extracting meaningful information from those measurements. In this course we present the most common sensors used in mobile robots and autonomous systems and then discuss strategies for extracting information from the sensors.",
    "ILOs defined at three levels": {
      "Level 1: What concepts should a student know/remember/explain?": [
        "familiar with physical and sensing principles for Camera, Stereo vision, LIDAR, SONAR, Time-of-Flight camera, GPS, actuators, inertial and internal sensors",
        "acquainted with measurements and error analysis, data analysis, and sensor calibration",
        "familiar with triangulation principle, basics of image and point cloud processing methods"
      ],
      "Level 2: What basic practical skills should a student be able to perform?": [
        "Understand how to remove systematic error and how to decrease statistical error",
        "Recover depth information from stereo vision, structure-from-light and TOF cameras",
        "Explain how Linear Regression and Least-Squares Fitting allow to minimize measurement errors"
      ],
      "Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?": [
        "Calibrate sensors to remove systematic errors",
        "Extract meaningful information from sensor’s data (features, objects, depth and accuracy information)",
        "Detect objects from 2D images",
        "Recover scene from 3D Point Cloud",
        "Filter noisy data",
        "Match models to datasets",
        "Fuse sensor’s data and apply Kalman Filtering",
        "Apply GPS, camera, LIDAR, RADAR, SONAR, IMU, Stereo camera for a mobile robot localization"
      ]
    }
  }

EXAMPLE 6:
COURSE: Requirements Engineering
DESCRIPTION: This course covers the following concepts: Requirements elicitation; Requirements specification; Requirements prototyping and implementation; Requirements verification; Requirements traceability.
INTENDED_LEARNING_OUTCOMES: {
    "What is the main purpose of this course?": "To introduce the motivation, conceptual background and terminology on which requirements engineering relies., To provide a comprehensive account of state-of-the-art techniques for requirements engineering., To let the students experience the actual requirements-caused problems faced by real software teams.",
    "ILOs defined at three levels": {
      "Level 1: What concepts should a student know/remember/explain?": [
        "System requirements",
        "Software requirements",
        "Domain knowledge",
        "Environment assumptions",
        "Environment-controlled phenomena",
        "Machine-controlled phenomena",
        "Environment-observed phenomena",
        "Machine-observed phenomena",
        "Problem space",
        "Solution space",
        "Prescriptive statements",
        "Descriptive statements",
        "Traceability links"
      ],
      "Level 2: What basic practical skills should a student be able to perform?": [
        "Difference between system and software requirements",
        "Difference between domain knowledge and environment assumptions",
        "Pairwise difference between environment- and machine-controlled (observed) phenomena",
        "Difference between the world and the machine",
        "Difference between problem and solution space",
        "Difference between prescriptive and descriptive statements",
        "Difference between vertical and horizontal traceability"
      ],
      "Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?": [
        "Requirements elicitation techniques",
        "Requirements specification techniques",
        "Prototyping and implementation techniques",
        "Negotiation techniques for modifying requirements",
        "Techniques for establishing traceability links, both vertical and horizontal",
        "Parameterized unit testing",
        "Acceptance testing"
      ]
    }
  }

Produce a similar json-like answer with course title, description and generated intended learning outcomes.
Now generate the INTENDED_LEARNING_OUTCOMES for the following:
"""


template_assessment = """Your task is to assist syllabus creation for the courses. You are given course title TITLE, course description DESCRIPTION and course topics COURSE_TOPICS. Generate a list of appropriate formative assessment and course activities, labeled as FINAL_ASSESSMENT,
for the given COURSE. As a reference, you are given several examples in EXAMPLES section.

EXAMPLES:

EXAMPLE 1:
TITLE: "Machine Learning"
DESCRIPTION: "This course covers the following concepts: Machine learning paradigms; Machine Learning approaches, and algorithms."
COURSE_TOPICS: [
    {
      "Section": "Supervised Learning",
      "Topics within the section": [
        "Introduction to Machine Learning",
        "Derivatives and Cost Function",
        "Data Pre-processing",
        "Linear Regression",
        "Multiple Linear Regression",
        "Gradient Descent",
        "Polynomial Regression",
        "Splines",
        "Bias-varaince Tradeoff",
        "Difference between classification and regression",
        "Logistic Regression",
        "Naive Bayes",
        "Bayesian Network",
        "KNN",
        "Confusion Metrics",
        "Performance Metrics",
        "Regularization",
        "Hyperplane Based Classification",
        "Perceptron Learning Algorithm",
        "Max-Margin Classification",
        "Support Vector Machines",
        "Slack Variables",
        "Lagrangian Support Vector Machines",
        "Kernel Trick"
      ]
    },
    {
      "Section": "Decision Trees and Ensemble Methods",
      "Topics within the section": [
        "Decision Trees",
        "Bagging",
        "Boosting",
        "Random Forest",
        "Adaboost"
      ]
    },
    {
      "Section": "Unsupervised Learning",
      "Topics within the section": [
        "K-means Clustering",
        "K-means++",
        "Hierarchical Clustering",
        "DBSCAN",
        "Mean-shift"
      ]
    },
    {
      "Section": "Deep Learning",
      "Topics within the section": [
        "Artificial Neural Networks",
        "Back-propagation",
        "Convolutional Neural Networks",
        "Autoencoder",
        "Variatonal Autoencoder",
        "Generative Adversairal Networks"
      ]
    }
]
FINAL_ASSESSMENT: {
      "Section 1": [
        "What does it mean for the standard least squares coefficient estimates of linear regression to be scale equivariant?",
        "Given a fitted regression model to a dataset, interpret its coefficients.",
        "Explain which regression model would be a better fit to model the relationship between response and predictor in a given data.",
        "If the number of training examples goes to infinity, how will it affect the bias and variance of a classification model?",
        "Given a two dimensional classification problem, determine if by using Logistic regression and regularization, a linear boundary can be estimated or not.",
        "Explain which classification model would be a better fit to for a given classification problem.",
        "Consider the Leave-one-out-CV error of standard two-class SVM. Argue that under a given value of slack variable, a given mathematical statement is either correct or incorrect.",
        "How does the choice of slack variable affect the bias-variance tradeoff in SVM?",
        "Explain which Kernel would be a better fit to be used in SVM for a given data."
      ],
      "Section 2": [
        "When a decision tree is grown to full depth, how does it affect tree’s bias and variance, and its response to noisy data?",
        "Argue if an ensemble model would be a better choice for a given classification problem or not.",
        "Given a particular iteration of boosting and other important information, calculate the weights of the Adaboost classifier."
      ],
      "Section 3": [
        "K-Means does not explicitly use a fitness function. What are the characteristics of the solutions that K-Means finds? Which fitness function does it implicitly minimize?",
        "Suppose we clustered a set of N data points using two different specified clustering algorithms. In both cases we obtained 5 clusters and in both cases the centers of the clusters are exactly the same. Can 3 points that are assigned to different clusters in one method be assigned to the same cluster in the other method?",
        "What are the characterics of noise points in DBSCAN?"
      ],
      "Section 4": [
        "Explain what is ReLU, what are its different variants, and what are their pros and cons?",
        "Calculate the number of parameters to be learned during training in a CNN, given all important information.",
        "Explain how a VAE can be used as a generative model."
      ]
}

EXAMPLE 2:
COURSE: Fundamentals of Robot Control
DESCRIPTION: This course covers the following concepts: Introductory nonlinear control over dynamic systems with the focus on robotics; Stability, pros and cons of nonlinear control systems.
COURSE_TOPICS: [
    {
      "Section": "Motion. Kinematics. Dynamics.",
      "Topics within the section": [
        "Free body motion",
        "Manipulator position and orientation",
        "Homogeneous transformations",
        "Forward and inverse kinematics",
        "Kinetic and potential energy",
        "Euler-Lagrange equations"
      ]
    },
    {
      "Section": "Linear systems. Stability",
      "Topics within the section": [
        "State-space equations",
        "Eigenvalues and eigenvectors",
        "Phase plane analysis",
        "Energy and stability",
        "Lyapunov’s direct method",
        "Lyapunov stability analysis"
      ]
    },
    {
      "Section": "Feedback control systems",
      "Topics within the section": [
        "Feedback and building control loops",
        "Stabilization and trajectory tracking",
        "Linear regulators (P, PD, PID)"
      ]
    },
    {
      "Section": "Feedback linearization",
      "Topics within the section": [
        "Joint-space inverse dynamics of serial manipulators",
        "Stabilization and trajectory tracking problems",
        "Input-state linearization"
      ]
    },
    {
      "Section": "Robust control",
      "Topics within the section": [
        "Sliding modes in dynamic systems",
        "Robust control in scalar and matrix form",
        "Stability and tuning of robust controllers",
        "Control law smoothening."
      ]
    }
]
"FINAL_ASSESSMENT": {
      "Section 1": [
        "What is a rotation matrix and what does it describe?",
        "How to find a homogeneous transformation matrix? How is it different from rotation matrix?",
        "What is manipulator Jacobian? How does it relate static forces and torques? How can one use the Jacobian to analyze manipulator singularities?",
        "What is physical nature of the terms of Euler-Lagrange equations of robot motion?",
        "What are the main properties of the basic terms of differential equations of motion (invertibility, positive definiteness, singularities, limits)."
      ],
      "Section 2": [
        "Evaluate stability of a linear system whose dynamics is written in the state-space form.",
        "What must be the properties of Lyapunov function candidate and its time derivative to confirm"
      ],
      "Local stability,\nGlobal stability of the system.": [
        "How to analyze system’s stability based on its phase portrait (with examples)?",
        "Describe physical motivation behind Lyapunov’s direct method and how it used to analyze stability of dynamical systems."
      ],
      "Section 3": [
        "What is the physical analog of PD-regulator in application to control over second-oder mechanical systems?",
        "For a given system described by differential equations, design a linear control system and analyze its stability.",
        "Describe pros and cons of linear controllers in application to nonlinear system control."
      ],
      "Section 4": [
        "What are the pros and cons of feedback linearization approach?",
        "Provide examples of systems (differential equations) for which feedback linearization can result in infinite control effort.",
        "What are the typical issues when applying feedback linearization approach to control over robotic manipulators?"
      ],
      "Section 5": [
        "Describe typical sources of uncertainties and parameter deviations in models of physical and mechanical systems, their typical ranges and influence on system behavior.",
        "Name pros and cons of robust control systems with and without control law smoothening.",
        "How to tune robust controller terms to compensate for system uncertainties?"
      ]
}

EXAMPLE 3:
COURSE: Managing Software Development
DESCRIPTION: This course covers the following concepts: People Management; Processes and Software Development Life-cycles; Planning and Controlling.
COURSE_TOPICS: [
    {
      "Section": "People Management",
      "Topics within the section": [
        "MSD Introduction",
        "OBU Case Study Discussion",
        "Managing Technical People",
        "Team formation, Decision Making and Conflict Resolution",
        "Managing Customer Expectations",
        "MCE Case Study Discussion"
      ]
    },
    {
      "Section": "Software development processes",
      "Topics within the section": [
        "Defining and measuring processes",
        "Case Study Exercise Discussion",
        "Software Development Life-cycles",
        "Process Frameworks and How to choose"
      ]
    },
    {
      "Section": "Defining project success criteria",
      "Topics within the section": [
        "Requirements Management",
        "Case Study Exercise Discussion",
        "Requirements case study/lecture",
        "Identifying and Managing Software Risk",
        "TBQ, Threshold of Success",
        "Risk statement discussion"
      ]
    },
    {
      "Section": "Planning and controlling software development projects",
      "Topics within the section": [
        "Introduction - Planning & Controlling Software Development Projects",
        "Work Breakdown Structures",
        "Estimation Methods",
        "Activity Planning",
        "Milestone Planning",
        "Release Planning",
        "Tracking Reporting & Controlling"
      ]
    }
]
FINAL_ASSESSMENT: {
      "Section 1": [
        "Based on a brief description of a situation on a project, give a recommendation for a leadership style. Justify.",
        "Name Tuckman’s team development stages? What activities are typical of each of those stages?",
        "Explain the Barry Boehm’s few on managing customers expectations. Give an example."
      ],
      "Section 2": [
        "Give definition of a process.",
        "What is a Software Development Life-Cycle and how does it differ from from a process?",
        "List several software development processes currently in use and give their trade-offs?",
        "Based on a brief description of a software project, what software development process would you recommend? Justify."
      ],
      "Section 3": [
        "Given a situation, identify, prioritise possible risks and discuss mitigation strategy.",
        "What is Threshold of Success and hos does it differ from Risks.",
        "Explain the condition-consequence definition for risk statements.",
        "Give an example of criticality assessment for risk statements."
      ],
      "Section 4": [
        "List several types of Work Breakdown Structures and discuss trade-offs.",
        "Apply critical path calculations to an activity graph. Give the latest start for a specific task.",
        "Define milestone planning.",
        "Explain MOSCOW method for release planning.",
        "During semester study and write a paper on a software engineering topic of your choice."
      ]
}

EXAMPLE 4:
COURSE: Dynamics Of Non Linear Robotic Systems
DESCRIPTION: This course covers the following concepts: Robotics; Robotic components; Robotic control.
COURSE_TOPICS: [
    {
      "Section": "Introduction to robotics",
      "Topics within the section": [
        "Introduction to Robotics, History of Robotics",
        "Introduction to Drones",
        "Introduction to Self driving cars",
        "Programming of Industrial Robot"
      ]
    },
    {
      "Section": "Kinematics",
      "Topics within the section": [
        "Rigid body and Homogeneous transformation",
        "Direct Kinematics",
        "Inverse Kinematics"
      ]
    },
    {
      "Section": "Differential kinematics",
      "Topics within the section": [
        "Differential kinematics",
        "Geometric calibration",
        "Trajectory Planning"
      ]
    },
    {
      "Section": "Dynamics",
      "Topics within the section": [
        "Dynamics of Rigid body",
        "Lagrange approach",
        "Newton-Euler approach"
      ]
    }
]
FINAL_ASSESSMENT: {
      "Section 1": [
        "Typical commands for programming industrial manipulator motions",
        "Types of robots and their application ares",
        "Control of self driving car"
      ],
      "Section 2": [
        "Transformation between reference frames",
        "Find Euler angles for given orientation matrix and transformation order",
        "Transformation between Cartesian and operational spaces",
        "Direct kinematic for SCARA robot",
        "Inverse kinematic for SCARA robot"
      ],
      "Section 3": [
        "Write Jacobian for Polarrobot",
        "Advantages and disadvantages parametric and non-parametric robot calibration.",
        "complete, irreducible geometric model for spherical manipulator",
        "Compute the joint trajectory q(t) from q(0) = 1 to q(2) = 4 with null initial and final velocities and accelerations. (polynomial)",
        "Obtain manipulator trajectory for given manipulator kinematics, initial and final states and velocity and acceleration limits/"
      ],
      "Section 4": [
        "Solve inverse dynamics problem for Cartesian robot",
        "Solve direct dynamics problem for RRR spherical manipulator",
        "Moving frame approach for dynamics modelling"
      ]
}

EXAMPLE 5:
COURSE: Requirements Engineering
DESCRIPTION: This course covers the following concepts: Requirements elicitation; Requirements specification; Requirements prototyping and implementation; Requirements verification; Requirements traceability.
COURSE_TOPICS: [
    {
      "Section": "Requirements elicitation and documentation",
      "Topics within the section": [
        "Foundations of requirements engineering",
        "The world and the machine",
        "Domain understanding and requirements elicitation",
        "Questions for interviews",
        "The requirements process",
        "Use cases",
        "Requirements specification and documentation"
      ]
    },
    {
      "Section": "Requirements prototyping and implementation",
      "Topics within the section": [
        "Mapping use cases to object models",
        "From use cases to user interface design",
        "Activity diagrams",
        "The psychopathology of everyday things",
        "Seamless requirements",
        "The anatomy of requirements"
      ]
    },
    {
      "Section": "Requirements verification and traceability",
      "Topics within the section": [
        "Parameterized unit tests",
        "Goal modelling",
        "Scrum & User stories",
        "Use case testing"
      ]
    }
]
FINAL_ASSESSMENT: {
      "Section 1": [
        "Present you experience of preparing and conducting the elicitation interview.",
        "How did you choose the stakeholder for interviewing?",
        "Did the interview go according to the plan?",
        "Which of the initially prepared questions you did not ask during the interview? Why?",
        "What questions you had to ask in addition to the initially prepared ones? Why?",
        "If you have been interviewed, how relevant were the interviewer’s questions?",
        "What conflicts did you have when merging the interview transcripts of your team members?",
        "How did you solve the merging conflicts?",
        "What lessons have you learned based on your experience as an interviewer and an interviewee?",
        "Present use cases constructed based on the elicited information.",
        "How do the use cases trace to the interview transcript?",
        "How does the interview transcript trace to the use cases?"
      ],
      "Section 2": [
        "Record and present a short demo of your MVP.",
        "What decisions did you have to take when implementing the MVP?",
        "How did you define your MVP?",
        "What did you have to change in the requirements document, and why?",
        "What requirements you decided to cover and not to cover in the MVP, and why?",
        "Present lessons learned from developing the MVP."
      ],
      "Section 3": [
        "Present the final system developed from the MVP received from another team.",
        "Introduce the project and its business goals.",
        "Evaluate the quality of the interview transcript.",
        "Evaluate the quality of the use cases.",
        "Evaluate the quality of the MVP and user interfaces.",
        "Reflect on the quality management process.",
        "Record and present demo of test runs.",
        "Reflect on teamwork and communication with other teams.",
        "Present lessons learned while implementing different parts of different projects coming from the other teams.",
        "Record and present demo runs of the software using the use cases as the reference.",
        "Describe strengths and weaknesses of the final implementation.",
        "Write an essay detailing your reflections on the overall course experience."
      ]
}

Produce a similar proper formatted JSON with course title, description and generated formative assessment and course activities.
Count the number of sections in COURSE_TOPICS and make sure that the number of sections in FINAL_ASSESSMENT is the same as in COURSE_TOPICS.
Make sure that the content of sections in FINAL_ASSESSMENT match the content of sections in COURSE_TOPICS. Do not generate other syllabus sections. Now generate the FINAL_ASSESSMENT in JSON format for the following:
"""
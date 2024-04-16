template = [
    {
        "role": "user",
        "content": 
        """
        Course title: Machine Learning
        Short description: This course covers the following concepts: Machine learning paradigms; Machine Learning approaches, and algorithms.
        """,
    },
    {
        "role": "assistant",
        "content": 
        """
        "Course Topics": [
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
        """,
    },
    {
        "role": "user",
        "content": 
        """
        Course title: Fundamentals of Robot Control
        Short description: This course covers the following concepts: Introductory nonlinear control over dynamic systems with the focus on robotics; Stability, pros and cons of nonlinear control systems.
        """,
    },
    {
        "role": "assistant",
        "content": 
        """
        "Course Topics": [
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
        """,
    },
    {
        "role": "user",
        "content": 
        """
        Course title: Managing Software Development
        Short description: This course covers the following concepts: People Management; Processes and Software Development Life-cycles; Planning and Controlling.
        """,
    },
    {
        "role": "assistant",
        "content": 
        """
        "Course Topics": [
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
        """,
    },
    {
        "role": "user",
        "content": 
        """
        Course title: Empirical Methods
        Short description: This course covers the following concepts: Goal-Question-Metric approach; Experimental design; Basics of statistics.
        """,
    },
    {
        "role": "assistant",
        "content": 
        """
        "Course Topics": [
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
        """,
    },
    {
        "role": "user",
        "content": 
        """
        Course title: Sensing, Perception & Actuation
        Short description: This course covers the following concepts: Physical principles of sensors and their limitations; Measurements, Sensor Calibration, Data and Error analysis; Development of algorithms for image processing, feature extraction and object recognition; 3D Point cloud processing and scene reconstruction; Linear Kalman Filter and Sensor Fusion.
        """,
    },
    {
        "role": "assistant",
        "content": 
        """
        "Course Topics": [
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
        """,
    },
    {
        "role": "user",
        "content": 
        """
        Course title: Requirements Engineering
        Short description: This course covers the following concepts: Requirements elicitation; Requirements specification; Requirements prototyping and implementation; Requirements verification; Requirements traceability.
        """,
    },
    {
        "role": "assistant",
        "content": 
        """
        "Course Topics": [
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
        """,
    },
]
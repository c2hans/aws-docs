---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/model-training-and-tuning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Model Training and Tuning
<a name="model-training-and-tuning"></a>

 Model Training and Tuning involves the selection of a ML model that is appropriate for the use case, followed by training and tuning of the ML model.

 One of the major challenges facing the public sector is the ability for team members to apply a consistent pattern or framework for working with multitudes of options that exist in this space. Different teams use different technologies and it is challenging to bring these into a uniform environment for increased visibility and tracking. For example, some teams may be using Python, while some other teams use R. Some teams may have standardized on TensorFlow, whereas other teams may have standardized on PyTorch. Challenges also exist in optimizing model training performance, input data formats, and distributed training. A significant amount of time is spent on fine tuning a model to achieve the expected performance.

 The AWS Cloud enables public sector customers to overcome challenges in model selection, training, and tuning as described in the following.

## Model Selection
<a name="model-selection"></a>

 [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides the flexibility to select from a wide number of options using a consistent underlying platform.
+  **Programming Language.** Amazon SageMaker AI notebook kernels provide the ability to use both Python, as well as R, natively. The [Amazon SageMaker AI Python SDK](https://sagemaker.readthedocs.io/en/stable/) provides open-source Python APIs and containers to train and deploy models in SageMaker. To use coding languages such as Stan or Julia, a Docker image can be created and brought into SageMaker for model training and inference (see Figure 3 below for more details on this option). To use programming languages like C\+\+ or Java, custom images on Amazon ECS/EKS can be used to perform model training.
+  **Built-in algorithms: [Amazon SageMaker AI Built-in Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)** provides several built-in algorithms covering different types of ML problems. These algorithms are already optimized for speed, scale, and accuracy. Additionally, for classification or regression with tabular data, SageMaker Autopilot can be used to automatically explore data, select algorithms relevant to the problem type, and prepare the data to facilitate model training and tuning. AutoML ranks all of the optimized models tested by their performance and finds out the best performing model. The AutoML approach is especially useful for application programmers who are new to ML.
+  **Script Mode:** For experienced ML programmers who are comfortable with using their own algorithms, Amazon SageMaker AI provides the option to write your custom code (script) in a text file with a .py extension (see Figure 1).
![Diagram showing custom training script on a supported framework](https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/images/custom-training-script.png)

 This option is known as “script mode” and the custom code can be written using any [SageMaker supported framework](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html). Code needs to be prepared and packaged in a Python file (.py extension), adding in some training environment variables as input arguments. Code that requires Python packages hosted on PyPi can be listed in a requirement.txt file and included in the code directory.
+  **Use a custom Docker image**: ML programmers may be using algorithms that are not included in a [SageMaker supported framework](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html), not hosted on PyPi, or written in a language like Stan and Julia. In these cases, the training of the algorithm and serving of the model can be done using a custom Docker image (see Figure 2 below).
![Diagram showing bring your own container](https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/images/bring-your-own-container.png)

 For more information on custom Docker images in SageMaker, see [Using Docker containers with SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html)

## Model Training
<a name="model-training"></a>

 [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides a number of built-in options for optimizing model training performance, input data formats, and distributed training.
+  **Data parallel:** ML training processes go through an entire dataset in one training cycle called an epoch. It is common to have multiple training iterations per epoch. When the training dataset is big, each epoch becomes time consuming. In these situations, SageMaker’s [distributed data parallel library](https://sagemaker.readthedocs.io/en/stable/api/training/smd_data_parallel.html) can be considered for running training jobs in parallel. The library optimizes the training job for AWS network infrastructure and Amazon EC2 instance topology, and takes advantage of gradient updates to communicate between nodes with a custom algorithm.
+  **Pipe mode:** Pipe mode accelerates the ML training process: instead of downloading data to the local Amazon EBS volume prior to starting the model training, Pipe mode streams data directly from S3 to the training algorithm while it is running. This enables the training job to start sooner, finish quicker, and need less disk space.
+  **Incremental training:** Amazon SageMaker AI supports [incremental training](https://docs.aws.amazon.com/sagemaker/latest/dg/incremental-training.html) to train a new model from an existing model artifact, to save both training time and resources. Incremental training may be considered when there are publicly available pre-trained models related to the ML use case. It can also be considered if an expanded dataset contains an underlying pattern that was not accounted in previous models, or to resume a stopped training job.
+  **Model Parallel training:** Sometimes ML models are too large to fit into GPU memory in a training process. In these situations, Amazon SageMaker AI’s [distributed model parallel library](https://sagemaker.readthedocs.io/en/stable/api/training/smd_model_parallel.html) can be used to automatically and efficiently split a model across multiple GPUs and instances and coordinate model training.

## Model Tuning
<a name="model-tuning"></a>

 [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides automatic hyperparameter tuning to find the best version of a model in an efficient manner, enabling public sector organizations to judiciously use their resource on other activities. SageMaker hyperparameter tuning runs many training jobs on a dataset using specified ranges of hyperparameters. It then chooses the hyperparameter values that result in a model that performs the best, as measured by a selected metric. The following best practices ensure a better tuning result:
+  **Limit the number of hyperparameters:** Up to 20 hyperparameters can be simultaneously specified to optimize a tuning job. However, limiting the search to a much smaller number is likely to give better results, as this can reduce the computational complexity of a hyperparameter tuning job. Moreover, a smaller number of hyperparameters provides better understanding of how a specific hyperparameter would affect the model performance.
+  **Choose hyperparameter ranges appropriately:** The range of values for hyperparameters can significantly affect the success of hyperparameter optimization. Better results are obtained by limiting the search to a small range of values. If the best metric values within a subset of the possible range are already known, consider limiting the range to that subset.
+  **Pay attention to scales for hyperparameters:** During hyperparameter tuning, SageMaker attempts to ﬁgure out if hyperparameters are log-scaled or linear-scaled. Initially, it assumes that hyperparameters are linear-scaled. If they are in fact log-scaled, it might take some time for SageMaker to discover that fact. Directly setting hyperparameters as log-scaled when they’re already known could improve hyperparameter optimization.
+  **Set the best number of concurrent training jobs:** Running more hyperparameter tuning jobs concurrently gets more work done quickly, but a tuning job improves only through successive rounds of experiments. Typically, running one training job at a time achieves the best results with the least amount of compute time.
+  **Report the wanted objective metric for tuning when the training job runs on multiple instances:** When a training job runs on multiple instances, hyperparameter tuning uses the last-reported objective metric value from all instances of that training job as the value of the objective metric for that training job. Therefore, distributed training jobs should be designed such that the objective metric reported is the one that is needed.
+  **Enable early stopping for hypermeter tuning job:** Early stopping helps reduce compute time and helps avoid overfitting the model. It stops the training jobs that a hyperparameter tuning job launches early when they are not improving significantly as measured by the objective metric.
+  **Run a warm start using previous tuning jobs:** Use a warm start for fine-tuning previous hyperparameter tuning jobs. A warm start uses information from the previous hyperparameter tuning jobs to increase the performance of the new hyperparameter tuning job by making the search for the best combination of hyperparameters more efficient.

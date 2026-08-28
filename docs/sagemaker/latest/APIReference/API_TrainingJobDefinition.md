---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobDefinition.html
---

# TrainingJobDefinition
<a name="API_TrainingJobDefinition"></a>

Defines the input needed to run a training job using the algorithm.

## Contents
<a name="API_TrainingJobDefinition_Contents"></a>

 ** InputDataConfig **   <a name="sagemaker-Type-TrainingJobDefinition-InputDataConfig"></a>
An array of `Channel` objects, each of which specifies an input source.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** OutputDataConfig **   <a name="sagemaker-Type-TrainingJobDefinition-OutputDataConfig"></a>
the path to the S3 bucket where you want to store model artifacts. SageMaker creates subfolders for the artifacts.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: Yes

 ** ResourceConfig **   <a name="sagemaker-Type-TrainingJobDefinition-ResourceConfig"></a>
The resources, including the ML compute instances and ML storage volumes, to use for model training.
Type: [ResourceConfig](API_ResourceConfig.md) object
Required: Yes

 ** StoppingCondition **   <a name="sagemaker-Type-TrainingJobDefinition-StoppingCondition"></a>
Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
To stop a job, SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: Yes

 ** TrainingInputMode **   <a name="sagemaker-Type-TrainingJobDefinition-TrainingInputMode"></a>
The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
 **Pipe mode**
If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.
 **File mode**
If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.
You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.
For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.
 **FastFile mode**
If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.
 `FastFile` mode works best when the data is read sequentially. Augmented manifest files aren't supported. The startup time is lower when there are fewer files in the S3 bucket provided.
Type: String
Valid Values: `Pipe | File | FastFile`
Required: Yes

 ** HyperParameters **   <a name="sagemaker-Type-TrainingJobDefinition-HyperParameters"></a>
The hyperparameters used for the training job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: No

## See Also
<a name="API_TrainingJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingJobDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

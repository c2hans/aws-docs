---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingJob.html
---

# ProcessingJob
<a name="API_ProcessingJob"></a>

An Amazon SageMaker processing job that is used to analyze data and evaluate models. For more information, see [Process Data and Evaluate Models](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html).

## Contents
<a name="API_ProcessingJob_Contents"></a>

 ** AppSpecification **   <a name="sagemaker-Type-ProcessingJob-AppSpecification"></a>
Configuration to run a processing job in a specified container image.
Type: [AppSpecification](API_AppSpecification.md) object
Required: No

 ** AutoMLJobArn **   <a name="sagemaker-Type-ProcessingJob-AutoMLJobArn"></a>
The Amazon Resource Name (ARN) of the AutoML job associated with this processing job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ProcessingJob-CreationTime"></a>
The time the processing job was created.
Type: Timestamp
Required: No

 ** Environment **   <a name="sagemaker-Type-ProcessingJob-Environment"></a>
Sets the environment variables in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`
Required: No

 ** ExitMessage **   <a name="sagemaker-Type-ProcessingJob-ExitMessage"></a>
A string, up to one KB in size, that contains metadata from the processing container when the processing job exits.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ExperimentConfig **   <a name="sagemaker-Type-ProcessingJob-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object
Required: No

 ** FailureReason **   <a name="sagemaker-Type-ProcessingJob-FailureReason"></a>
A string, up to one KB in size, that contains the reason a processing job failed, if it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ProcessingJob-LastModifiedTime"></a>
The time the processing job was last modified.
Type: Timestamp
Required: No

 ** MonitoringScheduleArn **   <a name="sagemaker-Type-ProcessingJob-MonitoringScheduleArn"></a>
The ARN of a monitoring schedule for an endpoint associated with this processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** NetworkConfig **   <a name="sagemaker-Type-ProcessingJob-NetworkConfig"></a>
Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.
Type: [NetworkConfig](API_NetworkConfig.md) object
Required: No

 ** ProcessingEndTime **   <a name="sagemaker-Type-ProcessingJob-ProcessingEndTime"></a>
The time that the processing job ended.
Type: Timestamp
Required: No

 ** ProcessingInputs **   <a name="sagemaker-Type-ProcessingJob-ProcessingInputs"></a>
List of input configurations for the processing job.
Type: Array of [ProcessingInput](API_ProcessingInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** ProcessingJobArn **   <a name="sagemaker-Type-ProcessingJob-ProcessingJobArn"></a>
The ARN of the processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:processing-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ProcessingJobName **   <a name="sagemaker-Type-ProcessingJob-ProcessingJobName"></a>
The name of the processing job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ProcessingJobStatus **   <a name="sagemaker-Type-ProcessingJob-ProcessingJobStatus"></a>
The status of the processing job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: No

 ** ProcessingOutputConfig **   <a name="sagemaker-Type-ProcessingJob-ProcessingOutputConfig"></a>
Configuration for uploading output from the processing container.
Type: [ProcessingOutputConfig](API_ProcessingOutputConfig.md) object
Required: No

 ** ProcessingResources **   <a name="sagemaker-Type-ProcessingJob-ProcessingResources"></a>
Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.
Type: [ProcessingResources](API_ProcessingResources.md) object
Required: No

 ** ProcessingStartTime **   <a name="sagemaker-Type-ProcessingJob-ProcessingStartTime"></a>
The time that the processing job started.
Type: Timestamp
Required: No

 ** RoleArn **   <a name="sagemaker-Type-ProcessingJob-RoleArn"></a>
The ARN of the role used to create the processing job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** StoppingCondition **   <a name="sagemaker-Type-ProcessingJob-StoppingCondition"></a>
Configures conditions under which the processing job should be stopped, such as how long the processing job has been running. After the condition is met, the processing job is stopped.
Type: [ProcessingStoppingCondition](API_ProcessingStoppingCondition.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-ProcessingJob-Tags"></a>
An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TrainingJobArn **   <a name="sagemaker-Type-ProcessingJob-TrainingJobArn"></a>
The ARN of the training job associated with this processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_ProcessingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringJobDefinition.html
---

# MonitoringJobDefinition
<a name="API_MonitoringJobDefinition"></a>

Defines the monitoring job.

## Contents
<a name="API_MonitoringJobDefinition_Contents"></a>

 ** MonitoringAppSpecification **   <a name="sagemaker-Type-MonitoringJobDefinition-MonitoringAppSpecification"></a>
Configures the monitoring job to run a specified Docker container image.
Type: [MonitoringAppSpecification](API_MonitoringAppSpecification.md) object
Required: Yes

 ** MonitoringInputs **   <a name="sagemaker-Type-MonitoringJobDefinition-MonitoringInputs"></a>
The array of inputs for the monitoring job. Currently we support monitoring an Amazon SageMaker AI Endpoint.
Type: Array of [MonitoringInput](API_MonitoringInput.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** MonitoringOutputConfig **   <a name="sagemaker-Type-MonitoringJobDefinition-MonitoringOutputConfig"></a>
The array of outputs from the monitoring job to be uploaded to Amazon S3.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object
Required: Yes

 ** MonitoringResources **   <a name="sagemaker-Type-MonitoringJobDefinition-MonitoringResources"></a>
Identifies the resources, ML compute instances, and ML storage volumes to deploy for a monitoring job. In distributed processing, you specify more than one instance.
Type: [MonitoringResources](API_MonitoringResources.md) object
Required: Yes

 ** RoleArn **   <a name="sagemaker-Type-MonitoringJobDefinition-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** BaselineConfig **   <a name="sagemaker-Type-MonitoringJobDefinition-BaselineConfig"></a>
Baseline configuration used to validate that the data conforms to the specified constraints and statistics
Type: [MonitoringBaselineConfig](API_MonitoringBaselineConfig.md) object
Required: No

 ** Environment **   <a name="sagemaker-Type-MonitoringJobDefinition-Environment"></a>
Sets the environment variables in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`
Required: No

 ** NetworkConfig **   <a name="sagemaker-Type-MonitoringJobDefinition-NetworkConfig"></a>
Specifies networking options for an monitoring job.
Type: [NetworkConfig](API_NetworkConfig.md) object
Required: No

 ** StoppingCondition **   <a name="sagemaker-Type-MonitoringJobDefinition-StoppingCondition"></a>
Specifies a time limit for how long the monitoring job is allowed to run.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object
Required: No

## See Also
<a name="API_MonitoringJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringJobDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OptimizationJobSummary.html
---

# OptimizationJobSummary
<a name="API_OptimizationJobSummary"></a>

Summarizes an optimization job by providing some of its key properties.

## Contents
<a name="API_OptimizationJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-OptimizationJobSummary-CreationTime"></a>
The time when you created the optimization job.
Type: Timestamp
Required: Yes

 ** DeploymentInstanceType **   <a name="sagemaker-Type-OptimizationJobSummary-DeploymentInstanceType"></a>
The type of instance that hosts the optimized model that you create with the optimization job.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.p6-b200.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge`
Required: Yes

 ** OptimizationJobArn **   <a name="sagemaker-Type-OptimizationJobSummary-OptimizationJobArn"></a>
The Amazon Resource Name (ARN) of the optimization job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:optimization-job/.*`
Required: Yes

 ** OptimizationJobName **   <a name="sagemaker-Type-OptimizationJobSummary-OptimizationJobName"></a>
The name that you assigned to the optimization job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** OptimizationJobStatus **   <a name="sagemaker-Type-OptimizationJobSummary-OptimizationJobStatus"></a>
The current status of the optimization job.
Type: String
Valid Values: `INPROGRESS | COMPLETED | FAILED | STARTING | STOPPING | STOPPED`
Required: Yes

 ** OptimizationTypes **   <a name="sagemaker-Type-OptimizationJobSummary-OptimizationTypes"></a>
The optimization techniques that are applied by the optimization job.
Type: Array of strings
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-OptimizationJobSummary-LastModifiedTime"></a>
The time when the optimization job was last updated.
Type: Timestamp
Required: No

 ** MaxInstanceCount **   <a name="sagemaker-Type-OptimizationJobSummary-MaxInstanceCount"></a>
The maximum number of instances to use for the optimization job.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** OptimizationEndTime **   <a name="sagemaker-Type-OptimizationJobSummary-OptimizationEndTime"></a>
The time when the optimization job finished processing.
Type: Timestamp
Required: No

 ** OptimizationStartTime **   <a name="sagemaker-Type-OptimizationJobSummary-OptimizationStartTime"></a>
The time when the optimization job started.
Type: Timestamp
Required: No

## See Also
<a name="API_OptimizationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OptimizationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OptimizationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OptimizationJobSummary)

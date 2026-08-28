---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_TargetedSentimentDetectionJobProperties.html
---

# TargetedSentimentDetectionJobProperties
<a name="API_TargetedSentimentDetectionJobProperties"></a>

Provides information about a targeted sentiment detection job.

## Contents
<a name="API_TargetedSentimentDetectionJobProperties_Contents"></a>

 ** DataAccessRoleArn **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** EndTime **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-EndTime"></a>
The time that the targeted sentiment detection job ended.
Type: Timestamp
Required: No

 ** InputDataConfig **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-InputDataConfig"></a>
The input properties for an inference job. The document reader config field applies only to non-text inputs for custom analysis.
Type: [InputDataConfig](API_InputDataConfig.md) object
Required: No

 ** JobArn **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-JobArn"></a>
The Amazon Resource Name (ARN) of the targeted sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, AWS Region, and the job ID. The format of the ARN is as follows:
 `arn:<partition>:comprehend:<region>:<account-id>:targeted-sentiment-detection-job/<job-id>`
The following is an example job ARN:
 `arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab`
Type: String
Length Constraints: Maximum length of 256.
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-]{1,64}/[a-zA-Z0-9](-*[a-zA-Z0-9])*((/dataset/[a-zA-Z0-9](-*[a-zA-Z0-9])*)|(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*))?`
Required: No

 ** JobId **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-JobId"></a>
The identifier assigned to the targeted sentiment detection job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobName **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-JobName"></a>
The name that you assigned to the targeted sentiment detection job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobStatus **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-JobStatus"></a>
The current status of the targeted sentiment detection job. If the status is `FAILED`, the `Messages` field shows the reason for the failure.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED | STOP_REQUESTED | STOPPED`
Required: No

 ** LanguageCode **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-LanguageCode"></a>
The language code of the input documents.
Type: String
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`
Required: No

 ** Message **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-Message"></a>
A description of the status of a job.
Type: String
Required: No

 ** OutputDataConfig **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-OutputDataConfig"></a>
Provides configuration parameters for the output of inference jobs.

Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: No

 ** SubmitTime **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-SubmitTime"></a>
The time that the targeted sentiment detection job was submitted for processing.
Type: Timestamp
Required: No

 ** VolumeKmsKeyId **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-VolumeKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data on the storage volume attached to the ML compute instance(s) that process the targeted sentiment detection job. The VolumeKmsKeyId can be either of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^\p{ASCII}+$`
Required: No

 ** VpcConfig **   <a name="comprehend-Type-TargetedSentimentDetectionJobProperties-VpcConfig"></a>
 Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_TargetedSentimentDetectionJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/TargetedSentimentDetectionJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/TargetedSentimentDetectionJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/TargetedSentimentDetectionJobProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

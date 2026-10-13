---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingSessionDetail.html
---

# TrainingSessionDetail
<a name="API_TrainingSessionDetail"></a>

Contains detailed information about a training session.

## Contents
<a name="API_TrainingSessionDetail_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-TrainingSessionDetail-CreationTime"></a>
The date and time that the training session was created.
Type: Timestamp
Required: Yes

 ** TrainingSessionArn **   <a name="sagemaker-Type-TrainingSessionDetail-TrainingSessionArn"></a>
The Amazon Resource Name (ARN) of the training session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:training-session/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingSessionName **   <a name="sagemaker-Type-TrainingSessionDetail-TrainingSessionName"></a>
The name of the training session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingSessionStatus **   <a name="sagemaker-Type-TrainingSessionDetail-TrainingSessionStatus"></a>
The current status of the training session.
Type: String
Valid Values: `Created | Blocked | Running | Failed | Scheduled | Stopping | Stopped | Expired | Deleting | DeletionFailed`
Required: Yes

 ** BillableTokenUsage **   <a name="sagemaker-Type-TrainingSessionDetail-BillableTokenUsage"></a>
The billable token usage for the training session.
Type: [BillableTokenUsage](API_BillableTokenUsage.md) object
Required: No

 ** EndTime **   <a name="sagemaker-Type-TrainingSessionDetail-EndTime"></a>
The date and time that the training session ended.
Type: Timestamp
Required: No

 ** ErrorDetails **   <a name="sagemaker-Type-TrainingSessionDetail-ErrorDetails"></a>
If the training session failed or is blocked, detailed error information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-TrainingSessionDetail-LastModifiedTime"></a>
The date and time that the training session was last modified.
Type: Timestamp
Required: No

 ** LastReceivedSequenceNumber **   <a name="sagemaker-Type-TrainingSessionDetail-LastReceivedSequenceNumber"></a>
The sequence number of the last training operation received by the session.
Type: Integer
Required: No

 ** LoraConfig **   <a name="sagemaker-Type-TrainingSessionDetail-LoraConfig"></a>
The Low-Rank Adaptation (LoRA) configuration for the training session.
Type: [LoraConfig](API_LoraConfig.md) object
Required: No

 ** ModelConfig **   <a name="sagemaker-Type-TrainingSessionDetail-ModelConfig"></a>
The configuration for the base model.
Type: [TrainingSessionModelConfig](API_TrainingSessionModelConfig.md) object
Required: No

 ** ModelPackageGroupArn **   <a name="sagemaker-Type-TrainingSessionDetail-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model package group where checkpoints are published.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`
Required: No

 ** OutputConfig **   <a name="sagemaker-Type-TrainingSessionDetail-OutputConfig"></a>
The output configuration for the training session.
Type: [TrainingSessionOutputConfig](API_TrainingSessionOutputConfig.md) object
Required: No

 ** RoleArn **   <a name="sagemaker-Type-TrainingSessionDetail-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the training session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Tags **   <a name="sagemaker-Type-TrainingSessionDetail-Tags"></a>
The tags associated with the training session.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-TrainingSessionDetail-VpcConfig"></a>
The Virtual Private Cloud (VPC) configuration for the training session.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_TrainingSessionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingSessionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingSessionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingSessionDetail)

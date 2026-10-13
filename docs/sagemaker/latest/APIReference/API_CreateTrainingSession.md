---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingSession.html
---

# CreateTrainingSession
<a name="API_CreateTrainingSession"></a>

Creates a training session in Amazon SageMaker. A training session provisions compute resources for fine-tuning a foundation model using Low-Rank Adaptation (LoRA). After the session is created, you can submit training operations and sample inference requests through the Amazon SageMaker Training Session Runtime API.

The following operations are related to `CreateTrainingSession`:
+  `DescribeTrainingSession`
+  `ListTrainingSessions`
+  `StopTrainingSession`
+  `DeleteTrainingSession`

## Request Syntax
<a name="API_CreateTrainingSession_RequestSyntax"></a>

```
{
   "LoraConfig": {
      "Alpha": {{number}},
      "Rank": {{number}}
   },
   "ModelConfig": {
      "AcceptEula": {{boolean}},
      "BaseModelArn": "{{string}}"
   },
   "ModelPackageGroupArn": "{{string}}",
   "OutputConfig": {
      "S3Location": {
         "KmsKeyArn": "{{string}}",
         "Path": "{{string}}"
      }
   },
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrainingSessionName": "{{string}}",
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateTrainingSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LoraConfig](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-LoraConfig"></a>
The Low-Rank Adaptation (LoRA) configuration for the training session, including the rank and alpha parameters.
Type: [LoraConfig](API_LoraConfig.md) object
Required: Yes

 ** [ModelConfig](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-ModelConfig"></a>
The configuration for the base model, including the model ARN and end-user license agreement (EULA) acceptance.
Type: [TrainingSessionModelConfig](API_TrainingSessionModelConfig.md) object
Required: Yes

 ** [ModelPackageGroupArn](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model package group where checkpoints and fine-tuned model artifacts are published.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`
Required: No

 ** [OutputConfig](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-OutputConfig"></a>
The output configuration for the training session, including the S3 location and optional encryption settings.
Type: [TrainingSessionOutputConfig](API_TrainingSessionOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker assumes to access resources on your behalf. The role must have permissions to access the output S3 path and model package group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-Tags"></a>
An array of key-value pairs to apply to the training session as tags. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrainingSessionName](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-TrainingSessionName"></a>
The name of the training session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [VpcConfig](#API_CreateTrainingSession_RequestSyntax) **   <a name="sagemaker-CreateTrainingSession-request-VpcConfig"></a>
The Virtual Private Cloud (VPC) configuration for the training session. Specify subnets and security groups to run the training session in your VPC.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateTrainingSession_ResponseSyntax"></a>

```
{
   "TrainingSessionArn": "string"
}
```

## Response Elements
<a name="API_CreateTrainingSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingSessionArn](#API_CreateTrainingSession_ResponseSyntax) **   <a name="sagemaker-CreateTrainingSession-response-TrainingSessionArn"></a>
The Amazon Resource Name (ARN) of the training session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:training-session/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateTrainingSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrainingSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateTrainingSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateTrainingSession)

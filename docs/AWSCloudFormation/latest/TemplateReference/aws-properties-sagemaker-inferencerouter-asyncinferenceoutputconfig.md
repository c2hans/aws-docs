---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencerouter-asyncinferenceoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter AsyncInferenceOutputConfig

Specifies the configuration for asynchronous inference invocation outputs.

## Syntax
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceoutputconfig-syntax.json"></a>

```json
{
  "[KmsKeyId](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-kmskeyid)" : {{String}},
  "[NotificationConfig](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-notificationconfig)" : {{AsyncInferenceNotificationConfig}},
  "[S3FailurePath](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-s3failurepath)" : {{String}},
  "[S3OutputPath](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceoutputconfig-syntax.yaml"></a>

```yaml
  [KmsKeyId](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-kmskeyid): {{String}}
  [NotificationConfig](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-notificationconfig): {{
    AsyncInferenceNotificationConfig}}
  [S3FailurePath](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-s3failurepath): {{String}}
  [S3OutputPath](#cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceoutputconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that SageMaker uses to encrypt the asynchronous inference output in Amazon S3.

*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]*$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationConfig`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-notificationconfig"></a>
Specifies the configuration for notifications of inference results for asynchronous inference.
*Required*: No
*Type*: [AsyncInferenceNotificationConfig](aws-properties-sagemaker-inferencerouter-asyncinferencenotificationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FailurePath`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-s3failurepath"></a>
The Amazon S3 location to upload failure inference responses to.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/])/?(.*)$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3OutputPath`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceoutputconfig-s3outputpath"></a>
The Amazon S3 location to upload inference responses to.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/])/?(.*)$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

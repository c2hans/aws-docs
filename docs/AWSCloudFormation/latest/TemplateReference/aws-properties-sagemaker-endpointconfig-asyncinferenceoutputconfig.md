---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig AsyncInferenceOutputConfig
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig"></a>

Specifies the configuration for asynchronous inference invocation outputs.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-kmskeyid)" : {{String}},
  "[NotificationConfig](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-notificationconfig)" : {{AsyncInferenceNotificationConfig}},
  "[S3FailurePath](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3failurepath)" : {{String}},
  "[S3OutputPath](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-kmskeyid): {{String}}
  [NotificationConfig](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-notificationconfig): {{
    AsyncInferenceNotificationConfig}}
  [S3FailurePath](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3failurepath): {{String}}
  [S3OutputPath](#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the asynchronous inference output in Amazon S3.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotificationConfig`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-notificationconfig"></a>
Specifies the configuration for notifications of inference results for asynchronous inference.
*Required*: No
*Type*: [AsyncInferenceNotificationConfig](aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3FailurePath`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3failurepath"></a>
The Amazon S3 location to upload failure inference responses to.
*Required*: No
*Type*: String
*Pattern*: `(https|s3)://([^/])/?(.*)`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputPath`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3outputpath"></a>
The Amazon S3 location to upload inference responses to.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencerouter-asyncinferencenotificationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter AsyncInferenceNotificationConfig

Specifies the configuration for notifications of inference results for asynchronous inference.

## Syntax
<a name="aws-properties-sagemaker-inferencerouter-asyncinferencenotificationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencerouter-asyncinferencenotificationconfig-syntax.json"></a>

```json
{
  "[ErrorTopic](#cfn-sagemaker-inferencerouter-asyncinferencenotificationconfig-errortopic)" : {{String}},
  "[SuccessTopic](#cfn-sagemaker-inferencerouter-asyncinferencenotificationconfig-successtopic)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencerouter-asyncinferencenotificationconfig-syntax.yaml"></a>

```yaml
  [ErrorTopic](#cfn-sagemaker-inferencerouter-asyncinferencenotificationconfig-errortopic): {{String}}
  [SuccessTopic](#cfn-sagemaker-inferencerouter-asyncinferencenotificationconfig-successtopic): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencerouter-asyncinferencenotificationconfig-properties"></a>

`ErrorTopic`  <a name="cfn-sagemaker-inferencerouter-asyncinferencenotificationconfig-errortopic"></a>
Amazon SNS topic to post a notification to when inference fails. If no topic is provided, no notification is sent on failure.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:sns:[a-z0-9-]*:[0-9]{12}:[a-zA-Z0-9_.-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessTopic`  <a name="cfn-sagemaker-inferencerouter-asyncinferencenotificationconfig-successtopic"></a>
Amazon SNS topic to post a notification to when inference completes successfully. If no topic is provided, no notification is sent on success.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:sns:[a-z0-9-]*:[0-9]{12}:[a-zA-Z0-9_.-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

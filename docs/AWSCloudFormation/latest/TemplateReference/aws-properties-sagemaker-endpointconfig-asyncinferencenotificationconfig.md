---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig AsyncInferenceNotificationConfig
<a name="aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig"></a>

Specifies the configuration for notifications of inference results for asynchronous inference.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig-syntax.json"></a>

```
{
  "[ErrorTopic](#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-errortopic)" : {{String}},
  "[IncludeInferenceResponseIn](#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-includeinferenceresponsein)" : {{[ String, ... ]}},
  "[SuccessTopic](#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-successtopic)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig-syntax.yaml"></a>

```
  [ErrorTopic](#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-errortopic): {{String}}
  [IncludeInferenceResponseIn](#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-includeinferenceresponsein): {{
    - String}}
  [SuccessTopic](#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-successtopic): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig-properties"></a>

`ErrorTopic`  <a name="cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-errortopic"></a>
Amazon SNS topic to post a notification to when an inference fails. If no topic is provided, no notification is sent on failure.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeInferenceResponseIn`  <a name="cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-includeinferenceresponsein"></a>
The Amazon SNS topics where you want the inference response to be included.
The inference response is included only if the response size is less than or equal to 128 KB.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SuccessTopic`  <a name="cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-successtopic"></a>
Amazon SNS topic to post a notification to when an inference completes successfully. If no topic is provided, no notification is sent on success.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

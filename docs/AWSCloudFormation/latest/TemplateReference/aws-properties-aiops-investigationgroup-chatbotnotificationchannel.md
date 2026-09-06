---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aiops-investigationgroup-chatbotnotificationchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AIOps::InvestigationGroup ChatbotNotificationChannel
<a name="aws-properties-aiops-investigationgroup-chatbotnotificationchannel"></a>

Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see [Getting started with Amazon Q in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html) and [Resource type defined by AWS Chatbot](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies).

## Syntax
<a name="aws-properties-aiops-investigationgroup-chatbotnotificationchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aiops-investigationgroup-chatbotnotificationchannel-syntax.json"></a>

```
{
  "[ChatConfigurationArns](#cfn-aiops-investigationgroup-chatbotnotificationchannel-chatconfigurationarns)" : {{[ String, ... ]}},
  "[SNSTopicArn](#cfn-aiops-investigationgroup-chatbotnotificationchannel-snstopicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aiops-investigationgroup-chatbotnotificationchannel-syntax.yaml"></a>

```
  [ChatConfigurationArns](#cfn-aiops-investigationgroup-chatbotnotificationchannel-chatconfigurationarns): {{
    - String}}
  [SNSTopicArn](#cfn-aiops-investigationgroup-chatbotnotificationchannel-snstopicarn): {{String}}
```

## Properties
<a name="aws-properties-aiops-investigationgroup-chatbotnotificationchannel-properties"></a>

`ChatConfigurationArns`  <a name="cfn-aiops-investigationgroup-chatbotnotificationchannel-chatconfigurationarns"></a>
Returns the Amazon Resource Name (ARN) of any third-party chat integrations configured for the account.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SNSTopicArn`  <a name="cfn-aiops-investigationgroup-chatbotnotificationchannel-snstopicarn"></a>
Returns the ARN of an Amazon SNS topic used for third-party chat integrations.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

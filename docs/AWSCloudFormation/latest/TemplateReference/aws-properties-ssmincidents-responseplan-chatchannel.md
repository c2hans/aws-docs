---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-chatchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan ChatChannel
<a name="aws-properties-ssmincidents-responseplan-chatchannel"></a>

The Amazon Q Developer in chat applications chat channel used for collaboration during an incident.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-chatchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-chatchannel-syntax.json"></a>

```
{
  "[ChatbotSns](#cfn-ssmincidents-responseplan-chatchannel-chatbotsns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-chatchannel-syntax.yaml"></a>

```
  [ChatbotSns](#cfn-ssmincidents-responseplan-chatchannel-chatbotsns): {{
    - String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-chatchannel-properties"></a>

`ChatbotSns`  <a name="cfn-ssmincidents-responseplan-chatchannel-chatbotsns"></a>
The Amazon SNS targets that Amazon Q Developer in chat applications uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel by using the Amazon SNS topics
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-sqsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule SqsParameters
<a name="aws-properties-events-rule-sqsparameters"></a>

The custom parameters for EventBridge to use for a target that is an Amazon SQS fair or FIFO queue.

## Syntax
<a name="aws-properties-events-rule-sqsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-sqsparameters-syntax.json"></a>

```
{
  "[MessageGroupId](#cfn-events-rule-sqsparameters-messagegroupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-rule-sqsparameters-syntax.yaml"></a>

```
  [MessageGroupId](#cfn-events-rule-sqsparameters-messagegroupid): {{String}}
```

## Properties
<a name="aws-properties-events-rule-sqsparameters-properties"></a>

`MessageGroupId`  <a name="cfn-events-rule-sqsparameters-messagegroupid"></a>
The ID of the message group to use as the target.
*Required*: Yes
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

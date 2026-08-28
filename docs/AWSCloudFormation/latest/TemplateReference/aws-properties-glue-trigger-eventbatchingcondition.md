---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-trigger-eventbatchingcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Trigger EventBatchingCondition
<a name="aws-properties-glue-trigger-eventbatchingcondition"></a>

Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

## Syntax
<a name="aws-properties-glue-trigger-eventbatchingcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-trigger-eventbatchingcondition-syntax.json"></a>

```
{
  "[BatchSize](#cfn-glue-trigger-eventbatchingcondition-batchsize)" : {{Integer}},
  "[BatchWindow](#cfn-glue-trigger-eventbatchingcondition-batchwindow)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-trigger-eventbatchingcondition-syntax.yaml"></a>

```
  [BatchSize](#cfn-glue-trigger-eventbatchingcondition-batchsize): {{Integer}}
  [BatchWindow](#cfn-glue-trigger-eventbatchingcondition-batchwindow): {{Integer}}
```

## Properties
<a name="aws-properties-glue-trigger-eventbatchingcondition-properties"></a>

`BatchSize`  <a name="cfn-glue-trigger-eventbatchingcondition-batchsize"></a>
Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BatchWindow`  <a name="cfn-glue-trigger-eventbatchingcondition-batchwindow"></a>
Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

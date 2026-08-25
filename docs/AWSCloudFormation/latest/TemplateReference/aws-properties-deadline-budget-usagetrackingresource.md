---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-budget-usagetrackingresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Budget UsageTrackingResource
<a name="aws-properties-deadline-budget-usagetrackingresource"></a>

The usage details of the allotted budget.

## Syntax
<a name="aws-properties-deadline-budget-usagetrackingresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-budget-usagetrackingresource-syntax.json"></a>

```
{
  "[QueueId](#cfn-deadline-budget-usagetrackingresource-queueid)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-budget-usagetrackingresource-syntax.yaml"></a>

```
  [QueueId](#cfn-deadline-budget-usagetrackingresource-queueid): {{String}}
```

## Properties
<a name="aws-properties-deadline-budget-usagetrackingresource-properties"></a>

`QueueId`  <a name="cfn-deadline-budget-usagetrackingresource-queueid"></a>
The queue ID.
*Required*: Yes
*Type*: String
*Pattern*: `^queue-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

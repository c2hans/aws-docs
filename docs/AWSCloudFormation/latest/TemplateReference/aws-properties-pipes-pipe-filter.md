---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe Filter
<a name="aws-properties-pipes-pipe-filter"></a>

Filter events using an event pattern. For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-properties-pipes-pipe-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-filter-syntax.json"></a>

```
{
  "[Pattern](#cfn-pipes-pipe-filter-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-filter-syntax.yaml"></a>

```
  [Pattern](#cfn-pipes-pipe-filter-pattern): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-filter-properties"></a>

`Pattern`  <a name="cfn-pipes-pipe-filter-pattern"></a>
The event pattern.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

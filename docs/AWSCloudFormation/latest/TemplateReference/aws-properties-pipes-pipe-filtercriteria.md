---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-filtercriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe FilterCriteria
<a name="aws-properties-pipes-pipe-filtercriteria"></a>

The collection of event patterns used to filter events.

To remove a filter, specify a `FilterCriteria` object with an empty array of `Filter` objects.

For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-properties-pipes-pipe-filtercriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-filtercriteria-syntax.json"></a>

```
{
  "[Filters](#cfn-pipes-pipe-filtercriteria-filters)" : {{[ Filter, ... ]}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-filtercriteria-syntax.yaml"></a>

```
  [Filters](#cfn-pipes-pipe-filtercriteria-filters): {{
    - Filter}}
```

## Properties
<a name="aws-properties-pipes-pipe-filtercriteria-properties"></a>

`Filters`  <a name="cfn-pipes-pipe-filtercriteria-filters"></a>
The event patterns.
*Required*: No
*Type*: Array of [Filter](aws-properties-pipes-pipe-filter.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

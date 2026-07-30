---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::GroupingConfiguration GroupingAttributeDefinition
<a name="aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition"></a>

A structure that defines how services should be grouped based on specific attributes. This includes the friendly name for the grouping, the source keys to derive values from, and an optional default value.

## Syntax
<a name="aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition-syntax.json"></a>

```
{
  "[DefaultGroupingValue](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-defaultgroupingvalue)" : {{String}},
  "[GroupingName](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-groupingname)" : {{String}},
  "[GroupingSourceKeys](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-groupingsourcekeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition-syntax.yaml"></a>

```
  [DefaultGroupingValue](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-defaultgroupingvalue): {{String}}
  [GroupingName](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-groupingname): {{String}}
  [GroupingSourceKeys](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-groupingsourcekeys): {{
    - String}}
```

## Properties
<a name="aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition-properties"></a>

`DefaultGroupingValue`  <a name="cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-defaultgroupingvalue"></a>
The default value to use for this grouping attribute when no value can be derived from the source keys. This ensures all services have a grouping value even if the source data is missing.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupingName`  <a name="cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-groupingname"></a>
The friendly name for this grouping attribute, such as `BusinessUnit` or `Environment`. This name is used to identify the grouping in the console and APIs.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupingSourceKeys`  <a name="cfn-applicationsignals-groupingconfiguration-groupingattributedefinition-groupingsourcekeys"></a>
An array of source keys used to derive the grouping attribute value from telemetry data, AWS tags, or other sources. For example, ["business\_unit", "team"] would look for values in those fields.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

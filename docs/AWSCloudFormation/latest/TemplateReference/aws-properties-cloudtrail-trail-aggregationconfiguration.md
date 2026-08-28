---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-trail-aggregationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Trail AggregationConfiguration
<a name="aws-properties-cloudtrail-trail-aggregationconfiguration"></a>

An object that contains configuration settings for aggregating events.

## Syntax
<a name="aws-properties-cloudtrail-trail-aggregationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-trail-aggregationconfiguration-syntax.json"></a>

```
{
  "[EventCategory](#cfn-cloudtrail-trail-aggregationconfiguration-eventcategory)" : {{String}},
  "[Templates](#cfn-cloudtrail-trail-aggregationconfiguration-templates)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudtrail-trail-aggregationconfiguration-syntax.yaml"></a>

```
  [EventCategory](#cfn-cloudtrail-trail-aggregationconfiguration-eventcategory): {{String}}
  [Templates](#cfn-cloudtrail-trail-aggregationconfiguration-templates): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudtrail-trail-aggregationconfiguration-properties"></a>

`EventCategory`  <a name="cfn-cloudtrail-trail-aggregationconfiguration-eventcategory"></a>
Specifies the event category for which aggregation should be performed.
*Required*: Yes
*Type*: String
*Allowed values*: `Data`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Templates`  <a name="cfn-cloudtrail-trail-aggregationconfiguration-templates"></a>
A list of aggregation templates that can be used to configure event aggregation.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

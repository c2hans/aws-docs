---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-cisscanconfiguration-time.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration Time
<a name="aws-properties-inspectorv2-cisscanconfiguration-time"></a>

The time.

## Syntax
<a name="aws-properties-inspectorv2-cisscanconfiguration-time-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-cisscanconfiguration-time-syntax.json"></a>

```
{
  "[TimeOfDay](#cfn-inspectorv2-cisscanconfiguration-time-timeofday)" : {{String}},
  "[TimeZone](#cfn-inspectorv2-cisscanconfiguration-time-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-cisscanconfiguration-time-syntax.yaml"></a>

```
  [TimeOfDay](#cfn-inspectorv2-cisscanconfiguration-time-timeofday): {{String}}
  [TimeZone](#cfn-inspectorv2-cisscanconfiguration-time-timezone): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-cisscanconfiguration-time-properties"></a>

`TimeOfDay`  <a name="cfn-inspectorv2-cisscanconfiguration-time-timeofday"></a>
The time of day in 24-hour format (00:00).
*Required*: Yes
*Type*: String
*Pattern*: `^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-inspectorv2-cisscanconfiguration-time-timezone"></a>
The timezone.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

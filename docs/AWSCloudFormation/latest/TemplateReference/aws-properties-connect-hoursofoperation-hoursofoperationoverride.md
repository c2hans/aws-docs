---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-hoursofoperation-hoursofoperationoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation HoursOfOperationOverride
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverride"></a>

Information about the hours of operations override.

## Syntax
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverride-syntax.json"></a>

```
{
  "[EffectiveFrom](#cfn-connect-hoursofoperation-hoursofoperationoverride-effectivefrom)" : {{String}},
  "[EffectiveTill](#cfn-connect-hoursofoperation-hoursofoperationoverride-effectivetill)" : {{String}},
  "[HoursOfOperationOverrideId](#cfn-connect-hoursofoperation-hoursofoperationoverride-hoursofoperationoverrideid)" : {{String}},
  "[OverrideConfig](#cfn-connect-hoursofoperation-hoursofoperationoverride-overrideconfig)" : {{[ HoursOfOperationOverrideConfig, ... ]}},
  "[OverrideDescription](#cfn-connect-hoursofoperation-hoursofoperationoverride-overridedescription)" : {{String}},
  "[OverrideName](#cfn-connect-hoursofoperation-hoursofoperationoverride-overridename)" : {{String}},
  "[OverrideType](#cfn-connect-hoursofoperation-hoursofoperationoverride-overridetype)" : {{String}},
  "[RecurrenceConfig](#cfn-connect-hoursofoperation-hoursofoperationoverride-recurrenceconfig)" : {{RecurrenceConfig}}
}
```

### YAML
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverride-syntax.yaml"></a>

```
  [EffectiveFrom](#cfn-connect-hoursofoperation-hoursofoperationoverride-effectivefrom): {{String}}
  [EffectiveTill](#cfn-connect-hoursofoperation-hoursofoperationoverride-effectivetill): {{String}}
  [HoursOfOperationOverrideId](#cfn-connect-hoursofoperation-hoursofoperationoverride-hoursofoperationoverrideid): {{String}}
  [OverrideConfig](#cfn-connect-hoursofoperation-hoursofoperationoverride-overrideconfig): {{
    - HoursOfOperationOverrideConfig}}
  [OverrideDescription](#cfn-connect-hoursofoperation-hoursofoperationoverride-overridedescription): {{String}}
  [OverrideName](#cfn-connect-hoursofoperation-hoursofoperationoverride-overridename): {{String}}
  [OverrideType](#cfn-connect-hoursofoperation-hoursofoperationoverride-overridetype): {{String}}
  [RecurrenceConfig](#cfn-connect-hoursofoperation-hoursofoperationoverride-recurrenceconfig): {{
    RecurrenceConfig}}
```

## Properties
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverride-properties"></a>

`EffectiveFrom`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-effectivefrom"></a>
The date from which the hours of operation override would be effective.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EffectiveTill`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-effectivetill"></a>
The date until the hours of operation override is effective.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HoursOfOperationOverrideId`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-hoursofoperationoverrideid"></a>
The identifier for the hours of operation override.
*Required*: No
*Type*: String
*Pattern*: `^[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideConfig`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-overrideconfig"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [HoursOfOperationOverrideConfig](aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideDescription`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-overridedescription"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideName`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-overridename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideType`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-overridetype"></a>
Whether the override will be defined as a *standard* or as a *recurring event*.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | OPEN | CLOSED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecurrenceConfig`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverride-recurrenceconfig"></a>
Configuration for a recurring event.
*Required*: No
*Type*: [RecurrenceConfig](aws-properties-connect-hoursofoperation-recurrenceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-rotation-weeklysetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Rotation WeeklySetting
<a name="aws-properties-ssmcontacts-rotation-weeklysetting"></a>

Information about rotations that recur weekly.

## Syntax
<a name="aws-properties-ssmcontacts-rotation-weeklysetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-rotation-weeklysetting-syntax.json"></a>

```
{
  "[DayOfWeek](#cfn-ssmcontacts-rotation-weeklysetting-dayofweek)" : {{String}},
  "[HandOffTime](#cfn-ssmcontacts-rotation-weeklysetting-handofftime)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-rotation-weeklysetting-syntax.yaml"></a>

```
  [DayOfWeek](#cfn-ssmcontacts-rotation-weeklysetting-dayofweek): {{String}}
  [HandOffTime](#cfn-ssmcontacts-rotation-weeklysetting-handofftime): {{String}}
```

## Properties
<a name="aws-properties-ssmcontacts-rotation-weeklysetting-properties"></a>

`DayOfWeek`  <a name="cfn-ssmcontacts-rotation-weeklysetting-dayofweek"></a>
The day of the week when weekly recurring on-call shift rotations begins.
*Required*: Yes
*Type*: String
*Allowed values*: `MON | TUE | WED | THU | FRI | SAT | SUN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HandOffTime`  <a name="cfn-ssmcontacts-rotation-weeklysetting-handofftime"></a>
The time of day when a weekly recurring on-call shift rotation begins.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

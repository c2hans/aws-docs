---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-rotation-recurrencesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Rotation RecurrenceSettings
<a name="aws-properties-ssmcontacts-rotation-recurrencesettings"></a>

Information about when an on-call rotation is in effect and how long the rotation period lasts.

## Syntax
<a name="aws-properties-ssmcontacts-rotation-recurrencesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-rotation-recurrencesettings-syntax.json"></a>

```
{
  "[DailySettings](#cfn-ssmcontacts-rotation-recurrencesettings-dailysettings)" : {{[ String, ... ]}},
  "[MonthlySettings](#cfn-ssmcontacts-rotation-recurrencesettings-monthlysettings)" : {{[ MonthlySetting, ... ]}},
  "[NumberOfOnCalls](#cfn-ssmcontacts-rotation-recurrencesettings-numberofoncalls)" : {{Integer}},
  "[RecurrenceMultiplier](#cfn-ssmcontacts-rotation-recurrencesettings-recurrencemultiplier)" : {{Integer}},
  "[ShiftCoverages](#cfn-ssmcontacts-rotation-recurrencesettings-shiftcoverages)" : {{[ ShiftCoverage, ... ]}},
  "[WeeklySettings](#cfn-ssmcontacts-rotation-recurrencesettings-weeklysettings)" : {{[ WeeklySetting, ... ]}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-rotation-recurrencesettings-syntax.yaml"></a>

```
  [DailySettings](#cfn-ssmcontacts-rotation-recurrencesettings-dailysettings): {{
    - String}}
  [MonthlySettings](#cfn-ssmcontacts-rotation-recurrencesettings-monthlysettings): {{
    - MonthlySetting}}
  [NumberOfOnCalls](#cfn-ssmcontacts-rotation-recurrencesettings-numberofoncalls): {{Integer}}
  [RecurrenceMultiplier](#cfn-ssmcontacts-rotation-recurrencesettings-recurrencemultiplier): {{Integer}}
  [ShiftCoverages](#cfn-ssmcontacts-rotation-recurrencesettings-shiftcoverages): {{
    - ShiftCoverage}}
  [WeeklySettings](#cfn-ssmcontacts-rotation-recurrencesettings-weeklysettings): {{
    - WeeklySetting}}
```

## Properties
<a name="aws-properties-ssmcontacts-rotation-recurrencesettings-properties"></a>

`DailySettings`  <a name="cfn-ssmcontacts-rotation-recurrencesettings-dailysettings"></a>
Information about on-call rotations that recur daily.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonthlySettings`  <a name="cfn-ssmcontacts-rotation-recurrencesettings-monthlysettings"></a>
Information about on-call rotations that recur monthly.
*Required*: No
*Type*: Array of [MonthlySetting](aws-properties-ssmcontacts-rotation-monthlysetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfOnCalls`  <a name="cfn-ssmcontacts-rotation-recurrencesettings-numberofoncalls"></a>
The number of contacts, or shift team members designated to be on call concurrently during a shift. For example, in an on-call schedule that contains ten contacts, a value of `2` designates that two of them are on call at any given time.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecurrenceMultiplier`  <a name="cfn-ssmcontacts-rotation-recurrencesettings-recurrencemultiplier"></a>
The number of days, weeks, or months a single rotation lasts.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShiftCoverages`  <a name="cfn-ssmcontacts-rotation-recurrencesettings-shiftcoverages"></a>
Information about the days of the week included in on-call rotation coverage.
*Required*: No
*Type*: Array of [ShiftCoverage](aws-properties-ssmcontacts-rotation-shiftcoverage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeeklySettings`  <a name="cfn-ssmcontacts-rotation-recurrencesettings-weeklysettings"></a>
Information about on-call rotations that recur weekly.
*Required*: No
*Type*: Array of [WeeklySetting](aws-properties-ssmcontacts-rotation-weeklysetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

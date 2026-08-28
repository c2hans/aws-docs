---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-hoursofoperation-overridetimeslice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation OverrideTimeSlice
<a name="aws-properties-connect-hoursofoperation-overridetimeslice"></a>

The start time or end time for an hours of operation override.

## Syntax
<a name="aws-properties-connect-hoursofoperation-overridetimeslice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-hoursofoperation-overridetimeslice-syntax.json"></a>

```
{
  "[Hours](#cfn-connect-hoursofoperation-overridetimeslice-hours)" : {{Integer}},
  "[Minutes](#cfn-connect-hoursofoperation-overridetimeslice-minutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connect-hoursofoperation-overridetimeslice-syntax.yaml"></a>

```
  [Hours](#cfn-connect-hoursofoperation-overridetimeslice-hours): {{Integer}}
  [Minutes](#cfn-connect-hoursofoperation-overridetimeslice-minutes): {{Integer}}
```

## Properties
<a name="aws-properties-connect-hoursofoperation-overridetimeslice-properties"></a>

`Hours`  <a name="cfn-connect-hoursofoperation-overridetimeslice-hours"></a>
The hours.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minutes`  <a name="cfn-connect-hoursofoperation-overridetimeslice-minutes"></a>
The minutes.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `59`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

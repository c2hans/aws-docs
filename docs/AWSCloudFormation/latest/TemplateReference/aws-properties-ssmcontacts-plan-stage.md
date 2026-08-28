---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-plan-stage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Plan Stage
<a name="aws-properties-ssmcontacts-plan-stage"></a>

A set amount of time that an escalation plan or engagement plan engages the specified contacts or contact methods.

## Syntax
<a name="aws-properties-ssmcontacts-plan-stage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-plan-stage-syntax.json"></a>

```
{
  "[DurationInMinutes](#cfn-ssmcontacts-plan-stage-durationinminutes)" : {{Integer}},
  "[Targets](#cfn-ssmcontacts-plan-stage-targets)" : {{[ Targets, ... ]}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-plan-stage-syntax.yaml"></a>

```
  [DurationInMinutes](#cfn-ssmcontacts-plan-stage-durationinminutes): {{Integer}}
  [Targets](#cfn-ssmcontacts-plan-stage-targets): {{
    - Targets}}
```

## Properties
<a name="aws-properties-ssmcontacts-plan-stage-properties"></a>

`DurationInMinutes`  <a name="cfn-ssmcontacts-plan-stage-durationinminutes"></a>
The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-ssmcontacts-plan-stage-targets"></a>
The contacts or contact methods that the escalation plan or engagement plan is engaging.
*Required*: No
*Type*: [Array](aws-properties-ssmcontacts-plan-targets.md) of [Targets](aws-properties-ssmcontacts-plan-targets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

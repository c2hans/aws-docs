---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy LastLaunched
<a name="aws-properties-imagebuilder-lifecyclepolicy-lastlaunched"></a>

Defines criteria to exclude AMIs from lifecycle actions based on the last time they were used to launch an instance.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-lastlaunched-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-lastlaunched-syntax.json"></a>

```
{
  "[Unit](#cfn-imagebuilder-lifecyclepolicy-lastlaunched-unit)" : {{String}},
  "[Value](#cfn-imagebuilder-lifecyclepolicy-lastlaunched-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-lastlaunched-syntax.yaml"></a>

```
  [Unit](#cfn-imagebuilder-lifecyclepolicy-lastlaunched-unit): {{String}}
  [Value](#cfn-imagebuilder-lifecyclepolicy-lastlaunched-value): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-lastlaunched-properties"></a>

`Unit`  <a name="cfn-imagebuilder-lifecyclepolicy-lastlaunched-unit"></a>
Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last instance launched from the AMI. For example: days, weeks, months, or years.
*Required*: Yes
*Type*: String
*Allowed values*: `DAYS | WEEKS | MONTHS | YEARS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-imagebuilder-lifecyclepolicy-lastlaunched-value"></a>
The integer number of units for the time period. For example `6` (months).
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

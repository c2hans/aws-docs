---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-limitsprofile-profilelimitvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::LimitsProfile ProfileLimitValue
<a name="aws-properties-quicksight-limitsprofile-profilelimitvalue"></a>

<a name="aws-properties-quicksight-limitsprofile-profilelimitvalue-description"></a>The `ProfileLimitValue` property type specifies Property description not available. for an [AWS::QuickSight::LimitsProfile](aws-resource-quicksight-limitsprofile.md).

## Syntax
<a name="aws-properties-quicksight-limitsprofile-profilelimitvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-limitsprofile-profilelimitvalue-syntax.json"></a>

```
{
  "[MaxValue](#cfn-quicksight-limitsprofile-profilelimitvalue-maxvalue)" : {{Number}},
  "[Unit](#cfn-quicksight-limitsprofile-profilelimitvalue-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-limitsprofile-profilelimitvalue-syntax.yaml"></a>

```
  [MaxValue](#cfn-quicksight-limitsprofile-profilelimitvalue-maxvalue): {{Number}}
  [Unit](#cfn-quicksight-limitsprofile-profilelimitvalue-unit): {{String}}
```

## Properties
<a name="aws-properties-quicksight-limitsprofile-profilelimitvalue-properties"></a>

`MaxValue`  <a name="cfn-quicksight-limitsprofile-profilelimitvalue-maxvalue"></a>
Property description not available.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-quicksight-limitsprofile-profilelimitvalue-unit"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `MB | GB | HOURS | DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

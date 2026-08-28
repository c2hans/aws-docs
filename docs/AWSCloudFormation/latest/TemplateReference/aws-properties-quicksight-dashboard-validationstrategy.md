---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-validationstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ValidationStrategy
<a name="aws-properties-quicksight-dashboard-validationstrategy"></a>

The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to `LENIENT`, validation is skipped for specific errors.

## Syntax
<a name="aws-properties-quicksight-dashboard-validationstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-validationstrategy-syntax.json"></a>

```
{
  "[Mode](#cfn-quicksight-dashboard-validationstrategy-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-validationstrategy-syntax.yaml"></a>

```
  [Mode](#cfn-quicksight-dashboard-validationstrategy-mode): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-validationstrategy-properties"></a>

`Mode`  <a name="cfn-quicksight-dashboard-validationstrategy-mode"></a>
The mode of validation for the asset to be created or updated. When you set this value to `STRICT`, strict validation for every error is enforced. When you set this value to `LENIENT`, validation is skipped for specific UI errors.
*Required*: Yes
*Type*: String
*Allowed values*: `STRICT | LENIENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

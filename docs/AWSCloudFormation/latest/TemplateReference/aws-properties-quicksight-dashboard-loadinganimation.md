---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-loadinganimation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard LoadingAnimation
<a name="aws-properties-quicksight-dashboard-loadinganimation"></a>

The configuration of loading animation in free-form layout.

## Syntax
<a name="aws-properties-quicksight-dashboard-loadinganimation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-loadinganimation-syntax.json"></a>

```
{
  "[Visibility](#cfn-quicksight-dashboard-loadinganimation-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-loadinganimation-syntax.yaml"></a>

```
  [Visibility](#cfn-quicksight-dashboard-loadinganimation-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-loadinganimation-properties"></a>

`Visibility`  <a name="cfn-quicksight-dashboard-loadinganimation-visibility"></a>
The visibility configuration of `LoadingAnimation`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

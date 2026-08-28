---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-customactionnavigationoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CustomActionNavigationOperation
<a name="aws-properties-quicksight-analysis-customactionnavigationoperation"></a>

The navigation operation that navigates between different sheets in the same analysis.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-customactionnavigationoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-customactionnavigationoperation-syntax.json"></a>

```
{
  "[LocalNavigationConfiguration](#cfn-quicksight-analysis-customactionnavigationoperation-localnavigationconfiguration)" : {{LocalNavigationConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-customactionnavigationoperation-syntax.yaml"></a>

```
  [LocalNavigationConfiguration](#cfn-quicksight-analysis-customactionnavigationoperation-localnavigationconfiguration): {{
    LocalNavigationConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-customactionnavigationoperation-properties"></a>

`LocalNavigationConfiguration`  <a name="cfn-quicksight-analysis-customactionnavigationoperation-localnavigationconfiguration"></a>
The configuration that chooses the navigation target.
*Required*: No
*Type*: [LocalNavigationConfiguration](aws-properties-quicksight-analysis-localnavigationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

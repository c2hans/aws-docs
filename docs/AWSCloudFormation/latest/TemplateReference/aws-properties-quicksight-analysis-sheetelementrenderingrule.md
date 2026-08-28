---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheetelementrenderingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetElementRenderingRule
<a name="aws-properties-quicksight-analysis-sheetelementrenderingrule"></a>

The rendering rules of a sheet that uses a free-form layout.

## Syntax
<a name="aws-properties-quicksight-analysis-sheetelementrenderingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheetelementrenderingrule-syntax.json"></a>

```
{
  "[ConfigurationOverrides](#cfn-quicksight-analysis-sheetelementrenderingrule-configurationoverrides)" : {{SheetElementConfigurationOverrides}},
  "[Expression](#cfn-quicksight-analysis-sheetelementrenderingrule-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheetelementrenderingrule-syntax.yaml"></a>

```
  [ConfigurationOverrides](#cfn-quicksight-analysis-sheetelementrenderingrule-configurationoverrides): {{
    SheetElementConfigurationOverrides}}
  [Expression](#cfn-quicksight-analysis-sheetelementrenderingrule-expression): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheetelementrenderingrule-properties"></a>

`ConfigurationOverrides`  <a name="cfn-quicksight-analysis-sheetelementrenderingrule-configurationoverrides"></a>
The override configuration of the rendering rules of a sheet.
*Required*: Yes
*Type*: [SheetElementConfigurationOverrides](aws-properties-quicksight-analysis-sheetelementconfigurationoverrides.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-analysis-sheetelementrenderingrule-expression"></a>
The expression of the rendering rules of a sheet.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

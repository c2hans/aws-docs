---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-templatesourceentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TemplateSourceEntity
<a name="aws-properties-quicksight-template-templatesourceentity"></a>

The source entity of the template.

## Syntax
<a name="aws-properties-quicksight-template-templatesourceentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-templatesourceentity-syntax.json"></a>

```
{
  "[SourceAnalysis](#cfn-quicksight-template-templatesourceentity-sourceanalysis)" : {{TemplateSourceAnalysis}},
  "[SourceTemplate](#cfn-quicksight-template-templatesourceentity-sourcetemplate)" : {{TemplateSourceTemplate}}
}
```

### YAML
<a name="aws-properties-quicksight-template-templatesourceentity-syntax.yaml"></a>

```
  [SourceAnalysis](#cfn-quicksight-template-templatesourceentity-sourceanalysis): {{
    TemplateSourceAnalysis}}
  [SourceTemplate](#cfn-quicksight-template-templatesourceentity-sourcetemplate): {{
    TemplateSourceTemplate}}
```

## Properties
<a name="aws-properties-quicksight-template-templatesourceentity-properties"></a>

`SourceAnalysis`  <a name="cfn-quicksight-template-templatesourceentity-sourceanalysis"></a>
The source analysis, if it is based on an analysis.
*Required*: No
*Type*: [TemplateSourceAnalysis](aws-properties-quicksight-template-templatesourceanalysis.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTemplate`  <a name="cfn-quicksight-template-templatesourceentity-sourcetemplate"></a>
The source template, if it is based on an template.
*Required*: No
*Type*: [TemplateSourceTemplate](aws-properties-quicksight-template-templatesourcetemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

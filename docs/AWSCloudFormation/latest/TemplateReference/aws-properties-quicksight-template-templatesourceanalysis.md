---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-templatesourceanalysis.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TemplateSourceAnalysis
<a name="aws-properties-quicksight-template-templatesourceanalysis"></a>

The source analysis of the template.

## Syntax
<a name="aws-properties-quicksight-template-templatesourceanalysis-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-templatesourceanalysis-syntax.json"></a>

```
{
  "[Arn](#cfn-quicksight-template-templatesourceanalysis-arn)" : {{String}},
  "[DataSetReferences](#cfn-quicksight-template-templatesourceanalysis-datasetreferences)" : {{[ DataSetReference, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-templatesourceanalysis-syntax.yaml"></a>

```
  [Arn](#cfn-quicksight-template-templatesourceanalysis-arn): {{String}}
  [DataSetReferences](#cfn-quicksight-template-templatesourceanalysis-datasetreferences): {{
    - DataSetReference}}
```

## Properties
<a name="aws-properties-quicksight-template-templatesourceanalysis-properties"></a>

`Arn`  <a name="cfn-quicksight-template-templatesourceanalysis-arn"></a>
The Amazon Resource Name (ARN) of the resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetReferences`  <a name="cfn-quicksight-template-templatesourceanalysis-datasetreferences"></a>
A structure containing information about the dataset references used as placeholders in the template.
*Required*: Yes
*Type*: Array of [DataSetReference](aws-properties-quicksight-template-datasetreference.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

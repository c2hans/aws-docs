---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-staticfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StaticFile
<a name="aws-properties-quicksight-analysis-staticfile"></a>

The static file.

## Syntax
<a name="aws-properties-quicksight-analysis-staticfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-staticfile-syntax.json"></a>

```
{
  "[ImageStaticFile](#cfn-quicksight-analysis-staticfile-imagestaticfile)" : {{ImageStaticFile}},
  "[SpatialStaticFile](#cfn-quicksight-analysis-staticfile-spatialstaticfile)" : {{SpatialStaticFile}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-staticfile-syntax.yaml"></a>

```
  [ImageStaticFile](#cfn-quicksight-analysis-staticfile-imagestaticfile): {{
    ImageStaticFile}}
  [SpatialStaticFile](#cfn-quicksight-analysis-staticfile-spatialstaticfile): {{
    SpatialStaticFile}}
```

## Properties
<a name="aws-properties-quicksight-analysis-staticfile-properties"></a>

`ImageStaticFile`  <a name="cfn-quicksight-analysis-staticfile-imagestaticfile"></a>
The image static file.
*Required*: No
*Type*: [ImageStaticFile](aws-properties-quicksight-analysis-imagestaticfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpatialStaticFile`  <a name="cfn-quicksight-analysis-staticfile-spatialstaticfile"></a>
The spacial static file.
*Required*: No
*Type*: [SpatialStaticFile](aws-properties-quicksight-analysis-spatialstaticfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

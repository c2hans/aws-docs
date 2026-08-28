---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-spatialstaticfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SpatialStaticFile
<a name="aws-properties-quicksight-analysis-spatialstaticfile"></a>

A static file that contains the geospatial data.

## Syntax
<a name="aws-properties-quicksight-analysis-spatialstaticfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-spatialstaticfile-syntax.json"></a>

```
{
  "[Source](#cfn-quicksight-analysis-spatialstaticfile-source)" : {{StaticFileSource}},
  "[StaticFileId](#cfn-quicksight-analysis-spatialstaticfile-staticfileid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-spatialstaticfile-syntax.yaml"></a>

```
  [Source](#cfn-quicksight-analysis-spatialstaticfile-source): {{
    StaticFileSource}}
  [StaticFileId](#cfn-quicksight-analysis-spatialstaticfile-staticfileid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-spatialstaticfile-properties"></a>

`Source`  <a name="cfn-quicksight-analysis-spatialstaticfile-source"></a>
The source of the spatial static file.
*Required*: No
*Type*: [StaticFileSource](aws-properties-quicksight-analysis-staticfilesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticFileId`  <a name="cfn-quicksight-analysis-spatialstaticfile-staticfileid"></a>
The ID of the spatial static file.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialstaticfilesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialStaticFileSource
<a name="aws-properties-quicksight-analysis-geospatialstaticfilesource"></a>

The source properties for a geospatial static file.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialstaticfilesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialstaticfilesource-syntax.json"></a>

```
{
  "[StaticFileId](#cfn-quicksight-analysis-geospatialstaticfilesource-staticfileid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialstaticfilesource-syntax.yaml"></a>

```
  [StaticFileId](#cfn-quicksight-analysis-geospatialstaticfilesource-staticfileid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialstaticfilesource-properties"></a>

`StaticFileId`  <a name="cfn-quicksight-analysis-geospatialstaticfilesource-staticfileid"></a>
The ID of the static file.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-filter-packagefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Filter PackageFilter
<a name="aws-properties-inspectorv2-filter-packagefilter"></a>

Contains information on the details of a package filter.

## Syntax
<a name="aws-properties-inspectorv2-filter-packagefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-filter-packagefilter-syntax.json"></a>

```
{
  "[Architecture](#cfn-inspectorv2-filter-packagefilter-architecture)" : {{StringFilter}},
  "[Epoch](#cfn-inspectorv2-filter-packagefilter-epoch)" : {{NumberFilter}},
  "[FilePath](#cfn-inspectorv2-filter-packagefilter-filepath)" : {{StringFilter}},
  "[Name](#cfn-inspectorv2-filter-packagefilter-name)" : {{StringFilter}},
  "[Release](#cfn-inspectorv2-filter-packagefilter-release)" : {{StringFilter}},
  "[SourceLambdaLayerArn](#cfn-inspectorv2-filter-packagefilter-sourcelambdalayerarn)" : {{StringFilter}},
  "[SourceLayerHash](#cfn-inspectorv2-filter-packagefilter-sourcelayerhash)" : {{StringFilter}},
  "[Version](#cfn-inspectorv2-filter-packagefilter-version)" : {{StringFilter}}
}
```

### YAML
<a name="aws-properties-inspectorv2-filter-packagefilter-syntax.yaml"></a>

```
  [Architecture](#cfn-inspectorv2-filter-packagefilter-architecture): {{
    StringFilter}}
  [Epoch](#cfn-inspectorv2-filter-packagefilter-epoch): {{
    NumberFilter}}
  [FilePath](#cfn-inspectorv2-filter-packagefilter-filepath): {{
    StringFilter}}
  [Name](#cfn-inspectorv2-filter-packagefilter-name): {{
    StringFilter}}
  [Release](#cfn-inspectorv2-filter-packagefilter-release): {{
    StringFilter}}
  [SourceLambdaLayerArn](#cfn-inspectorv2-filter-packagefilter-sourcelambdalayerarn): {{
    StringFilter}}
  [SourceLayerHash](#cfn-inspectorv2-filter-packagefilter-sourcelayerhash): {{
    StringFilter}}
  [Version](#cfn-inspectorv2-filter-packagefilter-version): {{
    StringFilter}}
```

## Properties
<a name="aws-properties-inspectorv2-filter-packagefilter-properties"></a>

`Architecture`  <a name="cfn-inspectorv2-filter-packagefilter-architecture"></a>
An object that contains details on the package architecture type to filter on.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Epoch`  <a name="cfn-inspectorv2-filter-packagefilter-epoch"></a>
An object that contains details on the package epoch to filter on.
*Required*: No
*Type*: [NumberFilter](aws-properties-inspectorv2-filter-numberfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilePath`  <a name="cfn-inspectorv2-filter-packagefilter-filepath"></a>
Property description not available.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-inspectorv2-filter-packagefilter-name"></a>
An object that contains details on the name of the package to filter on.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Release`  <a name="cfn-inspectorv2-filter-packagefilter-release"></a>
An object that contains details on the package release to filter on.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLambdaLayerArn`  <a name="cfn-inspectorv2-filter-packagefilter-sourcelambdalayerarn"></a>
Property description not available.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLayerHash`  <a name="cfn-inspectorv2-filter-packagefilter-sourcelayerhash"></a>
An object that contains details on the source layer hash to filter on.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-inspectorv2-filter-packagefilter-version"></a>
The package version to filter on.
*Required*: No
*Type*: [StringFilter](aws-properties-inspectorv2-filter-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

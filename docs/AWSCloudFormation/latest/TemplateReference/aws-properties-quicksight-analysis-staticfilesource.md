---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-staticfilesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StaticFileSource
<a name="aws-properties-quicksight-analysis-staticfilesource"></a>

The source of the static file.

## Syntax
<a name="aws-properties-quicksight-analysis-staticfilesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-staticfilesource-syntax.json"></a>

```
{
  "[S3Options](#cfn-quicksight-analysis-staticfilesource-s3options)" : {{StaticFileS3SourceOptions}},
  "[UrlOptions](#cfn-quicksight-analysis-staticfilesource-urloptions)" : {{StaticFileUrlSourceOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-staticfilesource-syntax.yaml"></a>

```
  [S3Options](#cfn-quicksight-analysis-staticfilesource-s3options): {{
    StaticFileS3SourceOptions}}
  [UrlOptions](#cfn-quicksight-analysis-staticfilesource-urloptions): {{
    StaticFileUrlSourceOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-staticfilesource-properties"></a>

`S3Options`  <a name="cfn-quicksight-analysis-staticfilesource-s3options"></a>
The structure that contains the Amazon S3 location to download the static file from.
*Required*: No
*Type*: [StaticFileS3SourceOptions](aws-properties-quicksight-analysis-staticfiles3sourceoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UrlOptions`  <a name="cfn-quicksight-analysis-staticfilesource-urloptions"></a>
The structure that contains the URL to download the static file from.
*Required*: No
*Type*: [StaticFileUrlSourceOptions](aws-properties-quicksight-analysis-staticfileurlsourceoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

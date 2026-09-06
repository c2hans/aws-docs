---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-staticfilesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard StaticFileSource
<a name="aws-properties-quicksight-dashboard-staticfilesource"></a>

The source of the static file.

## Syntax
<a name="aws-properties-quicksight-dashboard-staticfilesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-staticfilesource-syntax.json"></a>

```
{
  "[S3Options](#cfn-quicksight-dashboard-staticfilesource-s3options)" : {{StaticFileS3SourceOptions}},
  "[UrlOptions](#cfn-quicksight-dashboard-staticfilesource-urloptions)" : {{StaticFileUrlSourceOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-staticfilesource-syntax.yaml"></a>

```
  [S3Options](#cfn-quicksight-dashboard-staticfilesource-s3options): {{
    StaticFileS3SourceOptions}}
  [UrlOptions](#cfn-quicksight-dashboard-staticfilesource-urloptions): {{
    StaticFileUrlSourceOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-staticfilesource-properties"></a>

`S3Options`  <a name="cfn-quicksight-dashboard-staticfilesource-s3options"></a>
The structure that contains the Amazon S3 location to download the static file from.
*Required*: No
*Type*: [StaticFileS3SourceOptions](aws-properties-quicksight-dashboard-staticfiles3sourceoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UrlOptions`  <a name="cfn-quicksight-dashboard-staticfilesource-urloptions"></a>
The structure that contains the URL to download the static file from.
*Required*: No
*Type*: [StaticFileUrlSourceOptions](aws-properties-quicksight-dashboard-staticfileurlsourceoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

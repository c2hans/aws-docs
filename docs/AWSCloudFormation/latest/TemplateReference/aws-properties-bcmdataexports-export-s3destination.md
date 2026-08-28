---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-s3destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export S3Destination
<a name="aws-properties-bcmdataexports-export-s3destination"></a>

Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a data exports file.

## Syntax
<a name="aws-properties-bcmdataexports-export-s3destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-s3destination-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-bcmdataexports-export-s3destination-s3bucket)" : {{String}},
  "[S3BucketOwner](#cfn-bcmdataexports-export-s3destination-s3bucketowner)" : {{String}},
  "[S3OutputConfigurations](#cfn-bcmdataexports-export-s3destination-s3outputconfigurations)" : {{S3OutputConfigurations}},
  "[S3Prefix](#cfn-bcmdataexports-export-s3destination-s3prefix)" : {{String}},
  "[S3Region](#cfn-bcmdataexports-export-s3destination-s3region)" : {{String}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-s3destination-syntax.yaml"></a>

```
  [S3Bucket](#cfn-bcmdataexports-export-s3destination-s3bucket): {{String}}
  [S3BucketOwner](#cfn-bcmdataexports-export-s3destination-s3bucketowner): {{String}}
  [S3OutputConfigurations](#cfn-bcmdataexports-export-s3destination-s3outputconfigurations): {{
    S3OutputConfigurations}}
  [S3Prefix](#cfn-bcmdataexports-export-s3destination-s3prefix): {{String}}
  [S3Region](#cfn-bcmdataexports-export-s3destination-s3region): {{String}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-s3destination-properties"></a>

`S3Bucket`  <a name="cfn-bcmdataexports-export-s3destination-s3bucket"></a>
The name of the Amazon S3 bucket used as the destination of a data export file.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketOwner`  <a name="cfn-bcmdataexports-export-s3destination-s3bucketowner"></a>
The Amazon Web Services account ID that owns the S3 bucket used as the destination for the data export.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3OutputConfigurations`  <a name="cfn-bcmdataexports-export-s3destination-s3outputconfigurations"></a>
The output configuration for the data export.
*Required*: Yes
*Type*: [S3OutputConfigurations](aws-properties-bcmdataexports-export-s3outputconfigurations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Prefix`  <a name="cfn-bcmdataexports-export-s3destination-s3prefix"></a>
The S3 path prefix you want prepended to the name of your data export.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Region`  <a name="cfn-bcmdataexports-export-s3destination-s3region"></a>
The S3 bucket Region.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

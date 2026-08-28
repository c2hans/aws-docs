---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-filesystem-importdatarule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::FileSystem ImportDataRule
<a name="aws-properties-s3files-filesystem-importdatarule"></a>

Specifies a rule that controls how data is imported from S3 into the file system.

## Syntax
<a name="aws-properties-s3files-filesystem-importdatarule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-filesystem-importdatarule-syntax.json"></a>

```
{
  "[Prefix](#cfn-s3files-filesystem-importdatarule-prefix)" : {{String}},
  "[SizeLessThan](#cfn-s3files-filesystem-importdatarule-sizelessthan)" : {{Integer}},
  "[Trigger](#cfn-s3files-filesystem-importdatarule-trigger)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3files-filesystem-importdatarule-syntax.yaml"></a>

```
  [Prefix](#cfn-s3files-filesystem-importdatarule-prefix): {{String}}
  [SizeLessThan](#cfn-s3files-filesystem-importdatarule-sizelessthan): {{Integer}}
  [Trigger](#cfn-s3files-filesystem-importdatarule-trigger): {{String}}
```

## Properties
<a name="aws-properties-s3files-filesystem-importdatarule-properties"></a>

`Prefix`  <a name="cfn-s3files-filesystem-importdatarule-prefix"></a>
The S3 key prefix that scopes this import rule. Only objects with keys beginning with this prefix are subject to the rule.
*Required*: Yes
*Type*: String
*Pattern*: `^(|.*/)$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeLessThan`  <a name="cfn-s3files-filesystem-importdatarule-sizelessthan"></a>
The upper size limit in bytes for this import rule. Only objects with a size strictly less than this value will have data imported into the file system.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `52673613135872`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-s3files-filesystem-importdatarule-trigger"></a>
The event that triggers data import. Valid values are `ON_DIRECTORY_FIRST_ACCESS` (import when a directory is first accessed) and `ON_FILE_ACCESS` (import when a file is accessed).
*Required*: Yes
*Type*: String
*Allowed values*: `ON_DIRECTORY_FIRST_ACCESS | ON_FILE_ACCESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-sessionlogger-s3logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::SessionLogger S3LogConfiguration
<a name="aws-properties-workspacesweb-sessionlogger-s3logconfiguration"></a>

The S3 log configuration.

## Syntax
<a name="aws-properties-workspacesweb-sessionlogger-s3logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-sessionlogger-s3logconfiguration-syntax.json"></a>

```
{
  "[Bucket](#cfn-workspacesweb-sessionlogger-s3logconfiguration-bucket)" : {{String}},
  "[BucketOwner](#cfn-workspacesweb-sessionlogger-s3logconfiguration-bucketowner)" : {{String}},
  "[FolderStructure](#cfn-workspacesweb-sessionlogger-s3logconfiguration-folderstructure)" : {{String}},
  "[KeyPrefix](#cfn-workspacesweb-sessionlogger-s3logconfiguration-keyprefix)" : {{String}},
  "[LogFileFormat](#cfn-workspacesweb-sessionlogger-s3logconfiguration-logfileformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesweb-sessionlogger-s3logconfiguration-syntax.yaml"></a>

```
  [Bucket](#cfn-workspacesweb-sessionlogger-s3logconfiguration-bucket): {{String}}
  [BucketOwner](#cfn-workspacesweb-sessionlogger-s3logconfiguration-bucketowner): {{String}}
  [FolderStructure](#cfn-workspacesweb-sessionlogger-s3logconfiguration-folderstructure): {{String}}
  [KeyPrefix](#cfn-workspacesweb-sessionlogger-s3logconfiguration-keyprefix): {{String}}
  [LogFileFormat](#cfn-workspacesweb-sessionlogger-s3logconfiguration-logfileformat): {{String}}
```

## Properties
<a name="aws-properties-workspacesweb-sessionlogger-s3logconfiguration-properties"></a>

`Bucket`  <a name="cfn-workspacesweb-sessionlogger-s3logconfiguration-bucket"></a>
The S3 bucket name where logs are delivered.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwner`  <a name="cfn-workspacesweb-sessionlogger-s3logconfiguration-bucketowner"></a>
The expected bucket owner of the target S3 bucket. The caller must have permissions to write to the target bucket.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderStructure`  <a name="cfn-workspacesweb-sessionlogger-s3logconfiguration-folderstructure"></a>
The folder structure that defines the organizational structure for log files in S3.
*Required*: Yes
*Type*: String
*Allowed values*: `Flat | NestedByDate`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPrefix`  <a name="cfn-workspacesweb-sessionlogger-s3logconfiguration-keyprefix"></a>
The S3 path prefix that determines where log files are stored.
*Required*: No
*Type*: String
*Pattern*: `^[\d\w\-_/!().*']+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogFileFormat`  <a name="cfn-workspacesweb-sessionlogger-s3logconfiguration-logfileformat"></a>
The format of the LogFile that is written to S3.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONLines | Json`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

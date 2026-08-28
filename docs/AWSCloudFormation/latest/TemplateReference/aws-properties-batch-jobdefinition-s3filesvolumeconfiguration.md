---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-s3filesvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition S3FilesVolumeConfiguration
<a name="aws-properties-batch-jobdefinition-s3filesvolumeconfiguration"></a>

This is used when you're using an S3Files file system for job storage.

## Syntax
<a name="aws-properties-batch-jobdefinition-s3filesvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-s3filesvolumeconfiguration-syntax.json"></a>

```
{
  "[AccessPointArn](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-accesspointarn)" : {{String}},
  "[FileSystemArn](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-filesystemarn)" : {{String}},
  "[RootDirectory](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-rootdirectory)" : {{String}},
  "[TransitEncryptionPort](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-transitencryptionport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-s3filesvolumeconfiguration-syntax.yaml"></a>

```
  [AccessPointArn](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-accesspointarn): {{String}}
  [FileSystemArn](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-filesystemarn): {{String}}
  [RootDirectory](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-rootdirectory): {{String}}
  [TransitEncryptionPort](#cfn-batch-jobdefinition-s3filesvolumeconfiguration-transitencryptionport): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-s3filesvolumeconfiguration-properties"></a>

`AccessPointArn`  <a name="cfn-batch-jobdefinition-s3filesvolumeconfiguration-accesspointarn"></a>
The Amazon Resource Name (ARN) of the S3Files access point to use.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSystemArn`  <a name="cfn-batch-jobdefinition-s3filesvolumeconfiguration-filesystemarn"></a>
The Amazon Resource Name (ARN) of the S3Files file system to use.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RootDirectory`  <a name="cfn-batch-jobdefinition-s3filesvolumeconfiguration-rootdirectory"></a>
The directory within the S3Files file system to mount as the root directory.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitEncryptionPort`  <a name="cfn-batch-jobdefinition-s3filesvolumeconfiguration-transitencryptionport"></a>
The port to use when sending encrypted data between the Amazon ECS host and the S3Files file system server.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

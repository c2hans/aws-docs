---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition S3FilesVolumeConfiguration
<a name="aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration"></a>

This parameter is specified when you're using an Amazon S3 Files file system for task storage. For more information, see [Amazon S3 Files volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/s3files-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

**Important**
Your task definition must include a Task IAM Role. See [ IAM role for attaching your file system to AWS compute resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam-compute-role) for required permissions.

## Syntax
<a name="aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration-syntax.json"></a>

```
{
  "[AccessPointArn](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-accesspointarn)" : {{String}},
  "[FileSystemArn](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-filesystemarn)" : {{String}},
  "[RootDirectory](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-rootdirectory)" : {{String}},
  "[TransitEncryptionPort](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-transitencryptionport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration-syntax.yaml"></a>

```
  [AccessPointArn](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-accesspointarn): {{String}}
  [FileSystemArn](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-filesystemarn): {{String}}
  [RootDirectory](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-rootdirectory): {{String}}
  [TransitEncryptionPort](#cfn-ecs-taskdefinition-s3filesvolumeconfiguration-transitencryptionport): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration-properties"></a>

`AccessPointArn`  <a name="cfn-ecs-taskdefinition-s3filesvolumeconfiguration-accesspointarn"></a>
The full ARN of the S3 Files access point to use. If an access point is specified, the root directory value specified in the `S3FilesVolumeConfiguration` must either be omitted or set to `/` which will enforce the path set on the S3 Files access point. For more information, see [Creating S3 Files access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemArn`  <a name="cfn-ecs-taskdefinition-s3filesvolumeconfiguration-filesystemarn"></a>
The full ARN of the S3 Files file system to mount.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootDirectory`  <a name="cfn-ecs-taskdefinition-s3filesvolumeconfiguration-rootdirectory"></a>
The directory within the Amazon S3 Files file system to mount as the root directory. If this parameter is omitted, the root of the Amazon S3 Files file system will be used. Specifying `/` will have the same effect as omitting this parameter.
If a S3 Files access point is specified in the `accessPointArn`, the root directory parameter must either be omitted or set to `/` which will enforce the path set on the S3 Files access point.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitEncryptionPort`  <a name="cfn-ecs-taskdefinition-s3filesvolumeconfiguration-transitencryptionport"></a>
The port to use for sending encrypted data between the ECS host and the S3 Files file system. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon S3 Files mount helper uses. For more information, see [S3 Files mount helper](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-mounting.html).
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

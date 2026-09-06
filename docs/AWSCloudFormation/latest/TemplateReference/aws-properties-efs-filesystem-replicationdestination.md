---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-filesystem-replicationdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::FileSystem ReplicationDestination
<a name="aws-properties-efs-filesystem-replicationdestination"></a>

Describes the destination file system in the replication configuration.

## Syntax
<a name="aws-properties-efs-filesystem-replicationdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-filesystem-replicationdestination-syntax.json"></a>

```
{
  "[AvailabilityZoneName](#cfn-efs-filesystem-replicationdestination-availabilityzonename)" : {{String}},
  "[FileSystemId](#cfn-efs-filesystem-replicationdestination-filesystemid)" : {{String}},
  "[KmsKeyId](#cfn-efs-filesystem-replicationdestination-kmskeyid)" : {{String}},
  "[Region](#cfn-efs-filesystem-replicationdestination-region)" : {{String}},
  "[RoleArn](#cfn-efs-filesystem-replicationdestination-rolearn)" : {{String}},
  "[Status](#cfn-efs-filesystem-replicationdestination-status)" : {{String}},
  "[StatusMessage](#cfn-efs-filesystem-replicationdestination-statusmessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-filesystem-replicationdestination-syntax.yaml"></a>

```
  [AvailabilityZoneName](#cfn-efs-filesystem-replicationdestination-availabilityzonename): {{String}}
  [FileSystemId](#cfn-efs-filesystem-replicationdestination-filesystemid): {{String}}
  [KmsKeyId](#cfn-efs-filesystem-replicationdestination-kmskeyid): {{String}}
  [Region](#cfn-efs-filesystem-replicationdestination-region): {{String}}
  [RoleArn](#cfn-efs-filesystem-replicationdestination-rolearn): {{String}}
  [Status](#cfn-efs-filesystem-replicationdestination-status): {{String}}
  [StatusMessage](#cfn-efs-filesystem-replicationdestination-statusmessage): {{String}}
```

## Properties
<a name="aws-properties-efs-filesystem-replicationdestination-properties"></a>

`AvailabilityZoneName`  <a name="cfn-efs-filesystem-replicationdestination-availabilityzonename"></a>
 For One Zone file systems, the replication configuration must specify the Availability Zone in which the destination file system is located.
Use the format `us-east-1a` to specify the Availability Zone. For more information about One Zone file systems, see [EFS file system types](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html) in the *Amazon EFS User Guide*.
One Zone file system type is not available in all Availability Zones in AWS Regions where Amazon EFS is available.
*Required*: No
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSystemId`  <a name="cfn-efs-filesystem-replicationdestination-filesystemid"></a>
The ID of the destination Amazon EFS file system.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-efs-filesystem-replicationdestination-kmskeyid"></a>
The ID of an AWS KMS key used to protect the encrypted file system.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-efs-filesystem-replicationdestination-region"></a>
The AWS Region in which the destination file system is located.
For One Zone file systems, the replication configuration must specify the AWS Region in which the destination file system is located.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-efs-filesystem-replicationdestination-rolearn"></a>
The Amazon Resource Name (ARN) of the current source file system in the replication configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-efs-filesystem-replicationdestination-status"></a>
Describes the status of the replication configuration. For more information about replication status, see [Viewing replication details](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#restoring-backup-efsmonitoring-replication-status.html) in the *Amazon EFS User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DELETING | ERROR | PAUSED | PAUSING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusMessage`  <a name="cfn-efs-filesystem-replicationdestination-statusmessage"></a>
Message that provides details about the `PAUSED` or `ERRROR` state of the replication destination configuration. For more information about replication status messages, see [Viewing replication details](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#restoring-backup-efsmonitoring-replication-status.html) in the *Amazon EFS User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

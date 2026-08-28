---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBSnapshot
<a name="aws-resource-rds-dbsnapshot"></a>

Contains the details of an Amazon RDS DB snapshot.

This data type is used as a response element in the `DescribeDBSnapshots` action.

## Syntax
<a name="aws-resource-rds-dbsnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbsnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBSnapshot",
  "Properties" : {
      "[DBInstanceIdentifier](#cfn-rds-dbsnapshot-dbinstanceidentifier)" : {{String}},
      "[DBSnapshotIdentifier](#cfn-rds-dbsnapshot-dbsnapshotidentifier)" : {{String}},
      "[Tags](#cfn-rds-dbsnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbsnapshot-syntax.yaml"></a>

```
Type: AWS::RDS::DBSnapshot
Properties:
  [DBInstanceIdentifier](#cfn-rds-dbsnapshot-dbinstanceidentifier): {{String}}
  [DBSnapshotIdentifier](#cfn-rds-dbsnapshot-dbsnapshotidentifier): {{String}}
  [Tags](#cfn-rds-dbsnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-dbsnapshot-properties"></a>

`DBInstanceIdentifier`  <a name="cfn-rds-dbsnapshot-dbinstanceidentifier"></a>
Specifies the DB instance identifier of the DB instance this DB snapshot was created from.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBSnapshotIdentifier`  <a name="cfn-rds-dbsnapshot-dbsnapshotidentifier"></a>
Specifies the identifier for the DB snapshot.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-dbsnapshot-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbsnapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbsnapshot-return-values"></a>

### Ref
<a name="aws-resource-rds-dbsnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rds-dbsnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-dbsnapshot-return-values-fn--getatt-fn--getatt"></a>

`AllocatedStorage`  <a name="AllocatedStorage-fn::getatt"></a>
Specifies the allocated storage size in gibibytes (GiB).

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

`DbiResourceId`  <a name="DbiResourceId-fn::getatt"></a>
The identifier for the source DB instance, which can't be changed and which is unique to an AWS Region.

`DBSnapshotArn`  <a name="DBSnapshotArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the DB snapshot.

`Encrypted`  <a name="Encrypted-fn::getatt"></a>
Indicates whether the DB snapshot is encrypted.

`Engine`  <a name="Engine-fn::getatt"></a>
Specifies the name of the database engine.

`EngineVersion`  <a name="EngineVersion-fn::getatt"></a>
Specifies the version of the database engine.

`IAMDatabaseAuthenticationEnabled`  <a name="IAMDatabaseAuthenticationEnabled-fn::getatt"></a>
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

`InstanceCreateTime`  <a name="InstanceCreateTime-fn::getatt"></a>
Specifies the time in Coordinated Universal Time (UTC) when the DB instance, from which the snapshot was taken, was created.

`Iops`  <a name="Iops-fn::getatt"></a>
Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

`KmsKeyId`  <a name="KmsKeyId-fn::getatt"></a>
If `Encrypted` is true, the AWS KMS key identifier for the encrypted DB snapshot.
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

`LicenseModel`  <a name="LicenseModel-fn::getatt"></a>
License model information for the restored DB instance.

`MasterUsername`  <a name="MasterUsername-fn::getatt"></a>
Provides the master username for the DB snapshot.

`OptionGroupName`  <a name="OptionGroupName-fn::getatt"></a>
Provides the option group name for the DB snapshot.

`OriginalSnapshotCreateTime`  <a name="OriginalSnapshotCreateTime-fn::getatt"></a>
Specifies the time of the CreateDBSnapshot operation in Coordinated Universal Time (UTC). Doesn't change when the snapshot is copied.

`Port`  <a name="Port-fn::getatt"></a>
Specifies the port that the database engine was listening on at the time of the snapshot.

`SnapshotCreateTime`  <a name="SnapshotCreateTime-fn::getatt"></a>
Specifies when the snapshot was taken in Coordinated Universal Time (UTC). Changes for the copy when the snapshot is copied.

`SnapshotType`  <a name="SnapshotType-fn::getatt"></a>
Provides the type of the DB snapshot.

`Status`  <a name="Status-fn::getatt"></a>
Specifies the status of this DB snapshot.

`StorageThroughput`  <a name="StorageThroughput-fn::getatt"></a>
Specifies the storage throughput for the DB snapshot.

`StorageType`  <a name="StorageType-fn::getatt"></a>
Specifies the storage type associated with DB snapshot.

`VpcId`  <a name="VpcId-fn::getatt"></a>
Provides the VPC ID associated with the DB snapshot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

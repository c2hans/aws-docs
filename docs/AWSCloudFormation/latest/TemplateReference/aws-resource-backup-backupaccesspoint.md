---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-backup-backupaccesspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupAccessPoint
<a name="aws-resource-backup-backupaccesspoint"></a>

Creates a backup access point for an Amazon S3 recovery point. A backup access point provides on-demand, read-only access to the backup data in a recovery point through an Amazon S3 access point, without initiating a restore.

While a backup access point is active for a recovery point, AWS Backup pauses lifecycle transitions and blocks deletion of that recovery point.

## Syntax
<a name="aws-resource-backup-backupaccesspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-backup-backupaccesspoint-syntax.json"></a>

```
{
  "Type" : "AWS::Backup::BackupAccessPoint",
  "Properties" : {
      "[AccessPointInTime](#cfn-backup-backupaccesspoint-accesspointintime)" : {{String}},
      "[AccessPointPolicy](#cfn-backup-backupaccesspoint-accesspointpolicy)" : {{Json}},
      "[Name](#cfn-backup-backupaccesspoint-name)" : {{String}},
      "[RecoveryPointArn](#cfn-backup-backupaccesspoint-recoverypointarn)" : {{String}},
      "[Tags](#cfn-backup-backupaccesspoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-backup-backupaccesspoint-syntax.yaml"></a>

```
Type: AWS::Backup::BackupAccessPoint
Properties:
  [AccessPointInTime](#cfn-backup-backupaccesspoint-accesspointintime): {{String}}
  [AccessPointPolicy](#cfn-backup-backupaccesspoint-accesspointpolicy): {{Json}}
  [Name](#cfn-backup-backupaccesspoint-name): {{String}}
  [RecoveryPointArn](#cfn-backup-backupaccesspoint-recoverypointarn): {{String}}
  [Tags](#cfn-backup-backupaccesspoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-backup-backupaccesspoint-properties"></a>

`AccessPointInTime`  <a name="cfn-backup-backupaccesspoint-accesspointintime"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AccessPointPolicy`  <a name="cfn-backup-backupaccesspoint-accesspointpolicy"></a>
Property description not available.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-backup-backupaccesspoint-name"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)$`
*Minimum*: `3`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecoveryPointArn`  <a name="cfn-backup-backupaccesspoint-recoverypointarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[a-z-]*:[a-z-\d]+:[a-z-\d]+:).+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-backup-backupaccesspoint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-backup-backupaccesspoint-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-backup-backupaccesspoint-return-values"></a>

### Ref
<a name="aws-resource-backup-backupaccesspoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-backup-backupaccesspoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-backup-backupaccesspoint-return-values-fn--getatt-fn--getatt"></a>

`AccessPointMetadata.AccessPointInTime`  <a name="AccessPointMetadata.AccessPointInTime-fn::getatt"></a>
Property description not available.

`AccessPointMetadata.S3AccessPointAlias`  <a name="AccessPointMetadata.S3AccessPointAlias-fn::getatt"></a>
Property description not available.

`AccessPointMetadata.S3AccessPointArn`  <a name="AccessPointMetadata.S3AccessPointArn-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`BackupVaultArn`  <a name="BackupVaultArn-fn::getatt"></a>
Property description not available.

`BackupVaultName`  <a name="BackupVaultName-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
Property description not available.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

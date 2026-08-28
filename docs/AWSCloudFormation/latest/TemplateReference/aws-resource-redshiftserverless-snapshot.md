---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshiftserverless-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Snapshot
<a name="aws-resource-redshiftserverless-snapshot"></a>

A snapshot object that contains databases.

## Syntax
<a name="aws-resource-redshiftserverless-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshiftserverless-snapshot-syntax.json"></a>

```
{
  "Type" : "AWS::RedshiftServerless::Snapshot",
  "Properties" : {
      "[NamespaceName](#cfn-redshiftserverless-snapshot-namespacename)" : {{String}},
      "[RetentionPeriod](#cfn-redshiftserverless-snapshot-retentionperiod)" : {{Integer}},
      "[SnapshotName](#cfn-redshiftserverless-snapshot-snapshotname)" : {{String}},
      "[Tags](#cfn-redshiftserverless-snapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshiftserverless-snapshot-syntax.yaml"></a>

```
Type: AWS::RedshiftServerless::Snapshot
Properties:
  [NamespaceName](#cfn-redshiftserverless-snapshot-namespacename): {{String}}
  [RetentionPeriod](#cfn-redshiftserverless-snapshot-retentionperiod): {{Integer}}
  [SnapshotName](#cfn-redshiftserverless-snapshot-snapshotname): {{String}}
  [Tags](#cfn-redshiftserverless-snapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshiftserverless-snapshot-properties"></a>

`NamespaceName`  <a name="cfn-redshiftserverless-snapshot-namespacename"></a>
The name of the namepsace.
*Required*: No
*Type*: String
*Pattern*: `^(?=^[a-z0-9-]+$).{3,64}$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionPeriod`  <a name="cfn-redshiftserverless-snapshot-retentionperiod"></a>
The retention period of the snapshot created by the scheduled action.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotName`  <a name="cfn-redshiftserverless-snapshot-snapshotname"></a>
The name of the snapshot.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=^[a-z0-9-]+$).{3,64}$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshiftserverless-snapshot-tags"></a>
An array of [Tag objects](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html) to associate with the snapshot.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshiftserverless-snapshot-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-redshiftserverless-snapshot-return-values"></a>

### Ref
<a name="aws-resource-redshiftserverless-snapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshiftserverless-snapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshiftserverless-snapshot-return-values-fn--getatt-fn--getatt"></a>

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
The owner AWS; account of the snapshot.

`Snapshot.AdminUsername`  <a name="Snapshot.AdminUsername-fn::getatt"></a>
The username of the database within a snapshot.

`Snapshot.KmsKeyId`  <a name="Snapshot.KmsKeyId-fn::getatt"></a>
The unique identifier of the KMS key used to encrypt the snapshot.

`Snapshot.NamespaceArn`  <a name="Snapshot.NamespaceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the namespace the snapshot was created from.

`Snapshot.NamespaceName`  <a name="Snapshot.NamespaceName-fn::getatt"></a>
The name of the namepsace.

`Snapshot.OwnerAccount`  <a name="Snapshot.OwnerAccount-fn::getatt"></a>
The owner AWS; account of the snapshot.

`Snapshot.RetentionPeriod`  <a name="Snapshot.RetentionPeriod-fn::getatt"></a>
The retention period of the snapshot created by the scheduled action.

`Snapshot.SnapshotArn`  <a name="Snapshot.SnapshotArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the snapshot.

`Snapshot.SnapshotCreateTime`  <a name="Snapshot.SnapshotCreateTime-fn::getatt"></a>
The timestamp of when the snapshot was created.

`Snapshot.SnapshotName`  <a name="Snapshot.SnapshotName-fn::getatt"></a>
The name of the snapshot.

`Snapshot.Status`  <a name="Snapshot.Status-fn::getatt"></a>
The status of the snapshot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-snapshot-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Snapshot Snapshot
<a name="aws-properties-redshiftserverless-snapshot-snapshot"></a>

A snapshot object that contains databases.

## Syntax
<a name="aws-properties-redshiftserverless-snapshot-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-snapshot-snapshot-syntax.json"></a>

```
{
  "[AdminUsername](#cfn-redshiftserverless-snapshot-snapshot-adminusername)" : {{String}},
  "[KmsKeyId](#cfn-redshiftserverless-snapshot-snapshot-kmskeyid)" : {{String}},
  "[NamespaceArn](#cfn-redshiftserverless-snapshot-snapshot-namespacearn)" : {{String}},
  "[NamespaceName](#cfn-redshiftserverless-snapshot-snapshot-namespacename)" : {{String}},
  "[OwnerAccount](#cfn-redshiftserverless-snapshot-snapshot-owneraccount)" : {{String}},
  "[RetentionPeriod](#cfn-redshiftserverless-snapshot-snapshot-retentionperiod)" : {{Integer}},
  "[SnapshotArn](#cfn-redshiftserverless-snapshot-snapshot-snapshotarn)" : {{String}},
  "[SnapshotCreateTime](#cfn-redshiftserverless-snapshot-snapshot-snapshotcreatetime)" : {{String}},
  "[SnapshotName](#cfn-redshiftserverless-snapshot-snapshot-snapshotname)" : {{String}},
  "[Status](#cfn-redshiftserverless-snapshot-snapshot-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-snapshot-snapshot-syntax.yaml"></a>

```
  [AdminUsername](#cfn-redshiftserverless-snapshot-snapshot-adminusername): {{String}}
  [KmsKeyId](#cfn-redshiftserverless-snapshot-snapshot-kmskeyid): {{String}}
  [NamespaceArn](#cfn-redshiftserverless-snapshot-snapshot-namespacearn): {{String}}
  [NamespaceName](#cfn-redshiftserverless-snapshot-snapshot-namespacename): {{String}}
  [OwnerAccount](#cfn-redshiftserverless-snapshot-snapshot-owneraccount): {{String}}
  [RetentionPeriod](#cfn-redshiftserverless-snapshot-snapshot-retentionperiod): {{Integer}}
  [SnapshotArn](#cfn-redshiftserverless-snapshot-snapshot-snapshotarn): {{String}}
  [SnapshotCreateTime](#cfn-redshiftserverless-snapshot-snapshot-snapshotcreatetime): {{String}}
  [SnapshotName](#cfn-redshiftserverless-snapshot-snapshot-snapshotname): {{String}}
  [Status](#cfn-redshiftserverless-snapshot-snapshot-status): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-snapshot-snapshot-properties"></a>

`AdminUsername`  <a name="cfn-redshiftserverless-snapshot-snapshot-adminusername"></a>
The username of the database within a snapshot.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-redshiftserverless-snapshot-snapshot-kmskeyid"></a>
The unique identifier of the KMS key used to encrypt the snapshot.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceArn`  <a name="cfn-redshiftserverless-snapshot-snapshot-namespacearn"></a>
The Amazon Resource Name (ARN) of the namespace the snapshot was created from.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceName`  <a name="cfn-redshiftserverless-snapshot-snapshot-namespacename"></a>
The name of the namepsace.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerAccount`  <a name="cfn-redshiftserverless-snapshot-snapshot-owneraccount"></a>
The owner AWS; account of the snapshot.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionPeriod`  <a name="cfn-redshiftserverless-snapshot-snapshot-retentionperiod"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotArn`  <a name="cfn-redshiftserverless-snapshot-snapshot-snapshotarn"></a>
The Amazon Resource Name (ARN) of the snapshot.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotCreateTime`  <a name="cfn-redshiftserverless-snapshot-snapshot-snapshotcreatetime"></a>
The timestamp of when the snapshot was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotName`  <a name="cfn-redshiftserverless-snapshot-snapshot-snapshotname"></a>
The name of the snapshot.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-redshiftserverless-snapshot-snapshot-status"></a>
The status of the snapshot.
*Required*: No
*Type*: String
*Allowed values*: `AVAILABLE | CREATING | DELETED | CANCELLED | FAILED | COPYING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

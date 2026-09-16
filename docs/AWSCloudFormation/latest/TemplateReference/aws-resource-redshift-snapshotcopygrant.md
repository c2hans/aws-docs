---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-snapshotcopygrant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::SnapshotCopyGrant
<a name="aws-resource-redshift-snapshotcopygrant"></a>

Creates a snapshot copy grant that permits Amazon Redshift to use an encrypted symmetric key from AWS Key Management Service (KMS) to encrypt copied snapshots in a destination region.

 For more information about managing snapshot copy grants, go to [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.

## Syntax
<a name="aws-resource-redshift-snapshotcopygrant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-snapshotcopygrant-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::SnapshotCopyGrant",
  "Properties" : {
      "[KmsKeyId](#cfn-redshift-snapshotcopygrant-kmskeyid)" : {{String}},
      "[SnapshotCopyGrantName](#cfn-redshift-snapshotcopygrant-snapshotcopygrantname)" : {{String}},
      "[Tags](#cfn-redshift-snapshotcopygrant-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-snapshotcopygrant-syntax.yaml"></a>

```
Type: AWS::Redshift::SnapshotCopyGrant
Properties:
  [KmsKeyId](#cfn-redshift-snapshotcopygrant-kmskeyid): {{String}}
  [SnapshotCopyGrantName](#cfn-redshift-snapshotcopygrant-snapshotcopygrantname): {{String}}
  [Tags](#cfn-redshift-snapshotcopygrant-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-snapshotcopygrant-properties"></a>

`KmsKeyId`  <a name="cfn-redshift-snapshotcopygrant-kmskeyid"></a>
The unique identifier of the encrypted symmetric key in AWS KMS to which Amazon Redshift is granted permission.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotCopyGrantName`  <a name="cfn-redshift-snapshotcopygrant-snapshotcopygrantname"></a>
The name of the snapshot copy grant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-snapshotcopygrant-tags"></a>
A list of tag instances.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-snapshotcopygrant-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-snapshotcopygrant-return-values"></a>

### Ref
<a name="aws-resource-redshift-snapshotcopygrant-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-snapshotcopygrant-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-snapshotcopygrant-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

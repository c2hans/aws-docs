---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdbelastic-clustersnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDBElastic::ClusterSnapshot
<a name="aws-resource-docdbelastic-clustersnapshot"></a>

Returns information about a specific elastic cluster snapshot.

## Syntax
<a name="aws-resource-docdbelastic-clustersnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdbelastic-clustersnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::DocDBElastic::ClusterSnapshot",
  "Properties" : {
      "[ClusterArn](#cfn-docdbelastic-clustersnapshot-clusterarn)" : {{String}},
      "[SnapshotName](#cfn-docdbelastic-clustersnapshot-snapshotname)" : {{String}},
      "[Tags](#cfn-docdbelastic-clustersnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-docdbelastic-clustersnapshot-syntax.yaml"></a>

```
Type: AWS::DocDBElastic::ClusterSnapshot
Properties:
  [ClusterArn](#cfn-docdbelastic-clustersnapshot-clusterarn): {{String}}
  [SnapshotName](#cfn-docdbelastic-clustersnapshot-snapshotname): {{String}}
  [Tags](#cfn-docdbelastic-clustersnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-docdbelastic-clustersnapshot-properties"></a>

`ClusterArn`  <a name="cfn-docdbelastic-clustersnapshot-clusterarn"></a>
The ARN identifier of the elastic cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-docdbelastic-clustersnapshot-snapshotname"></a>
The name of the elastic cluster snapshot.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-docdbelastic-clustersnapshot-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-docdbelastic-clustersnapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-docdbelastic-clustersnapshot-return-values"></a>

### Ref
<a name="aws-resource-docdbelastic-clustersnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-docdbelastic-clustersnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-docdbelastic-clustersnapshot-return-values-fn--getatt-fn--getatt"></a>

`AdminUserName`  <a name="AdminUserName-fn::getatt"></a>
The name of the elastic cluster administrator.

`ClusterCreationTime`  <a name="ClusterCreationTime-fn::getatt"></a>
The time when the elastic cluster was created in Universal Coordinated Time (UTC).

`KmsKeyId`  <a name="KmsKeyId-fn::getatt"></a>
The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.

`SnapshotArn`  <a name="SnapshotArn-fn::getatt"></a>
The ARN identifier of the elastic cluster snapshot.

`SnapshotCreationTime`  <a name="SnapshotCreationTime-fn::getatt"></a>
The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).

`SnapshotType`  <a name="SnapshotType-fn::getatt"></a>
The type of cluster snapshots to be returned. You can specify one of the following values:
+ `automated` - Return all cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.
+ `manual` - Return all cluster snapshots that you have manually created for your AWS account.

`Status`  <a name="Status-fn::getatt"></a>
The status of the elastic cluster snapshot.

`SubnetIds`  <a name="SubnetIds-fn::getatt"></a>
The Amazon EC2 subnet IDs for the elastic cluster.

`VpcSecurityGroupIds`  <a name="VpcSecurityGroupIds-fn::getatt"></a>
A list of EC2 VPC security groups to associate with the elastic cluster.

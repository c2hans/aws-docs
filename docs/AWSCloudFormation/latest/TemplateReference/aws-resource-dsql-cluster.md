---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dsql-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DSQL::Cluster
<a name="aws-resource-dsql-cluster"></a>

The `AWS::DSQL::Cluster` resource specifies an cluster. You can use this resource to create, modify, and manage clusters.

This resource supports both single-Region clusters and multi-Region clusters through the `MultiRegionProperties` parameter.

**Note**
Creating multi-Region clusters requires additional IAM permissions beyond those needed for single-Region clusters.

**Important**
The witness Region specified in `multiRegionProperties.witnessRegion` cannot be the same as the cluster's Region.

 **Required permissions**

dsql:CreateCluster
Required to create a cluster.
Resources: `arn:aws:dsql:region:account-id:cluster/*`

dsql:TagResource
Permission to add tags to a resource.
Resources: `arn:aws:dsql:region:account-id:cluster/*`

dsql:PutMultiRegionProperties
Permission to configure multi-Region properties for a cluster.
Resources: `arn:aws:dsql:region:account-id:cluster/*`

dsql:AddPeerCluster
When specifying `multiRegionProperties.clusters`, permission to add peer clusters.
Resources:
+ Local cluster: `arn:aws:dsql:region:account-id:cluster/*`
+ Each peer cluster: exact ARN of each specified peer cluster

dsql:PutWitnessRegion
When specifying `multiRegionProperties.witnessRegion`, permission to set a witness Region. This permission is checked both in the cluster Region and in the witness Region.
Resources: `arn:aws:dsql:region:account-id:cluster/*`
Condition Keys: `dsql:WitnessRegion` (matching the specified witness region)

## Syntax
<a name="aws-resource-dsql-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dsql-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::DSQL::Cluster",
  "Properties" : {
      "[DeletionProtectionEnabled](#cfn-dsql-cluster-deletionprotectionenabled)" : {{Boolean}},
      "[KmsEncryptionKey](#cfn-dsql-cluster-kmsencryptionkey)" : {{String}},
      "[MultiRegionProperties](#cfn-dsql-cluster-multiregionproperties)" : {{MultiRegionProperties}},
      "[PolicyDocument](#cfn-dsql-cluster-policydocument)" : {{String}},
      "[Tags](#cfn-dsql-cluster-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-dsql-cluster-syntax.yaml"></a>

```
Type: AWS::DSQL::Cluster
Properties:
  [DeletionProtectionEnabled](#cfn-dsql-cluster-deletionprotectionenabled): {{Boolean}}
  [KmsEncryptionKey](#cfn-dsql-cluster-kmsencryptionkey): {{String}}
  [MultiRegionProperties](#cfn-dsql-cluster-multiregionproperties): {{
    MultiRegionProperties}}
  [PolicyDocument](#cfn-dsql-cluster-policydocument): {{String}}
  [Tags](#cfn-dsql-cluster-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-dsql-cluster-properties"></a>

`DeletionProtectionEnabled`  <a name="cfn-dsql-cluster-deletionprotectionenabled"></a>
Whether deletion protection is enabled on this cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsEncryptionKey`  <a name="cfn-dsql-cluster-kmsencryptionkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiRegionProperties`  <a name="cfn-dsql-cluster-multiregionproperties"></a>
Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.
*Required*: No
*Type*: [MultiRegionProperties](aws-properties-dsql-cluster-multiregionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDocument`  <a name="cfn-dsql-cluster-policydocument"></a>
A resource-based policy document in JSON format. Length constraints: Minimum length of 1. Maximum length of 20480 characters (approximately 20KB).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dsql-cluster-tags"></a>
A map of key and value pairs this cluster is tagged with.
*Required*: No
*Type*: Array of [Tag](aws-properties-dsql-cluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dsql-cluster-return-values"></a>

### Ref
<a name="aws-resource-dsql-cluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the cluster identifier.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dsql-cluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dsql-cluster-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The timestamp when the cluster was created, in ISO 8601 format.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The connection endpoint for the created cluster.

`Identifier`  <a name="Identifier-fn::getatt"></a>
The unique identifier assigned to the cluster upon creation.

`PolicyVersion`  <a name="PolicyVersion-fn::getatt"></a>
Property description not available.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the cluster. Used for IAM permissions and resource identification.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the cluster. Possible values include: CREATING, ACTIVE, DELETING, FAILED.
The cluster can have two additional status values when working with multi-Region clusters:
`PENDING_SETUP`—Indicates the cluster is being configured
`PENDING_DELETE`—Indicates the cluster is being deleted
**Note:** These status values only appear for multi-Region cluster operations.

`VpcEndpoint`  <a name="VpcEndpoint-fn::getatt"></a>
Property description not available.

`VpcEndpointServiceName`  <a name="VpcEndpointServiceName-fn::getatt"></a>
The VPC Endpoint Service name for the cluster. This can be used to create a VPC endpoint to connect to the cluster from within a VPC.

## See also
<a name="aws-resource-dsql-cluster--seealso"></a>

 See [ API reference](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_api_reference.html) for a full list of API operations to manage your resources in Aurora DSQL.

 See [MultiRegionProperties](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_MultiRegionProperties.html) for the data structure used for multi-Region clusters.

 See [Configuring multi-Region clusters using CloudFormation](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/mr-cluster-setup.html) to create multi-Region clusters using this CloudFormation resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

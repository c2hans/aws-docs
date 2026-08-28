---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptunegraph-graph.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::Graph
<a name="aws-resource-neptunegraph-graph"></a>

The `AWS::NeptuneGraph::Graph` resource creates an Amazon Neptune Analytics graph. Amazon Neptune Analytics is a memory-optimized graph database engine for analytics. For more information, see [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html).

You can use `AWS::NeptuneGraph::Graph.DeletionProtection` to help guard against unintended deletion of your graph.

## Syntax
<a name="aws-resource-neptunegraph-graph-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptunegraph-graph-syntax.json"></a>

```
{
  "Type" : "AWS::NeptuneGraph::Graph",
  "Properties" : {
      "[DeletionProtection](#cfn-neptunegraph-graph-deletionprotection)" : {{Boolean}},
      "[GraphName](#cfn-neptunegraph-graph-graphname)" : {{String}},
      "[KmsKeyIdentifier](#cfn-neptunegraph-graph-kmskeyidentifier)" : {{String}},
      "[ProvisionedMemory](#cfn-neptunegraph-graph-provisionedmemory)" : {{Integer}},
      "[PublicConnectivity](#cfn-neptunegraph-graph-publicconnectivity)" : {{Boolean}},
      "[ReplicaCount](#cfn-neptunegraph-graph-replicacount)" : {{Integer}},
      "[Tags](#cfn-neptunegraph-graph-tags)" : {{[ Tag, ... ]}},
      "[VectorSearchConfiguration](#cfn-neptunegraph-graph-vectorsearchconfiguration)" : {{VectorSearchConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-neptunegraph-graph-syntax.yaml"></a>

```
Type: AWS::NeptuneGraph::Graph
Properties:
  [DeletionProtection](#cfn-neptunegraph-graph-deletionprotection): {{Boolean}}
  [GraphName](#cfn-neptunegraph-graph-graphname): {{String}}
  [KmsKeyIdentifier](#cfn-neptunegraph-graph-kmskeyidentifier): {{String}}
  [ProvisionedMemory](#cfn-neptunegraph-graph-provisionedmemory): {{Integer}}
  [PublicConnectivity](#cfn-neptunegraph-graph-publicconnectivity): {{Boolean}}
  [ReplicaCount](#cfn-neptunegraph-graph-replicacount): {{Integer}}
  [Tags](#cfn-neptunegraph-graph-tags): {{
    - Tag}}
  [VectorSearchConfiguration](#cfn-neptunegraph-graph-vectorsearchconfiguration): {{
    VectorSearchConfiguration}}
```

## Properties
<a name="aws-resource-neptunegraph-graph-properties"></a>

`DeletionProtection`  <a name="cfn-neptunegraph-graph-deletionprotection"></a>
A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GraphName`  <a name="cfn-neptunegraph-graph-graphname"></a>
The graph name. For example: `my-graph-1`.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens.
If you don't specify a graph name, a unique graph name is generated for you using the prefix `graph-for`, followed by a combination of `Stack Name` and a `UUID`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyIdentifier`  <a name="cfn-neptunegraph-graph-kmskeyidentifier"></a>
The ARN of the KMS key used to encrypt data in the graph.
If not specified, the graph is encrypted with an AWS managed key.
You cannot change the KMS key after the graph is created.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProvisionedMemory`  <a name="cfn-neptunegraph-graph-provisionedmemory"></a>
The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.
Min = 16
*Required*: Yes
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PublicConnectivity`  <a name="cfn-neptunegraph-graph-publicconnectivity"></a>
Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated.
When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a `PrivateGraphEndpoint` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.
Default: If not specified, the default value is false.
If enabling public connectivity for the first time, there will be a delay while it is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicaCount`  <a name="cfn-neptunegraph-graph-replicacount"></a>
The number of replicas in other AZs.
Default: If not specified, the default value is 1.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-neptunegraph-graph-tags"></a>
Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptunegraph-graph-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VectorSearchConfiguration`  <a name="cfn-neptunegraph-graph-vectorsearchconfiguration"></a>
Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as `dimension=`value. Max = 65,535
*Required*: No
*Type*: [VectorSearchConfiguration](aws-properties-neptunegraph-graph-vectorsearchconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-neptunegraph-graph-return-values"></a>

### Ref
<a name="aws-resource-neptunegraph-graph-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the GraphId.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-neptunegraph-graph-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-neptunegraph-graph-return-values-fn--getatt-fn--getatt"></a>

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The connection endpoint for the graph. For example: `g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com`

`GraphArn`  <a name="GraphArn-fn::getatt"></a>
The ARN of the graph. For example: `arn:aws:neptune-graph:us-east-1:111122223333:graph/g-12a3bcdef4`

`GraphId`  <a name="GraphId-fn::getatt"></a>
The ID of the graph. For example: `g-12a3bcdef4`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

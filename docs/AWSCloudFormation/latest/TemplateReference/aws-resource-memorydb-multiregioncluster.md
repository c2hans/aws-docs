---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-memorydb-multiregioncluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::MultiRegionCluster
<a name="aws-resource-memorydb-multiregioncluster"></a>

Represents a multi-Region cluster.

## Syntax
<a name="aws-resource-memorydb-multiregioncluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-memorydb-multiregioncluster-syntax.json"></a>

```
{
  "Type" : "AWS::MemoryDB::MultiRegionCluster",
  "Properties" : {
      "[Description](#cfn-memorydb-multiregioncluster-description)" : {{String}},
      "[Engine](#cfn-memorydb-multiregioncluster-engine)" : {{String}},
      "[EngineVersion](#cfn-memorydb-multiregioncluster-engineversion)" : {{String}},
      "[MultiRegionClusterNameSuffix](#cfn-memorydb-multiregioncluster-multiregionclusternamesuffix)" : {{String}},
      "[MultiRegionParameterGroupName](#cfn-memorydb-multiregioncluster-multiregionparametergroupname)" : {{String}},
      "[NodeType](#cfn-memorydb-multiregioncluster-nodetype)" : {{String}},
      "[NumShards](#cfn-memorydb-multiregioncluster-numshards)" : {{Integer}},
      "[Tags](#cfn-memorydb-multiregioncluster-tags)" : {{[ Tag, ... ]}},
      "[TLSEnabled](#cfn-memorydb-multiregioncluster-tlsenabled)" : {{Boolean}},
      "[UpdateStrategy](#cfn-memorydb-multiregioncluster-updatestrategy)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-memorydb-multiregioncluster-syntax.yaml"></a>

```
Type: AWS::MemoryDB::MultiRegionCluster
Properties:
  [Description](#cfn-memorydb-multiregioncluster-description): {{String}}
  [Engine](#cfn-memorydb-multiregioncluster-engine): {{String}}
  [EngineVersion](#cfn-memorydb-multiregioncluster-engineversion): {{String}}
  [MultiRegionClusterNameSuffix](#cfn-memorydb-multiregioncluster-multiregionclusternamesuffix): {{String}}
  [MultiRegionParameterGroupName](#cfn-memorydb-multiregioncluster-multiregionparametergroupname): {{String}}
  [NodeType](#cfn-memorydb-multiregioncluster-nodetype): {{String}}
  [NumShards](#cfn-memorydb-multiregioncluster-numshards): {{Integer}}
  [Tags](#cfn-memorydb-multiregioncluster-tags): {{
    - Tag}}
  [TLSEnabled](#cfn-memorydb-multiregioncluster-tlsenabled): {{Boolean}}
  [UpdateStrategy](#cfn-memorydb-multiregioncluster-updatestrategy): {{String}}
```

## Properties
<a name="aws-resource-memorydb-multiregioncluster-properties"></a>

`Description`  <a name="cfn-memorydb-multiregioncluster-description"></a>
The description of the multi-Region cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-memorydb-multiregioncluster-engine"></a>
The name of the engine used by the multi-Region cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EngineVersion`  <a name="cfn-memorydb-multiregioncluster-engineversion"></a>
The version of the engine used by the multi-Region cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MultiRegionClusterNameSuffix`  <a name="cfn-memorydb-multiregioncluster-multiregionclusternamesuffix"></a>
A suffix to be added to the Multi-Region cluster name. Amazon MemoryDB automatically applies a prefix to the Multi-Region cluster Name when it is created. Each Amazon Region has its own prefix. For instance, a Multi-Region cluster Name created in the US-West-1 region will begin with "virxk", along with the suffix name you provide. The suffix guarantees uniqueness of the Multi-Region cluster name across multiple regions.
*Required*: No
*Type*: String
*Pattern*: `[a-z][a-z0-9\-]*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MultiRegionParameterGroupName`  <a name="cfn-memorydb-multiregioncluster-multiregionparametergroupname"></a>
The name of the multi-Region parameter group associated with the cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NodeType`  <a name="cfn-memorydb-multiregioncluster-nodetype"></a>
The node type used by the multi-Region cluster.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumShards`  <a name="cfn-memorydb-multiregioncluster-numshards"></a>
The number of shards in the multi-Region cluster.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-memorydb-multiregioncluster-tags"></a>
A list of tags to be applied to the multi-Region cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-memorydb-multiregioncluster-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TLSEnabled`  <a name="cfn-memorydb-multiregioncluster-tlsenabled"></a>
Indiciates if the multi-Region cluster is TLS enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpdateStrategy`  <a name="cfn-memorydb-multiregioncluster-updatestrategy"></a>
The strategy to use for the update operation. Supported values are "coordinated" or "uncoordinated".
*Required*: No
*Type*: String
*Allowed values*: `COORDINATED | UNCOORDINATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-memorydb-multiregioncluster-return-values"></a>

### Ref
<a name="aws-resource-memorydb-multiregioncluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-memorydb-multiregioncluster-return-values-fn--getatt"></a>

####
<a name="aws-resource-memorydb-multiregioncluster-return-values-fn--getatt-fn--getatt"></a>

`ARN`  <a name="ARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the multi-Region cluster.

`MultiRegionClusterName`  <a name="MultiRegionClusterName-fn::getatt"></a>
The name of the multi-Region cluster.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the multi-Region cluster.

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-neptunegraph-graph-vectorsearchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::Graph VectorSearchConfiguration
<a name="aws-properties-neptunegraph-graph-vectorsearchconfiguration"></a>

The vector-search configuration for the graph, which specifies the vector dimension to use in the vector index, if any.

## Syntax
<a name="aws-properties-neptunegraph-graph-vectorsearchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-neptunegraph-graph-vectorsearchconfiguration-syntax.json"></a>

```
{
  "[VectorSearchDimension](#cfn-neptunegraph-graph-vectorsearchconfiguration-vectorsearchdimension)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-neptunegraph-graph-vectorsearchconfiguration-syntax.yaml"></a>

```
  [VectorSearchDimension](#cfn-neptunegraph-graph-vectorsearchconfiguration-vectorsearchdimension): {{Integer}}
```

## Properties
<a name="aws-properties-neptunegraph-graph-vectorsearchconfiguration-properties"></a>

`VectorSearchDimension`  <a name="cfn-neptunegraph-graph-vectorsearchconfiguration-vectorsearchdimension"></a>
The number of dimensions.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

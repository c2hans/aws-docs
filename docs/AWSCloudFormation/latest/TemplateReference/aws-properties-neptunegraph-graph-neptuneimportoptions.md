---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-neptunegraph-graph-neptuneimportoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::Graph NeptuneImportOptions
<a name="aws-properties-neptunegraph-graph-neptuneimportoptions"></a>

Options for how to import Neptune data.

## Syntax
<a name="aws-properties-neptunegraph-graph-neptuneimportoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-neptunegraph-graph-neptuneimportoptions-syntax.json"></a>

```
{
  "[PreserveDefaultVertexLabels](#cfn-neptunegraph-graph-neptuneimportoptions-preservedefaultvertexlabels)" : {{Boolean}},
  "[PreserveEdgeIds](#cfn-neptunegraph-graph-neptuneimportoptions-preserveedgeids)" : {{Boolean}},
  "[S3ExportKmsKeyId](#cfn-neptunegraph-graph-neptuneimportoptions-s3exportkmskeyid)" : {{String}},
  "[S3ExportPath](#cfn-neptunegraph-graph-neptuneimportoptions-s3exportpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-neptunegraph-graph-neptuneimportoptions-syntax.yaml"></a>

```
  [PreserveDefaultVertexLabels](#cfn-neptunegraph-graph-neptuneimportoptions-preservedefaultvertexlabels): {{Boolean}}
  [PreserveEdgeIds](#cfn-neptunegraph-graph-neptuneimportoptions-preserveedgeids): {{Boolean}}
  [S3ExportKmsKeyId](#cfn-neptunegraph-graph-neptuneimportoptions-s3exportkmskeyid): {{String}}
  [S3ExportPath](#cfn-neptunegraph-graph-neptuneimportoptions-s3exportpath): {{String}}
```

## Properties
<a name="aws-properties-neptunegraph-graph-neptuneimportoptions-properties"></a>

`PreserveDefaultVertexLabels`  <a name="cfn-neptunegraph-graph-neptuneimportoptions-preservedefaultvertexlabels"></a>
Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided. Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting `preserveDefaultVertexLabels` to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when `preserveDefaultVertexLabels` is set to false.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreserveEdgeIds`  <a name="cfn-neptunegraph-graph-neptuneimportoptions-preserveedgeids"></a>
Neptune Analytics currently does not support user-defined edge IDs. The edge IDs are not imported by default. They are imported if `preserveEdgeIds` is set to true, and IDs are stored as properties on the relationships with the property name `neptuneEdgeId`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3ExportKmsKeyId`  <a name="cfn-neptunegraph-graph-neptuneimportoptions-s3exportkmskeyid"></a>
The KMS key used to encrypt data in the S3 bucket where the graph data is exported.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3ExportPath`  <a name="cfn-neptunegraph-graph-neptuneimportoptions-s3exportpath"></a>
The path to an S3 bucket from which to import data.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

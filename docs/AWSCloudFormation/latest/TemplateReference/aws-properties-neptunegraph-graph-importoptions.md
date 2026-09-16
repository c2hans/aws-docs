---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-neptunegraph-graph-importoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::Graph ImportOptions
<a name="aws-properties-neptunegraph-graph-importoptions"></a>

Options for how to perform an import.

## Syntax
<a name="aws-properties-neptunegraph-graph-importoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-neptunegraph-graph-importoptions-syntax.json"></a>

```
{
  "[Neptune](#cfn-neptunegraph-graph-importoptions-neptune)" : {{NeptuneImportOptions}}
}
```

### YAML
<a name="aws-properties-neptunegraph-graph-importoptions-syntax.yaml"></a>

```
  [Neptune](#cfn-neptunegraph-graph-importoptions-neptune): {{
    NeptuneImportOptions}}
```

## Properties
<a name="aws-properties-neptunegraph-graph-importoptions-properties"></a>

`Neptune`  <a name="cfn-neptunegraph-graph-importoptions-neptune"></a>
Options for importing data from a Neptune database.
*Required*: No
*Type*: [NeptuneImportOptions](aws-properties-neptunegraph-graph-neptuneimportoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

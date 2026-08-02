---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-nodeoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain NodeOption
<a name="aws-properties-opensearchservice-domain-nodeoption"></a>

Configuration settings for defining the node type within a cluster.

## Syntax
<a name="aws-properties-opensearchservice-domain-nodeoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-nodeoption-syntax.json"></a>

```
{
  "[NodeConfig](#cfn-opensearchservice-domain-nodeoption-nodeconfig)" : {{NodeConfig}},
  "[NodeType](#cfn-opensearchservice-domain-nodeoption-nodetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-nodeoption-syntax.yaml"></a>

```
  [NodeConfig](#cfn-opensearchservice-domain-nodeoption-nodeconfig): {{
    NodeConfig}}
  [NodeType](#cfn-opensearchservice-domain-nodeoption-nodetype): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-nodeoption-properties"></a>

`NodeConfig`  <a name="cfn-opensearchservice-domain-nodeoption-nodeconfig"></a>
Configuration options for defining the setup of any node type.
*Required*: No
*Type*: [NodeConfig](aws-properties-opensearchservice-domain-nodeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeType`  <a name="cfn-opensearchservice-domain-nodeoption-nodetype"></a>
Defines the type of node, such as coordinating nodes.
*Required*: No
*Type*: String
*Allowed values*: `coordinator`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

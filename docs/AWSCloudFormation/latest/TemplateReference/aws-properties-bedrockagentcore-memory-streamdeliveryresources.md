---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-streamdeliveryresources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory StreamDeliveryResources
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresources"></a>

Configuration for streaming memory record data to external resources.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresources-syntax.json"></a>

```
{
  "[Resources](#cfn-bedrockagentcore-memory-streamdeliveryresources-resources)" : {{[ StreamDeliveryResource, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresources-syntax.yaml"></a>

```
  [Resources](#cfn-bedrockagentcore-memory-streamdeliveryresources-resources): {{
    - StreamDeliveryResource}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresources-properties"></a>

`Resources`  <a name="cfn-bedrockagentcore-memory-streamdeliveryresources-resources"></a>
List of stream delivery resource configurations.
*Required*: Yes
*Type*: Array of [StreamDeliveryResource](aws-properties-bedrockagentcore-memory-streamdeliveryresource.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

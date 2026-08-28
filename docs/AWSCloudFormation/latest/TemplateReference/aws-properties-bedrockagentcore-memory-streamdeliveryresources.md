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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

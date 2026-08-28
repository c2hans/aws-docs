---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-streamdeliveryresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory StreamDeliveryResource
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresource"></a>

Supported stream delivery resource types.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresource-syntax.json"></a>

```
{
  "[Kinesis](#cfn-bedrockagentcore-memory-streamdeliveryresource-kinesis)" : {{KinesisResource}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresource-syntax.yaml"></a>

```
  [Kinesis](#cfn-bedrockagentcore-memory-streamdeliveryresource-kinesis): {{
    KinesisResource}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-streamdeliveryresource-properties"></a>

`Kinesis`  <a name="cfn-bedrockagentcore-memory-streamdeliveryresource-kinesis"></a>
Kinesis Data Stream configuration.
*Required*: No
*Type*: [KinesisResource](aws-properties-bedrockagentcore-memory-kinesisresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

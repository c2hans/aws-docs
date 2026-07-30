---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-kinesisresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory KinesisResource
<a name="aws-properties-bedrockagentcore-memory-kinesisresource"></a>

Configuration for Kinesis Data Stream delivery.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-kinesisresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-kinesisresource-syntax.json"></a>

```
{
  "[ContentConfigurations](#cfn-bedrockagentcore-memory-kinesisresource-contentconfigurations)" : {{[ ContentConfiguration, ... ]}},
  "[DataStreamArn](#cfn-bedrockagentcore-memory-kinesisresource-datastreamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-kinesisresource-syntax.yaml"></a>

```
  [ContentConfigurations](#cfn-bedrockagentcore-memory-kinesisresource-contentconfigurations): {{
    - ContentConfiguration}}
  [DataStreamArn](#cfn-bedrockagentcore-memory-kinesisresource-datastreamarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-kinesisresource-properties"></a>

`ContentConfigurations`  <a name="cfn-bedrockagentcore-memory-kinesisresource-contentconfigurations"></a>
Content configurations for stream delivery.
*Required*: Yes
*Type*: Array of [ContentConfiguration](aws-properties-bedrockagentcore-memory-contentconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataStreamArn`  <a name="cfn-bedrockagentcore-memory-kinesisresource-datastreamarn"></a>
ARN of the Kinesis Data Stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

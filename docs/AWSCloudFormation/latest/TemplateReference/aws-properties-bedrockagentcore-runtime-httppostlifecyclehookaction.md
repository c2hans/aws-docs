---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-httppostlifecyclehookaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime HttpPostLifecycleHookAction

<a name="aws-properties-bedrockagentcore-runtime-httppostlifecyclehookaction-description"></a>The `HttpPostLifecycleHookAction` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Runtime](aws-resource-bedrockagentcore-runtime.md).

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-httppostlifecyclehookaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-httppostlifecyclehookaction-syntax.json"></a>

```json
{
  "[Path](#cfn-bedrockagentcore-runtime-httppostlifecyclehookaction-path)" : {{String}},
  "[Port](#cfn-bedrockagentcore-runtime-httppostlifecyclehookaction-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-httppostlifecyclehookaction-syntax.yaml"></a>

```yaml
  [Path](#cfn-bedrockagentcore-runtime-httppostlifecyclehookaction-path): {{String}}
  [Port](#cfn-bedrockagentcore-runtime-httppostlifecyclehookaction-port): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-httppostlifecyclehookaction-properties"></a>

`Path`  <a name="cfn-bedrockagentcore-runtime-httppostlifecyclehookaction-path"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^/[A-Za-z0-9._~/-]*$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-bedrockagentcore-runtime-httppostlifecyclehookaction-port"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `8000`
*Maximum*: `12000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

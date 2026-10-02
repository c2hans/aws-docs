---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessBeforeInvocationHook
<a name="aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook"></a>

<a name="aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook-description"></a>The `HarnessBeforeInvocationHook` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Harness](aws-resource-bedrockagentcore-harness.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook-syntax.json"></a>

```
{
  "[Name](#cfn-bedrockagentcore-harness-harnessbeforeinvocationhook-name)" : {{String}},
  "[Target](#cfn-bedrockagentcore-harness-harnessbeforeinvocationhook-target)" : {{HarnessHookTarget}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook-syntax.yaml"></a>

```
  [Name](#cfn-bedrockagentcore-harness-harnessbeforeinvocationhook-name): {{String}}
  [Target](#cfn-bedrockagentcore-harness-harnessbeforeinvocationhook-target): {{
    HarnessHookTarget}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook-properties"></a>

`Name`  <a name="cfn-bedrockagentcore-harness-harnessbeforeinvocationhook-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-bedrockagentcore-harness-harnessbeforeinvocationhook-target"></a>
Property description not available.
*Required*: Yes
*Type*: [HarnessHookTarget](aws-properties-bedrockagentcore-harness-harnesshooktarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

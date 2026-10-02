---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesshook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessHook
<a name="aws-properties-bedrockagentcore-harness-harnesshook"></a>

<a name="aws-properties-bedrockagentcore-harness-harnesshook-description"></a>The `HarnessHook` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Harness](aws-resource-bedrockagentcore-harness.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesshook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesshook-syntax.json"></a>

```
{
  "[AfterInvocation](#cfn-bedrockagentcore-harness-harnesshook-afterinvocation)" : {{HarnessAfterInvocationHook}},
  "[AfterToolCall](#cfn-bedrockagentcore-harness-harnesshook-aftertoolcall)" : {{HarnessAfterToolCallHook}},
  "[BeforeInvocation](#cfn-bedrockagentcore-harness-harnesshook-beforeinvocation)" : {{HarnessBeforeInvocationHook}},
  "[BeforeToolCall](#cfn-bedrockagentcore-harness-harnesshook-beforetoolcall)" : {{HarnessBeforeToolCallHook}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesshook-syntax.yaml"></a>

```
  [AfterInvocation](#cfn-bedrockagentcore-harness-harnesshook-afterinvocation): {{
    HarnessAfterInvocationHook}}
  [AfterToolCall](#cfn-bedrockagentcore-harness-harnesshook-aftertoolcall): {{
    HarnessAfterToolCallHook}}
  [BeforeInvocation](#cfn-bedrockagentcore-harness-harnesshook-beforeinvocation): {{
    HarnessBeforeInvocationHook}}
  [BeforeToolCall](#cfn-bedrockagentcore-harness-harnesshook-beforetoolcall): {{
    HarnessBeforeToolCallHook}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesshook-properties"></a>

`AfterInvocation`  <a name="cfn-bedrockagentcore-harness-harnesshook-afterinvocation"></a>
Property description not available.
*Required*: No
*Type*: [HarnessAfterInvocationHook](aws-properties-bedrockagentcore-harness-harnessafterinvocationhook.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AfterToolCall`  <a name="cfn-bedrockagentcore-harness-harnesshook-aftertoolcall"></a>
Property description not available.
*Required*: No
*Type*: [HarnessAfterToolCallHook](aws-properties-bedrockagentcore-harness-harnessaftertoolcallhook.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BeforeInvocation`  <a name="cfn-bedrockagentcore-harness-harnesshook-beforeinvocation"></a>
Property description not available.
*Required*: No
*Type*: [HarnessBeforeInvocationHook](aws-properties-bedrockagentcore-harness-harnessbeforeinvocationhook.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BeforeToolCall`  <a name="cfn-bedrockagentcore-harness-harnesshook-beforetoolcall"></a>
Property description not available.
*Required*: No
*Type*: [HarnessBeforeToolCallHook](aws-properties-bedrockagentcore-harness-harnessbeforetoolcallhook.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-lifecycleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime LifecycleConfiguration
<a name="aws-properties-bedrockagentcore-runtime-lifecycleconfiguration"></a>

The lifecycle configuration for the AgentCore Runtime.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-lifecycleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-lifecycleconfiguration-syntax.json"></a>

```
{
  "[IdleRuntimeSessionTimeout](#cfn-bedrockagentcore-runtime-lifecycleconfiguration-idleruntimesessiontimeout)" : {{Integer}},
  "[MaxLifetime](#cfn-bedrockagentcore-runtime-lifecycleconfiguration-maxlifetime)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-lifecycleconfiguration-syntax.yaml"></a>

```
  [IdleRuntimeSessionTimeout](#cfn-bedrockagentcore-runtime-lifecycleconfiguration-idleruntimesessiontimeout): {{Integer}}
  [MaxLifetime](#cfn-bedrockagentcore-runtime-lifecycleconfiguration-maxlifetime): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-lifecycleconfiguration-properties"></a>

`IdleRuntimeSessionTimeout`  <a name="cfn-bedrockagentcore-runtime-lifecycleconfiguration-idleruntimesessiontimeout"></a>
The idle session timeout for the AgentCore Runtime.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `1209600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxLifetime`  <a name="cfn-bedrockagentcore-runtime-lifecycleconfiguration-maxlifetime"></a>
The maximum lifetime for the AgentCore Runtime.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `1209600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

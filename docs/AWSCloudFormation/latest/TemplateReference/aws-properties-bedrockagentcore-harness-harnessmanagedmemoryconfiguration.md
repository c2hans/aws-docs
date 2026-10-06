---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessManagedMemoryConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration"></a>

Configuration for managed memory creation.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-arn)" : {{String}},
  "[EncryptionKeyArn](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-encryptionkeyarn)" : {{String}},
  "[EventExpiryDuration](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-eventexpiryduration)" : {{Integer}},
  "[Strategies](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-strategies)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-arn): {{String}}
  [EncryptionKeyArn](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-encryptionkeyarn): {{String}}
  [EventExpiryDuration](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-eventexpiryduration): {{Integer}}
  [Strategies](#cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-strategies): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-arn"></a>
The ARN of the managed AgentCore Memory resource. Read-only on Get, ignored on Create/Update input.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyArn`  <a name="cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-encryptionkeyarn"></a>
Customer-managed KMS key. Defaults to AWS-owned key. Not updatable after creation.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventExpiryDuration`  <a name="cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-eventexpiryduration"></a>
Event retention in days. Defaults to 30.
*Required*: No
*Type*: Integer
*Minimum*: `3`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strategies`  <a name="cfn-bedrockagentcore-harness-harnessmanagedmemoryconfiguration-strategies"></a>
Strategy types to enable. Defaults to [SEMANTIC, SUMMARIZATION].
*Required*: No
*Type*: Array of String
*Allowed values*: `SEMANTIC | SUMMARIZATION | USER_PREFERENCE | EPISODIC`
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

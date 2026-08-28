---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-policyengine.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PolicyEngine
<a name="aws-resource-bedrockagentcore-policyengine"></a>

Specifies a policy engine for Amazon Bedrock AgentCore. A policy engine provides Cedar-based authorization to control what actions your AI agents can perform.

For more information, see [Control agent actions with Amazon Bedrock AgentCore policy engines](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-engine.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-policyengine-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-policyengine-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::PolicyEngine",
  "Properties" : {
      "[Description](#cfn-bedrockagentcore-policyengine-description)" : {{String}},
      "[EncryptionKeyArn](#cfn-bedrockagentcore-policyengine-encryptionkeyarn)" : {{String}},
      "[Name](#cfn-bedrockagentcore-policyengine-name)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-policyengine-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-policyengine-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::PolicyEngine
Properties:
  [Description](#cfn-bedrockagentcore-policyengine-description): {{String}}
  [EncryptionKeyArn](#cfn-bedrockagentcore-policyengine-encryptionkeyarn): {{String}}
  [Name](#cfn-bedrockagentcore-policyengine-name): {{String}}
  [Tags](#cfn-bedrockagentcore-policyengine-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-policyengine-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-policyengine-description"></a>
A human-readable description of the policy engine's purpose and scope. Limited to 4,096 characters, this helps administrators understand the policy engine's role in the overall governance strategy.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyArn`  <a name="cfn-bedrockagentcore-policyengine-encryptionkeyarn"></a>
The ARN of the KMS key used to encrypt the policy engine data.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-policyengine-name"></a>
The customer-assigned immutable name for the policy engine. This human-readable identifier must be unique within the account and cannot exceed 48 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]*$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-policyengine-tags"></a>
The tags for the policy engine.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-policyengine-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-policyengine-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-policyengine-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the policy engine. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/MyPolicyEngine-a1b2c3d4e5`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-policyengine-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-policyengine-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the policy engine was created.

`PolicyEngineArn`  <a name="PolicyEngineArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the policy engine.

`PolicyEngineId`  <a name="PolicyEngineId-fn::getatt"></a>
The unique identifier of the policy engine.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the policy engine.

`StatusReasons`  <a name="StatusReasons-fn::getatt"></a>
Additional information about the current status of the policy engine.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the policy engine was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

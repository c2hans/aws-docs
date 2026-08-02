---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Policy
<a name="aws-resource-bedrockagentcore-policy"></a>

Specifies a Cedar authorization policy within an Amazon Bedrock AgentCore policy engine. A policy defines the authorization logic that controls what actions your AI agents can perform.

For more information, see [Control agent actions with Amazon Bedrock AgentCore policy engines](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-engine.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-policy-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Policy",
  "Properties" : {
      "[Definition](#cfn-bedrockagentcore-policy-definition)" : {{PolicyDefinition}},
      "[Description](#cfn-bedrockagentcore-policy-description)" : {{String}},
      "[EnforcementMode](#cfn-bedrockagentcore-policy-enforcementmode)" : {{String}},
      "[Name](#cfn-bedrockagentcore-policy-name)" : {{String}},
      "[PolicyEngineId](#cfn-bedrockagentcore-policy-policyengineid)" : {{String}},
      "[ValidationMode](#cfn-bedrockagentcore-policy-validationmode)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-policy-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Policy
Properties:
  [Definition](#cfn-bedrockagentcore-policy-definition): {{
    PolicyDefinition}}
  [Description](#cfn-bedrockagentcore-policy-description): {{String}}
  [EnforcementMode](#cfn-bedrockagentcore-policy-enforcementmode): {{String}}
  [Name](#cfn-bedrockagentcore-policy-name): {{String}}
  [PolicyEngineId](#cfn-bedrockagentcore-policy-policyengineid): {{String}}
  [ValidationMode](#cfn-bedrockagentcore-policy-validationmode): {{String}}
```

## Properties
<a name="aws-resource-bedrockagentcore-policy-properties"></a>

`Definition`  <a name="cfn-bedrockagentcore-policy-definition"></a>
The Cedar policy statement that defines the access control rules. This contains the actual policy logic used for agent behavior control and access decisions.
*Required*: Yes
*Type*: [PolicyDefinition](aws-properties-bedrockagentcore-policy-policydefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-policy-description"></a>
A human-readable description of the policy's purpose and functionality. Limited to 4,096 characters, this helps administrators understand and manage the policy.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnforcementMode`  <a name="cfn-bedrockagentcore-policy-enforcementmode"></a>
The enforcement mode for the policy. Determines whether the policy contributes to the enforce decision. Valid values include:
+ `ACTIVE` - The policy is evaluated and its decision is enforced by the policy engine.
+ `LOG_ONLY` - The policy is evaluated but its decision is observed only, allowing you to validate a policy against real traffic before promoting it to active enforcement.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | LOG_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-policy-name"></a>
The customer-assigned immutable name for the policy. This human-readable identifier must be unique within the account and cannot exceed 48 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]*$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyEngineId`  <a name="cfn-bedrockagentcore-policy-policyengineid"></a>
The identifier of the policy engine that manages this policy. This establishes the policy engine context for policy evaluation and management.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}$`
*Minimum*: `12`
*Maximum*: `59`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ValidationMode`  <a name="cfn-bedrockagentcore-policy-validationmode"></a>
The validation mode for the policy. Determines how Cedar analyzer validation results are handled.
*Required*: No
*Type*: String
*Allowed values*: `FAIL_ON_ANY_FINDINGS | IGNORE_ALL_FINDINGS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-policy-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-policy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the policy. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/MyPolicyEngine-a1b2c3d4e5/policy/MyPolicy-f6g7h8i9j0`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-policy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-policy-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the policy was created.

`PolicyArn`  <a name="PolicyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the policy.

`PolicyId`  <a name="PolicyId-fn::getatt"></a>
The unique identifier of the policy.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the policy.

`StatusReasons`  <a name="StatusReasons-fn::getatt"></a>
Additional information about the current status of the policy.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the policy was last updated.

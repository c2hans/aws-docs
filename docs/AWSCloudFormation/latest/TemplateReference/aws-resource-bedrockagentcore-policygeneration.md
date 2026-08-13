---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-policygeneration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PolicyGeneration
<a name="aws-resource-bedrockagentcore-policygeneration"></a>

<a name="aws-resource-bedrockagentcore-policygeneration-description"></a>The `AWS::BedrockAgentCore::PolicyGeneration` resource Property description not available. for BedrockAgentCore.

## Syntax
<a name="aws-resource-bedrockagentcore-policygeneration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-policygeneration-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::PolicyGeneration",
  "Properties" : {
      "[Name](#cfn-bedrockagentcore-policygeneration-name)" : {{String}},
      "[PolicyEngineId](#cfn-bedrockagentcore-policygeneration-policyengineid)" : {{String}},
      "[Resource](#cfn-bedrockagentcore-policygeneration-resource)" : {{Resource}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-policygeneration-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::PolicyGeneration
Properties:
  [Name](#cfn-bedrockagentcore-policygeneration-name): {{String}}
  [PolicyEngineId](#cfn-bedrockagentcore-policygeneration-policyengineid): {{String}}
  [Resource](#cfn-bedrockagentcore-policygeneration-resource): {{
    Resource}}
```

## Properties
<a name="aws-resource-bedrockagentcore-policygeneration-properties"></a>

`Name`  <a name="cfn-bedrockagentcore-policygeneration-name"></a>
The customer-assigned name for this policy generation request.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]*$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyEngineId`  <a name="cfn-bedrockagentcore-policygeneration-policyengineid"></a>
The identifier of the policy engine associated with this generation request.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}$`
*Minimum*: `12`
*Maximum*: `59`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resource`  <a name="cfn-bedrockagentcore-policygeneration-resource"></a>
The resource information associated with this policy generation.
*Required*: Yes
*Type*: [Resource](aws-properties-bedrockagentcore-policygeneration-resource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrockagentcore-policygeneration-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-policygeneration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-policygeneration-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-policygeneration-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when this policy generation request was created.

`PolicyGenerationArn`  <a name="PolicyGenerationArn-fn::getatt"></a>
The ARN of this policy generation request.

`PolicyGenerationId`  <a name="PolicyGenerationId-fn::getatt"></a>
The unique identifier for this policy generation request.

`Status`  <a name="Status-fn::getatt"></a>
The current status of this policy generation request.

`StatusReasons`  <a name="StatusReasons-fn::getatt"></a>
Additional information about the generation status.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when this policy generation was last updated.

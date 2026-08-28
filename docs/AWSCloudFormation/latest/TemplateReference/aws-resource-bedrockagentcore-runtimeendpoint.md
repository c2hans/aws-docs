---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-runtimeendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::RuntimeEndpoint
<a name="aws-resource-bedrockagentcore-runtimeendpoint"></a>

AgentCore Runtime is a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools using any open-source framework including LangGraph, CrewAI, and Strands Agents, any protocol, and any model.

For more information about using agent runtime endpoints in Amazon Bedrock AgentCore, see [AgentCore Runtime versioning and endpoints](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-runtime-versioning.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-runtimeendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-runtimeendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::RuntimeEndpoint",
  "Properties" : {
      "[AgentRuntimeId](#cfn-bedrockagentcore-runtimeendpoint-agentruntimeid)" : {{String}},
      "[AgentRuntimeVersion](#cfn-bedrockagentcore-runtimeendpoint-agentruntimeversion)" : {{String}},
      "[Description](#cfn-bedrockagentcore-runtimeendpoint-description)" : {{String}},
      "[Name](#cfn-bedrockagentcore-runtimeendpoint-name)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-runtimeendpoint-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-runtimeendpoint-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::RuntimeEndpoint
Properties:
  [AgentRuntimeId](#cfn-bedrockagentcore-runtimeendpoint-agentruntimeid): {{String}}
  [AgentRuntimeVersion](#cfn-bedrockagentcore-runtimeendpoint-agentruntimeversion): {{String}}
  [Description](#cfn-bedrockagentcore-runtimeendpoint-description): {{String}}
  [Name](#cfn-bedrockagentcore-runtimeendpoint-name): {{String}}
  [Tags](#cfn-bedrockagentcore-runtimeendpoint-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-runtimeendpoint-properties"></a>

`AgentRuntimeId`  <a name="cfn-bedrockagentcore-runtimeendpoint-agentruntimeid"></a>
The unique identifier of the AgentCore Runtime.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AgentRuntimeVersion`  <a name="cfn-bedrockagentcore-runtimeendpoint-agentruntimeversion"></a>
The version of the AgentCore Runtime to use for the endpoint.
*Required*: No
*Type*: String
*Pattern*: `^([1-9][0-9]{0,4})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-runtimeendpoint-description"></a>
The description of the AgentCore Runtime endpoint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-runtimeendpoint-name"></a>
The name of the AgentCore Runtime endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-runtimeendpoint-tags"></a>
The tags for the AgentCore Runtime endpoint.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-runtimeendpoint-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-runtimeendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the runtime endpoint. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/MyRuntime-a1b2c3d4e5/runtime-endpoint/MyEndpoint-f6g7h8i9j0`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-runtimeendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-runtimeendpoint-return-values-fn--getatt-fn--getatt"></a>

`AgentRuntimeArn`  <a name="AgentRuntimeArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime.

`AgentRuntimeEndpointArn`  <a name="AgentRuntimeEndpointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the AgentCore Runtime endpoint was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reason for failure if the AgentCore Runtime endpoint is in a failed state.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the AgentCore Runtime endpoint.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp when the AgentCore Runtime endpoint was last updated.

`LiveVersion`  <a name="LiveVersion-fn::getatt"></a>
The currently deployed version of the AgentCore Runtime on the endpoint.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the AgentCore Runtime endpoint.

`TargetVersion`  <a name="TargetVersion-fn::getatt"></a>
The target version of the AgentCore Runtime for the endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

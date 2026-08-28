---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-runtime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime
<a name="aws-resource-bedrockagentcore-runtime"></a>

Contains information about an agent runtime. An agent runtime is the execution environment for a Amazon Bedrock Agent.

AgentCore Runtime is a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools using any open-source framework including LangGraph, CrewAI, and Strands Agents, any protocol, and any model.

For more information about using agent runtime in Amazon Bedrock AgentCore, see [Host agent or tools with Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-runtime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-runtime-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Runtime",
  "Properties" : {
      "[AgentRuntimeArtifact](#cfn-bedrockagentcore-runtime-agentruntimeartifact)" : {{AgentRuntimeArtifact}},
      "[AgentRuntimeName](#cfn-bedrockagentcore-runtime-agentruntimename)" : {{String}},
      "[AuthorizerConfiguration](#cfn-bedrockagentcore-runtime-authorizerconfiguration)" : {{AuthorizerConfiguration}},
      "[CapacityProviderConfiguration](#cfn-bedrockagentcore-runtime-capacityproviderconfiguration)" : {{CapacityProviderConfiguration}},
      "[Description](#cfn-bedrockagentcore-runtime-description)" : {{String}},
      "[EnvironmentVariables](#cfn-bedrockagentcore-runtime-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
      "[FilesystemConfigurations](#cfn-bedrockagentcore-runtime-filesystemconfigurations)" : {{[ FilesystemConfiguration, ... ]}},
      "[LifecycleConfiguration](#cfn-bedrockagentcore-runtime-lifecycleconfiguration)" : {{LifecycleConfiguration}},
      "[NetworkConfiguration](#cfn-bedrockagentcore-runtime-networkconfiguration)" : {{NetworkConfiguration}},
      "[ProtocolConfiguration](#cfn-bedrockagentcore-runtime-protocolconfiguration)" : {{String}},
      "[RequestHeaderConfiguration](#cfn-bedrockagentcore-runtime-requestheaderconfiguration)" : {{RequestHeaderConfiguration}},
      "[RoleArn](#cfn-bedrockagentcore-runtime-rolearn)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-runtime-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-runtime-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Runtime
Properties:
  [AgentRuntimeArtifact](#cfn-bedrockagentcore-runtime-agentruntimeartifact): {{
    AgentRuntimeArtifact}}
  [AgentRuntimeName](#cfn-bedrockagentcore-runtime-agentruntimename): {{String}}
  [AuthorizerConfiguration](#cfn-bedrockagentcore-runtime-authorizerconfiguration): {{
    AuthorizerConfiguration}}
  [CapacityProviderConfiguration](#cfn-bedrockagentcore-runtime-capacityproviderconfiguration): {{
    CapacityProviderConfiguration}}
  [Description](#cfn-bedrockagentcore-runtime-description): {{String}}
  [EnvironmentVariables](#cfn-bedrockagentcore-runtime-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [FilesystemConfigurations](#cfn-bedrockagentcore-runtime-filesystemconfigurations): {{
    - FilesystemConfiguration}}
  [LifecycleConfiguration](#cfn-bedrockagentcore-runtime-lifecycleconfiguration): {{
    LifecycleConfiguration}}
  [NetworkConfiguration](#cfn-bedrockagentcore-runtime-networkconfiguration): {{
    NetworkConfiguration}}
  [ProtocolConfiguration](#cfn-bedrockagentcore-runtime-protocolconfiguration): {{String}}
  [RequestHeaderConfiguration](#cfn-bedrockagentcore-runtime-requestheaderconfiguration): {{
    RequestHeaderConfiguration}}
  [RoleArn](#cfn-bedrockagentcore-runtime-rolearn): {{String}}
  [Tags](#cfn-bedrockagentcore-runtime-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-runtime-properties"></a>

`AgentRuntimeArtifact`  <a name="cfn-bedrockagentcore-runtime-agentruntimeartifact"></a>
The artifact of the AgentCore Runtime.
*Required*: Yes
*Type*: [AgentRuntimeArtifact](aws-properties-bedrockagentcore-runtime-agentruntimeartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentRuntimeName`  <a name="cfn-bedrockagentcore-runtime-agentruntimename"></a>
The name of the AgentCore Runtime.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z][a-zA-Z0-9_]{0,47}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthorizerConfiguration`  <a name="cfn-bedrockagentcore-runtime-authorizerconfiguration"></a>
The authorizer configuration for the AgentCore Runtime.
*Required*: No
*Type*: [AuthorizerConfiguration](aws-properties-bedrockagentcore-runtime-authorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityProviderConfiguration`  <a name="cfn-bedrockagentcore-runtime-capacityproviderconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [CapacityProviderConfiguration](aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-runtime-description"></a>
The description of the AgentCore Runtime.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-bedrockagentcore-runtime-environmentvariables"></a>
Environment variables to set in the AgentCore Runtime environment.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilesystemConfigurations`  <a name="cfn-bedrockagentcore-runtime-filesystemconfigurations"></a>
The filesystem configurations for the runtime environment.
*Required*: No
*Type*: Array of [FilesystemConfiguration](aws-properties-bedrockagentcore-runtime-filesystemconfiguration.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfiguration`  <a name="cfn-bedrockagentcore-runtime-lifecycleconfiguration"></a>
The lifecycle configuration for the AgentCore Runtime.
*Required*: No
*Type*: [LifecycleConfiguration](aws-properties-bedrockagentcore-runtime-lifecycleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-bedrockagentcore-runtime-networkconfiguration"></a>
The network configuration for the AgentCore Runtime.
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-bedrockagentcore-runtime-networkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-bedrockagentcore-runtime-protocolconfiguration"></a>
The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.
*Required*: No
*Type*: String
*Allowed values*: `MCP | HTTP | A2A | AGUI`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequestHeaderConfiguration`  <a name="cfn-bedrockagentcore-runtime-requestheaderconfiguration"></a>
Configuration for HTTP request headers that will be passed through to the runtime.
*Required*: No
*Type*: [RequestHeaderConfiguration](aws-properties-bedrockagentcore-runtime-requestheaderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-bedrockagentcore-runtime-rolearn"></a>
The IAM role ARN that provides permissions for the AgentCore Runtime.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-runtime-tags"></a>
The tags for the agent.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-runtime-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-runtime-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the agent runtime. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/MyRuntime-a1b2c3d4e5`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-runtime-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-runtime-return-values-fn--getatt-fn--getatt"></a>

`AgentRuntimeArn`  <a name="AgentRuntimeArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime.

`AgentRuntimeId`  <a name="AgentRuntimeId-fn::getatt"></a>
The unique identifier of the AgentCore Runtime.

`AgentRuntimeVersion`  <a name="AgentRuntimeVersion-fn::getatt"></a>
The version of the AgentCore Runtime.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the AgentCore Runtime was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reason for failure if the AgentCore Runtime is in a failed state.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp when the AgentCore Runtime was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the AgentCore Runtime.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

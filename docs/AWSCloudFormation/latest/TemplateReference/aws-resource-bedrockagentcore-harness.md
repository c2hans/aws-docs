---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-harness.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness
<a name="aws-resource-bedrockagentcore-harness"></a>

Specifies a harness for Amazon Bedrock AgentCore. A harness is a managed agent loop that lets you define and invoke AI agents with a single API call. Specify a model, system prompt, and tools inline — the harness handles orchestration, tool execution, memory management, and response generation. Each session runs in an isolated microVM with filesystem and shell access, supporting use cases like code generation, data analysis, and deep research.

For more information, see [Build agents with Amazon Bedrock AgentCore Harness](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-harness-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-harness-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Harness",
  "Properties" : {
      "[AllowedTools](#cfn-bedrockagentcore-harness-allowedtools)" : {{[ String, ... ]}},
      "[AuthorizerConfiguration](#cfn-bedrockagentcore-harness-authorizerconfiguration)" : {{AuthorizerConfiguration}},
      "[Environment](#cfn-bedrockagentcore-harness-environment)" : {{HarnessEnvironmentProvider}},
      "[EnvironmentArtifact](#cfn-bedrockagentcore-harness-environmentartifact)" : {{HarnessEnvironmentArtifact}},
      "[EnvironmentVariables](#cfn-bedrockagentcore-harness-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ExecutionRoleArn](#cfn-bedrockagentcore-harness-executionrolearn)" : {{String}},
      "[HarnessName](#cfn-bedrockagentcore-harness-harnessname)" : {{String}},
      "[MaxIterations](#cfn-bedrockagentcore-harness-maxiterations)" : {{Integer}},
      "[MaxTokens](#cfn-bedrockagentcore-harness-maxtokens)" : {{Integer}},
      "[Memory](#cfn-bedrockagentcore-harness-memory)" : {{HarnessMemoryConfiguration}},
      "[Model](#cfn-bedrockagentcore-harness-model)" : {{HarnessModelConfiguration}},
      "[Skills](#cfn-bedrockagentcore-harness-skills)" : {{[ HarnessSkill, ... ]}},
      "[SystemPrompt](#cfn-bedrockagentcore-harness-systemprompt)" : {{[ HarnessSystemContentBlock, ... ]}},
      "[Tags](#cfn-bedrockagentcore-harness-tags)" : {{[ Tag, ... ]}},
      "[TimeoutSeconds](#cfn-bedrockagentcore-harness-timeoutseconds)" : {{Integer}},
      "[Tools](#cfn-bedrockagentcore-harness-tools)" : {{[ HarnessTool, ... ]}},
      "[Truncation](#cfn-bedrockagentcore-harness-truncation)" : {{HarnessTruncationConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-harness-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Harness
Properties:
  [AllowedTools](#cfn-bedrockagentcore-harness-allowedtools): {{
    - String}}
  [AuthorizerConfiguration](#cfn-bedrockagentcore-harness-authorizerconfiguration): {{
    AuthorizerConfiguration}}
  [Environment](#cfn-bedrockagentcore-harness-environment): {{
    HarnessEnvironmentProvider}}
  [EnvironmentArtifact](#cfn-bedrockagentcore-harness-environmentartifact): {{
    HarnessEnvironmentArtifact}}
  [EnvironmentVariables](#cfn-bedrockagentcore-harness-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [ExecutionRoleArn](#cfn-bedrockagentcore-harness-executionrolearn): {{String}}
  [HarnessName](#cfn-bedrockagentcore-harness-harnessname): {{String}}
  [MaxIterations](#cfn-bedrockagentcore-harness-maxiterations): {{Integer}}
  [MaxTokens](#cfn-bedrockagentcore-harness-maxtokens): {{Integer}}
  [Memory](#cfn-bedrockagentcore-harness-memory): {{
    HarnessMemoryConfiguration}}
  [Model](#cfn-bedrockagentcore-harness-model): {{
    HarnessModelConfiguration}}
  [Skills](#cfn-bedrockagentcore-harness-skills): {{
    - HarnessSkill}}
  [SystemPrompt](#cfn-bedrockagentcore-harness-systemprompt): {{
    - HarnessSystemContentBlock}}
  [Tags](#cfn-bedrockagentcore-harness-tags): {{
    - Tag}}
  [TimeoutSeconds](#cfn-bedrockagentcore-harness-timeoutseconds): {{Integer}}
  [Tools](#cfn-bedrockagentcore-harness-tools): {{
    - HarnessTool}}
  [Truncation](#cfn-bedrockagentcore-harness-truncation): {{
    HarnessTruncationConfiguration}}
```

## Properties
<a name="aws-resource-bedrockagentcore-harness-properties"></a>

`AllowedTools`  <a name="cfn-bedrockagentcore-harness-allowedtools"></a>
The allowed tools of the harness. All tools are allowed by default.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizerConfiguration`  <a name="cfn-bedrockagentcore-harness-authorizerconfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.
*Required*: No
*Type*: [AuthorizerConfiguration](aws-properties-bedrockagentcore-harness-authorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-bedrockagentcore-harness-environment"></a>
The compute environment on which the Harness runs.
*Required*: No
*Type*: [HarnessEnvironmentProvider](aws-properties-bedrockagentcore-harness-harnessenvironmentprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentArtifact`  <a name="cfn-bedrockagentcore-harness-environmentartifact"></a>
The environment artifact (e.g., container) in which the Harness operates.
*Required*: No
*Type*: [HarnessEnvironmentArtifact](aws-properties-bedrockagentcore-harness-harnessenvironmentartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-bedrockagentcore-harness-environmentvariables"></a>
Environment variables exposed in the environment in which the harness operates.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-bedrockagentcore-harness-executionrolearn"></a>
IAM role the harness assumes when running.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HarnessName`  <a name="cfn-bedrockagentcore-harness-harnessname"></a>
The name of the harness.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,39}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxIterations`  <a name="cfn-bedrockagentcore-harness-maxiterations"></a>
The maximum number of iterations in the agent loop allowed before exiting per invocation.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTokens`  <a name="cfn-bedrockagentcore-harness-maxtokens"></a>
The maximum total number of output tokens the agent can generate across all model calls within a single invocation.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Memory`  <a name="cfn-bedrockagentcore-harness-memory"></a>
AgentCore Memory instance configuration for short and long term memory.
*Required*: No
*Type*: [HarnessMemoryConfiguration](aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-bedrockagentcore-harness-model"></a>
The configuration of the default model used by the Harness.
*Required*: Yes
*Type*: [HarnessModelConfiguration](aws-properties-bedrockagentcore-harness-harnessmodelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Skills`  <a name="cfn-bedrockagentcore-harness-skills"></a>
The skills of the harness.
*Required*: No
*Type*: Array of [HarnessSkill](aws-properties-bedrockagentcore-harness-harnessskill.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemPrompt`  <a name="cfn-bedrockagentcore-harness-systemprompt"></a>
The system prompt of the harness.
*Required*: No
*Type*: Array of [HarnessSystemContentBlock](aws-properties-bedrockagentcore-harness-harnesssystemcontentblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-harness-tags"></a>
Tags to apply to the harness resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-harness-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutSeconds`  <a name="cfn-bedrockagentcore-harness-timeoutseconds"></a>
The maximum duration per invocation.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tools`  <a name="cfn-bedrockagentcore-harness-tools"></a>
The tools of the harness.
*Required*: No
*Type*: Array of [HarnessTool](aws-properties-bedrockagentcore-harness-harnesstool.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Truncation`  <a name="cfn-bedrockagentcore-harness-truncation"></a>
Configuration for truncating model context.
*Required*: No
*Type*: [HarnessTruncationConfiguration](aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-harness-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-harness-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-harness-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-harness-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the harness.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The createdAt time of the harness.

`Environment.AgentCoreRuntimeEnvironment.AgentRuntimeArn`  <a name="Environment.AgentCoreRuntimeEnvironment.AgentRuntimeArn-fn::getatt"></a>
The ARN of the underlying AgentCore Runtime.

`Environment.AgentCoreRuntimeEnvironment.AgentRuntimeId`  <a name="Environment.AgentCoreRuntimeEnvironment.AgentRuntimeId-fn::getatt"></a>
The ID of the underlying AgentCore Runtime.

`Environment.AgentCoreRuntimeEnvironment.AgentRuntimeName`  <a name="Environment.AgentCoreRuntimeEnvironment.AgentRuntimeName-fn::getatt"></a>
The name of the underlying AgentCore Runtime.

`HarnessId`  <a name="HarnessId-fn::getatt"></a>
The ID of the harness.

`Memory.ManagedMemoryConfiguration.Arn`  <a name="Memory.ManagedMemoryConfiguration.Arn-fn::getatt"></a>
The ARN of the harness.

`Status`  <a name="Status-fn::getatt"></a>
The status of the harness.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The updatedAt time of the harness.

`Version`  <a name="Version-fn::getatt"></a>
The version of the harness. Incremented on every successful UpdateHarness.

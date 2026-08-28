---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessAgentCoreRuntimeEnvironment
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment"></a>

The AgentCore Runtime environment for a harness.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-syntax.json"></a>

```
{
  "[AgentRuntimeArn](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimearn)" : {{String}},
  "[AgentRuntimeId](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimeid)" : {{String}},
  "[AgentRuntimeName](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimename)" : {{String}},
  "[FilesystemConfigurations](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-filesystemconfigurations)" : {{[ FilesystemConfiguration, ... ]}},
  "[LifecycleConfiguration](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-lifecycleconfiguration)" : {{LifecycleConfiguration}},
  "[NetworkConfiguration](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-networkconfiguration)" : {{NetworkConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-syntax.yaml"></a>

```
  [AgentRuntimeArn](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimearn): {{String}}
  [AgentRuntimeId](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimeid): {{String}}
  [AgentRuntimeName](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimename): {{String}}
  [FilesystemConfigurations](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-filesystemconfigurations): {{
    - FilesystemConfiguration}}
  [LifecycleConfiguration](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-lifecycleconfiguration): {{
    LifecycleConfiguration}}
  [NetworkConfiguration](#cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-networkconfiguration): {{
    NetworkConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-properties"></a>

`AgentRuntimeArn`  <a name="cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimearn"></a>
The ARN of the underlying AgentCore Runtime.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentRuntimeId`  <a name="cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimeid"></a>
The ID of the underlying AgentCore Runtime.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentRuntimeName`  <a name="cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-agentruntimename"></a>
The name of the underlying AgentCore Runtime.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilesystemConfigurations`  <a name="cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-filesystemconfigurations"></a>
The filesystem configurations for the runtime environment.
*Required*: No
*Type*: Array of [FilesystemConfiguration](aws-properties-bedrockagentcore-harness-filesystemconfiguration.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfiguration`  <a name="cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-lifecycleconfiguration"></a>
LifecycleConfiguration lets you manage the lifecycle of runtime sessions and resources in AgentCore Runtime. This configuration helps optimize resource utilization by automatically cleaning up idle sessions and preventing long-running instances from consuming resources indefinitely.
*Required*: No
*Type*: [LifecycleConfiguration](aws-properties-bedrockagentcore-harness-lifecycleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-bedrockagentcore-harness-harnessagentcoreruntimeenvironment-networkconfiguration"></a>
SecurityConfig for the Agent.
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-bedrockagentcore-harness-networkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

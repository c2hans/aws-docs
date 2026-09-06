---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-customorchestration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent CustomOrchestration
<a name="aws-properties-bedrock-agent-customorchestration"></a>

Contains details of the custom orchestration configured for the agent.

## Syntax
<a name="aws-properties-bedrock-agent-customorchestration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-customorchestration-syntax.json"></a>

```
{
  "[Executor](#cfn-bedrock-agent-customorchestration-executor)" : {{OrchestrationExecutor}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-customorchestration-syntax.yaml"></a>

```
  [Executor](#cfn-bedrock-agent-customorchestration-executor): {{
    OrchestrationExecutor}}
```

## Properties
<a name="aws-properties-bedrock-agent-customorchestration-properties"></a>

`Executor`  <a name="cfn-bedrock-agent-customorchestration-executor"></a>
The structure of the executor invoking the actions in custom orchestration.
*Required*: No
*Type*: [OrchestrationExecutor](aws-properties-bedrock-agent-orchestrationexecutor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

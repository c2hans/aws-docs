---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-orchestrationexecutor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent OrchestrationExecutor
<a name="aws-properties-bedrock-agent-orchestrationexecutor"></a>

The structure of the executor invoking the actions in custom orchestration.

## Syntax
<a name="aws-properties-bedrock-agent-orchestrationexecutor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-orchestrationexecutor-syntax.json"></a>

```
{
  "[Lambda](#cfn-bedrock-agent-orchestrationexecutor-lambda)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-orchestrationexecutor-syntax.yaml"></a>

```
  [Lambda](#cfn-bedrock-agent-orchestrationexecutor-lambda): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-orchestrationexecutor-properties"></a>

`Lambda`  <a name="cfn-bedrock-agent-orchestrationexecutor-lambda"></a>
The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z0-9-]{1,20}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-containerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness ContainerConfiguration
<a name="aws-properties-bedrockagentcore-harness-containerconfiguration"></a>

Representation of a container configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-containerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-containerconfiguration-syntax.json"></a>

```
{
  "[ContainerUri](#cfn-bedrockagentcore-harness-containerconfiguration-containeruri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-containerconfiguration-syntax.yaml"></a>

```
  [ContainerUri](#cfn-bedrockagentcore-harness-containerconfiguration-containeruri): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-containerconfiguration-properties"></a>

`ContainerUri`  <a name="cfn-bedrockagentcore-harness-containerconfiguration-containeruri"></a>
The ECR URI of the container.
*Required*: Yes
*Type*: String
*Pattern*: `^(([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com(\.cn)?|public\.ecr\.aws)/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?::([^:@]{1,300}))?(?:@(.+))?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

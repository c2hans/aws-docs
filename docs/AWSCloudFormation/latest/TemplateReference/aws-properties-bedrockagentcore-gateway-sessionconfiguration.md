---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-sessionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway SessionConfiguration
<a name="aws-properties-bedrockagentcore-gateway-sessionconfiguration"></a>

The session configuration for an MCP gateway. This structure defines settings that control session behavior.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-sessionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-sessionconfiguration-syntax.json"></a>

```
{
  "[SessionTimeoutInSeconds](#cfn-bedrockagentcore-gateway-sessionconfiguration-sessiontimeoutinseconds)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-sessionconfiguration-syntax.yaml"></a>

```
  [SessionTimeoutInSeconds](#cfn-bedrockagentcore-gateway-sessionconfiguration-sessiontimeoutinseconds): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-sessionconfiguration-properties"></a>

`SessionTimeoutInSeconds`  <a name="cfn-bedrockagentcore-gateway-sessionconfiguration-sessiontimeoutinseconds"></a>
The session timeout in seconds. After this timeout, the session expires and subsequent requests to this session will receive an error. The minimum value is 900 seconds (15 minutes), the maximum value is 28800 seconds (8 hours), and the default value is 3600 seconds (1 hour).
*Required*: No
*Type*: Number
*Minimum*: `900`
*Maximum*: `28800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget McpLambdaTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration"></a>

The Lambda configuration for a Model Context Protocol target. This structure defines how the gateway uses a Lambda function to communicate with the target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-syntax.json"></a>

```
{
  "[LambdaArn](#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-lambdaarn)" : {{String}},
  "[ToolSchema](#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-toolschema)" : {{ToolSchema}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-syntax.yaml"></a>

```
  [LambdaArn](#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-lambdaarn): {{String}}
  [ToolSchema](#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-toolschema): {{
    ToolSchema}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-properties"></a>

`LambdaArn`  <a name="cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-lambdaarn"></a>
The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to communicate with the target.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolSchema`  <a name="cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-toolschema"></a>
The tool schema for the Lambda function. This schema defines the structure of the tools that the Lambda function provides.
*Required*: Yes
*Type*: [ToolSchema](aws-properties-bedrockagentcore-gatewaytarget-toolschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

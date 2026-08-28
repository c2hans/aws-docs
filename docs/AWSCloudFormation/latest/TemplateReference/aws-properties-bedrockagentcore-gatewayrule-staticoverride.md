---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-staticoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule StaticOverride
<a name="aws-properties-bedrockagentcore-gatewayrule-staticoverride"></a>

A static configuration bundle override.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-staticoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-staticoverride-syntax.json"></a>

```
{
  "[BundleArn](#cfn-bedrockagentcore-gatewayrule-staticoverride-bundlearn)" : {{String}},
  "[BundleVersion](#cfn-bedrockagentcore-gatewayrule-staticoverride-bundleversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-staticoverride-syntax.yaml"></a>

```
  [BundleArn](#cfn-bedrockagentcore-gatewayrule-staticoverride-bundlearn): {{String}}
  [BundleVersion](#cfn-bedrockagentcore-gatewayrule-staticoverride-bundleversion): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-staticoverride-properties"></a>

`BundleArn`  <a name="cfn-bedrockagentcore-gatewayrule-staticoverride-bundlearn"></a>
The Amazon Resource Name (ARN) of the configuration bundle to apply.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BundleVersion`  <a name="cfn-bedrockagentcore-gatewayrule-staticoverride-bundleversion"></a>
The version of the configuration bundle to apply.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

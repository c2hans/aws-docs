---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-connectorsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ConnectorSource
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorsource"></a>

The source identifying the connector integration.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorsource-syntax.json"></a>

```
{
  "[ConnectorId](#cfn-bedrockagentcore-gatewaytarget-connectorsource-connectorid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorsource-syntax.yaml"></a>

```
  [ConnectorId](#cfn-bedrockagentcore-gatewaytarget-connectorsource-connectorid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorsource-properties"></a>

`ConnectorId`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorsource-connectorid"></a>
The identifier for the connector integration (for example, `bedrock-knowledge-bases`).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

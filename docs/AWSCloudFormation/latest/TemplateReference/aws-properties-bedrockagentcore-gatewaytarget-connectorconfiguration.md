---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ConnectorConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration"></a>

Configuration for a single tool within a connector.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-description)" : {{String}},
  "[Name](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-name)" : {{String}},
  "[ParameterOverrides](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-parameteroverrides)" : {{[ ConnectorParameterOverride, ... ]}},
  "[ParameterValues](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-parametervalues)" : {{}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-description): {{String}}
  [Name](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-name): {{String}}
  [ParameterOverrides](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-parameteroverrides): {{
    - ConnectorParameterOverride}}
  [ParameterValues](#cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-parametervalues): {{
    }}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-description"></a>
An agent-facing description override for this tool.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-name"></a>
The tool or operation name (for example, `retrieve` or `webSearch`).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_-]*$`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterOverrides`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-parameteroverrides"></a>
Parameters to expose to the agent at runtime, with optional description overrides.
*Required*: No
*Type*: Array of [ConnectorParameterOverride](aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValues`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorconfiguration-parametervalues"></a>
Parameters to set as fixed or default values when provisioning this tool.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

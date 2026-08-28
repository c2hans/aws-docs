---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-providerprefix.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ProviderPrefix
<a name="aws-properties-bedrockagentcore-gatewaytarget-providerprefix"></a>

The configuration that controls how a provider prefix is applied to model IDs during translation.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-providerprefix-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-providerprefix-syntax.json"></a>

```
{
  "[Separator](#cfn-bedrockagentcore-gatewaytarget-providerprefix-separator)" : {{String}},
  "[Strip](#cfn-bedrockagentcore-gatewaytarget-providerprefix-strip)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-providerprefix-syntax.yaml"></a>

```
  [Separator](#cfn-bedrockagentcore-gatewaytarget-providerprefix-separator): {{String}}
  [Strip](#cfn-bedrockagentcore-gatewaytarget-providerprefix-strip): {{Boolean}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-providerprefix-properties"></a>

`Separator`  <a name="cfn-bedrockagentcore-gatewaytarget-providerprefix-separator"></a>
The single character that separates the provider prefix from the model name (for example, `.`). The default is `.`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strip`  <a name="cfn-bedrockagentcore-gatewaytarget-providerprefix-strip"></a>
Whether clients can omit the provider prefix from model IDs. If `true`, the gateway accepts model IDs without the prefix and restores the full prefixed form before forwarding to the provider. The default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

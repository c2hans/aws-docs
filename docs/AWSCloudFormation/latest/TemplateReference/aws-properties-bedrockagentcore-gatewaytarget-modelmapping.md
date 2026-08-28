---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-modelmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ModelMapping
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelmapping"></a>

The configuration that translates model IDs between client-facing names and provider model IDs.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelmapping-syntax.json"></a>

```
{
  "[ProviderPrefix](#cfn-bedrockagentcore-gatewaytarget-modelmapping-providerprefix)" : {{ProviderPrefix}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelmapping-syntax.yaml"></a>

```
  [ProviderPrefix](#cfn-bedrockagentcore-gatewaytarget-modelmapping-providerprefix): {{
    ProviderPrefix}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelmapping-properties"></a>

`ProviderPrefix`  <a name="cfn-bedrockagentcore-gatewaytarget-modelmapping-providerprefix"></a>
The provider prefix configuration used for model ID translation.
*Required*: No
*Type*: [ProviderPrefix](aws-properties-bedrockagentcore-gatewaytarget-providerprefix.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

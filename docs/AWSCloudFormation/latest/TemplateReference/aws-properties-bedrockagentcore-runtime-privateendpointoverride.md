---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-privateendpointoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime PrivateEndpointOverride
<a name="aws-properties-bedrockagentcore-runtime-privateendpointoverride"></a>

A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-privateendpointoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-privateendpointoverride-syntax.json"></a>

```
{
  "[Domain](#cfn-bedrockagentcore-runtime-privateendpointoverride-domain)" : {{String}},
  "[PrivateEndpoint](#cfn-bedrockagentcore-runtime-privateendpointoverride-privateendpoint)" : {{PrivateEndpoint}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-privateendpointoverride-syntax.yaml"></a>

```
  [Domain](#cfn-bedrockagentcore-runtime-privateendpointoverride-domain): {{String}}
  [PrivateEndpoint](#cfn-bedrockagentcore-runtime-privateendpointoverride-privateendpoint): {{
    PrivateEndpoint}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-privateendpointoverride-properties"></a>

`Domain`  <a name="cfn-bedrockagentcore-runtime-privateendpointoverride-domain"></a>
The domain to override with a private endpoint.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-runtime-privateendpointoverride-privateendpoint"></a>
The private endpoint configuration for the specified domain.
*Required*: Yes
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-runtime-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

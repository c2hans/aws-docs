---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ApiGatewayToolOverride
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride"></a>

Settings to override configurations for a tool.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-description)" : {{String}},
  "[Method](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-method)" : {{String}},
  "[Name](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-name)" : {{String}},
  "[Path](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-description): {{String}}
  [Method](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-method): {{String}}
  [Name](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-name): {{String}}
  [Path](#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-path): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-description"></a>
The description of the tool. Provides information about the purpose and usage of the tool. If not provided, uses the description from the API's OpenAPI specification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Method`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-method"></a>
The HTTP method to expose for the specified path.
*Required*: Yes
*Type*: String
*Allowed values*: `GET | DELETE | HEAD | OPTIONS | PATCH | PUT | POST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-name"></a>
The name of tool. Identifies the tool in the Model Context Protocol.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-path"></a>
Resource path in the REST API (e.g., `/pets`). Must explicitly match an existing path in the REST API.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

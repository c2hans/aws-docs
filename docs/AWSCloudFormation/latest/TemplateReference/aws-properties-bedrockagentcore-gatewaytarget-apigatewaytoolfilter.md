---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ApiGatewayToolFilter
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter"></a>

Specifies which operations from an API Gateway REST API are exposed as tools. Tool names and descriptions are derived from the operationId and description fields in the API's exported OpenAPI specification.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-syntax.json"></a>

```
{
  "[FilterPath](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-filterpath)" : {{String}},
  "[Methods](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-methods)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-syntax.yaml"></a>

```
  [FilterPath](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-filterpath): {{String}}
  [Methods](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-methods): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-properties"></a>

`FilterPath`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-filterpath"></a>
Resource path to match in the REST API. Supports exact paths (for example, `/pets`) or wildcard paths (for example, `/pets/*` to match all paths under `/pets`). Must match existing paths in the REST API.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Methods`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-methods"></a>
The methods to filter for.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

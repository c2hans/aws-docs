---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget MetadataConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration"></a>

Configuration for HTTP header and query parameter propagation between the gateway and target servers.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration-syntax.json"></a>

```
{
  "[AllowedQueryParameters](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedqueryparameters)" : {{[ String, ... ]}},
  "[AllowedRequestHeaders](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedrequestheaders)" : {{[ String, ... ]}},
  "[AllowedResponseHeaders](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedresponseheaders)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration-syntax.yaml"></a>

```
  [AllowedQueryParameters](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedqueryparameters): {{
    - String}}
  [AllowedRequestHeaders](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedrequestheaders): {{
    - String}}
  [AllowedResponseHeaders](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedresponseheaders): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration-properties"></a>

`AllowedQueryParameters`  <a name="cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedqueryparameters"></a>
A list of URL query parameters that are allowed to be propagated from incoming gateway URL to the target.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedRequestHeaders`  <a name="cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedrequestheaders"></a>
A list of HTTP headers that are allowed to be propagated from incoming client requests to the target.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedResponseHeaders`  <a name="cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedresponseheaders"></a>
A list of HTTP headers that are allowed to be propagated from the target response back to the client.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

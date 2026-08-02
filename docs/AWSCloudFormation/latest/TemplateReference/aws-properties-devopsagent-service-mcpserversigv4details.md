---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserversigv4details.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerSigV4Details
<a name="aws-properties-devopsagent-service-mcpserversigv4details"></a>

<a name="aws-properties-devopsagent-service-mcpserversigv4details-description"></a>The `MCPServerSigV4Details` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-mcpserversigv4details-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserversigv4details-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-mcpserversigv4details-authorizationconfig)" : {{MCPServerSigV4AuthorizationConfig}},
  "[Description](#cfn-devopsagent-service-mcpserversigv4details-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-mcpserversigv4details-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-service-mcpserversigv4details-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserversigv4details-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-mcpserversigv4details-authorizationconfig): {{
    MCPServerSigV4AuthorizationConfig}}
  [Description](#cfn-devopsagent-service-mcpserversigv4details-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-mcpserversigv4details-endpoint): {{String}}
  [Name](#cfn-devopsagent-service-mcpserversigv4details-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserversigv4details-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-mcpserversigv4details-authorizationconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [MCPServerSigV4AuthorizationConfig](aws-properties-devopsagent-service-mcpserversigv4authorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-mcpserversigv4details-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-mcpserversigv4details-endpoint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-mcpserversigv4details-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

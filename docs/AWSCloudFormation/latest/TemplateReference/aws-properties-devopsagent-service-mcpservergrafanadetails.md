---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpservergrafanadetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerGrafanaDetails
<a name="aws-properties-devopsagent-service-mcpservergrafanadetails"></a>

<a name="aws-properties-devopsagent-service-mcpservergrafanadetails-description"></a>The `MCPServerGrafanaDetails` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-mcpservergrafanadetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpservergrafanadetails-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-mcpservergrafanadetails-authorizationconfig)" : {{MCPServerGrafanaAuthorizationConfig}},
  "[Description](#cfn-devopsagent-service-mcpservergrafanadetails-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-mcpservergrafanadetails-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-service-mcpservergrafanadetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpservergrafanadetails-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-mcpservergrafanadetails-authorizationconfig): {{
    MCPServerGrafanaAuthorizationConfig}}
  [Description](#cfn-devopsagent-service-mcpservergrafanadetails-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-mcpservergrafanadetails-endpoint): {{String}}
  [Name](#cfn-devopsagent-service-mcpservergrafanadetails-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpservergrafanadetails-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-mcpservergrafanadetails-authorizationconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [MCPServerGrafanaAuthorizationConfig](aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-mcpservergrafanadetails-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-mcpservergrafanadetails-endpoint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-mcpservergrafanadetails-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

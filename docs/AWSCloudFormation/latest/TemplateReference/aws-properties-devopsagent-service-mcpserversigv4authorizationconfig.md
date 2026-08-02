---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserversigv4authorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerSigV4AuthorizationConfig
<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig"></a>

<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig-description"></a>The `MCPServerSigV4AuthorizationConfig` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig-syntax.json"></a>

```
{
  "[CustomHeaders](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-customheaders)" : {{{{{Key}}: {{Value}}, ...}}},
  "[McpRoleArn](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-mcprolearn)" : {{String}},
  "[Region](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-region)" : {{String}},
  "[RoleArn](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-rolearn)" : {{String}},
  "[Service](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig-syntax.yaml"></a>

```
  [CustomHeaders](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-customheaders): {{
    {{Key}}: {{Value}}}}
  [McpRoleArn](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-mcprolearn): {{String}}
  [Region](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-region): {{String}}
  [RoleArn](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-rolearn): {{String}}
  [Service](#cfn-devopsagent-service-mcpserversigv4authorizationconfig-service): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig-properties"></a>

`CustomHeaders`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-customheaders"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McpRoleArn`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-mcprolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-region"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(\*|[a-z]{2,4}(-[a-z]+)+-\d+)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-rolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-service"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

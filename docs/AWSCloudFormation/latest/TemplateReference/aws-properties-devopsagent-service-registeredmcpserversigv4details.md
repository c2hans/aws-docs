---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredmcpserversigv4details.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredMCPServerSigV4Details
<a name="aws-properties-devopsagent-service-registeredmcpserversigv4details"></a>

SigV4-authenticated MCP server details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registeredmcpserversigv4details-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredmcpserversigv4details-syntax.json"></a>

```
{
  "[CustomHeaders](#cfn-devopsagent-service-registeredmcpserversigv4details-customheaders)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Description](#cfn-devopsagent-service-registeredmcpserversigv4details-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-registeredmcpserversigv4details-endpoint)" : {{String}},
  "[McpRoleArn](#cfn-devopsagent-service-registeredmcpserversigv4details-mcprolearn)" : {{String}},
  "[Name](#cfn-devopsagent-service-registeredmcpserversigv4details-name)" : {{String}},
  "[Region](#cfn-devopsagent-service-registeredmcpserversigv4details-region)" : {{String}},
  "[RoleArn](#cfn-devopsagent-service-registeredmcpserversigv4details-rolearn)" : {{String}},
  "[Service](#cfn-devopsagent-service-registeredmcpserversigv4details-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredmcpserversigv4details-syntax.yaml"></a>

```
  [CustomHeaders](#cfn-devopsagent-service-registeredmcpserversigv4details-customheaders): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-devopsagent-service-registeredmcpserversigv4details-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-registeredmcpserversigv4details-endpoint): {{String}}
  [McpRoleArn](#cfn-devopsagent-service-registeredmcpserversigv4details-mcprolearn): {{String}}
  [Name](#cfn-devopsagent-service-registeredmcpserversigv4details-name): {{String}}
  [Region](#cfn-devopsagent-service-registeredmcpserversigv4details-region): {{String}}
  [RoleArn](#cfn-devopsagent-service-registeredmcpserversigv4details-rolearn): {{String}}
  [Service](#cfn-devopsagent-service-registeredmcpserversigv4details-service): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredmcpserversigv4details-properties"></a>

`CustomHeaders`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-customheaders"></a>
The custom headers that the SigV4-authenticated MCP server receives.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-description"></a>
An optional description for the MCP server.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-endpoint"></a>
The MCP server endpoint URL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McpRoleArn`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-mcprolearn"></a>
The ARN of the IAM role used for SigV4 signing. This property is absent when you haven't configured a dedicated role.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-name"></a>
The MCP server name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-region"></a>
The AWS Region used for SigV4 signing.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-rolearn"></a>
The ARN of the IAM role used for SigV4 signing.
This property is deprecated. Use `McpRoleArn` instead.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-devopsagent-service-registeredmcpserversigv4details-service"></a>
The AWS service name used for SigV4 signing.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

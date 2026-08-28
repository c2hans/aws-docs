---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserversigv4authorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerSigV4AuthorizationConfig
<a name="aws-properties-devopsagent-service-mcpserversigv4authorizationconfig"></a>

The SigV4 authorization configuration for an MCP server.

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
Custom headers to include in requests to the SigV4-authenticated MCP server.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McpRoleArn`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-mcprolearn"></a>
The ARN of the IAM role to assume for SigV4 signing. If omitted, the service resolves credentials at runtime through a monitor account association.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-region"></a>
The AWS Region used for SigV4 signing, or `*` for SigV4a multi-Region signing.
*Required*: Yes
*Type*: String
*Pattern*: `^(\*|[a-z]{2,4}(-[a-z]+)+-\d+)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-rolearn"></a>
The ARN of the IAM role to assume for SigV4 signing.
This property is deprecated. Use `McpRoleArn` instead.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-devopsagent-service-mcpserversigv4authorizationconfig-service"></a>
The AWS service name used for SigV4 signing.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

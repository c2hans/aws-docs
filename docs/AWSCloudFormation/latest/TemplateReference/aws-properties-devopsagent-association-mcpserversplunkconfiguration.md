---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-mcpserversplunkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association MCPServerSplunkConfiguration
<a name="aws-properties-devopsagent-association-mcpserversplunkconfiguration"></a>

Configuration for Splunk MCP server integration. Defines the server name, endpoint URL, optional description, and webhook update settings.

## Syntax
<a name="aws-properties-devopsagent-association-mcpserversplunkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-mcpserversplunkconfiguration-syntax.json"></a>

```
{
  "[Description](#cfn-devopsagent-association-mcpserversplunkconfiguration-description)" : {{String}},
  "[EnableWebhookUpdates](#cfn-devopsagent-association-mcpserversplunkconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[Endpoint](#cfn-devopsagent-association-mcpserversplunkconfiguration-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-association-mcpserversplunkconfiguration-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-mcpserversplunkconfiguration-syntax.yaml"></a>

```
  [Description](#cfn-devopsagent-association-mcpserversplunkconfiguration-description): {{String}}
  [EnableWebhookUpdates](#cfn-devopsagent-association-mcpserversplunkconfiguration-enablewebhookupdates): {{Boolean}}
  [Endpoint](#cfn-devopsagent-association-mcpserversplunkconfiguration-endpoint): {{String}}
  [Name](#cfn-devopsagent-association-mcpserversplunkconfiguration-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-mcpserversplunkconfiguration-properties"></a>

`Description`  <a name="cfn-devopsagent-association-mcpserversplunkconfiguration-description"></a>
The description of the MCP server.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-mcpserversplunkconfiguration-enablewebhookupdates"></a>
When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-association-mcpserversplunkconfiguration-endpoint"></a>
The MCP server endpoint URL. Must be an HTTPS URL.
*Required*: No
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-association-mcpserversplunkconfiguration-name"></a>
The name of the MCP server. The name must match the pattern `^[a-zA-Z0-9_-]+$`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

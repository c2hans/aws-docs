---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-imagebuilder-agentaccesssetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::ImageBuilder AgentAccessSetting

A permission setting for an agent action. Each setting specifies an agent action and whether it is enabled or disabled.

## Syntax
<a name="aws-properties-appstream-imagebuilder-agentaccesssetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-imagebuilder-agentaccesssetting-syntax.json"></a>

```json
{
  "[AgentAction](#cfn-appstream-imagebuilder-agentaccesssetting-agentaction)" : {{String}},
  "[Permission](#cfn-appstream-imagebuilder-agentaccesssetting-permission)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-imagebuilder-agentaccesssetting-syntax.yaml"></a>

```yaml
  [AgentAction](#cfn-appstream-imagebuilder-agentaccesssetting-agentaction): {{String}}
  [Permission](#cfn-appstream-imagebuilder-agentaccesssetting-permission): {{String}}
```

## Properties
<a name="aws-properties-appstream-imagebuilder-agentaccesssetting-properties"></a>

`AgentAction`  <a name="cfn-appstream-imagebuilder-agentaccesssetting-agentaction"></a>
The agent action to configure. Valid values are COMPUTER\_VISION, COMPUTER\_INPUT, and FORWARD\_MCP\_TOOLS. If you enable COMPUTER\_INPUT, you must also enable COMPUTER\_VISION.
*Required*: Yes
*Type*: String
*Allowed values*: `COMPUTER_VISION | COMPUTER_INPUT | FORWARD_MCP_TOOLS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permission`  <a name="cfn-appstream-imagebuilder-agentaccesssetting-permission"></a>
Whether the agent action is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

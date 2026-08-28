---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-connector-connectorasyncmdnconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Connector ConnectorAsyncMdnConfig
<a name="aws-properties-transfer-connector-connectorasyncmdnconfig"></a>

<a name="aws-properties-transfer-connector-connectorasyncmdnconfig-description"></a>The `ConnectorAsyncMdnConfig` property type specifies Property description not available. for an [AWS::Transfer::Connector](aws-resource-transfer-connector.md).

## Syntax
<a name="aws-properties-transfer-connector-connectorasyncmdnconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-connector-connectorasyncmdnconfig-syntax.json"></a>

```
{
  "[ServerIds](#cfn-transfer-connector-connectorasyncmdnconfig-serverids)" : {{[ String, ... ]}},
  "[Url](#cfn-transfer-connector-connectorasyncmdnconfig-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-connector-connectorasyncmdnconfig-syntax.yaml"></a>

```
  [ServerIds](#cfn-transfer-connector-connectorasyncmdnconfig-serverids): {{
    - String}}
  [Url](#cfn-transfer-connector-connectorasyncmdnconfig-url): {{String}}
```

## Properties
<a name="aws-properties-transfer-connector-connectorasyncmdnconfig-properties"></a>

`ServerIds`  <a name="cfn-transfer-connector-connectorasyncmdnconfig-serverids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-transfer-connector-connectorasyncmdnconfig-url"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

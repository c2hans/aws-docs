---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-connector-connectorasyncmdnconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Connector ConnectorAsyncMdnConfig
<a name="aws-properties-transfer-connector-connectorasyncmdnconfig"></a>

Contains the configuration details for asynchronous Message Disposition Notification (MDN) responses in AS2 connectors. This configuration specifies where asynchronous MDN responses should be sent and which servers should handle them.

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
A list of server identifiers that can handle asynchronous MDN responses. You can specify between 1 and 10 server IDs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-transfer-connector-connectorasyncmdnconfig-url"></a>
The URL endpoint where asynchronous MDN responses should be sent.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

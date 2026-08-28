---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-connectordefinitionversion-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ConnectorDefinitionVersion Connector
<a name="aws-properties-greengrass-connectordefinitionversion-connector"></a>

<a name="aws-properties-greengrass-connectordefinitionversion-connector-description"></a>Connectors are modules that provide built-in integration with local infrastructure, device protocols, AWS, and other cloud services. For more information, see [Integrate with Services and Protocols Using Greengrass Connectors](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-connectordefinitionversion-connector-inheritance"></a> In an CloudFormation template, the `Connectors` property of the [`AWS::Greengrass::ConnectorDefinitionVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html) resource contains a list of `Connector` property types.

## Syntax
<a name="aws-properties-greengrass-connectordefinitionversion-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-connectordefinitionversion-connector-syntax.json"></a>

```
{
  "[ConnectorArn](#cfn-greengrass-connectordefinitionversion-connector-connectorarn)" : {{String}},
  "[Id](#cfn-greengrass-connectordefinitionversion-connector-id)" : {{String}},
  "[Parameters](#cfn-greengrass-connectordefinitionversion-connector-parameters)" : {{Json}}
}
```

### YAML
<a name="aws-properties-greengrass-connectordefinitionversion-connector-syntax.yaml"></a>

```
  [ConnectorArn](#cfn-greengrass-connectordefinitionversion-connector-connectorarn): {{String}}
  [Id](#cfn-greengrass-connectordefinitionversion-connector-id): {{String}}
  [Parameters](#cfn-greengrass-connectordefinitionversion-connector-parameters): {{Json}}
```

## Properties
<a name="aws-properties-greengrass-connectordefinitionversion-connector-properties"></a>

`ConnectorArn`  <a name="cfn-greengrass-connectordefinitionversion-connector-connectorarn"></a>
The Amazon Resource Name (ARN) of the connector.
For more information about connectors provided by AWS, see [Greengrass Connectors Provided by AWS](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors-list.html).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Id`  <a name="cfn-greengrass-connectordefinitionversion-connector-id"></a>
A descriptive or arbitrary ID for the connector. This value must be unique within the connector definition version. Maximum length is 128 characters with pattern `[a-zA-Z0-9:_-]+`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-greengrass-connectordefinitionversion-connector-parameters"></a>
The parameters or configuration that the connector uses.
For more information about connectors provided by AWS, see [Greengrass Connectors Provided by AWS](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors-list.html).
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-connectordefinitionversion-connector--seealso"></a>
+ [Connector](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connector.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

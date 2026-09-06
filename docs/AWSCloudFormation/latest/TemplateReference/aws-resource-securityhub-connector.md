---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Connector
<a name="aws-resource-securityhub-connector"></a>

Creates a connector to a third-party cloud provider in Security Hub CSPM. A connector establishes a connection between Security Hub CSPM and a third-party cloud provider, enabling Security Hub CSPM to ingest security findings and resource data from the connected environment.

## Syntax
<a name="aws-resource-securityhub-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-connector-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::Connector",
  "Properties" : {
      "[Description](#cfn-securityhub-connector-description)" : {{String}},
      "[Name](#cfn-securityhub-connector-name)" : {{String}},
      "[Provider](#cfn-securityhub-connector-provider)" : {{Provider}},
      "[Tags](#cfn-securityhub-connector-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-connector-syntax.yaml"></a>

```
Type: AWS::SecurityHub::Connector
Properties:
  [Description](#cfn-securityhub-connector-description): {{String}}
  [Name](#cfn-securityhub-connector-name): {{String}}
  [Provider](#cfn-securityhub-connector-provider): {{
    Provider}}
  [Tags](#cfn-securityhub-connector-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-connector-properties"></a>

`Description`  <a name="cfn-securityhub-connector-description"></a>
The description of the connector.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-securityhub-connector-name"></a>
The name of the connector.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Provider`  <a name="cfn-securityhub-connector-provider"></a>
Property description not available.
*Required*: Yes
*Type*: [Provider](aws-properties-securityhub-connector-provider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityhub-connector-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-connector-return-values"></a>

### Ref
<a name="aws-resource-securityhub-connector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-securityhub-connector-return-values-fn--getatt"></a>

####
<a name="aws-resource-securityhub-connector-return-values-fn--getatt-fn--getatt"></a>

`ConnectorArn`  <a name="ConnectorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connector.

`ConnectorId`  <a name="ConnectorId-fn::getatt"></a>
The unique identifier of the connector.

`ConnectorStatus`  <a name="ConnectorStatus-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The ISO 8601 UTC timestamp indicating when the connector was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The service principal that created the connector.

`EnablementStatus`  <a name="EnablementStatus-fn::getatt"></a>
The enablement status of the connector.

`Issues`  <a name="Issues-fn::getatt"></a>
Property description not available.

`LastCheckedAt`  <a name="LastCheckedAt-fn::getatt"></a>
Property description not available.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
Property description not available.

`Message`  <a name="Message-fn::getatt"></a>
Property description not available.

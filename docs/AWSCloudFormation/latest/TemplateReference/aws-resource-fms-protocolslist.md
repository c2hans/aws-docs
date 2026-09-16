---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fms-protocolslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::ProtocolsList
<a name="aws-resource-fms-protocolslist"></a>

Creates an AWS Firewall Manager protocols list.

## Syntax
<a name="aws-resource-fms-protocolslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fms-protocolslist-syntax.json"></a>

```
{
  "Type" : "AWS::FMS::ProtocolsList",
  "Properties" : {
      "[ListName](#cfn-fms-protocolslist-listname)" : {{String}},
      "[ProtocolsList](#cfn-fms-protocolslist-protocolslist)" : {{[ String, ... ]}},
      "[Tags](#cfn-fms-protocolslist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fms-protocolslist-syntax.yaml"></a>

```
Type: AWS::FMS::ProtocolsList
Properties:
  [ListName](#cfn-fms-protocolslist-listname): {{String}}
  [ProtocolsList](#cfn-fms-protocolslist-protocolslist): {{
    - String}}
  [Tags](#cfn-fms-protocolslist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fms-protocolslist-properties"></a>

`ListName`  <a name="cfn-fms-protocolslist-listname"></a>
The name of the AWS Firewall Manager protocols list.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolsList`  <a name="cfn-fms-protocolslist-protocolslist"></a>
An array of protocols in the AWS Firewall Manager protocols list.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-fms-protocolslist-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-fms-protocolslist-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fms-protocolslist-return-values"></a>

### Ref
<a name="aws-resource-fms-protocolslist-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fms-protocolslist-return-values-fn--getatt"></a>

####
<a name="aws-resource-fms-protocolslist-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The time that the AWS Firewall Manager protocols list was created.

`LastUpdateTime`  <a name="LastUpdateTime-fn::getatt"></a>
The time that the AWS Firewall Manager protocols list was last updated.

`ListId`  <a name="ListId-fn::getatt"></a>
The ID of the AWS Firewall Manager protocols list.

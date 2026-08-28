---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-putassetpropertyvalueentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule PutAssetPropertyValueEntry
<a name="aws-properties-iot-topicrule-putassetpropertyvalueentry"></a>

An asset property value entry containing the following information.

## Syntax
<a name="aws-properties-iot-topicrule-putassetpropertyvalueentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-putassetpropertyvalueentry-syntax.json"></a>

```
{
  "[AssetId](#cfn-iot-topicrule-putassetpropertyvalueentry-assetid)" : {{String}},
  "[EntryId](#cfn-iot-topicrule-putassetpropertyvalueentry-entryid)" : {{String}},
  "[PropertyAlias](#cfn-iot-topicrule-putassetpropertyvalueentry-propertyalias)" : {{String}},
  "[PropertyId](#cfn-iot-topicrule-putassetpropertyvalueentry-propertyid)" : {{String}},
  "[PropertyValues](#cfn-iot-topicrule-putassetpropertyvalueentry-propertyvalues)" : {{[ AssetPropertyValue, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-putassetpropertyvalueentry-syntax.yaml"></a>

```
  [AssetId](#cfn-iot-topicrule-putassetpropertyvalueentry-assetid): {{String}}
  [EntryId](#cfn-iot-topicrule-putassetpropertyvalueentry-entryid): {{String}}
  [PropertyAlias](#cfn-iot-topicrule-putassetpropertyvalueentry-propertyalias): {{String}}
  [PropertyId](#cfn-iot-topicrule-putassetpropertyvalueentry-propertyid): {{String}}
  [PropertyValues](#cfn-iot-topicrule-putassetpropertyvalueentry-propertyvalues): {{
    - AssetPropertyValue}}
```

## Properties
<a name="aws-properties-iot-topicrule-putassetpropertyvalueentry-properties"></a>

`AssetId`  <a name="cfn-iot-topicrule-putassetpropertyvalueentry-assetid"></a>
The ID of the AWS IoT SiteWise asset. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId`. Accepts substitution templates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntryId`  <a name="cfn-iot-topicrule-putassetpropertyvalueentry-entryid"></a>
Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyAlias`  <a name="cfn-iot-topicrule-putassetpropertyvalueentry-propertyalias"></a>
The name of the property alias associated with your asset property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId`. Accepts substitution templates.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyId`  <a name="cfn-iot-topicrule-putassetpropertyvalueentry-propertyid"></a>
The ID of the asset's property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId`. Accepts substitution templates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyValues`  <a name="cfn-iot-topicrule-putassetpropertyvalueentry-propertyvalues"></a>
A list of property values to insert that each contain timestamp, quality, and value (TQV) information.
*Required*: Yes
*Type*: Array of [AssetPropertyValue](aws-properties-iot-topicrule-assetpropertyvalue.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

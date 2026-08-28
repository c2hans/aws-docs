---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-iotsitewiseaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule IotSiteWiseAction
<a name="aws-properties-iot-topicrule-iotsitewiseaction"></a>

Describes an action to send data from an MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

## Syntax
<a name="aws-properties-iot-topicrule-iotsitewiseaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-iotsitewiseaction-syntax.json"></a>

```
{
  "[PutAssetPropertyValueEntries](#cfn-iot-topicrule-iotsitewiseaction-putassetpropertyvalueentries)" : {{[ PutAssetPropertyValueEntry, ... ]}},
  "[RoleArn](#cfn-iot-topicrule-iotsitewiseaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-iotsitewiseaction-syntax.yaml"></a>

```
  [PutAssetPropertyValueEntries](#cfn-iot-topicrule-iotsitewiseaction-putassetpropertyvalueentries): {{
    - PutAssetPropertyValueEntry}}
  [RoleArn](#cfn-iot-topicrule-iotsitewiseaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-iotsitewiseaction-properties"></a>

`PutAssetPropertyValueEntries`  <a name="cfn-iot-topicrule-iotsitewiseaction-putassetpropertyvalueentries"></a>
A list of asset property value entries.
*Required*: Yes
*Type*: Array of [PutAssetPropertyValueEntry](aws-properties-iot-topicrule-putassetpropertyvalueentry.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-iotsitewiseaction-rolearn"></a>
The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoT SiteWise. (`"Action": "iotsitewise:BatchPutAssetPropertyValue"`). The trust policy can restrict access to specific asset hierarchy paths.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

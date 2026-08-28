---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-iotsitewise.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel IotSiteWise
<a name="aws-properties-iotevents-alarmmodel-iotsitewise"></a>

Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise.

You must use expressions for all parameters in `IotSiteWiseAction`. The expressions accept literals, operators, functions, references, and substitutions templates.

**Examples**
+ For literal values, the expressions must contain single quotes. For example, the value for the `propertyAlias` parameter can be `'/company/windfarm/3/turbine/7/temperature'`.
+ For references, you must specify either variables or input values. For example, the value for the `assetId` parameter can be `$input.TurbineInput.assetId1`.
+ For a substitution template, you must use `${}`, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

  In the following example, the value for the `propertyAlias` parameter uses a substitution template.

   `'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'`

You must specify either `propertyAlias` or both `assetId` and `propertyId` to identify the target asset property in AWS IoT SiteWise.

For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *AWS IoT Events Developer Guide*.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-iotsitewise-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-iotsitewise-syntax.json"></a>

```
{
  "[AssetId](#cfn-iotevents-alarmmodel-iotsitewise-assetid)" : {{String}},
  "[EntryId](#cfn-iotevents-alarmmodel-iotsitewise-entryid)" : {{String}},
  "[PropertyAlias](#cfn-iotevents-alarmmodel-iotsitewise-propertyalias)" : {{String}},
  "[PropertyId](#cfn-iotevents-alarmmodel-iotsitewise-propertyid)" : {{String}},
  "[PropertyValue](#cfn-iotevents-alarmmodel-iotsitewise-propertyvalue)" : {{AssetPropertyValue}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-iotsitewise-syntax.yaml"></a>

```
  [AssetId](#cfn-iotevents-alarmmodel-iotsitewise-assetid): {{String}}
  [EntryId](#cfn-iotevents-alarmmodel-iotsitewise-entryid): {{String}}
  [PropertyAlias](#cfn-iotevents-alarmmodel-iotsitewise-propertyalias): {{String}}
  [PropertyId](#cfn-iotevents-alarmmodel-iotsitewise-propertyid): {{String}}
  [PropertyValue](#cfn-iotevents-alarmmodel-iotsitewise-propertyvalue): {{
    AssetPropertyValue}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-iotsitewise-properties"></a>

`AssetId`  <a name="cfn-iotevents-alarmmodel-iotsitewise-assetid"></a>
The ID of the asset that has the specified property.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntryId`  <a name="cfn-iotevents-alarmmodel-iotsitewise-entryid"></a>
A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyAlias`  <a name="cfn-iotevents-alarmmodel-iotsitewise-propertyalias"></a>
The alias of the asset property.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyId`  <a name="cfn-iotevents-alarmmodel-iotsitewise-propertyid"></a>
The ID of the asset property.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyValue`  <a name="cfn-iotevents-alarmmodel-iotsitewise-propertyvalue"></a>
The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.
*Required*: No
*Type*: [AssetPropertyValue](aws-properties-iotevents-alarmmodel-assetpropertyvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

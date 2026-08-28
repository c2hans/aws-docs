---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotfleetwise-statetemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::StateTemplate
<a name="aws-resource-iotfleetwise-statetemplate"></a>

Creates a mechanism for vehicle owners to track the state of their vehicles. State templates determine which signal updates the vehicle sends to the cloud.

For more information, see [State templates](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/state-templates.html) in the *AWS IoT FleetWise Developer Guide*.

**Important**
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability ](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *AWS IoT FleetWise Developer Guide*.

## Syntax
<a name="aws-resource-iotfleetwise-statetemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotfleetwise-statetemplate-syntax.json"></a>

```
{
  "Type" : "AWS::IoTFleetWise::StateTemplate",
  "Properties" : {
      "[DataExtraDimensions](#cfn-iotfleetwise-statetemplate-dataextradimensions)" : {{[ String, ... ]}},
      "[Description](#cfn-iotfleetwise-statetemplate-description)" : {{String}},
      "[MetadataExtraDimensions](#cfn-iotfleetwise-statetemplate-metadataextradimensions)" : {{[ String, ... ]}},
      "[Name](#cfn-iotfleetwise-statetemplate-name)" : {{String}},
      "[SignalCatalogArn](#cfn-iotfleetwise-statetemplate-signalcatalogarn)" : {{String}},
      "[StateTemplateProperties](#cfn-iotfleetwise-statetemplate-statetemplateproperties)" : {{[ String, ... ]}},
      "[Tags](#cfn-iotfleetwise-statetemplate-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotfleetwise-statetemplate-syntax.yaml"></a>

```
Type: AWS::IoTFleetWise::StateTemplate
Properties:
  [DataExtraDimensions](#cfn-iotfleetwise-statetemplate-dataextradimensions): {{
    - String}}
  [Description](#cfn-iotfleetwise-statetemplate-description): {{String}}
  [MetadataExtraDimensions](#cfn-iotfleetwise-statetemplate-metadataextradimensions): {{
    - String}}
  [Name](#cfn-iotfleetwise-statetemplate-name): {{String}}
  [SignalCatalogArn](#cfn-iotfleetwise-statetemplate-signalcatalogarn): {{String}}
  [StateTemplateProperties](#cfn-iotfleetwise-statetemplate-statetemplateproperties): {{
    - String}}
  [Tags](#cfn-iotfleetwise-statetemplate-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotfleetwise-statetemplate-properties"></a>

`DataExtraDimensions`  <a name="cfn-iotfleetwise-statetemplate-dataextradimensions"></a>
A list of vehicle attributes associated with the payload published on the state template's MQTT topic.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `150 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iotfleetwise-statetemplate-description"></a>
A brief description of the state template.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataExtraDimensions`  <a name="cfn-iotfleetwise-statetemplate-metadataextradimensions"></a>
A list of vehicle attributes to associate with the user properties of the messages published on the state template's MQTT topic. For example, if you add `Vehicle.Attributes.Make` and `Vehicle.Attributes.Model` attributes, these attributes are included as user properties with the MQTT message.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `150 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotfleetwise-statetemplate-name"></a>
The unique alias of the state template.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z\d\-_:]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SignalCatalogArn`  <a name="cfn-iotfleetwise-statetemplate-signalcatalogarn"></a>
The Amazon Resource Name (ARN) of the signal catalog associated with the state template.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StateTemplateProperties`  <a name="cfn-iotfleetwise-statetemplate-statetemplateproperties"></a>
A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `150 | 500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotfleetwise-statetemplate-tags"></a>
Metadata that can be used to manage the state template.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotfleetwise-statetemplate-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotfleetwise-statetemplate-return-values"></a>

### Ref
<a name="aws-resource-iotfleetwise-statetemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iotfleetwise-statetemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-iotfleetwise-statetemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the state template.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the state template was created, in seconds since epoch (January 1, 1970 at midnight UTC time).

`Id`  <a name="Id-fn::getatt"></a>
The unique ID of the state template.

`LastModificationTime`  <a name="LastModificationTime-fn::getatt"></a>
The time the state template was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

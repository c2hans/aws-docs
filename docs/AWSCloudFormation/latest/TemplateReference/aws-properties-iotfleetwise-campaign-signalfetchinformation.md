---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-signalfetchinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign SignalFetchInformation
<a name="aws-properties-iotfleetwise-campaign-signalfetchinformation"></a>

Information about the signal to be fetched.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-signalfetchinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-signalfetchinformation-syntax.json"></a>

```
{
  "[Actions](#cfn-iotfleetwise-campaign-signalfetchinformation-actions)" : {{[ String, ... ]}},
  "[ConditionLanguageVersion](#cfn-iotfleetwise-campaign-signalfetchinformation-conditionlanguageversion)" : {{Number}},
  "[FullyQualifiedName](#cfn-iotfleetwise-campaign-signalfetchinformation-fullyqualifiedname)" : {{String}},
  "[SignalFetchConfig](#cfn-iotfleetwise-campaign-signalfetchinformation-signalfetchconfig)" : {{SignalFetchConfig}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-signalfetchinformation-syntax.yaml"></a>

```
  [Actions](#cfn-iotfleetwise-campaign-signalfetchinformation-actions): {{
    - String}}
  [ConditionLanguageVersion](#cfn-iotfleetwise-campaign-signalfetchinformation-conditionlanguageversion): {{Number}}
  [FullyQualifiedName](#cfn-iotfleetwise-campaign-signalfetchinformation-fullyqualifiedname): {{String}}
  [SignalFetchConfig](#cfn-iotfleetwise-campaign-signalfetchinformation-signalfetchconfig): {{
    SignalFetchConfig}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-signalfetchinformation-properties"></a>

`Actions`  <a name="cfn-iotfleetwise-campaign-signalfetchinformation-actions"></a>
The actions to be performed by the signal fetch.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `2048 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConditionLanguageVersion`  <a name="cfn-iotfleetwise-campaign-signalfetchinformation-conditionlanguageversion"></a>
The version of the condition language used.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FullyQualifiedName`  <a name="cfn-iotfleetwise-campaign-signalfetchinformation-fullyqualifiedname"></a>
The fully qualified name of the signal to be fetched.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.]+$`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SignalFetchConfig`  <a name="cfn-iotfleetwise-campaign-signalfetchinformation-signalfetchconfig"></a>
The configuration of the signal fetch operation.
*Required*: Yes
*Type*: [SignalFetchConfig](aws-properties-iotfleetwise-campaign-signalfetchconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

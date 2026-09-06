---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-customdecodinginterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest CustomDecodingInterface
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodinginterface"></a>

Represents a custom network interface as defined by the customer.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodinginterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodinginterface-syntax.json"></a>

```
{
  "[Name](#cfn-iotfleetwise-decodermanifest-customdecodinginterface-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodinginterface-syntax.yaml"></a>

```
  [Name](#cfn-iotfleetwise-decodermanifest-customdecodinginterface-name): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodinginterface-properties"></a>

`Name`  <a name="cfn-iotfleetwise-decodermanifest-customdecodinginterface-name"></a>
The name of the interface.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z\d\-_:]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

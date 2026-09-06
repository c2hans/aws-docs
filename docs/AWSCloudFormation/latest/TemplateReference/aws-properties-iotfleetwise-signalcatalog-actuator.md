---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-signalcatalog-actuator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::SignalCatalog Actuator
<a name="aws-properties-iotfleetwise-signalcatalog-actuator"></a>

A signal that represents a vehicle device such as the engine, heater, and door locks. Data from an actuator reports the state of a certain vehicle device.

**Note**
 Updating actuator data can change the state of a device. For example, you can turn on or off the heater by updating its actuator data.

## Syntax
<a name="aws-properties-iotfleetwise-signalcatalog-actuator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-signalcatalog-actuator-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-iotfleetwise-signalcatalog-actuator-allowedvalues)" : {{[ String, ... ]}},
  "[AssignedValue](#cfn-iotfleetwise-signalcatalog-actuator-assignedvalue)" : {{String}},
  "[DataType](#cfn-iotfleetwise-signalcatalog-actuator-datatype)" : {{String}},
  "[Description](#cfn-iotfleetwise-signalcatalog-actuator-description)" : {{String}},
  "[FullyQualifiedName](#cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname)" : {{String}},
  "[Max](#cfn-iotfleetwise-signalcatalog-actuator-max)" : {{Number}},
  "[Min](#cfn-iotfleetwise-signalcatalog-actuator-min)" : {{Number}},
  "[Unit](#cfn-iotfleetwise-signalcatalog-actuator-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-signalcatalog-actuator-syntax.yaml"></a>

```
  [AllowedValues](#cfn-iotfleetwise-signalcatalog-actuator-allowedvalues): {{
    - String}}
  [AssignedValue](#cfn-iotfleetwise-signalcatalog-actuator-assignedvalue): {{String}}
  [DataType](#cfn-iotfleetwise-signalcatalog-actuator-datatype): {{String}}
  [Description](#cfn-iotfleetwise-signalcatalog-actuator-description): {{String}}
  [FullyQualifiedName](#cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname): {{String}}
  [Max](#cfn-iotfleetwise-signalcatalog-actuator-max): {{Number}}
  [Min](#cfn-iotfleetwise-signalcatalog-actuator-min): {{Number}}
  [Unit](#cfn-iotfleetwise-signalcatalog-actuator-unit): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-signalcatalog-actuator-properties"></a>

`AllowedValues`  <a name="cfn-iotfleetwise-signalcatalog-actuator-allowedvalues"></a>
 A list of possible values an actuator can take.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssignedValue`  <a name="cfn-iotfleetwise-signalcatalog-actuator-assignedvalue"></a>
 A specified value for the actuator.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-iotfleetwise-signalcatalog-actuator-datatype"></a>
The specified data type of the actuator.
*Required*: Yes
*Type*: String
*Allowed values*: `INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | BOOLEAN | FLOAT | DOUBLE | STRING | UNIX_TIMESTAMP | INT8_ARRAY | UINT8_ARRAY | INT16_ARRAY | UINT16_ARRAY | INT32_ARRAY | UINT32_ARRAY | INT64_ARRAY | UINT64_ARRAY | BOOLEAN_ARRAY | FLOAT_ARRAY | DOUBLE_ARRAY | STRING_ARRAY | UNIX_TIMESTAMP_ARRAY | UNKNOWN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iotfleetwise-signalcatalog-actuator-description"></a>
 A brief description of the actuator.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FullyQualifiedName`  <a name="cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname"></a>
The fully qualified name of the actuator. For example, the fully qualified name of an actuator might be `Vehicle.Front.Left.Door.Lock`.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_.]+`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Max`  <a name="cfn-iotfleetwise-signalcatalog-actuator-max"></a>
 The specified possible maximum value of an actuator.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-iotfleetwise-signalcatalog-actuator-min"></a>
 The specified possible minimum value of an actuator.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-iotfleetwise-signalcatalog-actuator-unit"></a>
 The scientific unit for the actuator.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

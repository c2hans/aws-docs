---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-signalcatalog-sensor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::SignalCatalog Sensor
<a name="aws-properties-iotfleetwise-signalcatalog-sensor"></a>

An input component that reports the environmental condition of a vehicle.

**Note**
You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.

## Syntax
<a name="aws-properties-iotfleetwise-signalcatalog-sensor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-signalcatalog-sensor-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-iotfleetwise-signalcatalog-sensor-allowedvalues)" : {{[ String, ... ]}},
  "[DataType](#cfn-iotfleetwise-signalcatalog-sensor-datatype)" : {{String}},
  "[Description](#cfn-iotfleetwise-signalcatalog-sensor-description)" : {{String}},
  "[FullyQualifiedName](#cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname)" : {{String}},
  "[Max](#cfn-iotfleetwise-signalcatalog-sensor-max)" : {{Number}},
  "[Min](#cfn-iotfleetwise-signalcatalog-sensor-min)" : {{Number}},
  "[Unit](#cfn-iotfleetwise-signalcatalog-sensor-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-signalcatalog-sensor-syntax.yaml"></a>

```
  [AllowedValues](#cfn-iotfleetwise-signalcatalog-sensor-allowedvalues): {{
    - String}}
  [DataType](#cfn-iotfleetwise-signalcatalog-sensor-datatype): {{String}}
  [Description](#cfn-iotfleetwise-signalcatalog-sensor-description): {{String}}
  [FullyQualifiedName](#cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname): {{String}}
  [Max](#cfn-iotfleetwise-signalcatalog-sensor-max): {{Number}}
  [Min](#cfn-iotfleetwise-signalcatalog-sensor-min): {{Number}}
  [Unit](#cfn-iotfleetwise-signalcatalog-sensor-unit): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-signalcatalog-sensor-properties"></a>

`AllowedValues`  <a name="cfn-iotfleetwise-signalcatalog-sensor-allowedvalues"></a>
 A list of possible values a sensor can take.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-iotfleetwise-signalcatalog-sensor-datatype"></a>
The specified data type of the sensor.
*Required*: Yes
*Type*: String
*Allowed values*: `INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | BOOLEAN | FLOAT | DOUBLE | STRING | UNIX_TIMESTAMP | INT8_ARRAY | UINT8_ARRAY | INT16_ARRAY | UINT16_ARRAY | INT32_ARRAY | UINT32_ARRAY | INT64_ARRAY | UINT64_ARRAY | BOOLEAN_ARRAY | FLOAT_ARRAY | DOUBLE_ARRAY | STRING_ARRAY | UNIX_TIMESTAMP_ARRAY | UNKNOWN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iotfleetwise-signalcatalog-sensor-description"></a>
 A brief description of a sensor.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FullyQualifiedName`  <a name="cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname"></a>
The fully qualified name of the sensor. For example, the fully qualified name of a sensor might be `Vehicle.Body.Engine.Battery`.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_.]+`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Max`  <a name="cfn-iotfleetwise-signalcatalog-sensor-max"></a>
 The specified possible maximum value of the sensor.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-iotfleetwise-signalcatalog-sensor-min"></a>
 The specified possible minimum value of the sensor.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-iotfleetwise-signalcatalog-sensor-unit"></a>
 The scientific unit of measurement for data collected by the sensor.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

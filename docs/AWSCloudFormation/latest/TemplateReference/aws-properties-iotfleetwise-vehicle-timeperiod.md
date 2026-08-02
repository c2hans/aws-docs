---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-vehicle-timeperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Vehicle TimePeriod
<a name="aws-properties-iotfleetwise-vehicle-timeperiod"></a>

The length of time between state template updates.

## Syntax
<a name="aws-properties-iotfleetwise-vehicle-timeperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-vehicle-timeperiod-syntax.json"></a>

```
{
  "[Unit](#cfn-iotfleetwise-vehicle-timeperiod-unit)" : {{String}},
  "[Value](#cfn-iotfleetwise-vehicle-timeperiod-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-vehicle-timeperiod-syntax.yaml"></a>

```
  [Unit](#cfn-iotfleetwise-vehicle-timeperiod-unit): {{String}}
  [Value](#cfn-iotfleetwise-vehicle-timeperiod-value): {{Number}}
```

## Properties
<a name="aws-properties-iotfleetwise-vehicle-timeperiod-properties"></a>

`Unit`  <a name="cfn-iotfleetwise-vehicle-timeperiod-unit"></a>
A unit of time.
*Required*: Yes
*Type*: String
*Allowed values*: `MILLISECOND | SECOND | MINUTE | HOUR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotfleetwise-vehicle-timeperiod-value"></a>
A number of time units.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

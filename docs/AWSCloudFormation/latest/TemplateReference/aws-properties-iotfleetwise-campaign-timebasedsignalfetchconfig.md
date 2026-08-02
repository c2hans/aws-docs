---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign TimeBasedSignalFetchConfig
<a name="aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig"></a>

Used to configure a frequency-based vehicle signal fetch.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig-syntax.json"></a>

```
{
  "[ExecutionFrequencyMs](#cfn-iotfleetwise-campaign-timebasedsignalfetchconfig-executionfrequencyms)" : {{Number}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig-syntax.yaml"></a>

```
  [ExecutionFrequencyMs](#cfn-iotfleetwise-campaign-timebasedsignalfetchconfig-executionfrequencyms): {{Number}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig-properties"></a>

`ExecutionFrequencyMs`  <a name="cfn-iotfleetwise-campaign-timebasedsignalfetchconfig-executionfrequencyms"></a>
The frequency with which the signal fetch will be executed.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

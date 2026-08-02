---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LookoutEquipment::InferenceScheduler InputNameConfiguration
<a name="aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration"></a>

<a name="aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration-description"></a>The `InputNameConfiguration` property type specifies Property description not available. for an [AWS::LookoutEquipment::InferenceScheduler](aws-resource-lookoutequipment-inferencescheduler.md).

## Syntax
<a name="aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration-syntax.json"></a>

```
{
  "[ComponentTimestampDelimiter](#cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-componenttimestampdelimiter)" : {{String}},
  "[TimestampFormat](#cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-timestampformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration-syntax.yaml"></a>

```
  [ComponentTimestampDelimiter](#cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-componenttimestampdelimiter): {{String}}
  [TimestampFormat](#cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-timestampformat): {{String}}
```

## Properties
<a name="aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration-properties"></a>

`ComponentTimestampDelimiter`  <a name="cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-componenttimestampdelimiter"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(\-|\_|\s)?$`
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestampFormat`  <a name="cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-timestampformat"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^EPOCH|yyyy-MM-dd-HH-mm-ss|yyyyMMddHHmmss$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

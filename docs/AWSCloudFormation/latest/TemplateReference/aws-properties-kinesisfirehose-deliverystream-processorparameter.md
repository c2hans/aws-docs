---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream ProcessorParameter
<a name="aws-properties-kinesisfirehose-deliverystream-processorparameter"></a>

The `ProcessorParameter` property specifies a processor parameter in a data processor for an Amazon Kinesis Data Firehose delivery stream.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-processorparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-processorparameter-syntax.json"></a>

```
{
  "[ParameterName](#cfn-kinesisfirehose-deliverystream-processorparameter-parametername)" : {{String}},
  "[ParameterValue](#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-processorparameter-syntax.yaml"></a>

```
  [ParameterName](#cfn-kinesisfirehose-deliverystream-processorparameter-parametername): {{String}}
  [ParameterValue](#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-processorparameter-properties"></a>

`ParameterName`  <a name="cfn-kinesisfirehose-deliverystream-processorparameter-parametername"></a>
The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds`. The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.
*Required*: Yes
*Type*: String
*Allowed values*: `LambdaArn | NumberOfRetries | MetadataExtractionQuery | JsonParsingEngine | RoleArn | BufferSizeInMBs | BufferIntervalInSeconds | SubRecordType | Delimiter | CompressionFormat | DataMessageExtraction`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue"></a>
The parameter value.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `5120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

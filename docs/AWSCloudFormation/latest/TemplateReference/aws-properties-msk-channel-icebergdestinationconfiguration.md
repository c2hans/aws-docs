---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-icebergdestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel IcebergDestinationConfiguration
<a name="aws-properties-msk-channel-icebergdestinationconfiguration"></a>

<a name="aws-properties-msk-channel-icebergdestinationconfiguration-description"></a>The `IcebergDestinationConfiguration` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-icebergdestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-icebergdestinationconfiguration-syntax.json"></a>

```
{
  "[AppendOnly](#cfn-msk-channel-icebergdestinationconfiguration-appendonly)" : {{Boolean}},
  "[Catalog](#cfn-msk-channel-icebergdestinationconfiguration-catalog)" : {{Catalog}},
  "[CompressionType](#cfn-msk-channel-icebergdestinationconfiguration-compressiontype)" : {{String}},
  "[DataFreshnessInSeconds](#cfn-msk-channel-icebergdestinationconfiguration-datafreshnessinseconds)" : {{Integer}},
  "[DeadLetterQueueS3](#cfn-msk-channel-icebergdestinationconfiguration-deadletterqueues3)" : {{DeadLetterQueueS3}},
  "[DestinationTableList](#cfn-msk-channel-icebergdestinationconfiguration-destinationtablelist)" : {{[ DestinationTable, ... ]}},
  "[SchemaEvolution](#cfn-msk-channel-icebergdestinationconfiguration-schemaevolution)" : {{SchemaEvolution}},
  "[ServiceExecutionRoleArn](#cfn-msk-channel-icebergdestinationconfiguration-serviceexecutionrolearn)" : {{String}},
  "[TableCreation](#cfn-msk-channel-icebergdestinationconfiguration-tablecreation)" : {{TableCreation}}
}
```

### YAML
<a name="aws-properties-msk-channel-icebergdestinationconfiguration-syntax.yaml"></a>

```
  [AppendOnly](#cfn-msk-channel-icebergdestinationconfiguration-appendonly): {{Boolean}}
  [Catalog](#cfn-msk-channel-icebergdestinationconfiguration-catalog): {{
    Catalog}}
  [CompressionType](#cfn-msk-channel-icebergdestinationconfiguration-compressiontype): {{String}}
  [DataFreshnessInSeconds](#cfn-msk-channel-icebergdestinationconfiguration-datafreshnessinseconds): {{Integer}}
  [DeadLetterQueueS3](#cfn-msk-channel-icebergdestinationconfiguration-deadletterqueues3): {{
    DeadLetterQueueS3}}
  [DestinationTableList](#cfn-msk-channel-icebergdestinationconfiguration-destinationtablelist): {{
    - DestinationTable}}
  [SchemaEvolution](#cfn-msk-channel-icebergdestinationconfiguration-schemaevolution): {{
    SchemaEvolution}}
  [ServiceExecutionRoleArn](#cfn-msk-channel-icebergdestinationconfiguration-serviceexecutionrolearn): {{String}}
  [TableCreation](#cfn-msk-channel-icebergdestinationconfiguration-tablecreation): {{
    TableCreation}}
```

## Properties
<a name="aws-properties-msk-channel-icebergdestinationconfiguration-properties"></a>

`AppendOnly`  <a name="cfn-msk-channel-icebergdestinationconfiguration-appendonly"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Catalog`  <a name="cfn-msk-channel-icebergdestinationconfiguration-catalog"></a>
Property description not available.
*Required*: No
*Type*: [Catalog](aws-properties-msk-channel-catalog.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompressionType`  <a name="cfn-msk-channel-icebergdestinationconfiguration-compressiontype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ZSTD | SNAPPY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataFreshnessInSeconds`  <a name="cfn-msk-channel-icebergdestinationconfiguration-datafreshnessinseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterQueueS3`  <a name="cfn-msk-channel-icebergdestinationconfiguration-deadletterqueues3"></a>
Property description not available.
*Required*: Yes
*Type*: [DeadLetterQueueS3](aws-properties-msk-channel-deadletterqueues3.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationTableList`  <a name="cfn-msk-channel-icebergdestinationconfiguration-destinationtablelist"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [DestinationTable](aws-properties-msk-channel-destinationtable.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaEvolution`  <a name="cfn-msk-channel-icebergdestinationconfiguration-schemaevolution"></a>
Property description not available.
*Required*: Yes
*Type*: [SchemaEvolution](aws-properties-msk-channel-schemaevolution.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceExecutionRoleArn`  <a name="cfn-msk-channel-icebergdestinationconfiguration-serviceexecutionrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:iam::[\w-]+:role.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableCreation`  <a name="cfn-msk-channel-icebergdestinationconfiguration-tablecreation"></a>
Property description not available.
*Required*: Yes
*Type*: [TableCreation](aws-properties-msk-channel-tablecreation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

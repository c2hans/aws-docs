---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream AmazonOpenSearchServerlessDestinationConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration"></a>

Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-syntax.json"></a>

```
{
  "[BufferingHints](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-bufferinghints)" : {{AmazonOpenSearchServerlessBufferingHints}},
  "[CloudWatchLoggingOptions](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-cloudwatchloggingoptions)" : {{CloudWatchLoggingOptions}},
  "[CollectionEndpoint](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-collectionendpoint)" : {{String}},
  "[IndexName](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-indexname)" : {{String}},
  "[ProcessingConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-processingconfiguration)" : {{ProcessingConfiguration}},
  "[RetryOptions](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-retryoptions)" : {{AmazonOpenSearchServerlessRetryOptions}},
  "[RoleARN](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-rolearn)" : {{String}},
  "[S3BackupMode](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3backupmode)" : {{String}},
  "[S3Configuration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3configuration)" : {{S3DestinationConfiguration}},
  "[VpcConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-vpcconfiguration)" : {{VpcConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-syntax.yaml"></a>

```
  [BufferingHints](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-bufferinghints): {{
    AmazonOpenSearchServerlessBufferingHints}}
  [CloudWatchLoggingOptions](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-cloudwatchloggingoptions): {{
    CloudWatchLoggingOptions}}
  [CollectionEndpoint](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-collectionendpoint): {{String}}
  [IndexName](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-indexname): {{String}}
  [ProcessingConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-processingconfiguration): {{
    ProcessingConfiguration}}
  [RetryOptions](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-retryoptions): {{
    AmazonOpenSearchServerlessRetryOptions}}
  [RoleARN](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-rolearn): {{String}}
  [S3BackupMode](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3backupmode): {{String}}
  [S3Configuration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3configuration): {{
    S3DestinationConfiguration}}
  [VpcConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-properties"></a>

`BufferingHints`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-bufferinghints"></a>
The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
*Required*: No
*Type*: [AmazonOpenSearchServerlessBufferingHints](aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CloudWatchLoggingOptions`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-cloudwatchloggingoptions"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchLoggingOptions](aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CollectionEndpoint`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-collectionendpoint"></a>
The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.
*Required*: No
*Type*: String
*Pattern*: `https:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexName`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-indexname"></a>
The Serverless offering for Amazon OpenSearch Service index name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessingConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-processingconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ProcessingConfiguration](aws-properties-kinesisfirehose-deliverystream-processingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryOptions`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-retryoptions"></a>
The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).
*Required*: No
*Type*: [AmazonOpenSearchServerlessRetryOptions](aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BackupMode`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3backupmode"></a>
Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.
*Required*: No
*Type*: String
*Allowed values*: `FailedDocumentsOnly | AllDocuments`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Configuration`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [S3DestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-vpcconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [VpcConfiguration](aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream
<a name="aws-resource-kinesisfirehose-deliverystream"></a>

The `AWS::KinesisFirehose::DeliveryStream` resource specifies an Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivery stream that delivers real-time streaming data to an Amazon Simple Storage Service (Amazon S3), Amazon Redshift, or Amazon Elasticsearch Service (Amazon ES) destination. For more information, see [Creating an Amazon Kinesis Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Kinesis Data Firehose Developer Guide*.

## Syntax
<a name="aws-resource-kinesisfirehose-deliverystream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesisfirehose-deliverystream-syntax.json"></a>

```
{
  "Type" : "AWS::KinesisFirehose::DeliveryStream",
  "Properties" : {
      "[AmazonOpenSearchServerlessDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration)" : {{AmazonOpenSearchServerlessDestinationConfiguration}},
      "[AmazonopensearchserviceDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration)" : {{AmazonopensearchserviceDestinationConfiguration}},
      "[DatabaseSourceConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration)" : {{DatabaseSourceConfiguration}},
      "[DeliveryStreamEncryptionConfigurationInput](#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput)" : {{DeliveryStreamEncryptionConfigurationInput}},
      "[DeliveryStreamName](#cfn-kinesisfirehose-deliverystream-deliverystreamname)" : {{String}},
      "[DeliveryStreamType](#cfn-kinesisfirehose-deliverystream-deliverystreamtype)" : {{String}},
      "[DirectPutSourceConfiguration](#cfn-kinesisfirehose-deliverystream-directputsourceconfiguration)" : {{DirectPutSourceConfiguration}},
      "[ElasticsearchDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration)" : {{ElasticsearchDestinationConfiguration}},
      "[ExtendedS3DestinationConfiguration](#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration)" : {{ExtendedS3DestinationConfiguration}},
      "[HttpEndpointDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration)" : {{HttpEndpointDestinationConfiguration}},
      "[IcebergDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration)" : {{IcebergDestinationConfiguration}},
      "[KinesisStreamSourceConfiguration](#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration)" : {{KinesisStreamSourceConfiguration}},
      "[MSKSourceConfiguration](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration)" : {{MSKSourceConfiguration}},
      "[RedshiftDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration)" : {{RedshiftDestinationConfiguration}},
      "[S3DestinationConfiguration](#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration)" : {{S3DestinationConfiguration}},
      "[SnowflakeDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration)" : {{SnowflakeDestinationConfiguration}},
      "[SplunkDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration)" : {{SplunkDestinationConfiguration}},
      "[Tags](#cfn-kinesisfirehose-deliverystream-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kinesisfirehose-deliverystream-syntax.yaml"></a>

```
Type: AWS::KinesisFirehose::DeliveryStream
Properties:
  [AmazonOpenSearchServerlessDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration): {{
    AmazonOpenSearchServerlessDestinationConfiguration}}
  [AmazonopensearchserviceDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration): {{
    AmazonopensearchserviceDestinationConfiguration}}
  [DatabaseSourceConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration): {{
    DatabaseSourceConfiguration}}
  [DeliveryStreamEncryptionConfigurationInput](#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput): {{
    DeliveryStreamEncryptionConfigurationInput}}
  [DeliveryStreamName](#cfn-kinesisfirehose-deliverystream-deliverystreamname): {{String}}
  [DeliveryStreamType](#cfn-kinesisfirehose-deliverystream-deliverystreamtype): {{String}}
  [DirectPutSourceConfiguration](#cfn-kinesisfirehose-deliverystream-directputsourceconfiguration): {{
    DirectPutSourceConfiguration}}
  [ElasticsearchDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration): {{
    ElasticsearchDestinationConfiguration}}
  [ExtendedS3DestinationConfiguration](#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration): {{
    ExtendedS3DestinationConfiguration}}
  [HttpEndpointDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration): {{
    HttpEndpointDestinationConfiguration}}
  [IcebergDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration): {{
    IcebergDestinationConfiguration}}
  [KinesisStreamSourceConfiguration](#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration): {{
    KinesisStreamSourceConfiguration}}
  [MSKSourceConfiguration](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration): {{
    MSKSourceConfiguration}}
  [RedshiftDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration): {{
    RedshiftDestinationConfiguration}}
  [S3DestinationConfiguration](#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration): {{
    S3DestinationConfiguration}}
  [SnowflakeDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration): {{
    SnowflakeDestinationConfiguration}}
  [SplunkDestinationConfiguration](#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration): {{
    SplunkDestinationConfiguration}}
  [Tags](#cfn-kinesisfirehose-deliverystream-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kinesisfirehose-deliverystream-properties"></a>

`AmazonOpenSearchServerlessDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration"></a>
Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.
*Required*: No
*Type*: [AmazonOpenSearchServerlessDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonopensearchserviceDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration"></a>
The destination in Amazon OpenSearch Service. You can specify only one destination.
*Required*: Conditional
*Type*: [AmazonopensearchserviceDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseSourceConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration"></a>
 The top level object for configuring streams with database as a source.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: [DatabaseSourceConfiguration](aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeliveryStreamEncryptionConfigurationInput`  <a name="cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput"></a>
Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).
*Required*: No
*Type*: [DeliveryStreamEncryptionConfigurationInput](aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryStreamName`  <a name="cfn-kinesisfirehose-deliverystream-deliverystreamname"></a>
The name of the Firehose stream.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9._-]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeliveryStreamType`  <a name="cfn-kinesisfirehose-deliverystream-deliverystreamtype"></a>
The Firehose stream type. This can be one of the following values:
+ `DirectPut`: Provider applications access the Firehose stream directly.
+ `KinesisStreamAsSource`: The Firehose stream uses a Kinesis data stream as a source.
*Required*: No
*Type*: String
*Allowed values*: `DatabaseAsSource | DirectPut | KinesisStreamAsSource | MSKAsSource`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectPutSourceConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-directputsourceconfiguration"></a>
The structure that configures parameters such as `ThroughputHintInMBs` for a stream configured with Direct PUT as a source.
*Required*: No
*Type*: [DirectPutSourceConfiguration](aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ElasticsearchDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration"></a>
An Amazon ES destination for the delivery stream.
Conditional. You must specify only one destination configuration.
If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires [some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt).
*Required*: Conditional
*Type*: [ElasticsearchDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExtendedS3DestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration"></a>
An Amazon S3 destination for the delivery stream.
Conditional. You must specify only one destination configuration.
If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires [some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt).
*Required*: Conditional
*Type*: [ExtendedS3DestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpEndpointDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration"></a>
Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.
*Required*: No
*Type*: [HttpEndpointDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IcebergDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration"></a>
 Specifies the destination configure settings for Apache Iceberg Table.
*Required*: No
*Type*: [IcebergDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisStreamSourceConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration"></a>
When a Kinesis stream is used as the source for the delivery stream, a [KinesisStreamSourceConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html) containing the Kinesis stream ARN and the role ARN for the source stream.
*Required*: No
*Type*: [KinesisStreamSourceConfiguration](aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MSKSourceConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-msksourceconfiguration"></a>
The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
*Required*: No
*Type*: [MSKSourceConfiguration](aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RedshiftDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration"></a>
An Amazon Redshift destination for the delivery stream.
Conditional. You must specify only one destination configuration.
If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires [some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt).
*Required*: Conditional
*Type*: [RedshiftDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-s3destinationconfiguration"></a>
The `S3DestinationConfiguration` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.
Conditional. You must specify only one destination configuration.
If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires [some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt).
*Required*: Conditional
*Type*: [S3DestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnowflakeDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration"></a>
Configure Snowflake destination
*Required*: No
*Type*: [SnowflakeDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SplunkDestinationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration"></a>
The configuration of a destination in Splunk for the delivery stream.
*Required*: No
*Type*: [SplunkDestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kinesisfirehose-deliverystream-tags"></a>
A set of tags to assign to the Firehose stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the AWS Billing and Cost Management User Guide.
You can specify up to 50 tags when creating a Firehose stream.
If you specify tags in the `CreateDeliveryStream` action, Amazon Data Firehose performs an additional authorization on the `firehose:TagDeliveryStream` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an `AccessDeniedException` such as following.
 **AccessDeniedException**
User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.
For an example IAM policy, see [Tag example.](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples)
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesisfirehose-deliverystream-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesisfirehose-deliverystream-return-values"></a>

### Ref
<a name="aws-resource-kinesisfirehose-deliverystream-return-values-ref"></a>

When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the delivery stream name, such as `mystack-deliverystream-1ABCD2EF3GHIJ`.

For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-kinesisfirehose-deliverystream-return-values-fn--getatt"></a>

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using Fn::GetAtt, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-kinesisfirehose-deliverystream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the delivery stream, such as `arn:aws:firehose:us-east-2:123456789012:deliverystream/delivery-stream-name`.

## Examples
<a name="aws-resource-kinesisfirehose-deliverystream--examples"></a>

**Topics**
+ [Create a Kinesis Data Firehose Delivery Stream](#aws-resource-kinesisfirehose-deliverystream--examples--Create_a_Kinesis_Data_Firehose_Delivery_Stream)
+ [Convert Record Format](#aws-resource-kinesisfirehose-deliverystream--examples--Convert_Record_Format)
+ [Specify an Amazon S3 Destination for the Delivery Stream](#aws-resource-kinesisfirehose-deliverystream--examples--Specify_an_Amazon_S3_Destination_for_the_Delivery_Stream)
+ [Specify a Kinesis Stream as the Source for the Delivery Stream](#aws-resource-kinesisfirehose-deliverystream--examples--Specify_a_Kinesis_Stream_as_the_Source_for_the_Delivery_Stream)

### Create a Kinesis Data Firehose Delivery Stream
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Create_a_Kinesis_Data_Firehose_Delivery_Stream"></a>

The following example creates a Kinesis Data Firehose delivery stream that delivers data to an Amazon ES destination. Kinesis Data Firehose backs up all data sent to the destination in an Amazon S3 bucket.

#### JSON
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Create_a_Kinesis_Data_Firehose_Delivery_Stream--json"></a>

```
"ElasticSearchDeliveryStream": {
   "Type": "AWS::KinesisFirehose::DeliveryStream",
   "Properties": {
      "ElasticsearchDestinationConfiguration": {
         "BufferingHints": {
            "IntervalInSeconds": 60,
            "SizeInMBs": 50
      },
      "CloudWatchLoggingOptions": {
         "Enabled": true,
         "LogGroupName": "deliverystream",
         "LogStreamName": "elasticsearchDelivery"
      },
      "DomainARN": { "Ref" : "MyDomainARN" },
      "IndexName": { "Ref" : "MyIndexName" },
      "IndexRotationPeriod": "NoRotation",
      "TypeName" : "fromFirehose",
      "RetryOptions": {
         "DurationInSeconds": "60"
      },
      "RoleARN": { "Fn::GetAtt" : ["ESdeliveryRole", "Arn"] },
      "S3BackupMode": "AllDocuments",
      "S3Configuration": {
         "BucketARN": { "Ref" : "MyBackupBucketARN" },
         "BufferingHints": {
            "IntervalInSeconds": "60",
            "SizeInMBs": "50"
         },
         "CompressionFormat": "UNCOMPRESSED",
         "Prefix": "firehose/",
         "RoleARN": { "Fn::GetAtt" : ["S3deliveryRole", "Arn"] },
         "CloudWatchLoggingOptions" : {
            "Enabled" : true,
            "LogGroupName" : "deliverystream",
            "LogStreamName" : "s3Backup"
         }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Create_a_Kinesis_Data_Firehose_Delivery_Stream--yaml"></a>

```
ElasticSearchDeliveryStream:
   Type: AWS::KinesisFirehose::DeliveryStream
   Properties:
      ElasticsearchDestinationConfiguration:
         BufferingHints:
            IntervalInSeconds: 60
            SizeInMBs: 50
         CloudWatchLoggingOptions:
            Enabled: true
            LogGroupName: "deliverystream"
            LogStreamName: "elasticsearchDelivery"
         DomainARN:
            Ref: "MyDomainARN"
         IndexName:
            Ref: "MyIndexName"
         IndexRotationPeriod: "NoRotation"
         TypeName: "fromFirehose"
         RetryOptions:
            DurationInSeconds: "60"
         RoleARN:
            Fn::GetAtt:
               - "ESdeliveryRole"
               - "Arn"
         S3BackupMode: "AllDocuments"
         S3Configuration:
            BucketARN:
               Ref: "MyBackupBucketARN"
            BufferingHints:
               IntervalInSeconds: "60"
               SizeInMBs: "50"
            CompressionFormat: "UNCOMPRESSED"
            Prefix: "firehose/"
            RoleARN:
               Fn::GetAtt:
                  - "S3deliveryRole"
                  - "Arn"
            CloudWatchLoggingOptions:
               Enabled: true
               LogGroupName: "deliverystream"
               LogStreamName: "s3Backup"
```

### Convert Record Format
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Convert_Record_Format"></a>

The following example shows record format conversion.

#### YAML
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Convert_Record_Format--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Stack for Firehose DeliveryStream S3 Destination.
Resources:

  GlueDatabase:
    Type: AWS::Glue::Database
    Properties:
      CatalogId: !Ref AWS::AccountId
      DatabaseInput: {}

  GlueTable:
    Type: AWS::Glue::Table
    Properties:
      CatalogId: !Ref AWS::AccountId
      DatabaseName: !Ref GlueDatabase
      TableInput:
        Owner: owner
        Retention: 0
        StorageDescriptor:
          Columns:
          - Name: pickup_latitude
            Type: double
          - Name: pickup_longitude
            Type: double
          - Name: dropoff_latitude
            Type: double
          - Name: dropoff_longitude
            Type: double
          - Name: trip_id
            Type: int
          - Name: trip_distance
            Type: double
          - Name: passenger_count
            Type: int
          - Name: pickup_datetime
            Type: timestamp
          - Name: dropoff_datetime
            Type: timestamp
          - Name: total_amount
            Type: double
          InputFormat: org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat
          OutputFormat: org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat
          Compressed: false
          NumberOfBuckets: -1
          SerdeInfo:
            SerializationLibrary: org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe
            Parameters:
              serialization.format: '1'
          BucketColumns: []
          SortColumns: []
          StoredAsSubDirectories: false
        PartitionKeys:
        - Name: year
          Type: string
        - Name: month
          Type: string
        - Name: day
          Type: string
        - Name: hour
          Type: string
        TableType: EXTERNAL_TABLE

  deliverystream:
    Type: AWS::KinesisFirehose::DeliveryStream
    Properties:
      DeliveryStreamType: DirectPut
      ExtendedS3DestinationConfiguration:
        RoleARN: !GetAtt deliveryRole.Arn
        BucketARN: !Join
          - ''
          - - 'arn:aws:s3:::'
            - !Ref s3bucket
        Prefix: !Join
          - ''
          - - !Ref GlueTable
            -  '/year=!{timestamp:YYYY}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/'
        ErrorOutputPrefix: !Join
          - ''
          - - !Ref GlueTable
            -  'error/!{firehose:error-output-type}/year=!{timestamp:YYYY}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/'
        BufferingHints:
          SizeInMBs: 128
          IntervalInSeconds: 300
        CompressionFormat: UNCOMPRESSED
        EncryptionConfiguration:
          NoEncryptionConfig: NoEncryption
        CloudWatchLoggingOptions:
          Enabled: true
          LogGroupName: !Join
            - ''
            - - 'KDF-'
              - !Ref GlueTable
          LogStreamName: S3Delivery
        S3BackupMode: Disabled
        DataFormatConversionConfiguration:
          SchemaConfiguration:
            CatalogId: !Ref AWS::AccountId
            RoleARN: !GetAtt deliveryRole.Arn
            DatabaseName: !Ref GlueDatabase
            TableName: !Ref GlueTable
            Region: !Ref AWS::Region
            VersionId: LATEST
          InputFormatConfiguration:
            Deserializer:
              OpenXJsonSerDe: {}
          OutputFormatConfiguration:
            Serializer:
              ParquetSerDe: {}
          Enabled: True

  s3bucket:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled

  deliveryRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: firehose.amazonaws.com
            Action: 'sts:AssumeRole'
            Condition:
              StringEquals:
                'sts:ExternalId': !Ref 'AWS::AccountId'
      Path: "/"
      Policies:
        - PolicyName: firehose_delivery_policy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - 's3:AbortMultipartUpload'
                  - 's3:GetBucketLocation'
                  - 's3:GetObject'
                  - 's3:ListBucket'
                  - 's3:ListBucketMultipartUploads'
                  - 's3:PutObject'
                Resource:
                  - !Join
                    - ''
                    - - 'arn:aws:s3:::'
                      - !Ref s3bucket
                  - !Join
                    - ''
                    - - 'arn:aws:s3:::'
                      - !Ref s3bucket
                      - '/*'
              - Effect: Allow
                Action: 'glue:GetTableVersions'
                Resource: '*'
              - Effect: Allow
                Action: 'logs:PutLogEvents'
                Resource:
                - !Join
                    - ''
                    - - 'arn:aws:logs:'
                      - !Ref 'AWS::Region'
                      - ':'
                      - !Ref 'AWS::AccountId'
                      - 'log-group:/aws/kinesisfirehose/KDF-'
                      - !Ref GlueTable
                      - ':log-stream:*'
Outputs:
  deliverysreamARN:
    Description: The ARN of the firehose delivery stream
    Value: !GetAtt deliverystream.Arn
```

### Specify an Amazon S3 Destination for the Delivery Stream
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Specify_an_Amazon_S3_Destination_for_the_Delivery_Stream"></a>

The following example uses the `ExtendedS3DestinationConfiguration` property to specify an Amazon S3 destination for the delivery stream.

#### JSON
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Specify_an_Amazon_S3_Destination_for_the_Delivery_Stream--json"></a>

```
{
  "Resources":{
    "Firehose":{
      "Type" : "AWS::KinesisFirehose::DeliveryStream",
      "Properties" : {
          "DeliveryStreamName" : "tester-partitioning-delimiter",
          "DeliveryStreamType" : "DirectPut",
          "ExtendedS3DestinationConfiguration":
            {
              "BucketARN": "arn:aws:s3:::dp-firehose-test",
              "BufferingHints": {
                "SizeInMBs": 128,
                "IntervalInSeconds": 900
              },
              "CompressionFormat": "UNCOMPRESSED",
              "ErrorOutputPrefix": "table/error/!{firehose:error-output-type}/dt=!{timestamp:yyyy'-'MM'-'dd}/h=!{timestamp:HH}/",
              "Prefix": "YYYY=!{partitionKeyFromQuery:YYYY}/MM=!{partitionKeyFromQuery:MM}//DD=!{partitionKeyFromQuery:DD}/HH=!{partitionKeyFromQuery:HH}/REGION=!{partitionKeyFromQuery:REGION}/SITEID=!{partitionKeyFromQuery:SITEID}/",
              "RoleARN": "arn:aws:iam::012345678912:role/service-role/KinesisFirehoseServiceRole-dp-kinesis-f-us-east-1-012345678912",
              "DynamicPartitioningConfiguration":
              {
                "Enabled": true,
                "RetryOptions": {
                  "DurationInSeconds": 300
                  }
                },
                "ProcessingConfiguration": {
                  "Enabled": true,
                  "Processors": [
                  {
                    "Type": "MetadataExtraction",
                    "Parameters": [
                      {
                      "ParameterName": "MetadataExtractionQuery",
                      "ParameterValue": "{YYYY : (.ts/1000) | strftime(\"%Y\"), MM : (.ts/1000) | strftime(\"%m\"), DD : (.ts/1000) | strftime(\"%d\"), HH: (.ts/1000) | strftime(\"%H\")}"
                      },
                      {
                        "ParameterName": "JsonParsingEngine",
                        "ParameterValue": "JQ-1.6"
                      }
                    ]
                  },
				    {
                    "Type": "AppendDelimiterToRecord",
                    "Parameters": [
                        {
                        "ParameterName": "Delimiter",
                        "ParameterValue": "\\n"
                      }
                    ]
                  }
                ]
                }
              }
            }
          }
        }
      }
```

#### YAML
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Specify_an_Amazon_S3_Destination_for_the_Delivery_Stream--yaml"></a>

```
---
Resources:
  Firehose:
    Type: AWS::KinesisFirehose::DeliveryStream
    Properties:
      DeliveryStreamName: tester-partitioning-delimiter
      DeliveryStreamType: DirectPut
      ExtendedS3DestinationConfiguration:
        BucketARN: arn:aws:s3:::dp-firehose-test
        BufferingHints:
          SizeInMBs: 128
          IntervalInSeconds: 900
        CompressionFormat: UNCOMPRESSED
        ErrorOutputPrefix: table/error/!{firehose:error-output-type}/dt=!{timestamp:yyyy'-'MM'-'dd}/h=!{timestamp:HH}/
        Prefix: YYYY=!{partitionKeyFromQuery:YYYY}/MM=!{partitionKeyFromQuery:MM}//DD=!{partitionKeyFromQuery:DD}/HH=!{partitionKeyFromQuery:HH}/REGION=!{partitionKeyFromQuery:REGION}/SITEID=!{partitionKeyFromQuery:SITEID}/
        RoleARN: arn:aws:iam::012345678912:role/service-role/KinesisFirehoseServiceRole-dp-kinesis-f-us-east-1-012345678912
        DynamicPartitioningConfiguration:
          Enabled: true
          RetryOptions:
            DurationInSeconds: 300
        ProcessingConfiguration:
          Enabled: true
          Processors:
          - Type: MetadataExtraction
            Parameters:
            - ParameterName: MetadataExtractionQuery
              ParameterValue: '{YYYY : (.ts/1000) | strftime("%Y"), MM : (.ts/1000)
                | strftime("%m"), DD : (.ts/1000) | strftime("%d"), HH: (.ts/1000)
                | strftime("%H")}'
            - ParameterName: JsonParsingEngine
              ParameterValue: JQ-1.6
          - Type: AppendDelimiterToRecord
            Parameters:
            - ParameterName: Delimiter
              ParameterValue: "\\n"
```

### Specify a Kinesis Stream as the Source for the Delivery Stream
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Specify_a_Kinesis_Stream_as_the_Source_for_the_Delivery_Stream"></a>

The following example uses the `KinesisStreamSourceConfiguration` property to specify a Kinesis stream as the source for the delivery stream.

#### JSON
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Specify_a_Kinesis_Stream_as_the_Source_for_the_Delivery_Stream--json"></a>

```
{
    "Parameters": {
        "deliveryRoleArn": {
            "Type": "String"
        },
        "deliveryStreamName": {
            "Type": "String"
        },
        "kinesisStreamARN": {
            "Type": "String"
        },
        "kinesisStreamRoleArn": {
            "Type": "String"
        },
        "s3bucketArn": {
            "Type": "String"
        }
    },
    "Resources": {
        "Deliverystream": {
            "Type": "AWS::KinesisFirehose::DeliveryStream",
            "Properties": {
                "DeliveryStreamName": {
                    "Ref": "deliveryStreamName"
                },
                "DeliveryStreamType": "KinesisStreamAsSource",
                "KinesisStreamSourceConfiguration": {
                    "KinesisStreamARN": {
                        "Ref": "kinesisStreamARN"
                    },
                    "RoleARN": {
                        "Ref": "kinesisStreamRoleArn"
                    }
                },
                "ExtendedS3DestinationConfiguration": {
                    "BucketARN": {
                        "Ref": "s3bucketArn"
                    },
                    "BufferingHints": {
                        "IntervalInSeconds": 60,
                        "SizeInMBs": 50
                    },
                    "CompressionFormat": "UNCOMPRESSED",
                    "Prefix": "firehose/",
                    "RoleARN": {
                        "Ref": "deliveryRoleArn"
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-kinesisfirehose-deliverystream--examples--Specify_a_Kinesis_Stream_as_the_Source_for_the_Delivery_Stream--yaml"></a>

```
Parameters:
    deliveryRoleArn:
        Type: String
    deliveryStreamName:
        Type: String
    kinesisStreamARN :
        Type : String
    kinesisStreamRoleArn:
        Type : String
    s3bucketArn:
        Type: String
Resources :
    Deliverystream:
        Type: AWS::KinesisFirehose::DeliveryStream
        Properties:
            DeliveryStreamName: !Ref deliveryStreamName
            DeliveryStreamType: KinesisStreamAsSource
            KinesisStreamSourceConfiguration:
                KinesisStreamARN: !Ref kinesisStreamARN
                RoleARN: !Ref kinesisStreamRoleArn
            ExtendedS3DestinationConfiguration:
                BucketARN: !Ref s3bucketArn
                BufferingHints:
                    IntervalInSeconds: 60
                    SizeInMBs: 50
                CompressionFormat: UNCOMPRESSED
                Prefix: firehose/
                RoleARN: !Ref deliveryRoleArn
```

## See also
<a name="aws-resource-kinesisfirehose-deliverystream--seealso"></a>
+ [CreateDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html) in the *Amazon Kinesis Data Firehose API Reference*.

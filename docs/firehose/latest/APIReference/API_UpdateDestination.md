---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_UpdateDestination.html
---

# UpdateDestination
<a name="API_UpdateDestination"></a>

Updates the specified destination of the specified Firehose stream.

Use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target Firehose stream remains active while the configurations are updated, so data writes to the Firehose stream can continue during this process. The updated configurations are usually effective within a few minutes.

Switching between Amazon OpenSearch Service and other services is not supported. For an Amazon OpenSearch Service destination, you can only update to another Amazon OpenSearch Service destination.

If the destination type is the same, Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if [EncryptionConfiguration](API_EncryptionConfiguration.md) is not specified, then the existing `EncryptionConfiguration` is maintained on the destination.

If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Firehose does not merge any parameters. In this case, all parameters must be specified.

Firehose uses `CurrentDeliveryStreamVersionId` to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using [DescribeDeliveryStream](API_DescribeDeliveryStream.md). Use the new version ID to set `CurrentDeliveryStreamVersionId` in the next call.

## Request Syntax
<a name="API_UpdateDestination_RequestSyntax"></a>

```
{
   "AmazonOpenSearchServerlessDestinationUpdate": {
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "CollectionEndpoint": "{{string}}",
      "IndexName": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      }
   },
   "AmazonopensearchserviceDestinationUpdate": {
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "ClusterEndpoint": "{{string}}",
      "DocumentIdOptions": {
         "DefaultDocumentIdFormat": "{{string}}"
      },
      "DomainARN": "{{string}}",
      "IndexName": "{{string}}",
      "IndexRotationPeriod": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "TypeName": "{{string}}"
   },
   "CurrentDeliveryStreamVersionId": "{{string}}",
   "DeliveryStreamName": "{{string}}",
   "DestinationId": "{{string}}",
   "ElasticsearchDestinationUpdate": {
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "ClusterEndpoint": "{{string}}",
      "DocumentIdOptions": {
         "DefaultDocumentIdFormat": "{{string}}"
      },
      "DomainARN": "{{string}}",
      "IndexName": "{{string}}",
      "IndexRotationPeriod": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "TypeName": "{{string}}"
   },
   "ExtendedS3DestinationUpdate": {
      "BucketARN": "{{string}}",
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "CompressionFormat": "{{string}}",
      "CustomTimeZone": "{{string}}",
      "DataFormatConversionConfiguration": {
         "Enabled": {{boolean}},
         "InputFormatConfiguration": {
            "Deserializer": {
               "HiveJsonSerDe": {
                  "TimestampFormats": [ "{{string}}" ]
               },
               "OpenXJsonSerDe": {
                  "CaseInsensitive": {{boolean}},
                  "ColumnToJsonKeyMappings": {
                     "{{string}}" : "{{string}}"
                  },
                  "ConvertDotsInJsonKeysToUnderscores": {{boolean}}
               }
            }
         },
         "OutputFormatConfiguration": {
            "Serializer": {
               "OrcSerDe": {
                  "BlockSizeBytes": {{number}},
                  "BloomFilterColumns": [ "{{string}}" ],
                  "BloomFilterFalsePositiveProbability": {{number}},
                  "Compression": "{{string}}",
                  "DictionaryKeyThreshold": {{number}},
                  "EnablePadding": {{boolean}},
                  "FormatVersion": "{{string}}",
                  "PaddingTolerance": {{number}},
                  "RowIndexStride": {{number}},
                  "StripeSizeBytes": {{number}}
               },
               "ParquetSerDe": {
                  "BlockSizeBytes": {{number}},
                  "Compression": "{{string}}",
                  "EnableDictionaryCompression": {{boolean}},
                  "MaxPaddingBytes": {{number}},
                  "PageSizeBytes": {{number}},
                  "WriterVersion": "{{string}}"
               }
            }
         },
         "SchemaConfiguration": {
            "CatalogId": "{{string}}",
            "DatabaseName": "{{string}}",
            "Region": "{{string}}",
            "RoleARN": "{{string}}",
            "TableName": "{{string}}",
            "VersionId": "{{string}}"
         }
      },
      "DynamicPartitioningConfiguration": {
         "Enabled": {{boolean}},
         "RetryOptions": {
            "DurationInSeconds": {{number}}
         }
      },
      "EncryptionConfiguration": {
         "KMSEncryptionConfig": {
            "AWSKMSKeyARN": "{{string}}"
         },
         "NoEncryptionConfig": "{{string}}"
      },
      "ErrorOutputPrefix": "{{string}}",
      "FileExtension": "{{string}}",
      "Prefix": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RoleARN": "{{string}}",
      "S3BackupMode": "{{string}}",
      "S3BackupUpdate": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      }
   },
   "HttpEndpointDestinationUpdate": {
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "EndpointConfiguration": {
         "AccessKey": "{{string}}",
         "Name": "{{string}}",
         "Url": "{{string}}"
      },
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RequestConfiguration": {
         "CommonAttributes": [
            {
               "AttributeName": "{{string}}",
               "AttributeValue": "{{string}}"
            }
         ],
         "ContentEncoding": "{{string}}"
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3BackupMode": "{{string}}",
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      }
   },
   "IcebergDestinationUpdate": {
      "AppendOnly": {{boolean}},
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CatalogConfiguration": {
         "CatalogARN": "{{string}}",
         "WarehouseLocation": "{{string}}"
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "DestinationTableConfigurationList": [
         {
            "DestinationDatabaseName": "{{string}}",
            "DestinationTableName": "{{string}}",
            "PartitionSpec": {
               "Identity": [
                  {
                     "SourceName": "{{string}}"
                  }
               ]
            },
            "S3ErrorOutputPrefix": "{{string}}",
            "UniqueKeys": [ "{{string}}" ]
         }
      ],
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3BackupMode": "{{string}}",
      "S3Configuration": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "SchemaEvolutionConfiguration": {
         "Enabled": {{boolean}}
      },
      "TableCreationConfiguration": {
         "Enabled": {{boolean}}
      }
   },
   "RedshiftDestinationUpdate": {
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "ClusterJDBCURL": "{{string}}",
      "CopyCommand": {
         "CopyOptions": "{{string}}",
         "DataTableColumns": "{{string}}",
         "DataTableName": "{{string}}"
      },
      "Password": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3BackupMode": "{{string}}",
      "S3BackupUpdate": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      },
      "Username": "{{string}}"
   },
   "S3DestinationUpdate": {
      "BucketARN": "{{string}}",
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "CompressionFormat": "{{string}}",
      "EncryptionConfiguration": {
         "KMSEncryptionConfig": {
            "AWSKMSKeyARN": "{{string}}"
         },
         "NoEncryptionConfig": "{{string}}"
      },
      "ErrorOutputPrefix": "{{string}}",
      "Prefix": "{{string}}",
      "RoleARN": "{{string}}"
   },
   "SnowflakeDestinationUpdate": {
      "AccountUrl": "{{string}}",
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "ContentColumnName": "{{string}}",
      "Database": "{{string}}",
      "DataLoadingOption": "{{string}}",
      "KeyPassphrase": "{{string}}",
      "MetaDataColumnName": "{{string}}",
      "PrivateKey": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "RoleARN": "{{string}}",
      "S3BackupMode": "{{string}}",
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "Schema": "{{string}}",
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      },
      "SnowflakeRoleConfiguration": {
         "Enabled": {{boolean}},
         "SnowflakeRole": "{{string}}"
      },
      "Table": "{{string}}",
      "User": "{{string}}"
   },
   "SplunkDestinationUpdate": {
      "BufferingHints": {
         "IntervalInSeconds": {{number}},
         "SizeInMBs": {{number}}
      },
      "CloudWatchLoggingOptions": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      },
      "HECAcknowledgmentTimeoutInSeconds": {{number}},
      "HECEndpoint": "{{string}}",
      "HECEndpointType": "{{string}}",
      "HECToken": "{{string}}",
      "ProcessingConfiguration": {
         "Enabled": {{boolean}},
         "Processors": [
            {
               "Parameters": [
                  {
                     "ParameterName": "{{string}}",
                     "ParameterValue": "{{string}}"
                  }
               ],
               "Type": "{{string}}"
            }
         ]
      },
      "RetryOptions": {
         "DurationInSeconds": {{number}}
      },
      "S3BackupMode": "{{string}}",
      "S3Update": {
         "BucketARN": "{{string}}",
         "BufferingHints": {
            "IntervalInSeconds": {{number}},
            "SizeInMBs": {{number}}
         },
         "CloudWatchLoggingOptions": {
            "Enabled": {{boolean}},
            "LogGroupName": "{{string}}",
            "LogStreamName": "{{string}}"
         },
         "CompressionFormat": "{{string}}",
         "EncryptionConfiguration": {
            "KMSEncryptionConfig": {
               "AWSKMSKeyARN": "{{string}}"
            },
            "NoEncryptionConfig": "{{string}}"
         },
         "ErrorOutputPrefix": "{{string}}",
         "Prefix": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_UpdateDestination_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AmazonOpenSearchServerlessDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-AmazonOpenSearchServerlessDestinationUpdate"></a>
Describes an update for a destination in the Serverless offering for Amazon OpenSearch Service.
Type: [AmazonOpenSearchServerlessDestinationUpdate](API_AmazonOpenSearchServerlessDestinationUpdate.md) object
Required: No

 ** [AmazonopensearchserviceDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-AmazonopensearchserviceDestinationUpdate"></a>
Describes an update for a destination in Amazon OpenSearch Service.
Type: [AmazonopensearchserviceDestinationUpdate](API_AmazonopensearchserviceDestinationUpdate.md) object
Required: No

 ** [CurrentDeliveryStreamVersionId](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-CurrentDeliveryStreamVersionId"></a>
Obtain this value from the `VersionId` result of [DeliveryStreamDescription](API_DeliveryStreamDescription.md). This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the `VersionId` value is updated. The service then performs a merge of the old configuration with the new configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[0-9]+`
Required: Yes

 ** [DeliveryStreamName](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [DestinationId](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-DestinationId"></a>
The ID of the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [ElasticsearchDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-ElasticsearchDestinationUpdate"></a>
Describes an update for a destination in Amazon OpenSearch Service.
Type: [ElasticsearchDestinationUpdate](API_ElasticsearchDestinationUpdate.md) object
Required: No

 ** [ExtendedS3DestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-ExtendedS3DestinationUpdate"></a>
Describes an update for a destination in Amazon S3.
Type: [ExtendedS3DestinationUpdate](API_ExtendedS3DestinationUpdate.md) object
Required: No

 ** [HttpEndpointDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-HttpEndpointDestinationUpdate"></a>
Describes an update to the specified HTTP endpoint destination.
Type: [HttpEndpointDestinationUpdate](API_HttpEndpointDestinationUpdate.md) object
Required: No

 ** [IcebergDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-IcebergDestinationUpdate"></a>
 Describes an update for a destination in Apache Iceberg Tables.
Type: [IcebergDestinationUpdate](API_IcebergDestinationUpdate.md) object
Required: No

 ** [RedshiftDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-RedshiftDestinationUpdate"></a>
Describes an update for a destination in Amazon Redshift.
Type: [RedshiftDestinationUpdate](API_RedshiftDestinationUpdate.md) object
Required: No

 ** [S3DestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-S3DestinationUpdate"></a>
[Deprecated] Describes an update for a destination in Amazon S3.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

 ** [SnowflakeDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-SnowflakeDestinationUpdate"></a>
Update to the Snowflake destination configuration settings.
Type: [SnowflakeDestinationUpdate](API_SnowflakeDestinationUpdate.md) object
Required: No

 ** [SplunkDestinationUpdate](#API_UpdateDestination_RequestSyntax) **   <a name="Firehose-UpdateDestination-request-SplunkDestinationUpdate"></a>
Describes an update for a destination in Splunk.
Type: [SplunkDestinationUpdate](API_SplunkDestinationUpdate.md) object
Required: No

## Response Elements
<a name="API_UpdateDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
Another modification has already happened. Fetch `VersionId` again and use it to update the destination.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter has a value that is not valid.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already in use and not available for this operation.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDestination_Examples"></a>

### Example
<a name="API_UpdateDestination_Example_1"></a>

The following JSON updates the buffering hints for the destination to 150 seconds and 2 MiB. You can obtain the other values that you need to use in this example from the response to a [DescribeDeliveryStream](API_DescribeDeliveryStream.md) invocation for the Firehose stream in question.

#### Sample Request
<a name="API_UpdateDestination_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.UpdateDestination
{
  "CurrentDeliveryStreamVersionId": "1",
  "DeliveryStreamName": "exampleStreamName",
  "DestinationId": "destinationId-000000000001",
  "ExtendedS3DestinationUpdate": {
    "BucketARN": "arn:aws:s3:::somebucket",
    "BufferingHints": {
      "IntervalInSeconds": 150,
      "SizeInMBs": 2
    },
    "RoleARN": "arn:aws:iam::111222333444:role/exampleStreamName"
  }
}
```

#### Sample Response
<a name="API_UpdateDestination_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_UpdateDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/UpdateDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/UpdateDestination)

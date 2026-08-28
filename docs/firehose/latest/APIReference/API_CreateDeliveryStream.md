---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html
---

# CreateDeliveryStream
<a name="API_CreateDeliveryStream"></a>

Creates a Firehose stream.

By default, you can create up to 5,000 Firehose streams per AWS Region.

This is an asynchronous operation that immediately returns. The initial status of the Firehose stream is `CREATING`. After the Firehose stream is created, its status is `ACTIVE` and it now accepts data. If the Firehose stream creation fails, the status transitions to `CREATING_FAILED`. Attempts to send data to a delivery stream that is not in the `ACTIVE` state cause an exception. To check the state of a Firehose stream, use [DescribeDeliveryStream](API_DescribeDeliveryStream.md).

If the status of a Firehose stream is `CREATING_FAILED`, this status doesn't change, and you can't invoke `CreateDeliveryStream` again on it. However, you can invoke the [DeleteDeliveryStream](API_DeleteDeliveryStream.md) operation to delete it.

A Firehose stream can be configured to receive records directly from providers using [PutRecord](API_PutRecord.md) or [PutRecordBatch](API_PutRecordBatch.md), or it can be configured to use an existing Kinesis stream as its source. To specify a Kinesis data stream as input, set the `DeliveryStreamType` parameter to `KinesisStreamAsSource`, and provide the Kinesis stream Amazon Resource Name (ARN) and role ARN in the `KinesisStreamSourceConfiguration` parameter.

To create a Firehose stream with server-side encryption (SSE) enabled, include [DeliveryStreamEncryptionConfigurationInput](API_DeliveryStreamEncryptionConfigurationInput.md) in your request. This is optional. You can also invoke [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md) to turn on SSE for an existing Firehose stream that doesn't have SSE enabled.

A Firehose stream is configured with a single destination, such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon OpenSearch Service, Amazon OpenSearch Serverless, Splunk, and any custom HTTP endpoint or HTTP endpoints owned by or supported by third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, and Sumo Logic. You must specify only one of the following destination configuration parameters: `ExtendedS3DestinationConfiguration`, `S3DestinationConfiguration`, `ElasticsearchDestinationConfiguration`, `RedshiftDestinationConfiguration`, or `SplunkDestinationConfiguration`.

When you specify `S3DestinationConfiguration`, you can also provide the following optional values: BufferingHints, `EncryptionConfiguration`, and `CompressionFormat`. By default, if no `BufferingHints` value is provided, Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. `BufferingHints` is a hint, so there are some cases where the service cannot adhere to these conditions strictly. For example, record boundaries might be such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3.

A few notes about Amazon Redshift as a destination:
+ An Amazon Redshift destination requires an S3 bucket as intermediate location. Firehose first delivers data to Amazon S3 and then uses `COPY` syntax to load data into an Amazon Redshift table. This is specified in the `RedshiftDestinationConfiguration.S3Configuration` parameter.
+ The compression formats `SNAPPY` or `ZIP` cannot be specified in `RedshiftDestinationConfiguration.S3Configuration` because the Amazon Redshift `COPY` operation that reads from the S3 bucket doesn't support these compression formats.
+ We strongly recommend that you use the user name and password you provide exclusively with Firehose, and that the permissions for the account are restricted for Amazon Redshift `INSERT` permissions.

Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Firehose principal to assume the role, and the role should have permissions that allow the service to deliver the data. For more information, see [Grant Firehose Access to an Amazon S3 Destination](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3) in the *Amazon Firehose Developer Guide*.

For more information about creating a policy for this action, see [Controlling access](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html).

## Request Syntax
<a name="API_CreateDeliveryStream_RequestSyntax"></a>

```
{
   "AmazonOpenSearchServerlessDestinationConfiguration": {
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
      "VpcConfiguration": {
         "RoleARN": "{{string}}",
         "SecurityGroupIds": [ "{{string}}" ],
         "SubnetIds": [ "{{string}}" ]
      }
   },
   "AmazonopensearchserviceDestinationConfiguration": {
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
      "TypeName": "{{string}}",
      "VpcConfiguration": {
         "RoleARN": "{{string}}",
         "SecurityGroupIds": [ "{{string}}" ],
         "SubnetIds": [ "{{string}}" ]
      }
   },
   "DatabaseSourceConfiguration": {
      "Columns": {
         "Exclude": [ "{{string}}" ],
         "Include": [ "{{string}}" ]
      },
      "Databases": {
         "Exclude": [ "{{string}}" ],
         "Include": [ "{{string}}" ]
      },
      "DatabaseSourceAuthenticationConfiguration": {
         "SecretsManagerConfiguration": {
            "Enabled": {{boolean}},
            "RoleARN": "{{string}}",
            "SecretARN": "{{string}}"
         }
      },
      "DatabaseSourceVPCConfiguration": {
         "VpcEndpointServiceName": "{{string}}"
      },
      "Endpoint": "{{string}}",
      "Port": {{number}},
      "SnapshotWatermarkTable": "{{string}}",
      "SSLMode": "{{string}}",
      "SurrogateKeys": [ "{{string}}" ],
      "Tables": {
         "Exclude": [ "{{string}}" ],
         "Include": [ "{{string}}" ]
      },
      "Type": "{{string}}"
   },
   "DeliveryStreamEncryptionConfigurationInput": {
      "KeyARN": "{{string}}",
      "KeyType": "{{string}}"
   },
   "DeliveryStreamName": "{{string}}",
   "DeliveryStreamType": "{{string}}",
   "DirectPutSourceConfiguration": {
      "ThroughputHintInMBs": {{number}}
   },
   "ElasticsearchDestinationConfiguration": {
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
      "TypeName": "{{string}}",
      "VpcConfiguration": {
         "RoleARN": "{{string}}",
         "SecurityGroupIds": [ "{{string}}" ],
         "SubnetIds": [ "{{string}}" ]
      }
   },
   "ExtendedS3DestinationConfiguration": {
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
      "S3BackupConfiguration": {
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
      "S3BackupMode": "{{string}}"
   },
   "HttpEndpointDestinationConfiguration": {
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
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      }
   },
   "IcebergDestinationConfiguration": {
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
   "KinesisStreamSourceConfiguration": {
      "KinesisStreamARN": "{{string}}",
      "RoleARN": "{{string}}"
   },
   "MSKSourceConfiguration": {
      "AuthenticationConfiguration": {
         "Connectivity": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "MSKClusterARN": "{{string}}",
      "ReadFromTimestamp": {{number}},
      "TopicName": "{{string}}"
   },
   "RedshiftDestinationConfiguration": {
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
      "S3BackupConfiguration": {
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
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      },
      "Username": "{{string}}"
   },
   "S3DestinationConfiguration": {
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
   "SnowflakeDestinationConfiguration": {
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
      "SnowflakeVpcConfiguration": {
         "PrivateLinkVpceId": "{{string}}"
      },
      "Table": "{{string}}",
      "User": "{{string}}"
   },
   "SplunkDestinationConfiguration": {
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
      "SecretsManagerConfiguration": {
         "Enabled": {{boolean}},
         "RoleARN": "{{string}}",
         "SecretARN": "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDeliveryStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AmazonOpenSearchServerlessDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-AmazonOpenSearchServerlessDestinationConfiguration"></a>
The destination in the Serverless offering for Amazon OpenSearch Service. You can specify only one destination.
Type: [AmazonOpenSearchServerlessDestinationConfiguration](API_AmazonOpenSearchServerlessDestinationConfiguration.md) object
Required: No

 ** [AmazonopensearchserviceDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-AmazonopensearchserviceDestinationConfiguration"></a>
The destination in Amazon OpenSearch Service. You can specify only one destination.
Type: [AmazonopensearchserviceDestinationConfiguration](API_AmazonopensearchserviceDestinationConfiguration.md) object
Required: No

 ** [DatabaseSourceConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-DatabaseSourceConfiguration"></a>
 The top level object for configuring streams with database as a source.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseSourceConfiguration](API_DatabaseSourceConfiguration.md) object
Required: No

 ** [DeliveryStreamEncryptionConfigurationInput](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-DeliveryStreamEncryptionConfigurationInput"></a>
Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).
Type: [DeliveryStreamEncryptionConfigurationInput](API_DeliveryStreamEncryptionConfigurationInput.md) object
Required: No

 ** [DeliveryStreamName](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-DeliveryStreamName"></a>
The name of the Firehose stream. This name must be unique per AWS account in the same AWS Region. If the Firehose streams are in different accounts or different Regions, you can have multiple Firehose streams with the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [DeliveryStreamType](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-DeliveryStreamType"></a>
The Firehose stream type. This parameter can be one of the following values:
+  `DirectPut`: Provider applications access the Firehose stream directly.
+  `KinesisStreamAsSource`: The Firehose stream uses a Kinesis data stream as a source.
Type: String
Valid Values: `DirectPut | KinesisStreamAsSource | MSKAsSource | DatabaseAsSource`
Required: No

 ** [DirectPutSourceConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-DirectPutSourceConfiguration"></a>
The structure that configures parameters such as `ThroughputHintInMBs` for a stream configured with Direct PUT as a source.
Type: [DirectPutSourceConfiguration](API_DirectPutSourceConfiguration.md) object
Required: No

 ** [ElasticsearchDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-ElasticsearchDestinationConfiguration"></a>
The destination in Amazon OpenSearch Service. You can specify only one destination.
Type: [ElasticsearchDestinationConfiguration](API_ElasticsearchDestinationConfiguration.md) object
Required: No

 ** [ExtendedS3DestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-ExtendedS3DestinationConfiguration"></a>
The destination in Amazon S3. You can specify only one destination.
Type: [ExtendedS3DestinationConfiguration](API_ExtendedS3DestinationConfiguration.md) object
Required: No

 ** [HttpEndpointDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-HttpEndpointDestinationConfiguration"></a>
Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.
Type: [HttpEndpointDestinationConfiguration](API_HttpEndpointDestinationConfiguration.md) object
Required: No

 ** [IcebergDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-IcebergDestinationConfiguration"></a>
 Configure Apache Iceberg Tables destination.
Type: [IcebergDestinationConfiguration](API_IcebergDestinationConfiguration.md) object
Required: No

 ** [KinesisStreamSourceConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-KinesisStreamSourceConfiguration"></a>
When a Kinesis data stream is used as the source for the Firehose stream, a [KinesisStreamSourceConfiguration](API_KinesisStreamSourceConfiguration.md) containing the Kinesis data stream Amazon Resource Name (ARN) and the role ARN for the source stream.
Type: [KinesisStreamSourceConfiguration](API_KinesisStreamSourceConfiguration.md) object
Required: No

 ** [MSKSourceConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-MSKSourceConfiguration"></a>
The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
Type: [MSKSourceConfiguration](API_MSKSourceConfiguration.md) object
Required: No

 ** [RedshiftDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-RedshiftDestinationConfiguration"></a>
The destination in Amazon Redshift. You can specify only one destination.
Type: [RedshiftDestinationConfiguration](API_RedshiftDestinationConfiguration.md) object
Required: No

 ** [S3DestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-S3DestinationConfiguration"></a>
[Deprecated] The destination in Amazon S3. You can specify only one destination.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: No

 ** [SnowflakeDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-SnowflakeDestinationConfiguration"></a>
Configure Snowflake destination
Type: [SnowflakeDestinationConfiguration](API_SnowflakeDestinationConfiguration.md) object
Required: No

 ** [SplunkDestinationConfiguration](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-SplunkDestinationConfiguration"></a>
The destination in Splunk. You can specify only one destination.
Type: [SplunkDestinationConfiguration](API_SplunkDestinationConfiguration.md) object
Required: No

 ** [Tags](#API_CreateDeliveryStream_RequestSyntax) **   <a name="Firehose-CreateDeliveryStream-request-Tags"></a>
A set of tags to assign to the Firehose stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the AWS Billing and Cost Management User Guide.
You can specify up to 50 tags when creating a Firehose stream.
If you specify tags in the `CreateDeliveryStream` action, Amazon Data Firehose performs an additional authorization on the `firehose:TagDeliveryStream` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an `AccessDeniedException` such as following.
 **AccessDeniedException**
User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.
For an example IAM policy, see [Tag example.](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples)
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateDeliveryStream_ResponseSyntax"></a>

```
{
   "DeliveryStreamARN": "string"
}
```

## Response Elements
<a name="API_CreateDeliveryStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeliveryStreamARN](#API_CreateDeliveryStream_ResponseSyntax) **   <a name="Firehose-CreateDeliveryStream-response-DeliveryStreamARN"></a>
The ARN of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:firehose:[a-zA-Z0-9\-]+:\d{12}:deliverystream/[a-zA-Z0-9._-]+`

## Errors
<a name="API_CreateDeliveryStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgumentException **
The specified input parameter has a value that is not valid.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** InvalidKMSResourceException **
Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: `AccessDeniedException`, `InvalidStateException`, `DisabledException`, or `NotFoundException`.
HTTP Status Code: 400

 ** LimitExceededException **
You have already reached the limit for a requested resource.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already in use and not available for this operation.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_CreateDeliveryStream_Examples"></a>

### Example
<a name="API_CreateDeliveryStream_Example_1"></a>

The following JSON example creates a Firehose stream named `exampleStreamName` with an Amazon S3 destination. To use this example, first replace the placeholders for the `RoleARN` and `BucketARN` keys with valid strings. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

#### Sample Request
<a name="API_CreateDeliveryStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.CreateDeliveryStream
{
    "DeliveryStreamName": "exampleStreamName",
    "S3DestinationConfiguration": {
        "RoleARN": "insert-role-ARN",
        "BucketARN": "insert-bucket-ARN",
        "BufferingHints": {
            "SizeInMBs": 3,
            "IntervalInSeconds": 60
        },
        "CompressionFormat": "ZIP"
    }
}
```

#### Sample Response
<a name="API_CreateDeliveryStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "DeliveryStreamARN": "arn:aws:firehose:us-east-1:814985986679:deliverystream/exampleStreamName"
}
```

## See Also
<a name="API_CreateDeliveryStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/CreateDeliveryStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/CreateDeliveryStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

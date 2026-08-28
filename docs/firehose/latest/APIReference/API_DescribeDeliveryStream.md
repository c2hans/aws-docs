---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DescribeDeliveryStream.html
---

# DescribeDeliveryStream
<a name="API_DescribeDeliveryStream"></a>

Describes the specified Firehose stream and its status. For example, after your Firehose stream is created, call `DescribeDeliveryStream` to see whether the Firehose stream is `ACTIVE` and therefore ready for data to be sent to it.

If the status of a Firehose stream is `CREATING_FAILED`, this status doesn't change, and you can't invoke [CreateDeliveryStream](API_CreateDeliveryStream.md) again on it. However, you can invoke the [DeleteDeliveryStream](API_DeleteDeliveryStream.md) operation to delete it. If the status is `DELETING_FAILED`, you can force deletion by invoking [DeleteDeliveryStream](API_DeleteDeliveryStream.md) again but with [DeleteDeliveryStream:AllowForceDelete](API_DeleteDeliveryStream.md#Firehose-DeleteDeliveryStream-request-AllowForceDelete) set to true.

## Request Syntax
<a name="API_DescribeDeliveryStream_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}",
   "ExclusiveStartDestinationId": "{{string}}",
   "Limit": {{number}}
}
```

## Request Parameters
<a name="API_DescribeDeliveryStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_DescribeDeliveryStream_RequestSyntax) **   <a name="Firehose-DescribeDeliveryStream-request-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ExclusiveStartDestinationId](#API_DescribeDeliveryStream_RequestSyntax) **   <a name="Firehose-DescribeDeliveryStream-request-ExclusiveStartDestinationId"></a>
The ID of the destination to start returning the destination information. Firehose supports one destination per Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [Limit](#API_DescribeDeliveryStream_RequestSyntax) **   <a name="Firehose-DescribeDeliveryStream-request-Limit"></a>
The limit on the number of destinations to return. You can have one destination per Firehose stream.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## Response Syntax
<a name="API_DescribeDeliveryStream_ResponseSyntax"></a>

```
{
   "DeliveryStreamDescription": {
      "CreateTimestamp": number,
      "DeliveryStreamARN": "string",
      "DeliveryStreamEncryptionConfiguration": {
         "FailureDescription": {
            "Details": "string",
            "Type": "string"
         },
         "KeyARN": "string",
         "KeyType": "string",
         "Status": "string"
      },
      "DeliveryStreamName": "string",
      "DeliveryStreamStatus": "string",
      "DeliveryStreamType": "string",
      "Destinations": [
         {
            "AmazonOpenSearchServerlessDestinationDescription": {
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "CollectionEndpoint": "string",
               "IndexName": "string",
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "VpcConfigurationDescription": {
                  "RoleARN": "string",
                  "SecurityGroupIds": [ "string" ],
                  "SubnetIds": [ "string" ],
                  "VpcId": "string"
               }
            },
            "AmazonopensearchserviceDestinationDescription": {
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "ClusterEndpoint": "string",
               "DocumentIdOptions": {
                  "DefaultDocumentIdFormat": "string"
               },
               "DomainARN": "string",
               "IndexName": "string",
               "IndexRotationPeriod": "string",
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "TypeName": "string",
               "VpcConfigurationDescription": {
                  "RoleARN": "string",
                  "SecurityGroupIds": [ "string" ],
                  "SubnetIds": [ "string" ],
                  "VpcId": "string"
               }
            },
            "DestinationId": "string",
            "ElasticsearchDestinationDescription": {
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "ClusterEndpoint": "string",
               "DocumentIdOptions": {
                  "DefaultDocumentIdFormat": "string"
               },
               "DomainARN": "string",
               "IndexName": "string",
               "IndexRotationPeriod": "string",
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "TypeName": "string",
               "VpcConfigurationDescription": {
                  "RoleARN": "string",
                  "SecurityGroupIds": [ "string" ],
                  "SubnetIds": [ "string" ],
                  "VpcId": "string"
               }
            },
            "ExtendedS3DestinationDescription": {
               "BucketARN": "string",
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "CompressionFormat": "string",
               "CustomTimeZone": "string",
               "DataFormatConversionConfiguration": {
                  "Enabled": boolean,
                  "InputFormatConfiguration": {
                     "Deserializer": {
                        "HiveJsonSerDe": {
                           "TimestampFormats": [ "string" ]
                        },
                        "OpenXJsonSerDe": {
                           "CaseInsensitive": boolean,
                           "ColumnToJsonKeyMappings": {
                              "string" : "string"
                           },
                           "ConvertDotsInJsonKeysToUnderscores": boolean
                        }
                     }
                  },
                  "OutputFormatConfiguration": {
                     "Serializer": {
                        "OrcSerDe": {
                           "BlockSizeBytes": number,
                           "BloomFilterColumns": [ "string" ],
                           "BloomFilterFalsePositiveProbability": number,
                           "Compression": "string",
                           "DictionaryKeyThreshold": number,
                           "EnablePadding": boolean,
                           "FormatVersion": "string",
                           "PaddingTolerance": number,
                           "RowIndexStride": number,
                           "StripeSizeBytes": number
                        },
                        "ParquetSerDe": {
                           "BlockSizeBytes": number,
                           "Compression": "string",
                           "EnableDictionaryCompression": boolean,
                           "MaxPaddingBytes": number,
                           "PageSizeBytes": number,
                           "WriterVersion": "string"
                        }
                     }
                  },
                  "SchemaConfiguration": {
                     "CatalogId": "string",
                     "DatabaseName": "string",
                     "Region": "string",
                     "RoleARN": "string",
                     "TableName": "string",
                     "VersionId": "string"
                  }
               },
               "DynamicPartitioningConfiguration": {
                  "Enabled": boolean,
                  "RetryOptions": {
                     "DurationInSeconds": number
                  }
               },
               "EncryptionConfiguration": {
                  "KMSEncryptionConfig": {
                     "AWSKMSKeyARN": "string"
                  },
                  "NoEncryptionConfig": "string"
               },
               "ErrorOutputPrefix": "string",
               "FileExtension": "string",
               "Prefix": "string",
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RoleARN": "string",
               "S3BackupDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "S3BackupMode": "string"
            },
            "HttpEndpointDestinationDescription": {
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "EndpointConfiguration": {
                  "Name": "string",
                  "Url": "string"
               },
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RequestConfiguration": {
                  "CommonAttributes": [
                     {
                        "AttributeName": "string",
                        "AttributeValue": "string"
                     }
                  ],
                  "ContentEncoding": "string"
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "SecretsManagerConfiguration": {
                  "Enabled": boolean,
                  "RoleARN": "string",
                  "SecretARN": "string"
               }
            },
            "IcebergDestinationDescription": {
               "AppendOnly": boolean,
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CatalogConfiguration": {
                  "CatalogARN": "string",
                  "WarehouseLocation": "string"
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "DestinationTableConfigurationList": [
                  {
                     "DestinationDatabaseName": "string",
                     "DestinationTableName": "string",
                     "PartitionSpec": {
                        "Identity": [
                           {
                              "SourceName": "string"
                           }
                        ]
                     },
                     "S3ErrorOutputPrefix": "string",
                     "UniqueKeys": [ "string" ]
                  }
               ],
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "SchemaEvolutionConfiguration": {
                  "Enabled": boolean
               },
               "TableCreationConfiguration": {
                  "Enabled": boolean
               }
            },
            "RedshiftDestinationDescription": {
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "ClusterJDBCURL": "string",
               "CopyCommand": {
                  "CopyOptions": "string",
                  "DataTableColumns": "string",
                  "DataTableName": "string"
               },
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "SecretsManagerConfiguration": {
                  "Enabled": boolean,
                  "RoleARN": "string",
                  "SecretARN": "string"
               },
               "Username": "string"
            },
            "S3DestinationDescription": {
               "BucketARN": "string",
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "CompressionFormat": "string",
               "EncryptionConfiguration": {
                  "KMSEncryptionConfig": {
                     "AWSKMSKeyARN": "string"
                  },
                  "NoEncryptionConfig": "string"
               },
               "ErrorOutputPrefix": "string",
               "Prefix": "string",
               "RoleARN": "string"
            },
            "SnowflakeDestinationDescription": {
               "AccountUrl": "string",
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "ContentColumnName": "string",
               "Database": "string",
               "DataLoadingOption": "string",
               "MetaDataColumnName": "string",
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "RoleARN": "string",
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "Schema": "string",
               "SecretsManagerConfiguration": {
                  "Enabled": boolean,
                  "RoleARN": "string",
                  "SecretARN": "string"
               },
               "SnowflakeRoleConfiguration": {
                  "Enabled": boolean,
                  "SnowflakeRole": "string"
               },
               "SnowflakeVpcConfiguration": {
                  "PrivateLinkVpceId": "string"
               },
               "Table": "string",
               "User": "string"
            },
            "SplunkDestinationDescription": {
               "BufferingHints": {
                  "IntervalInSeconds": number,
                  "SizeInMBs": number
               },
               "CloudWatchLoggingOptions": {
                  "Enabled": boolean,
                  "LogGroupName": "string",
                  "LogStreamName": "string"
               },
               "HECAcknowledgmentTimeoutInSeconds": number,
               "HECEndpoint": "string",
               "HECEndpointType": "string",
               "HECToken": "string",
               "ProcessingConfiguration": {
                  "Enabled": boolean,
                  "Processors": [
                     {
                        "Parameters": [
                           {
                              "ParameterName": "string",
                              "ParameterValue": "string"
                           }
                        ],
                        "Type": "string"
                     }
                  ]
               },
               "RetryOptions": {
                  "DurationInSeconds": number
               },
               "S3BackupMode": "string",
               "S3DestinationDescription": {
                  "BucketARN": "string",
                  "BufferingHints": {
                     "IntervalInSeconds": number,
                     "SizeInMBs": number
                  },
                  "CloudWatchLoggingOptions": {
                     "Enabled": boolean,
                     "LogGroupName": "string",
                     "LogStreamName": "string"
                  },
                  "CompressionFormat": "string",
                  "EncryptionConfiguration": {
                     "KMSEncryptionConfig": {
                        "AWSKMSKeyARN": "string"
                     },
                     "NoEncryptionConfig": "string"
                  },
                  "ErrorOutputPrefix": "string",
                  "Prefix": "string",
                  "RoleARN": "string"
               },
               "SecretsManagerConfiguration": {
                  "Enabled": boolean,
                  "RoleARN": "string",
                  "SecretARN": "string"
               }
            }
         }
      ],
      "FailureDescription": {
         "Details": "string",
         "Type": "string"
      },
      "HasMoreDestinations": boolean,
      "LastUpdateTimestamp": number,
      "Source": {
         "DatabaseSourceDescription": {
            "Columns": {
               "Exclude": [ "string" ],
               "Include": [ "string" ]
            },
            "Databases": {
               "Exclude": [ "string" ],
               "Include": [ "string" ]
            },
            "DatabaseSourceAuthenticationConfiguration": {
               "SecretsManagerConfiguration": {
                  "Enabled": boolean,
                  "RoleARN": "string",
                  "SecretARN": "string"
               }
            },
            "DatabaseSourceVPCConfiguration": {
               "VpcEndpointServiceName": "string"
            },
            "Endpoint": "string",
            "Port": number,
            "SnapshotInfo": [
               {
                  "FailureDescription": {
                     "Details": "string",
                     "Type": "string"
                  },
                  "Id": "string",
                  "RequestedBy": "string",
                  "RequestTimestamp": number,
                  "Status": "string",
                  "Table": "string"
               }
            ],
            "SnapshotWatermarkTable": "string",
            "SSLMode": "string",
            "SurrogateKeys": [ "string" ],
            "Tables": {
               "Exclude": [ "string" ],
               "Include": [ "string" ]
            },
            "Type": "string"
         },
         "DirectPutSourceDescription": {
            "ThroughputHintInMBs": number
         },
         "KinesisStreamSourceDescription": {
            "DeliveryStartTimestamp": number,
            "KinesisStreamARN": "string",
            "RoleARN": "string"
         },
         "MSKSourceDescription": {
            "AuthenticationConfiguration": {
               "Connectivity": "string",
               "RoleARN": "string"
            },
            "DeliveryStartTimestamp": number,
            "MSKClusterARN": "string",
            "ReadFromTimestamp": number,
            "TopicName": "string"
         }
      },
      "VersionId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeDeliveryStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeliveryStreamDescription](#API_DescribeDeliveryStream_ResponseSyntax) **   <a name="Firehose-DescribeDeliveryStream-response-DeliveryStreamDescription"></a>
Information about the Firehose stream.
Type: [DeliveryStreamDescription](API_DeliveryStreamDescription.md) object

## Errors
<a name="API_DescribeDeliveryStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDeliveryStream_Examples"></a>

### Example
<a name="API_DescribeDeliveryStream_Example_1"></a>

The following JSON example describes a Firehose stream.

#### Sample Request
<a name="API_DescribeDeliveryStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.DescribeDeliveryStream
{
    "DeliveryStreamName": "exampleStreamName"
}
```

#### Sample Response
<a name="API_DescribeDeliveryStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "DeliveryStreamDescription": {
    "DeliveryStreamType": "DirectPut",
    "HasMoreDestinations": false,
    "VersionId": "1",
    "CreateTimestamp": 1517595920.596,
    "DeliveryStreamARN": "arn:aws:firehose:us-east-1:111222333444:deliverystream/exampleStreamName",
    "DeliveryStreamStatus": "ACTIVE",
    "DeliveryStreamName": "exampleStreamName",
    "DeliveryStreamEncryptionConfiguration": {
      "Status": "DISABLED"
    },
    "Destinations": [
      {
        "DestinationId": "destinationId-000000000001",
        "ExtendedS3DestinationDescription": {
          "RoleARN": "arn:aws:iam::111222333444:role/exampleStreamName",
          "Prefix": "",
          "BufferingHints": {
            "IntervalInSeconds": 60,
            "SizeInMBs": 1
          },
          "EncryptionConfiguration": {
            "NoEncryptionConfig": "NoEncryption"
          },
          "CompressionFormat": "UNCOMPRESSED",
          "S3BackupMode": "Disabled",
          "CloudWatchLoggingOptions": {
            "Enabled": true,
            "LogStreamName": "S3Delivery",
            "LogGroupName": "/aws/kinesisfirehose/exampleStreamName"
          },
          "BucketARN": "arn:aws:s3:::somebucket",
          "ProcessingConfiguration": {
            "Enabled": false,
            "Processors": []
          }
        },
        "S3DestinationDescription": {
          "RoleARN": "arn:aws:iam::111222333444:role/exampleStreamName",
          "Prefix": "",
          "BufferingHints": {
            "IntervalInSeconds": 60,
            "SizeInMBs": 1
          },
          "EncryptionConfiguration": {
            "NoEncryptionConfig": "NoEncryption"
          },
          "CompressionFormat": "UNCOMPRESSED",
          "CloudWatchLoggingOptions": {
            "Enabled": true,
            "LogStreamName": "S3Delivery",
            "LogGroupName": "/aws/kinesisfirehose/exampleStreamName"
          },
          "BucketARN": "arn:aws:s3:::somebucket"
        }
      }
    ]
  }
}
```

## See Also
<a name="API_DescribeDeliveryStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/DescribeDeliveryStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DescribeDeliveryStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

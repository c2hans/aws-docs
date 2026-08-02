---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates a Managed Service for Apache Flink application. For information about creating a Managed Service for Apache Flink application, see [Creating an Application](https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html).

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
{
   "ApplicationConfiguration": {
      "ApplicationCodeConfiguration": {
         "CodeContent": {
            "S3ContentLocation": {
               "BucketARN": "{{string}}",
               "FileKey": "{{string}}",
               "ObjectVersion": "{{string}}"
            },
            "TextContent": "{{string}}",
            "ZipFileContent": {{blob}}
         },
         "CodeContentType": "{{string}}"
      },
      "ApplicationEncryptionConfiguration": {
         "KeyId": "{{string}}",
         "KeyType": "{{string}}"
      },
      "ApplicationSnapshotConfiguration": {
         "SnapshotsEnabled": {{boolean}}
      },
      "ApplicationSystemRollbackConfiguration": {
         "RollbackEnabled": {{boolean}}
      },
      "EnvironmentProperties": {
         "PropertyGroups": [
            {
               "PropertyGroupId": "{{string}}",
               "PropertyMap": {
                  "{{string}}" : "{{string}}"
               }
            }
         ]
      },
      "FlinkApplicationConfiguration": {
         "CheckpointConfiguration": {
            "CheckpointingEnabled": {{boolean}},
            "CheckpointInterval": {{number}},
            "ConfigurationType": "{{string}}",
            "MinPauseBetweenCheckpoints": {{number}}
         },
         "MonitoringConfiguration": {
            "ConfigurationType": "{{string}}",
            "LogLevel": "{{string}}",
            "MetricsLevel": "{{string}}"
         },
         "ParallelismConfiguration": {
            "AutoScalingEnabled": {{boolean}},
            "ConfigurationType": "{{string}}",
            "Parallelism": {{number}},
            "ParallelismPerKPU": {{number}}
         }
      },
      "SqlApplicationConfiguration": {
         "Inputs": [
            {
               "InputParallelism": {
                  "Count": {{number}}
               },
               "InputProcessingConfiguration": {
                  "InputLambdaProcessor": {
                     "ResourceARN": "{{string}}"
                  }
               },
               "InputSchema": {
                  "RecordColumns": [
                     {
                        "Mapping": "{{string}}",
                        "Name": "{{string}}",
                        "SqlType": "{{string}}"
                     }
                  ],
                  "RecordEncoding": "{{string}}",
                  "RecordFormat": {
                     "MappingParameters": {
                        "CSVMappingParameters": {
                           "RecordColumnDelimiter": "{{string}}",
                           "RecordRowDelimiter": "{{string}}"
                        },
                        "JSONMappingParameters": {
                           "RecordRowPath": "{{string}}"
                        }
                     },
                     "RecordFormatType": "{{string}}"
                  }
               },
               "KinesisFirehoseInput": {
                  "ResourceARN": "{{string}}"
               },
               "KinesisStreamsInput": {
                  "ResourceARN": "{{string}}"
               },
               "NamePrefix": "{{string}}"
            }
         ],
         "Outputs": [
            {
               "DestinationSchema": {
                  "RecordFormatType": "{{string}}"
               },
               "KinesisFirehoseOutput": {
                  "ResourceARN": "{{string}}"
               },
               "KinesisStreamsOutput": {
                  "ResourceARN": "{{string}}"
               },
               "LambdaOutput": {
                  "ResourceARN": "{{string}}"
               },
               "Name": "{{string}}"
            }
         ],
         "ReferenceDataSources": [
            {
               "ReferenceSchema": {
                  "RecordColumns": [
                     {
                        "Mapping": "{{string}}",
                        "Name": "{{string}}",
                        "SqlType": "{{string}}"
                     }
                  ],
                  "RecordEncoding": "{{string}}",
                  "RecordFormat": {
                     "MappingParameters": {
                        "CSVMappingParameters": {
                           "RecordColumnDelimiter": "{{string}}",
                           "RecordRowDelimiter": "{{string}}"
                        },
                        "JSONMappingParameters": {
                           "RecordRowPath": "{{string}}"
                        }
                     },
                     "RecordFormatType": "{{string}}"
                  }
               },
               "S3ReferenceDataSource": {
                  "BucketARN": "{{string}}",
                  "FileKey": "{{string}}"
               },
               "TableName": "{{string}}"
            }
         ]
      },
      "VpcConfigurations": [
         {
            "SecurityGroupIds": [ "{{string}}" ],
            "SubnetIds": [ "{{string}}" ]
         }
      ],
      "ZeppelinApplicationConfiguration": {
         "CatalogConfiguration": {
            "GlueDataCatalogConfiguration": {
               "DatabaseARN": "{{string}}"
            }
         },
         "CustomArtifactsConfiguration": [
            {
               "ArtifactType": "{{string}}",
               "MavenReference": {
                  "ArtifactId": "{{string}}",
                  "GroupId": "{{string}}",
                  "Version": "{{string}}"
               },
               "S3ContentLocation": {
                  "BucketARN": "{{string}}",
                  "FileKey": "{{string}}",
                  "ObjectVersion": "{{string}}"
               }
            }
         ],
         "DeployAsApplicationConfiguration": {
            "S3ContentLocation": {
               "BasePath": "{{string}}",
               "BucketARN": "{{string}}"
            }
         },
         "MonitoringConfiguration": {
            "LogLevel": "{{string}}"
         }
      }
   },
   "ApplicationDescription": "{{string}}",
   "ApplicationMode": "{{string}}",
   "ApplicationName": "{{string}}",
   "CloudWatchLoggingOptions": [
      {
         "LogStreamARN": "{{string}}"
      }
   ],
   "RuntimeEnvironment": "{{string}}",
   "ServiceExecutionRole": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-ApplicationConfiguration"></a>
Use this parameter to configure the application.
Type: [ApplicationConfiguration](API_ApplicationConfiguration.md) object
Required: No

 ** [ApplicationDescription](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-ApplicationDescription"></a>
A summary description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ApplicationMode](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-ApplicationMode"></a>
Use the `STREAMING` mode to create a Managed Service for Apache Flink application. To create a Managed Service for Apache Flink Studio notebook, use the `INTERACTIVE` mode.
Type: String
Valid Values: `STREAMING | INTERACTIVE`
Required: No

 ** [ApplicationName](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-ApplicationName"></a>
The name of your application (for example, `sample-app`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CloudWatchLoggingOptions](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-CloudWatchLoggingOptions"></a>
Use this parameter to configure an Amazon CloudWatch log stream to monitor application configuration errors.
Type: Array of [CloudWatchLoggingOption](API_CloudWatchLoggingOption.md) objects
Required: No

 ** [RuntimeEnvironment](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-RuntimeEnvironment"></a>
The runtime environment for the application.
Type: String
Valid Values: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20`
Required: Yes

 ** [ServiceExecutionRole](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-ServiceExecutionRole"></a>
The IAM role used by the application to access Kinesis data streams, Kinesis Data Firehose delivery streams, Amazon S3 objects, and other external resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [Tags](#API_CreateApplication_RequestSyntax) **   <a name="APIReference-CreateApplication-request-Tags"></a>
A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see [Using Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
{
   "ApplicationDetail": {
      "ApplicationARN": "string",
      "ApplicationConfigurationDescription": {
         "ApplicationCodeConfigurationDescription": {
            "CodeContentDescription": {
               "CodeMD5": "string",
               "CodeSize": number,
               "S3ApplicationCodeLocationDescription": {
                  "BucketARN": "string",
                  "FileKey": "string",
                  "ObjectVersion": "string"
               },
               "TextContent": "string"
            },
            "CodeContentType": "string"
         },
         "ApplicationEncryptionConfigurationDescription": {
            "KeyId": "string",
            "KeyType": "string"
         },
         "ApplicationSnapshotConfigurationDescription": {
            "SnapshotsEnabled": boolean
         },
         "ApplicationSystemRollbackConfigurationDescription": {
            "RollbackEnabled": boolean
         },
         "EnvironmentPropertyDescriptions": {
            "PropertyGroupDescriptions": [
               {
                  "PropertyGroupId": "string",
                  "PropertyMap": {
                     "string" : "string"
                  }
               }
            ]
         },
         "FlinkApplicationConfigurationDescription": {
            "CheckpointConfigurationDescription": {
               "CheckpointingEnabled": boolean,
               "CheckpointInterval": number,
               "ConfigurationType": "string",
               "MinPauseBetweenCheckpoints": number
            },
            "JobPlanDescription": "string",
            "MonitoringConfigurationDescription": {
               "ConfigurationType": "string",
               "LogLevel": "string",
               "MetricsLevel": "string"
            },
            "ParallelismConfigurationDescription": {
               "AutoScalingEnabled": boolean,
               "ConfigurationType": "string",
               "CurrentParallelism": number,
               "Parallelism": number,
               "ParallelismPerKPU": number
            }
         },
         "RunConfigurationDescription": {
            "ApplicationRestoreConfigurationDescription": {
               "ApplicationRestoreType": "string",
               "SnapshotName": "string"
            },
            "FlinkRunConfigurationDescription": {
               "AllowNonRestoredState": boolean
            }
         },
         "SqlApplicationConfigurationDescription": {
            "InputDescriptions": [
               {
                  "InAppStreamNames": [ "string" ],
                  "InputId": "string",
                  "InputParallelism": {
                     "Count": number
                  },
                  "InputProcessingConfigurationDescription": {
                     "InputLambdaProcessorDescription": {
                        "ResourceARN": "string",
                        "RoleARN": "string"
                     }
                  },
                  "InputSchema": {
                     "RecordColumns": [
                        {
                           "Mapping": "string",
                           "Name": "string",
                           "SqlType": "string"
                        }
                     ],
                     "RecordEncoding": "string",
                     "RecordFormat": {
                        "MappingParameters": {
                           "CSVMappingParameters": {
                              "RecordColumnDelimiter": "string",
                              "RecordRowDelimiter": "string"
                           },
                           "JSONMappingParameters": {
                              "RecordRowPath": "string"
                           }
                        },
                        "RecordFormatType": "string"
                     }
                  },
                  "InputStartingPositionConfiguration": {
                     "InputStartingPosition": "string"
                  },
                  "KinesisFirehoseInputDescription": {
                     "ResourceARN": "string",
                     "RoleARN": "string"
                  },
                  "KinesisStreamsInputDescription": {
                     "ResourceARN": "string",
                     "RoleARN": "string"
                  },
                  "NamePrefix": "string"
               }
            ],
            "OutputDescriptions": [
               {
                  "DestinationSchema": {
                     "RecordFormatType": "string"
                  },
                  "KinesisFirehoseOutputDescription": {
                     "ResourceARN": "string",
                     "RoleARN": "string"
                  },
                  "KinesisStreamsOutputDescription": {
                     "ResourceARN": "string",
                     "RoleARN": "string"
                  },
                  "LambdaOutputDescription": {
                     "ResourceARN": "string",
                     "RoleARN": "string"
                  },
                  "Name": "string",
                  "OutputId": "string"
               }
            ],
            "ReferenceDataSourceDescriptions": [
               {
                  "ReferenceId": "string",
                  "ReferenceSchema": {
                     "RecordColumns": [
                        {
                           "Mapping": "string",
                           "Name": "string",
                           "SqlType": "string"
                        }
                     ],
                     "RecordEncoding": "string",
                     "RecordFormat": {
                        "MappingParameters": {
                           "CSVMappingParameters": {
                              "RecordColumnDelimiter": "string",
                              "RecordRowDelimiter": "string"
                           },
                           "JSONMappingParameters": {
                              "RecordRowPath": "string"
                           }
                        },
                        "RecordFormatType": "string"
                     }
                  },
                  "S3ReferenceDataSourceDescription": {
                     "BucketARN": "string",
                     "FileKey": "string",
                     "ReferenceRoleARN": "string"
                  },
                  "TableName": "string"
               }
            ]
         },
         "VpcConfigurationDescriptions": [
            {
               "SecurityGroupIds": [ "string" ],
               "SubnetIds": [ "string" ],
               "VpcConfigurationId": "string",
               "VpcId": "string"
            }
         ],
         "ZeppelinApplicationConfigurationDescription": {
            "CatalogConfigurationDescription": {
               "GlueDataCatalogConfigurationDescription": {
                  "DatabaseARN": "string"
               }
            },
            "CustomArtifactsConfigurationDescription": [
               {
                  "ArtifactType": "string",
                  "MavenReferenceDescription": {
                     "ArtifactId": "string",
                     "GroupId": "string",
                     "Version": "string"
                  },
                  "S3ContentLocationDescription": {
                     "BucketARN": "string",
                     "FileKey": "string",
                     "ObjectVersion": "string"
                  }
               }
            ],
            "DeployAsApplicationConfigurationDescription": {
               "S3ContentLocationDescription": {
                  "BasePath": "string",
                  "BucketARN": "string"
               }
            },
            "MonitoringConfigurationDescription": {
               "LogLevel": "string"
            }
         }
      },
      "ApplicationDescription": "string",
      "ApplicationMaintenanceConfigurationDescription": {
         "ApplicationMaintenanceWindowEndTime": "string",
         "ApplicationMaintenanceWindowStartTime": "string"
      },
      "ApplicationMode": "string",
      "ApplicationName": "string",
      "ApplicationStatus": "string",
      "ApplicationVersionCreateTimestamp": number,
      "ApplicationVersionId": number,
      "ApplicationVersionRolledBackFrom": number,
      "ApplicationVersionRolledBackTo": number,
      "ApplicationVersionUpdatedFrom": number,
      "CloudWatchLoggingOptionDescriptions": [
         {
            "CloudWatchLoggingOptionId": "string",
            "LogStreamARN": "string",
            "RoleARN": "string"
         }
      ],
      "ConditionalToken": "string",
      "CreateTimestamp": number,
      "LastUpdateTimestamp": number,
      "RuntimeEnvironment": "string",
      "ServiceExecutionRole": "string"
   }
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationDetail](#API_CreateApplication_ResponseSyntax) **   <a name="APIReference-CreateApplication-response-ApplicationDetail"></a>
In response to your `CreateApplication` request, Managed Service for Apache Flink returns a response with details of the application it created.
Type: [ApplicationDetail](API_ApplicationDetail.md) object

## Errors
<a name="API_CreateApplication_Errors"></a>

 ** CodeValidationException **
The user-provided application code (query) is not valid. This can be a simple syntax error.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

 ** LimitExceededException **
The number of allowed resources has been exceeded.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** TooManyTagsException **
Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CreateApplication)

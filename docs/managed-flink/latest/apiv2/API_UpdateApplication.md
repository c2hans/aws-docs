---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates an existing Managed Service for Apache Flink application. Using this operation, you can update application code, input configuration, and output configuration.

Managed Service for Apache Flink updates the `ApplicationVersionId` each time you update your application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
{
   "ApplicationConfigurationUpdate": {
      "ApplicationCodeConfigurationUpdate": {
         "CodeContentTypeUpdate": "{{string}}",
         "CodeContentUpdate": {
            "S3ContentLocationUpdate": {
               "BucketARNUpdate": "{{string}}",
               "FileKeyUpdate": "{{string}}",
               "ObjectVersionUpdate": "{{string}}"
            },
            "TextContentUpdate": "{{string}}",
            "ZipFileContentUpdate": {{blob}}
         }
      },
      "ApplicationEncryptionConfigurationUpdate": {
         "KeyIdUpdate": "{{string}}",
         "KeyTypeUpdate": "{{string}}"
      },
      "ApplicationSnapshotConfigurationUpdate": {
         "SnapshotsEnabledUpdate": {{boolean}}
      },
      "ApplicationSystemRollbackConfigurationUpdate": {
         "RollbackEnabledUpdate": {{boolean}}
      },
      "EnvironmentPropertyUpdates": {
         "PropertyGroups": [
            {
               "PropertyGroupId": "{{string}}",
               "PropertyMap": {
                  "{{string}}" : "{{string}}"
               }
            }
         ]
      },
      "FlinkApplicationConfigurationUpdate": {
         "CheckpointConfigurationUpdate": {
            "CheckpointingEnabledUpdate": {{boolean}},
            "CheckpointIntervalUpdate": {{number}},
            "ConfigurationTypeUpdate": "{{string}}",
            "MinPauseBetweenCheckpointsUpdate": {{number}}
         },
         "MonitoringConfigurationUpdate": {
            "ConfigurationTypeUpdate": "{{string}}",
            "LogLevelUpdate": "{{string}}",
            "MetricsLevelUpdate": "{{string}}"
         },
         "ParallelismConfigurationUpdate": {
            "AutoScalingEnabledUpdate": {{boolean}},
            "ConfigurationTypeUpdate": "{{string}}",
            "ParallelismPerKPUUpdate": {{number}},
            "ParallelismUpdate": {{number}}
         }
      },
      "SqlApplicationConfigurationUpdate": {
         "InputUpdates": [
            {
               "InputId": "{{string}}",
               "InputParallelismUpdate": {
                  "CountUpdate": {{number}}
               },
               "InputProcessingConfigurationUpdate": {
                  "InputLambdaProcessorUpdate": {
                     "ResourceARNUpdate": "{{string}}"
                  }
               },
               "InputSchemaUpdate": {
                  "RecordColumnUpdates": [
                     {
                        "Mapping": "{{string}}",
                        "Name": "{{string}}",
                        "SqlType": "{{string}}"
                     }
                  ],
                  "RecordEncodingUpdate": "{{string}}",
                  "RecordFormatUpdate": {
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
               "KinesisFirehoseInputUpdate": {
                  "ResourceARNUpdate": "{{string}}"
               },
               "KinesisStreamsInputUpdate": {
                  "ResourceARNUpdate": "{{string}}"
               },
               "NamePrefixUpdate": "{{string}}"
            }
         ],
         "OutputUpdates": [
            {
               "DestinationSchemaUpdate": {
                  "RecordFormatType": "{{string}}"
               },
               "KinesisFirehoseOutputUpdate": {
                  "ResourceARNUpdate": "{{string}}"
               },
               "KinesisStreamsOutputUpdate": {
                  "ResourceARNUpdate": "{{string}}"
               },
               "LambdaOutputUpdate": {
                  "ResourceARNUpdate": "{{string}}"
               },
               "NameUpdate": "{{string}}",
               "OutputId": "{{string}}"
            }
         ],
         "ReferenceDataSourceUpdates": [
            {
               "ReferenceId": "{{string}}",
               "ReferenceSchemaUpdate": {
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
               "S3ReferenceDataSourceUpdate": {
                  "BucketARNUpdate": "{{string}}",
                  "FileKeyUpdate": "{{string}}"
               },
               "TableNameUpdate": "{{string}}"
            }
         ]
      },
      "VpcConfigurationUpdates": [
         {
            "SecurityGroupIdUpdates": [ "{{string}}" ],
            "SubnetIdUpdates": [ "{{string}}" ],
            "VpcConfigurationId": "{{string}}"
         }
      ],
      "ZeppelinApplicationConfigurationUpdate": {
         "CatalogConfigurationUpdate": {
            "GlueDataCatalogConfigurationUpdate": {
               "DatabaseARNUpdate": "{{string}}"
            }
         },
         "CustomArtifactsConfigurationUpdate": [
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
         "DeployAsApplicationConfigurationUpdate": {
            "S3ContentLocationUpdate": {
               "BasePathUpdate": "{{string}}",
               "BucketARNUpdate": "{{string}}"
            }
         },
         "MonitoringConfigurationUpdate": {
            "LogLevelUpdate": "{{string}}"
         }
      }
   },
   "ApplicationName": "{{string}}",
   "CloudWatchLoggingOptionUpdates": [
      {
         "CloudWatchLoggingOptionId": "{{string}}",
         "LogStreamARNUpdate": "{{string}}"
      }
   ],
   "ConditionalToken": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "RunConfigurationUpdate": {
      "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "{{string}}",
         "SnapshotName": "{{string}}"
      },
      "FlinkRunConfiguration": {
         "AllowNonRestoredState": {{boolean}}
      }
   },
   "RuntimeEnvironmentUpdate": "{{string}}",
   "ServiceExecutionRoleUpdate": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationConfigurationUpdate](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-ApplicationConfigurationUpdate"></a>
Describes application configuration updates.
Type: [ApplicationConfigurationUpdate](API_ApplicationConfigurationUpdate.md) object
Required: No

 ** [ApplicationName](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-ApplicationName"></a>
The name of the application to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CloudWatchLoggingOptionUpdates](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-CloudWatchLoggingOptionUpdates"></a>
Describes application Amazon CloudWatch logging option updates. You can only update existing CloudWatch logging options with this action. To add a new CloudWatch logging option, use [AddApplicationCloudWatchLoggingOption](API_AddApplicationCloudWatchLoggingOption.md).
Type: Array of [CloudWatchLoggingOptionUpdate](API_CloudWatchLoggingOptionUpdate.md) objects
Required: No

 ** [ConditionalToken](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-ConditionalToken"></a>
A value you use to implement strong concurrency for application updates. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You get the application's current `ConditionalToken` using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_+/=]+`
Required: No

 ** [CurrentApplicationVersionId](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-CurrentApplicationVersionId"></a>
The current application version ID. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`.You can retrieve the application version ID using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** [RunConfigurationUpdate](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-RunConfigurationUpdate"></a>
Describes updates to the application's starting parameters.
Type: [RunConfigurationUpdate](API_RunConfigurationUpdate.md) object
Required: No

 ** [RuntimeEnvironmentUpdate](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-RuntimeEnvironmentUpdate"></a>
Updates the Managed Service for Apache Flink runtime environment used to run your code. To avoid issues you must:
+ Ensure your new jar and dependencies are compatible with the new runtime selected.
+ Ensure your new code's state is compatible with the snapshot from which your application will start
Type: String
Valid Values: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20`
Required: No

 ** [ServiceExecutionRoleUpdate](#API_UpdateApplication_RequestSyntax) **   <a name="APIReference-UpdateApplication-request-ServiceExecutionRoleUpdate"></a>
Describes updates to the service execution role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

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
   },
   "OperationId": "string"
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationDetail](#API_UpdateApplication_ResponseSyntax) **   <a name="APIReference-UpdateApplication-response-ApplicationDetail"></a>
Describes application updates.
Type: [ApplicationDetail](API_ApplicationDetail.md) object

 ** [OperationId](#API_UpdateApplication_ResponseSyntax) **   <a name="APIReference-UpdateApplication-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_UpdateApplication_Errors"></a>

 ** CodeValidationException **
The user-provided application code (query) is not valid. This can be a simple syntax error.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidApplicationConfigurationException **
The user-provided application configuration is not valid.
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

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

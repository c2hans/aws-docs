---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RollbackApplication.html
---

# RollbackApplication
<a name="API_RollbackApplication"></a>

Reverts the application to the previous running version. You can roll back an application if you suspect it is stuck in a transient status or in the running status.

You can roll back an application only if it is in the `UPDATING`, `AUTOSCALING`, or `RUNNING` statuses.

When you rollback an application, it loads state data from the last successful snapshot. If the application has no snapshots, Managed Service for Apache Flink rejects the rollback request.

## Request Syntax
<a name="API_RollbackApplication_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}}
}
```

## Request Parameters
<a name="API_RollbackApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_RollbackApplication_RequestSyntax) **   <a name="APIReference-RollbackApplication-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_RollbackApplication_RequestSyntax) **   <a name="APIReference-RollbackApplication-request-CurrentApplicationVersionId"></a>
The current application version ID. You can retrieve the application version ID using [DescribeApplication](API_DescribeApplication.md).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

## Response Syntax
<a name="API_RollbackApplication_ResponseSyntax"></a>

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
<a name="API_RollbackApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationDetail](#API_RollbackApplication_ResponseSyntax) **   <a name="APIReference-RollbackApplication-response-ApplicationDetail"></a>
Describes the application, including the application Amazon Resource Name (ARN), status, latest version, and input and output configurations.
Type: [ApplicationDetail](API_ApplicationDetail.md) object

 ** [OperationId](#API_RollbackApplication_ResponseSyntax) **   <a name="APIReference-RollbackApplication-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_RollbackApplication_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_RollbackApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/RollbackApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/RollbackApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

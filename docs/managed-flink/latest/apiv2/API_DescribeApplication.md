---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplication.html
---

# DescribeApplication
<a name="API_DescribeApplication"></a>

Returns information about a specific Managed Service for Apache Flink application.

If you want to retrieve a list of all applications in your account, use the [ListApplications](API_ListApplications.md) operation.

## Request Syntax
<a name="API_DescribeApplication_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "IncludeAdditionalDetails": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DescribeApplication_RequestSyntax) **   <a name="APIReference-DescribeApplication-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [IncludeAdditionalDetails](#API_DescribeApplication_RequestSyntax) **   <a name="APIReference-DescribeApplication-request-IncludeAdditionalDetails"></a>
Displays verbose information about a Managed Service for Apache Flink application, including the application's job plan.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeApplication_ResponseSyntax"></a>

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
<a name="API_DescribeApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationDetail](#API_DescribeApplication_ResponseSyntax) **   <a name="APIReference-DescribeApplication-response-ApplicationDetail"></a>
Provides a description of the application, such as the application's Amazon Resource Name (ARN), status, and latest version.
Type: [ApplicationDetail](API_ApplicationDetail.md) object

## Errors
<a name="API_DescribeApplication_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DescribeApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DescribeApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

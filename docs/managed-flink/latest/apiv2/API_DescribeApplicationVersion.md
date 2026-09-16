---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationVersion.html
---

# DescribeApplicationVersion
<a name="API_DescribeApplicationVersion"></a>

Provides a detailed description of a specified version of the application. To see a list of all the versions of an application, invoke the [ListApplicationVersions](API_ListApplicationVersions.md) operation.

**Note**
This operation is supported only for Managed Service for Apache Flink.

## Request Syntax
<a name="API_DescribeApplicationVersion_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "ApplicationVersionId": {{number}}
}
```

## Request Parameters
<a name="API_DescribeApplicationVersion_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DescribeApplicationVersion_RequestSyntax) **   <a name="APIReference-DescribeApplicationVersion-request-ApplicationName"></a>
The name of the application for which you want to get the version description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ApplicationVersionId](#API_DescribeApplicationVersion_RequestSyntax) **   <a name="APIReference-DescribeApplicationVersion-request-ApplicationVersionId"></a>
The ID of the application version for which you want to get the description.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

## Response Syntax
<a name="API_DescribeApplicationVersion_ResponseSyntax"></a>

```
{
   "ApplicationVersionDetail": {
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
<a name="API_DescribeApplicationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationVersionDetail](#API_DescribeApplicationVersion_ResponseSyntax) **   <a name="APIReference-DescribeApplicationVersion-response-ApplicationVersionDetail"></a>
Describes the application, including the application Amazon Resource Name (ARN), status, latest version, and input and output configurations.
Type: [ApplicationDetail](API_ApplicationDetail.md) object

## Errors
<a name="API_DescribeApplicationVersion_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplicationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationVersion)

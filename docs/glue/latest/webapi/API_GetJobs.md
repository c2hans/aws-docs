---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetJobs.html
---

# GetJobs
<a name="API_GetJobs"></a>

Retrieves all current job definitions.

## Request Syntax
<a name="API_GetJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetJobs_RequestSyntax) **   <a name="Glue-GetJobs-request-MaxResults"></a>
The maximum size of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetJobs_RequestSyntax) **   <a name="Glue-GetJobs-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_GetJobs_ResponseSyntax"></a>

```
{
   "Jobs": [
      {
         "AllocatedCapacity": number,
         "CodeGenConfigurationNodes": {
            "string" : {
               "Aggregate": {
                  "Aggs": [
                     {
                        "AggFunc": "string",
                        "Column": [ "string" ]
                     }
                  ],
                  "Groups": [
                     [ "string" ]
                  ],
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "AmazonRedshiftSource": {
                  "Data": {
                     "AccessType": "string",
                     "Action": "string",
                     "AdvancedOptions": [
                        {
                           "Key": "string",
                           "Value": "string"
                        }
                     ],
                     "CatalogDatabase": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "CatalogRedshiftSchema": "string",
                     "CatalogRedshiftTable": "string",
                     "CatalogTable": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "Connection": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "CrawlerConnection": "string",
                     "IamRole": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "MergeAction": "string",
                     "MergeClause": "string",
                     "MergeWhenMatched": "string",
                     "MergeWhenNotMatched": "string",
                     "PostAction": "string",
                     "PreAction": "string",
                     "SampleQuery": "string",
                     "Schema": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "SelectedColumns": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "SourceType": "string",
                     "StagingTable": "string",
                     "Table": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "TablePrefix": "string",
                     "TableSchema": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "TempDir": "string",
                     "Upsert": boolean
                  },
                  "Name": "string"
               },
               "AmazonRedshiftTarget": {
                  "Data": {
                     "AccessType": "string",
                     "Action": "string",
                     "AdvancedOptions": [
                        {
                           "Key": "string",
                           "Value": "string"
                        }
                     ],
                     "CatalogDatabase": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "CatalogRedshiftSchema": "string",
                     "CatalogRedshiftTable": "string",
                     "CatalogTable": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "Connection": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "CrawlerConnection": "string",
                     "IamRole": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "MergeAction": "string",
                     "MergeClause": "string",
                     "MergeWhenMatched": "string",
                     "MergeWhenNotMatched": "string",
                     "PostAction": "string",
                     "PreAction": "string",
                     "SampleQuery": "string",
                     "Schema": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "SelectedColumns": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "SourceType": "string",
                     "StagingTable": "string",
                     "Table": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "TablePrefix": "string",
                     "TableSchema": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "TempDir": "string",
                     "Upsert": boolean
                  },
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "ApplyMapping": {
                  "Inputs": [ "string" ],
                  "Mapping": [
                     {
                        "Children": [
                           "Mapping"
                        ],
                        "Dropped": boolean,
                        "FromPath": [ "string" ],
                        "FromType": "string",
                        "ToKey": "string",
                        "ToType": "string"
                     }
                  ],
                  "Name": "string"
               },
               "AthenaConnectorSource": {
                  "ConnectionName": "string",
                  "ConnectionTable": "string",
                  "ConnectionType": "string",
                  "ConnectorName": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "SchemaName": "string"
               },
               "CatalogDeltaSource": {
                  "AdditionalDeltaOptions": {
                     "string" : "string"
                  },
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Table": "string"
               },
               "CatalogHudiSource": {
                  "AdditionalHudiOptions": {
                     "string" : "string"
                  },
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Table": "string"
               },
               "CatalogIcebergSource": {
                  "AdditionalIcebergOptions": {
                     "string" : "string"
                  },
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Table": "string"
               },
               "CatalogKafkaSource": {
                  "Database": "string",
                  "DataPreviewOptions": {
                     "PollingTime": number,
                     "RecordPollingLimit": number
                  },
                  "DetectSchema": boolean,
                  "Name": "string",
                  "StreamingOptions": {
                     "AddRecordTimestamp": "string",
                     "Assign": "string",
                     "BootstrapServers": "string",
                     "Classification": "string",
                     "ConnectionName": "string",
                     "Delimiter": "string",
                     "EmitConsumerLagMetrics": "string",
                     "EndingOffsets": "string",
                     "IncludeHeaders": boolean,
                     "MaxOffsetsPerTrigger": number,
                     "MinPartitions": number,
                     "NumRetries": number,
                     "PollTimeoutMs": number,
                     "RetryIntervalMs": number,
                     "SecurityProtocol": "string",
                     "StartingOffsets": "string",
                     "StartingTimestamp": "string",
                     "SubscribePattern": "string",
                     "TopicName": "string"
                  },
                  "Table": "string",
                  "WindowSize": number
               },
               "CatalogKinesisSource": {
                  "Database": "string",
                  "DataPreviewOptions": {
                     "PollingTime": number,
                     "RecordPollingLimit": number
                  },
                  "DetectSchema": boolean,
                  "Name": "string",
                  "StreamingOptions": {
                     "AddIdleTimeBetweenReads": boolean,
                     "AddRecordTimestamp": "string",
                     "AvoidEmptyBatches": boolean,
                     "Classification": "string",
                     "Delimiter": "string",
                     "DescribeShardInterval": number,
                     "EmitConsumerLagMetrics": "string",
                     "EndpointUrl": "string",
                     "FanoutConsumerARN": "string",
                     "IdleTimeBetweenReadsInMs": number,
                     "MaxFetchRecordsPerShard": number,
                     "MaxFetchTimeInMs": number,
                     "MaxRecordPerRead": number,
                     "MaxRetryIntervalMs": number,
                     "NumRetries": number,
                     "RetryIntervalMs": number,
                     "RoleArn": "string",
                     "RoleSessionName": "string",
                     "StartingPosition": "string",
                     "StartingTimestamp": "string",
                     "StreamArn": "string",
                     "StreamName": "string"
                  },
                  "Table": "string",
                  "WindowSize": number
               },
               "CatalogSource": {
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "PartitionPredicate": "string",
                  "Table": "string"
               },
               "CatalogTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Table": "string"
               },
               "ConnectorDataSource": {
                  "ConnectionType": "string",
                  "Data": {
                     "string" : "string"
                  },
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "ConnectorDataTarget": {
                  "ConnectionType": "string",
                  "Data": {
                     "string" : "string"
                  },
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "CustomCode": {
                  "ClassName": "string",
                  "Code": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "DirectJDBCSource": {
                  "ConnectionName": "string",
                  "ConnectionType": "string",
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "RedshiftTmpDir": "string",
                  "Table": "string"
               },
               "DirectKafkaSource": {
                  "DataPreviewOptions": {
                     "PollingTime": number,
                     "RecordPollingLimit": number
                  },
                  "DetectSchema": boolean,
                  "Name": "string",
                  "StreamingOptions": {
                     "AddRecordTimestamp": "string",
                     "Assign": "string",
                     "BootstrapServers": "string",
                     "Classification": "string",
                     "ConnectionName": "string",
                     "Delimiter": "string",
                     "EmitConsumerLagMetrics": "string",
                     "EndingOffsets": "string",
                     "IncludeHeaders": boolean,
                     "MaxOffsetsPerTrigger": number,
                     "MinPartitions": number,
                     "NumRetries": number,
                     "PollTimeoutMs": number,
                     "RetryIntervalMs": number,
                     "SecurityProtocol": "string",
                     "StartingOffsets": "string",
                     "StartingTimestamp": "string",
                     "SubscribePattern": "string",
                     "TopicName": "string"
                  },
                  "WindowSize": number
               },
               "DirectKinesisSource": {
                  "DataPreviewOptions": {
                     "PollingTime": number,
                     "RecordPollingLimit": number
                  },
                  "DetectSchema": boolean,
                  "Name": "string",
                  "StreamingOptions": {
                     "AddIdleTimeBetweenReads": boolean,
                     "AddRecordTimestamp": "string",
                     "AvoidEmptyBatches": boolean,
                     "Classification": "string",
                     "Delimiter": "string",
                     "DescribeShardInterval": number,
                     "EmitConsumerLagMetrics": "string",
                     "EndpointUrl": "string",
                     "FanoutConsumerARN": "string",
                     "IdleTimeBetweenReadsInMs": number,
                     "MaxFetchRecordsPerShard": number,
                     "MaxFetchTimeInMs": number,
                     "MaxRecordPerRead": number,
                     "MaxRetryIntervalMs": number,
                     "NumRetries": number,
                     "RetryIntervalMs": number,
                     "RoleArn": "string",
                     "RoleSessionName": "string",
                     "StartingPosition": "string",
                     "StartingTimestamp": "string",
                     "StreamArn": "string",
                     "StreamName": "string"
                  },
                  "WindowSize": number
               },
               "DropDuplicates": {
                  "Columns": [
                     [ "string" ]
                  ],
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "DropFields": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Paths": [
                     [ "string" ]
                  ]
               },
               "DropNullFields": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "NullCheckBoxList": {
                     "IsEmpty": boolean,
                     "IsNegOne": boolean,
                     "IsNullString": boolean
                  },
                  "NullTextList": [
                     {
                        "Datatype": {
                           "Id": "string",
                           "Label": "string"
                        },
                        "Value": "string"
                     }
                  ]
               },
               "DynamicTransform": {
                  "FunctionName": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Parameters": [
                     {
                        "IsOptional": boolean,
                        "ListType": "string",
                        "Name": "string",
                        "Type": "string",
                        "ValidationMessage": "string",
                        "ValidationRule": "string",
                        "Value": [ "string" ]
                     }
                  ],
                  "Path": "string",
                  "TransformName": "string",
                  "Version": "string"
               },
               "DynamoDBCatalogSource": {
                  "AdditionalOptions": {
                     "DynamodbExport": "string",
                     "DynamodbUnnestDDBJson": boolean
                  },
                  "Database": "string",
                  "Name": "string",
                  "PitrEnabled": boolean,
                  "Table": "string"
               },
               "DynamoDBELTConnectorSource": {
                  "ConnectionOptions": {
                     "DynamodbExport": "string",
                     "DynamodbS3Bucket": "string",
                     "DynamodbS3BucketOwner": "string",
                     "DynamodbS3Prefix": "string",
                     "DynamodbStsRoleArn": "string",
                     "DynamodbTableArn": "string",
                     "DynamodbUnnestDDBJson": boolean
                  },
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "EvaluateDataQuality": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Output": "string",
                  "PublishingOptions": {
                     "CloudWatchMetricsEnabled": boolean,
                     "EvaluationContext": "string",
                     "ResultsPublishingEnabled": boolean,
                     "ResultsS3Prefix": "string"
                  },
                  "Ruleset": "string",
                  "StopJobOnFailureOptions": {
                     "StopJobOnFailureTiming": "string"
                  }
               },
               "EvaluateDataQualityMultiFrame": {
                  "AdditionalDataSources": {
                     "string" : "string"
                  },
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "PublishingOptions": {
                     "CloudWatchMetricsEnabled": boolean,
                     "EvaluationContext": "string",
                     "ResultsPublishingEnabled": boolean,
                     "ResultsS3Prefix": "string"
                  },
                  "Ruleset": "string",
                  "StopJobOnFailureOptions": {
                     "StopJobOnFailureTiming": "string"
                  }
               },
               "FillMissingValues": {
                  "FilledPath": "string",
                  "ImputedPath": "string",
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "Filter": {
                  "Filters": [
                     {
                        "Negated": boolean,
                        "Operation": "string",
                        "Values": [
                           {
                              "Type": "string",
                              "Value": [ "string" ]
                           }
                        ]
                     }
                  ],
                  "Inputs": [ "string" ],
                  "LogicalOperator": "string",
                  "Name": "string"
               },
               "GovernedCatalogSource": {
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number
                  },
                  "Database": "string",
                  "Name": "string",
                  "PartitionPredicate": "string",
                  "Table": "string"
               },
               "GovernedCatalogTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "SchemaChangePolicy": {
                     "EnableUpdateCatalog": boolean,
                     "UpdateBehavior": "string"
                  },
                  "Table": "string"
               },
               "JDBCConnectorSource": {
                  "AdditionalOptions": {
                     "DataTypeMapping": {
                        "string" : "string"
                     },
                     "FilterPredicate": "string",
                     "JobBookmarkKeys": [ "string" ],
                     "JobBookmarkKeysSortOrder": "string",
                     "LowerBound": number,
                     "NumPartitions": number,
                     "PartitionColumn": "string",
                     "UpperBound": number
                  },
                  "ConnectionName": "string",
                  "ConnectionTable": "string",
                  "ConnectionType": "string",
                  "ConnectorName": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Query": "string"
               },
               "JDBCConnectorTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "ConnectionName": "string",
                  "ConnectionTable": "string",
                  "ConnectionType": "string",
                  "ConnectorName": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "Join": {
                  "Columns": [
                     {
                        "From": "string",
                        "Keys": [
                           [ "string" ]
                        ]
                     }
                  ],
                  "Inputs": [ "string" ],
                  "JoinType": "string",
                  "Name": "string"
               },
               "Merge": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "PrimaryKeys": [
                     [ "string" ]
                  ],
                  "Source": "string"
               },
               "MicrosoftSQLServerCatalogSource": {
                  "Database": "string",
                  "Name": "string",
                  "Table": "string"
               },
               "MicrosoftSQLServerCatalogTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Table": "string"
               },
               "MySQLCatalogSource": {
                  "Database": "string",
                  "Name": "string",
                  "Table": "string"
               },
               "MySQLCatalogTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Table": "string"
               },
               "OracleSQLCatalogSource": {
                  "Database": "string",
                  "Name": "string",
                  "Table": "string"
               },
               "OracleSQLCatalogTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Table": "string"
               },
               "PIIDetection": {
                  "DetectionParameters": "string",
                  "DetectionSensitivity": "string",
                  "EntityTypesToDetect": [ "string" ],
                  "Inputs": [ "string" ],
                  "MaskValue": "string",
                  "MatchPattern": "string",
                  "Name": "string",
                  "NumLeftCharsToExclude": number,
                  "NumRightCharsToExclude": number,
                  "OutputColumnName": "string",
                  "PiiType": "string",
                  "RedactChar": "string",
                  "RedactText": "string",
                  "SampleFraction": number,
                  "ThresholdFraction": number
               },
               "PostgreSQLCatalogSource": {
                  "Database": "string",
                  "Name": "string",
                  "Table": "string"
               },
               "PostgreSQLCatalogTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Table": "string"
               },
               "Recipe": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "RecipeReference": {
                     "RecipeArn": "string",
                     "RecipeVersion": "string"
                  },
                  "RecipeSteps": [
                     {
                        "Action": {
                           "Operation": "string",
                           "Parameters": {
                              "string" : "string"
                           }
                        },
                        "ConditionExpressions": [
                           {
                              "Condition": "string",
                              "TargetColumn": "string",
                              "Value": "string"
                           }
                        ]
                     }
                  ]
               },
               "RedshiftSource": {
                  "Database": "string",
                  "Name": "string",
                  "RedshiftTmpDir": "string",
                  "Table": "string",
                  "TmpDirIAMRole": "string"
               },
               "RedshiftTarget": {
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "RedshiftTmpDir": "string",
                  "Table": "string",
                  "TmpDirIAMRole": "string",
                  "UpsertRedshiftOptions": {
                     "ConnectionName": "string",
                     "TableLocation": "string",
                     "UpsertKeys": [ "string" ]
                  }
               },
               "RelationalCatalogSource": {
                  "Database": "string",
                  "Name": "string",
                  "Table": "string"
               },
               "RenameField": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "SourcePath": [ "string" ],
                  "TargetPath": [ "string" ]
               },
               "Route": {
                  "GroupFiltersList": [
                     {
                        "Filters": [
                           {
                              "Negated": boolean,
                              "Operation": "string",
                              "Values": [
                                 {
                                    "Type": "string",
                                    "Value": [ "string" ]
                                 }
                              ]
                           }
                        ],
                        "GroupName": "string",
                        "LogicalOperator": "string"
                     }
                  ],
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "S3CatalogDeltaSource": {
                  "AdditionalDeltaOptions": {
                     "string" : "string"
                  },
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Table": "string"
               },
               "S3CatalogHudiSource": {
                  "AdditionalHudiOptions": {
                     "string" : "string"
                  },
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Table": "string"
               },
               "S3CatalogIcebergSource": {
                  "AdditionalIcebergOptions": {
                     "string" : "string"
                  },
                  "Database": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Table": "string"
               },
               "S3CatalogSource": {
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number
                  },
                  "Database": "string",
                  "Name": "string",
                  "PartitionPredicate": "string",
                  "Table": "string"
               },
               "S3CatalogTarget": {
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "SchemaChangePolicy": {
                     "EnableUpdateCatalog": boolean,
                     "UpdateBehavior": "string"
                  },
                  "Table": "string"
               },
               "S3CsvSource": {
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number,
                     "EnableSamplePath": boolean,
                     "SamplePath": "string"
                  },
                  "CompressionType": "string",
                  "Escaper": "string",
                  "Exclusions": [ "string" ],
                  "GroupFiles": "string",
                  "GroupSize": "string",
                  "MaxBand": number,
                  "MaxFilesInBand": number,
                  "Multiline": boolean,
                  "Name": "string",
                  "OptimizePerformance": boolean,
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Paths": [ "string" ],
                  "QuoteChar": "string",
                  "Recurse": boolean,
                  "Separator": "string",
                  "SkipFirst": boolean,
                  "WithHeader": boolean,
                  "WriteHeader": boolean
               },
               "S3DeltaCatalogTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "SchemaChangePolicy": {
                     "EnableUpdateCatalog": boolean,
                     "UpdateBehavior": "string"
                  },
                  "Table": "string"
               },
               "S3DeltaDirectTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Compression": "string",
                  "Format": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "NumberTargetPartitions": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Path": "string",
                  "SchemaChangePolicy": {
                     "Database": "string",
                     "EnableUpdateCatalog": boolean,
                     "Table": "string",
                     "UpdateBehavior": "string"
                  }
               },
               "S3DeltaSource": {
                  "AdditionalDeltaOptions": {
                     "string" : "string"
                  },
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number,
                     "EnableSamplePath": boolean,
                     "SamplePath": "string"
                  },
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Paths": [ "string" ]
               },
               "S3DirectTarget": {
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Compression": "string",
                  "Format": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "NumberTargetPartitions": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Path": "string",
                  "SchemaChangePolicy": {
                     "Database": "string",
                     "EnableUpdateCatalog": boolean,
                     "Table": "string",
                     "UpdateBehavior": "string"
                  }
               },
               "S3ExcelSource": {
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number,
                     "EnableSamplePath": boolean,
                     "SamplePath": "string"
                  },
                  "CompressionType": "string",
                  "Exclusions": [ "string" ],
                  "GroupFiles": "string",
                  "GroupSize": "string",
                  "MaxBand": number,
                  "MaxFilesInBand": number,
                  "Name": "string",
                  "NumberRows": number,
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Paths": [ "string" ],
                  "Recurse": boolean,
                  "SkipFooter": number
               },
               "S3GlueParquetTarget": {
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Compression": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "NumberTargetPartitions": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Path": "string",
                  "SchemaChangePolicy": {
                     "Database": "string",
                     "EnableUpdateCatalog": boolean,
                     "Table": "string",
                     "UpdateBehavior": "string"
                  }
               },
               "S3HudiCatalogTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "SchemaChangePolicy": {
                     "EnableUpdateCatalog": boolean,
                     "UpdateBehavior": "string"
                  },
                  "Table": "string"
               },
               "S3HudiDirectTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Compression": "string",
                  "Format": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "NumberTargetPartitions": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Path": "string",
                  "SchemaChangePolicy": {
                     "Database": "string",
                     "EnableUpdateCatalog": boolean,
                     "Table": "string",
                     "UpdateBehavior": "string"
                  }
               },
               "S3HudiSource": {
                  "AdditionalHudiOptions": {
                     "string" : "string"
                  },
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number,
                     "EnableSamplePath": boolean,
                     "SamplePath": "string"
                  },
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Paths": [ "string" ]
               },
               "S3HyperDirectTarget": {
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Compression": "string",
                  "Format": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Path": "string",
                  "SchemaChangePolicy": {
                     "Database": "string",
                     "EnableUpdateCatalog": boolean,
                     "Table": "string",
                     "UpdateBehavior": "string"
                  }
               },
               "S3IcebergCatalogTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Database": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "SchemaChangePolicy": {
                     "EnableUpdateCatalog": boolean,
                     "UpdateBehavior": "string"
                  },
                  "Table": "string"
               },
               "S3IcebergDirectTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "AutoDataQuality": {
                     "EvaluationContext": "string",
                     "IsEnabled": boolean
                  },
                  "Compression": "string",
                  "Format": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "NumberTargetPartitions": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "PartitionKeys": [
                     [ "string" ]
                  ],
                  "Path": "string",
                  "SchemaChangePolicy": {
                     "Database": "string",
                     "EnableUpdateCatalog": boolean,
                     "Table": "string",
                     "UpdateBehavior": "string"
                  }
               },
               "S3JsonSource": {
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number,
                     "EnableSamplePath": boolean,
                     "SamplePath": "string"
                  },
                  "CompressionType": "string",
                  "Exclusions": [ "string" ],
                  "GroupFiles": "string",
                  "GroupSize": "string",
                  "JsonPath": "string",
                  "MaxBand": number,
                  "MaxFilesInBand": number,
                  "Multiline": boolean,
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Paths": [ "string" ],
                  "Recurse": boolean
               },
               "S3ParquetSource": {
                  "AdditionalOptions": {
                     "BoundedFiles": number,
                     "BoundedSize": number,
                     "EnableSamplePath": boolean,
                     "SamplePath": "string"
                  },
                  "CompressionType": "string",
                  "Exclusions": [ "string" ],
                  "GroupFiles": "string",
                  "GroupSize": "string",
                  "MaxBand": number,
                  "MaxFilesInBand": number,
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "Paths": [ "string" ],
                  "Recurse": boolean
               },
               "SelectFields": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Paths": [
                     [ "string" ]
                  ]
               },
               "SelectFromCollection": {
                  "Index": number,
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "SnowflakeSource": {
                  "Data": {
                     "Action": "string",
                     "AdditionalOptions": {
                        "string" : "string"
                     },
                     "AutoPushdown": boolean,
                     "Connection": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "Database": "string",
                     "IamRole": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "MergeAction": "string",
                     "MergeClause": "string",
                     "MergeWhenMatched": "string",
                     "MergeWhenNotMatched": "string",
                     "PostAction": "string",
                     "PreAction": "string",
                     "SampleQuery": "string",
                     "Schema": "string",
                     "SelectedColumns": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "SourceType": "string",
                     "StagingTable": "string",
                     "Table": "string",
                     "TableSchema": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "TempDir": "string",
                     "Upsert": boolean
                  },
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "SnowflakeTarget": {
                  "Data": {
                     "Action": "string",
                     "AdditionalOptions": {
                        "string" : "string"
                     },
                     "AutoPushdown": boolean,
                     "Connection": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "Database": "string",
                     "IamRole": {
                        "Description": "string",
                        "Label": "string",
                        "Value": "string"
                     },
                     "MergeAction": "string",
                     "MergeClause": "string",
                     "MergeWhenMatched": "string",
                     "MergeWhenNotMatched": "string",
                     "PostAction": "string",
                     "PreAction": "string",
                     "SampleQuery": "string",
                     "Schema": "string",
                     "SelectedColumns": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "SourceType": "string",
                     "StagingTable": "string",
                     "Table": "string",
                     "TableSchema": [
                        {
                           "Description": "string",
                           "Label": "string",
                           "Value": "string"
                        }
                     ],
                     "TempDir": "string",
                     "Upsert": boolean
                  },
                  "Inputs": [ "string" ],
                  "Name": "string"
               },
               "SparkConnectorSource": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "ConnectionName": "string",
                  "ConnectionType": "string",
                  "ConnectorName": "string",
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "SparkConnectorTarget": {
                  "AdditionalOptions": {
                     "string" : "string"
                  },
                  "ConnectionName": "string",
                  "ConnectionType": "string",
                  "ConnectorName": "string",
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ]
               },
               "SparkSQL": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "OutputSchemas": [
                     {
                        "Columns": [
                           {
                              "GlueStudioType": "string",
                              "Name": "string",
                              "Type": "string"
                           }
                        ]
                     }
                  ],
                  "SqlAliases": [
                     {
                        "Alias": "string",
                        "From": "string"
                     }
                  ],
                  "SqlQuery": "string"
               },
               "Spigot": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Path": "string",
                  "Prob": number,
                  "Topk": number
               },
               "SplitFields": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "Paths": [
                     [ "string" ]
                  ]
               },
               "Union": {
                  "Inputs": [ "string" ],
                  "Name": "string",
                  "UnionType": "string"
               }
            }
         },
         "Command": {
            "Name": "string",
            "PythonVersion": "string",
            "Runtime": "string",
            "ScriptLocation": "string"
         },
         "Connections": {
            "Connections": [ "string" ]
         },
         "CreatedOn": number,
         "DefaultArguments": {
            "string" : "string"
         },
         "Description": "string",
         "ExecutionClass": "string",
         "ExecutionProperty": {
            "MaxConcurrentRuns": number
         },
         "GlueVersion": "string",
         "JobMode": "string",
         "JobRunQueuingEnabled": boolean,
         "LastModifiedOn": number,
         "LogUri": "string",
         "MaintenanceWindow": "string",
         "MaxCapacity": number,
         "MaxRetries": number,
         "Name": "string",
         "NonOverridableArguments": {
            "string" : "string"
         },
         "NotificationProperty": {
            "NotifyDelayAfter": number
         },
         "NumberOfWorkers": number,
         "ProfileName": "string",
         "Role": "string",
         "SecurityConfiguration": "string",
         "SourceControlDetails": {
            "AuthStrategy": "string",
            "AuthToken": "string",
            "Branch": "string",
            "Folder": "string",
            "LastCommitId": "string",
            "Owner": "string",
            "Provider": "string",
            "Repository": "string"
         },
         "Timeout": number,
         "WorkerType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Jobs](#API_GetJobs_ResponseSyntax) **   <a name="Glue-GetJobs-response-Jobs"></a>
A list of job definitions.
Type: Array of [Job](API_Job.md) objects

 ** [NextToken](#API_GetJobs_ResponseSyntax) **   <a name="Glue-GetJobs-response-NextToken"></a>
A continuation token, if not all job definitions have yet been returned.
Type: String

## Errors
<a name="API_GetJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

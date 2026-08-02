---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateJob.html
---

# CreateJob
<a name="API_CreateJob"></a>

Creates a new job definition.

## Request Syntax
<a name="API_CreateJob_RequestSyntax"></a>

```
{
   "AllocatedCapacity": {{number}},
   "CodeGenConfigurationNodes": {
      "{{string}}" : {
         "Aggregate": {
            "Aggs": [
               {
                  "AggFunc": "{{string}}",
                  "Column": [ "{{string}}" ]
               }
            ],
            "Groups": [
               [ "{{string}}" ]
            ],
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "AmazonRedshiftSource": {
            "Data": {
               "AccessType": "{{string}}",
               "Action": "{{string}}",
               "AdvancedOptions": [
                  {
                     "Key": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "CatalogDatabase": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "CatalogRedshiftSchema": "{{string}}",
               "CatalogRedshiftTable": "{{string}}",
               "CatalogTable": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "Connection": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "CrawlerConnection": "{{string}}",
               "IamRole": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "MergeAction": "{{string}}",
               "MergeClause": "{{string}}",
               "MergeWhenMatched": "{{string}}",
               "MergeWhenNotMatched": "{{string}}",
               "PostAction": "{{string}}",
               "PreAction": "{{string}}",
               "SampleQuery": "{{string}}",
               "Schema": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "SelectedColumns": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "SourceType": "{{string}}",
               "StagingTable": "{{string}}",
               "Table": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "TablePrefix": "{{string}}",
               "TableSchema": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "TempDir": "{{string}}",
               "Upsert": {{boolean}}
            },
            "Name": "{{string}}"
         },
         "AmazonRedshiftTarget": {
            "Data": {
               "AccessType": "{{string}}",
               "Action": "{{string}}",
               "AdvancedOptions": [
                  {
                     "Key": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "CatalogDatabase": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "CatalogRedshiftSchema": "{{string}}",
               "CatalogRedshiftTable": "{{string}}",
               "CatalogTable": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "Connection": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "CrawlerConnection": "{{string}}",
               "IamRole": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "MergeAction": "{{string}}",
               "MergeClause": "{{string}}",
               "MergeWhenMatched": "{{string}}",
               "MergeWhenNotMatched": "{{string}}",
               "PostAction": "{{string}}",
               "PreAction": "{{string}}",
               "SampleQuery": "{{string}}",
               "Schema": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "SelectedColumns": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "SourceType": "{{string}}",
               "StagingTable": "{{string}}",
               "Table": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "TablePrefix": "{{string}}",
               "TableSchema": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "TempDir": "{{string}}",
               "Upsert": {{boolean}}
            },
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "ApplyMapping": {
            "Inputs": [ "{{string}}" ],
            "Mapping": [
               {
                  "Children": [
                     "Mapping"
                  ],
                  "Dropped": {{boolean}},
                  "FromPath": [ "{{string}}" ],
                  "FromType": "{{string}}",
                  "ToKey": "{{string}}",
                  "ToType": "{{string}}"
               }
            ],
            "Name": "{{string}}"
         },
         "AthenaConnectorSource": {
            "ConnectionName": "{{string}}",
            "ConnectionTable": "{{string}}",
            "ConnectionType": "{{string}}",
            "ConnectorName": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "SchemaName": "{{string}}"
         },
         "CatalogDeltaSource": {
            "AdditionalDeltaOptions": {
               "{{string}}" : "{{string}}"
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Table": "{{string}}"
         },
         "CatalogHudiSource": {
            "AdditionalHudiOptions": {
               "{{string}}" : "{{string}}"
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Table": "{{string}}"
         },
         "CatalogIcebergSource": {
            "AdditionalIcebergOptions": {
               "{{string}}" : "{{string}}"
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Table": "{{string}}"
         },
         "CatalogKafkaSource": {
            "Database": "{{string}}",
            "DataPreviewOptions": {
               "PollingTime": {{number}},
               "RecordPollingLimit": {{number}}
            },
            "DetectSchema": {{boolean}},
            "Name": "{{string}}",
            "StreamingOptions": {
               "AddRecordTimestamp": "{{string}}",
               "Assign": "{{string}}",
               "BootstrapServers": "{{string}}",
               "Classification": "{{string}}",
               "ConnectionName": "{{string}}",
               "Delimiter": "{{string}}",
               "EmitConsumerLagMetrics": "{{string}}",
               "EndingOffsets": "{{string}}",
               "IncludeHeaders": {{boolean}},
               "MaxOffsetsPerTrigger": {{number}},
               "MinPartitions": {{number}},
               "NumRetries": {{number}},
               "PollTimeoutMs": {{number}},
               "RetryIntervalMs": {{number}},
               "SecurityProtocol": "{{string}}",
               "StartingOffsets": "{{string}}",
               "StartingTimestamp": "{{string}}",
               "SubscribePattern": "{{string}}",
               "TopicName": "{{string}}"
            },
            "Table": "{{string}}",
            "WindowSize": {{number}}
         },
         "CatalogKinesisSource": {
            "Database": "{{string}}",
            "DataPreviewOptions": {
               "PollingTime": {{number}},
               "RecordPollingLimit": {{number}}
            },
            "DetectSchema": {{boolean}},
            "Name": "{{string}}",
            "StreamingOptions": {
               "AddIdleTimeBetweenReads": {{boolean}},
               "AddRecordTimestamp": "{{string}}",
               "AvoidEmptyBatches": {{boolean}},
               "Classification": "{{string}}",
               "Delimiter": "{{string}}",
               "DescribeShardInterval": {{number}},
               "EmitConsumerLagMetrics": "{{string}}",
               "EndpointUrl": "{{string}}",
               "FanoutConsumerARN": "{{string}}",
               "IdleTimeBetweenReadsInMs": {{number}},
               "MaxFetchRecordsPerShard": {{number}},
               "MaxFetchTimeInMs": {{number}},
               "MaxRecordPerRead": {{number}},
               "MaxRetryIntervalMs": {{number}},
               "NumRetries": {{number}},
               "RetryIntervalMs": {{number}},
               "RoleArn": "{{string}}",
               "RoleSessionName": "{{string}}",
               "StartingPosition": "{{string}}",
               "StartingTimestamp": "{{string}}",
               "StreamArn": "{{string}}",
               "StreamName": "{{string}}"
            },
            "Table": "{{string}}",
            "WindowSize": {{number}}
         },
         "CatalogSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "PartitionPredicate": "{{string}}",
            "Table": "{{string}}"
         },
         "CatalogTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Table": "{{string}}"
         },
         "ConnectorDataSource": {
            "ConnectionType": "{{string}}",
            "Data": {
               "{{string}}" : "{{string}}"
            },
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "ConnectorDataTarget": {
            "ConnectionType": "{{string}}",
            "Data": {
               "{{string}}" : "{{string}}"
            },
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "CustomCode": {
            "ClassName": "{{string}}",
            "Code": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "DirectJDBCSource": {
            "ConnectionName": "{{string}}",
            "ConnectionType": "{{string}}",
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "RedshiftTmpDir": "{{string}}",
            "Table": "{{string}}"
         },
         "DirectKafkaSource": {
            "DataPreviewOptions": {
               "PollingTime": {{number}},
               "RecordPollingLimit": {{number}}
            },
            "DetectSchema": {{boolean}},
            "Name": "{{string}}",
            "StreamingOptions": {
               "AddRecordTimestamp": "{{string}}",
               "Assign": "{{string}}",
               "BootstrapServers": "{{string}}",
               "Classification": "{{string}}",
               "ConnectionName": "{{string}}",
               "Delimiter": "{{string}}",
               "EmitConsumerLagMetrics": "{{string}}",
               "EndingOffsets": "{{string}}",
               "IncludeHeaders": {{boolean}},
               "MaxOffsetsPerTrigger": {{number}},
               "MinPartitions": {{number}},
               "NumRetries": {{number}},
               "PollTimeoutMs": {{number}},
               "RetryIntervalMs": {{number}},
               "SecurityProtocol": "{{string}}",
               "StartingOffsets": "{{string}}",
               "StartingTimestamp": "{{string}}",
               "SubscribePattern": "{{string}}",
               "TopicName": "{{string}}"
            },
            "WindowSize": {{number}}
         },
         "DirectKinesisSource": {
            "DataPreviewOptions": {
               "PollingTime": {{number}},
               "RecordPollingLimit": {{number}}
            },
            "DetectSchema": {{boolean}},
            "Name": "{{string}}",
            "StreamingOptions": {
               "AddIdleTimeBetweenReads": {{boolean}},
               "AddRecordTimestamp": "{{string}}",
               "AvoidEmptyBatches": {{boolean}},
               "Classification": "{{string}}",
               "Delimiter": "{{string}}",
               "DescribeShardInterval": {{number}},
               "EmitConsumerLagMetrics": "{{string}}",
               "EndpointUrl": "{{string}}",
               "FanoutConsumerARN": "{{string}}",
               "IdleTimeBetweenReadsInMs": {{number}},
               "MaxFetchRecordsPerShard": {{number}},
               "MaxFetchTimeInMs": {{number}},
               "MaxRecordPerRead": {{number}},
               "MaxRetryIntervalMs": {{number}},
               "NumRetries": {{number}},
               "RetryIntervalMs": {{number}},
               "RoleArn": "{{string}}",
               "RoleSessionName": "{{string}}",
               "StartingPosition": "{{string}}",
               "StartingTimestamp": "{{string}}",
               "StreamArn": "{{string}}",
               "StreamName": "{{string}}"
            },
            "WindowSize": {{number}}
         },
         "DropDuplicates": {
            "Columns": [
               [ "{{string}}" ]
            ],
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "DropFields": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Paths": [
               [ "{{string}}" ]
            ]
         },
         "DropNullFields": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "NullCheckBoxList": {
               "IsEmpty": {{boolean}},
               "IsNegOne": {{boolean}},
               "IsNullString": {{boolean}}
            },
            "NullTextList": [
               {
                  "Datatype": {
                     "Id": "{{string}}",
                     "Label": "{{string}}"
                  },
                  "Value": "{{string}}"
               }
            ]
         },
         "DynamicTransform": {
            "FunctionName": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Parameters": [
               {
                  "IsOptional": {{boolean}},
                  "ListType": "{{string}}",
                  "Name": "{{string}}",
                  "Type": "{{string}}",
                  "ValidationMessage": "{{string}}",
                  "ValidationRule": "{{string}}",
                  "Value": [ "{{string}}" ]
               }
            ],
            "Path": "{{string}}",
            "TransformName": "{{string}}",
            "Version": "{{string}}"
         },
         "DynamoDBCatalogSource": {
            "AdditionalOptions": {
               "DynamodbExport": "{{string}}",
               "DynamodbUnnestDDBJson": {{boolean}}
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "PitrEnabled": {{boolean}},
            "Table": "{{string}}"
         },
         "DynamoDBELTConnectorSource": {
            "ConnectionOptions": {
               "DynamodbExport": "{{string}}",
               "DynamodbS3Bucket": "{{string}}",
               "DynamodbS3BucketOwner": "{{string}}",
               "DynamodbS3Prefix": "{{string}}",
               "DynamodbStsRoleArn": "{{string}}",
               "DynamodbTableArn": "{{string}}",
               "DynamodbUnnestDDBJson": {{boolean}}
            },
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "EvaluateDataQuality": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Output": "{{string}}",
            "PublishingOptions": {
               "CloudWatchMetricsEnabled": {{boolean}},
               "EvaluationContext": "{{string}}",
               "ResultsPublishingEnabled": {{boolean}},
               "ResultsS3Prefix": "{{string}}"
            },
            "Ruleset": "{{string}}",
            "StopJobOnFailureOptions": {
               "StopJobOnFailureTiming": "{{string}}"
            }
         },
         "EvaluateDataQualityMultiFrame": {
            "AdditionalDataSources": {
               "{{string}}" : "{{string}}"
            },
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "PublishingOptions": {
               "CloudWatchMetricsEnabled": {{boolean}},
               "EvaluationContext": "{{string}}",
               "ResultsPublishingEnabled": {{boolean}},
               "ResultsS3Prefix": "{{string}}"
            },
            "Ruleset": "{{string}}",
            "StopJobOnFailureOptions": {
               "StopJobOnFailureTiming": "{{string}}"
            }
         },
         "FillMissingValues": {
            "FilledPath": "{{string}}",
            "ImputedPath": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "Filter": {
            "Filters": [
               {
                  "Negated": {{boolean}},
                  "Operation": "{{string}}",
                  "Values": [
                     {
                        "Type": "{{string}}",
                        "Value": [ "{{string}}" ]
                     }
                  ]
               }
            ],
            "Inputs": [ "{{string}}" ],
            "LogicalOperator": "{{string}}",
            "Name": "{{string}}"
         },
         "GovernedCatalogSource": {
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}}
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "PartitionPredicate": "{{string}}",
            "Table": "{{string}}"
         },
         "GovernedCatalogTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "SchemaChangePolicy": {
               "EnableUpdateCatalog": {{boolean}},
               "UpdateBehavior": "{{string}}"
            },
            "Table": "{{string}}"
         },
         "JDBCConnectorSource": {
            "AdditionalOptions": {
               "DataTypeMapping": {
                  "{{string}}" : "{{string}}"
               },
               "FilterPredicate": "{{string}}",
               "JobBookmarkKeys": [ "{{string}}" ],
               "JobBookmarkKeysSortOrder": "{{string}}",
               "LowerBound": {{number}},
               "NumPartitions": {{number}},
               "PartitionColumn": "{{string}}",
               "UpperBound": {{number}}
            },
            "ConnectionName": "{{string}}",
            "ConnectionTable": "{{string}}",
            "ConnectionType": "{{string}}",
            "ConnectorName": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Query": "{{string}}"
         },
         "JDBCConnectorTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "ConnectionName": "{{string}}",
            "ConnectionTable": "{{string}}",
            "ConnectionType": "{{string}}",
            "ConnectorName": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "Join": {
            "Columns": [
               {
                  "From": "{{string}}",
                  "Keys": [
                     [ "{{string}}" ]
                  ]
               }
            ],
            "Inputs": [ "{{string}}" ],
            "JoinType": "{{string}}",
            "Name": "{{string}}"
         },
         "Merge": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "PrimaryKeys": [
               [ "{{string}}" ]
            ],
            "Source": "{{string}}"
         },
         "MicrosoftSQLServerCatalogSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "MicrosoftSQLServerCatalogTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "MySQLCatalogSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "MySQLCatalogTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "OracleSQLCatalogSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "OracleSQLCatalogTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "PIIDetection": {
            "DetectionParameters": "{{string}}",
            "DetectionSensitivity": "{{string}}",
            "EntityTypesToDetect": [ "{{string}}" ],
            "Inputs": [ "{{string}}" ],
            "MaskValue": "{{string}}",
            "MatchPattern": "{{string}}",
            "Name": "{{string}}",
            "NumLeftCharsToExclude": {{number}},
            "NumRightCharsToExclude": {{number}},
            "OutputColumnName": "{{string}}",
            "PiiType": "{{string}}",
            "RedactChar": "{{string}}",
            "RedactText": "{{string}}",
            "SampleFraction": {{number}},
            "ThresholdFraction": {{number}}
         },
         "PostgreSQLCatalogSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "PostgreSQLCatalogTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "Recipe": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "RecipeReference": {
               "RecipeArn": "{{string}}",
               "RecipeVersion": "{{string}}"
            },
            "RecipeSteps": [
               {
                  "Action": {
                     "Operation": "{{string}}",
                     "Parameters": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "ConditionExpressions": [
                     {
                        "Condition": "{{string}}",
                        "TargetColumn": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "RedshiftSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "RedshiftTmpDir": "{{string}}",
            "Table": "{{string}}",
            "TmpDirIAMRole": "{{string}}"
         },
         "RedshiftTarget": {
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "RedshiftTmpDir": "{{string}}",
            "Table": "{{string}}",
            "TmpDirIAMRole": "{{string}}",
            "UpsertRedshiftOptions": {
               "ConnectionName": "{{string}}",
               "TableLocation": "{{string}}",
               "UpsertKeys": [ "{{string}}" ]
            }
         },
         "RelationalCatalogSource": {
            "Database": "{{string}}",
            "Name": "{{string}}",
            "Table": "{{string}}"
         },
         "RenameField": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "SourcePath": [ "{{string}}" ],
            "TargetPath": [ "{{string}}" ]
         },
         "Route": {
            "GroupFiltersList": [
               {
                  "Filters": [
                     {
                        "Negated": {{boolean}},
                        "Operation": "{{string}}",
                        "Values": [
                           {
                              "Type": "{{string}}",
                              "Value": [ "{{string}}" ]
                           }
                        ]
                     }
                  ],
                  "GroupName": "{{string}}",
                  "LogicalOperator": "{{string}}"
               }
            ],
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "S3CatalogDeltaSource": {
            "AdditionalDeltaOptions": {
               "{{string}}" : "{{string}}"
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Table": "{{string}}"
         },
         "S3CatalogHudiSource": {
            "AdditionalHudiOptions": {
               "{{string}}" : "{{string}}"
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Table": "{{string}}"
         },
         "S3CatalogIcebergSource": {
            "AdditionalIcebergOptions": {
               "{{string}}" : "{{string}}"
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Table": "{{string}}"
         },
         "S3CatalogSource": {
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}}
            },
            "Database": "{{string}}",
            "Name": "{{string}}",
            "PartitionPredicate": "{{string}}",
            "Table": "{{string}}"
         },
         "S3CatalogTarget": {
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "SchemaChangePolicy": {
               "EnableUpdateCatalog": {{boolean}},
               "UpdateBehavior": "{{string}}"
            },
            "Table": "{{string}}"
         },
         "S3CsvSource": {
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}},
               "EnableSamplePath": {{boolean}},
               "SamplePath": "{{string}}"
            },
            "CompressionType": "{{string}}",
            "Escaper": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "GroupFiles": "{{string}}",
            "GroupSize": "{{string}}",
            "MaxBand": {{number}},
            "MaxFilesInBand": {{number}},
            "Multiline": {{boolean}},
            "Name": "{{string}}",
            "OptimizePerformance": {{boolean}},
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Paths": [ "{{string}}" ],
            "QuoteChar": "{{string}}",
            "Recurse": {{boolean}},
            "Separator": "{{string}}",
            "SkipFirst": {{boolean}},
            "WithHeader": {{boolean}},
            "WriteHeader": {{boolean}}
         },
         "S3DeltaCatalogTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "SchemaChangePolicy": {
               "EnableUpdateCatalog": {{boolean}},
               "UpdateBehavior": "{{string}}"
            },
            "Table": "{{string}}"
         },
         "S3DeltaDirectTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Compression": "{{string}}",
            "Format": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "NumberTargetPartitions": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Path": "{{string}}",
            "SchemaChangePolicy": {
               "Database": "{{string}}",
               "EnableUpdateCatalog": {{boolean}},
               "Table": "{{string}}",
               "UpdateBehavior": "{{string}}"
            }
         },
         "S3DeltaSource": {
            "AdditionalDeltaOptions": {
               "{{string}}" : "{{string}}"
            },
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}},
               "EnableSamplePath": {{boolean}},
               "SamplePath": "{{string}}"
            },
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Paths": [ "{{string}}" ]
         },
         "S3DirectTarget": {
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Compression": "{{string}}",
            "Format": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "NumberTargetPartitions": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Path": "{{string}}",
            "SchemaChangePolicy": {
               "Database": "{{string}}",
               "EnableUpdateCatalog": {{boolean}},
               "Table": "{{string}}",
               "UpdateBehavior": "{{string}}"
            }
         },
         "S3ExcelSource": {
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}},
               "EnableSamplePath": {{boolean}},
               "SamplePath": "{{string}}"
            },
            "CompressionType": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "GroupFiles": "{{string}}",
            "GroupSize": "{{string}}",
            "MaxBand": {{number}},
            "MaxFilesInBand": {{number}},
            "Name": "{{string}}",
            "NumberRows": {{number}},
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Paths": [ "{{string}}" ],
            "Recurse": {{boolean}},
            "SkipFooter": {{number}}
         },
         "S3GlueParquetTarget": {
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Compression": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "NumberTargetPartitions": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Path": "{{string}}",
            "SchemaChangePolicy": {
               "Database": "{{string}}",
               "EnableUpdateCatalog": {{boolean}},
               "Table": "{{string}}",
               "UpdateBehavior": "{{string}}"
            }
         },
         "S3HudiCatalogTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "SchemaChangePolicy": {
               "EnableUpdateCatalog": {{boolean}},
               "UpdateBehavior": "{{string}}"
            },
            "Table": "{{string}}"
         },
         "S3HudiDirectTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Compression": "{{string}}",
            "Format": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "NumberTargetPartitions": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Path": "{{string}}",
            "SchemaChangePolicy": {
               "Database": "{{string}}",
               "EnableUpdateCatalog": {{boolean}},
               "Table": "{{string}}",
               "UpdateBehavior": "{{string}}"
            }
         },
         "S3HudiSource": {
            "AdditionalHudiOptions": {
               "{{string}}" : "{{string}}"
            },
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}},
               "EnableSamplePath": {{boolean}},
               "SamplePath": "{{string}}"
            },
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Paths": [ "{{string}}" ]
         },
         "S3HyperDirectTarget": {
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Compression": "{{string}}",
            "Format": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Path": "{{string}}",
            "SchemaChangePolicy": {
               "Database": "{{string}}",
               "EnableUpdateCatalog": {{boolean}},
               "Table": "{{string}}",
               "UpdateBehavior": "{{string}}"
            }
         },
         "S3IcebergCatalogTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Database": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "SchemaChangePolicy": {
               "EnableUpdateCatalog": {{boolean}},
               "UpdateBehavior": "{{string}}"
            },
            "Table": "{{string}}"
         },
         "S3IcebergDirectTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "AutoDataQuality": {
               "EvaluationContext": "{{string}}",
               "IsEnabled": {{boolean}}
            },
            "Compression": "{{string}}",
            "Format": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "NumberTargetPartitions": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "PartitionKeys": [
               [ "{{string}}" ]
            ],
            "Path": "{{string}}",
            "SchemaChangePolicy": {
               "Database": "{{string}}",
               "EnableUpdateCatalog": {{boolean}},
               "Table": "{{string}}",
               "UpdateBehavior": "{{string}}"
            }
         },
         "S3JsonSource": {
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}},
               "EnableSamplePath": {{boolean}},
               "SamplePath": "{{string}}"
            },
            "CompressionType": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "GroupFiles": "{{string}}",
            "GroupSize": "{{string}}",
            "JsonPath": "{{string}}",
            "MaxBand": {{number}},
            "MaxFilesInBand": {{number}},
            "Multiline": {{boolean}},
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Paths": [ "{{string}}" ],
            "Recurse": {{boolean}}
         },
         "S3ParquetSource": {
            "AdditionalOptions": {
               "BoundedFiles": {{number}},
               "BoundedSize": {{number}},
               "EnableSamplePath": {{boolean}},
               "SamplePath": "{{string}}"
            },
            "CompressionType": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "GroupFiles": "{{string}}",
            "GroupSize": "{{string}}",
            "MaxBand": {{number}},
            "MaxFilesInBand": {{number}},
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "Paths": [ "{{string}}" ],
            "Recurse": {{boolean}}
         },
         "SelectFields": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Paths": [
               [ "{{string}}" ]
            ]
         },
         "SelectFromCollection": {
            "Index": {{number}},
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "SnowflakeSource": {
            "Data": {
               "Action": "{{string}}",
               "AdditionalOptions": {
                  "{{string}}" : "{{string}}"
               },
               "AutoPushdown": {{boolean}},
               "Connection": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "Database": "{{string}}",
               "IamRole": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "MergeAction": "{{string}}",
               "MergeClause": "{{string}}",
               "MergeWhenMatched": "{{string}}",
               "MergeWhenNotMatched": "{{string}}",
               "PostAction": "{{string}}",
               "PreAction": "{{string}}",
               "SampleQuery": "{{string}}",
               "Schema": "{{string}}",
               "SelectedColumns": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "SourceType": "{{string}}",
               "StagingTable": "{{string}}",
               "Table": "{{string}}",
               "TableSchema": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "TempDir": "{{string}}",
               "Upsert": {{boolean}}
            },
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "SnowflakeTarget": {
            "Data": {
               "Action": "{{string}}",
               "AdditionalOptions": {
                  "{{string}}" : "{{string}}"
               },
               "AutoPushdown": {{boolean}},
               "Connection": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "Database": "{{string}}",
               "IamRole": {
                  "Description": "{{string}}",
                  "Label": "{{string}}",
                  "Value": "{{string}}"
               },
               "MergeAction": "{{string}}",
               "MergeClause": "{{string}}",
               "MergeWhenMatched": "{{string}}",
               "MergeWhenNotMatched": "{{string}}",
               "PostAction": "{{string}}",
               "PreAction": "{{string}}",
               "SampleQuery": "{{string}}",
               "Schema": "{{string}}",
               "SelectedColumns": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "SourceType": "{{string}}",
               "StagingTable": "{{string}}",
               "Table": "{{string}}",
               "TableSchema": [
                  {
                     "Description": "{{string}}",
                     "Label": "{{string}}",
                     "Value": "{{string}}"
                  }
               ],
               "TempDir": "{{string}}",
               "Upsert": {{boolean}}
            },
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}"
         },
         "SparkConnectorSource": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "ConnectionName": "{{string}}",
            "ConnectionType": "{{string}}",
            "ConnectorName": "{{string}}",
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "SparkConnectorTarget": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "ConnectionName": "{{string}}",
            "ConnectionType": "{{string}}",
            "ConnectorName": "{{string}}",
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ]
         },
         "SparkSQL": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "OutputSchemas": [
               {
                  "Columns": [
                     {
                        "GlueStudioType": "{{string}}",
                        "Name": "{{string}}",
                        "Type": "{{string}}"
                     }
                  ]
               }
            ],
            "SqlAliases": [
               {
                  "Alias": "{{string}}",
                  "From": "{{string}}"
               }
            ],
            "SqlQuery": "{{string}}"
         },
         "Spigot": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Path": "{{string}}",
            "Prob": {{number}},
            "Topk": {{number}}
         },
         "SplitFields": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "Paths": [
               [ "{{string}}" ]
            ]
         },
         "Union": {
            "Inputs": [ "{{string}}" ],
            "Name": "{{string}}",
            "UnionType": "{{string}}"
         }
      }
   },
   "Command": {
      "Name": "{{string}}",
      "PythonVersion": "{{string}}",
      "Runtime": "{{string}}",
      "ScriptLocation": "{{string}}"
   },
   "Connections": {
      "Connections": [ "{{string}}" ]
   },
   "DefaultArguments": {
      "{{string}}" : "{{string}}"
   },
   "Description": "{{string}}",
   "ExecutionClass": "{{string}}",
   "ExecutionProperty": {
      "MaxConcurrentRuns": {{number}}
   },
   "GlueVersion": "{{string}}",
   "JobMode": "{{string}}",
   "JobRunQueuingEnabled": {{boolean}},
   "LogUri": "{{string}}",
   "MaintenanceWindow": "{{string}}",
   "MaxCapacity": {{number}},
   "MaxRetries": {{number}},
   "Name": "{{string}}",
   "NonOverridableArguments": {
      "{{string}}" : "{{string}}"
   },
   "NotificationProperty": {
      "NotifyDelayAfter": {{number}}
   },
   "NumberOfWorkers": {{number}},
   "Role": "{{string}}",
   "SecurityConfiguration": "{{string}}",
   "SourceControlDetails": {
      "AuthStrategy": "{{string}}",
      "AuthToken": "{{string}}",
      "Branch": "{{string}}",
      "Folder": "{{string}}",
      "LastCommitId": "{{string}}",
      "Owner": "{{string}}",
      "Provider": "{{string}}",
      "Repository": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Timeout": {{number}},
   "WorkerType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllocatedCapacity](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-AllocatedCapacity"></a>
This parameter is deprecated. Use `MaxCapacity` instead.
The number of AWS Glue data processing units (DPUs) to allocate to this Job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
Type: Integer
Required: No

 ** [CodeGenConfigurationNodes](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-CodeGenConfigurationNodes"></a>
The representation of a directed acyclic graph on which both the Glue Studio visual component and Glue Studio code generation is based.
Type: String to [CodeGenConfigurationNode](API_CodeGenConfigurationNode.md) object map
Key Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** [Command](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Command"></a>
The `JobCommand` that runs this job.
Type: [JobCommand](API_JobCommand.md) object
Required: Yes

 ** [Connections](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Connections"></a>
The connections used for this job.
Type: [ConnectionsList](API_ConnectionsList.md) object
Required: No

 ** [DefaultArguments](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-DefaultArguments"></a>
The default arguments for every run of this job, specified as name-value pairs.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.
For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Spark jobs, see the [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Ray jobs, see [Using job parameters in Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html) in the developer guide.
Type: String to string map
Required: No

 ** [Description](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Description"></a>
Description of the job being defined.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [ExecutionClass](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-ExecutionClass"></a>
Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.
The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.
Only jobs with AWS Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX`. The flexible execution class is available for Spark jobs.
Type: String
Length Constraints: Maximum length of 16.
Valid Values: `FLEX | STANDARD`
Required: No

 ** [ExecutionProperty](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-ExecutionProperty"></a>
An `ExecutionProperty` specifying the maximum number of concurrent runs allowed for this job.
Type: [ExecutionProperty](API_ExecutionProperty.md) object
Required: No

 ** [GlueVersion](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-GlueVersion"></a>
In Spark jobs, `GlueVersion` determines the versions of Apache Spark and Python that AWS Glue available in a job. The Python version indicates the version supported for jobs of type Spark.
Ray jobs should set `GlueVersion` to `4.0` or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the `Runtime` parameter of the Job command.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 5.1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** [JobMode](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-JobMode"></a>
A mode that describes how a job was created. Valid values are:
+  `SCRIPT` - The job was created using the AWS Glue Studio script editor.
+  `VISUAL` - The job was created using the AWS Glue Studio visual editor.
+  `NOTEBOOK` - The job was created using an interactive sessions notebook.
When the `JobMode` field is missing or null, `SCRIPT` is assigned as the default value.
Type: String
Valid Values: `SCRIPT | VISUAL | NOTEBOOK`
Required: No

 ** [JobRunQueuingEnabled](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-JobRunQueuingEnabled"></a>
Specifies whether job run queuing is enabled for the job runs for this job.
A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be considered for queueing.
If this field does not match the value set in the job run, then the value from the job run field will be used.
Type: Boolean
Required: No

 ** [LogUri](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-LogUri"></a>
This field is reserved for future use.
Type: String
Required: No

 ** [MaintenanceWindow](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-MaintenanceWindow"></a>
This field specifies a day of the week and hour for a maintenance window for streaming jobs. AWS Glue periodically performs maintenance activities. During these maintenance windows, AWS Glue will need to restart your streaming jobs.
 AWS Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.
Type: String
Pattern: `^(Sun|Mon|Tue|Wed|Thu|Fri|Sat):([01]?[0-9]|2[0-3])$`
Required: No

 ** [MaxCapacity](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-MaxCapacity"></a>
For Glue version 1.0 or earlier jobs, using the standard worker type, the number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
For Glue version 2.0\+ jobs, you cannot specify a `Maximum capacity`. Instead, you should specify a `Worker type` and the `Number of workers`.
Do not set `MaxCapacity` if using `WorkerType` and `NumberOfWorkers`.
The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:
+ When you specify a Python shell job (`JobCommand.Name`="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
+ When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl") or Apache Spark streaming ETL job (`JobCommand.Name`="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
Type: Double
Required: No

 ** [MaxRetries](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-MaxRetries"></a>
The maximum number of times to retry this job if it fails.
Type: Integer
Required: No

 ** [Name](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Name"></a>
The name you assign to this job definition. It must be unique in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [NonOverridableArguments](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-NonOverridableArguments"></a>
Arguments for this job that are not overridden when providing job arguments in a job run, specified as name-value pairs.
Type: String to string map
Required: No

 ** [NotificationProperty](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-NotificationProperty"></a>
Specifies configuration properties of a job notification.
Type: [NotificationProperty](API_NotificationProperty.md) object
Required: No

 ** [NumberOfWorkers](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when a job runs.
Type: Integer
Required: No

 ** [Role](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Role"></a>
The name or Amazon Resource Name (ARN) of the IAM role associated with this job.
Type: String
Required: Yes

 ** [SecurityConfiguration](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [SourceControlDetails](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-SourceControlDetails"></a>
The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository.
Type: [SourceControlDetails](API_SourceControlDetails.md) object
Required: No

 ** [Tags](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Tags"></a>
The tags to use with this job. You may use tags to limit access to the job. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Timeout](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-Timeout"></a>
The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status.
Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.
When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.
Any existing AWS Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.
For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [WorkerType](#API_CreateJob_RequestSyntax) **   <a name="Glue-CreateJob-request-WorkerType"></a>
The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.
+ For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
+ For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
+ For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Spain), Europe (Stockholm), and South America (São Paulo).
+ For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS Regions as supported for the `G.4X` worker type.
+ For the `G.025X` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for AWS Glue version 3.0 or later streaming jobs.
+ For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## Response Syntax
<a name="API_CreateJob_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateJob_ResponseSyntax) **   <a name="Glue-CreateJob-response-Name"></a>
The unique name that was provided for this job definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateJob)

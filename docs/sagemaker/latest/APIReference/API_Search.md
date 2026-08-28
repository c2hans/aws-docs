---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html
---

# Search
<a name="API_Search"></a>

Finds SageMaker resources that match a search query. Matching resources are returned as a list of `SearchRecord` objects in the response. You can sort the search results by any resource property in a ascending or descending order.

You can query against the following value types: numeric, text, Boolean, and timestamp.

**Note**
The Search API may provide access to otherwise restricted data. See [Amazon SageMaker API Permissions: Actions, Permissions, and Resources Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html) for more information.

## Request Syntax
<a name="API_Search_RequestSyntax"></a>

```
{
   "CrossAccountFilterOption": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Resource": "{{string}}",
   "SearchExpression": {
      "Filters": [
         {
            "Name": "{{string}}",
            "Operator": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NestedFilters": [
         {
            "Filters": [
               {
                  "Name": "{{string}}",
                  "Operator": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "NestedPropertyName": "{{string}}"
         }
      ],
      "Operator": "{{string}}",
      "SubExpressions": [
         "SearchExpression"
      ]
   },
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "VisibilityConditions": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_Search_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CrossAccountFilterOption](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-CrossAccountFilterOption"></a>
 A cross account filter option. When the value is `"CrossAccount"` the search results will only include resources made discoverable to you from other accounts. When the value is `"SameAccount"` or `null` the search results will only include resources from your account. Default is `null`. For more information on searching for resources made discoverable to your account, see [ Search discoverable resources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-discoverability-use.html) in the SageMaker Developer Guide. The maximum number of `ResourceCatalog`s viewable is 1000.
Type: String
Valid Values: `SameAccount | CrossAccount`
Required: No

 ** [MaxResults](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-NextToken"></a>
If more than `MaxResults` resources match the specified `SearchExpression`, the response includes a `NextToken`. The `NextToken` can be passed to the next `SearchRequest` to continue retrieving results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [Resource](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-Resource"></a>
The name of the SageMaker resource to search for.
Type: String
Valid Values: `TrainingJob | Experiment | ExperimentTrial | ExperimentTrialComponent | Endpoint | Model | ModelPackage | ModelPackageGroup | Pipeline | PipelineExecution | FeatureGroup | FeatureMetadata | Image | ImageVersion | Project | HyperParameterTuningJob | ModelCard | PipelineVersion | Job`
Required: Yes

 ** [SearchExpression](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-SearchExpression"></a>
A Boolean conditional statement. Resources must satisfy this condition to be included in search results. You must provide at least one subexpression, filter, or nested filter. The maximum number of recursive `SubExpressions`, `NestedFilters`, and `Filters` that can be included in a `SearchExpression` object is 50.
Type: [SearchExpression](API_SearchExpression.md) object
Required: No

 ** [SortBy](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-SortBy"></a>
The name of the resource property used to sort the `SearchResults`. The default is `LastModifiedTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: No

 ** [SortOrder](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-SortOrder"></a>
How `SearchResults` are ordered. Valid values are `Ascending` or `Descending`. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [VisibilityConditions](#API_Search_RequestSyntax) **   <a name="sagemaker-Search-request-VisibilityConditions"></a>
 Limits the results of your search request to the resources that you can access.
Type: Array of [VisibilityConditions](API_VisibilityConditions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_Search_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Results": [
      {
         "Endpoint": {
            "CreationTime": number,
            "DataCaptureConfig": {
               "CaptureStatus": "string",
               "CurrentSamplingPercentage": number,
               "DestinationS3Uri": "string",
               "EnableCapture": boolean,
               "KmsKeyId": "string"
            },
            "EndpointArn": "string",
            "EndpointConfigName": "string",
            "EndpointName": "string",
            "EndpointStatus": "string",
            "FailureReason": "string",
            "LastModifiedTime": number,
            "MonitoringSchedules": [
               {
                  "CreationTime": number,
                  "EndpointName": "string",
                  "FailureReason": "string",
                  "LastModifiedTime": number,
                  "LastMonitoringExecutionSummary": {
                     "CreationTime": number,
                     "EndpointName": "string",
                     "FailureReason": "string",
                     "LastModifiedTime": number,
                     "MonitoringExecutionStatus": "string",
                     "MonitoringJobDefinitionName": "string",
                     "MonitoringScheduleName": "string",
                     "MonitoringType": "string",
                     "ProcessingJobArn": "string",
                     "ScheduledTime": number
                  },
                  "MonitoringScheduleArn": "string",
                  "MonitoringScheduleConfig": {
                     "MonitoringJobDefinition": {
                        "BaselineConfig": {
                           "BaseliningJobName": "string",
                           "ConstraintsResource": {
                              "S3Uri": "string"
                           },
                           "StatisticsResource": {
                              "S3Uri": "string"
                           }
                        },
                        "Environment": {
                           "string" : "string"
                        },
                        "MonitoringAppSpecification": {
                           "ContainerArguments": [ "string" ],
                           "ContainerEntrypoint": [ "string" ],
                           "ImageUri": "string",
                           "PostAnalyticsProcessorSourceUri": "string",
                           "RecordPreprocessorSourceUri": "string"
                        },
                        "MonitoringInputs": [
                           {
                              "BatchTransformInput": {
                                 "DataCapturedDestinationS3Uri": "string",
                                 "DatasetFormat": {
                                    "Csv": {
                                       "Header": boolean
                                    },
                                    "Json": {
                                       "Line": boolean
                                    },
                                    "Parquet": {
                                    }
                                 },
                                 "EndTimeOffset": "string",
                                 "ExcludeFeaturesAttribute": "string",
                                 "FeaturesAttribute": "string",
                                 "InferenceAttribute": "string",
                                 "LocalPath": "string",
                                 "ProbabilityAttribute": "string",
                                 "ProbabilityThresholdAttribute": number,
                                 "S3DataDistributionType": "string",
                                 "S3InputMode": "string",
                                 "StartTimeOffset": "string"
                              },
                              "EndpointInput": {
                                 "EndpointName": "string",
                                 "EndTimeOffset": "string",
                                 "ExcludeFeaturesAttribute": "string",
                                 "FeaturesAttribute": "string",
                                 "InferenceAttribute": "string",
                                 "LocalPath": "string",
                                 "ProbabilityAttribute": "string",
                                 "ProbabilityThresholdAttribute": number,
                                 "S3DataDistributionType": "string",
                                 "S3InputMode": "string",
                                 "StartTimeOffset": "string"
                              }
                           }
                        ],
                        "MonitoringOutputConfig": {
                           "KmsKeyId": "string",
                           "MonitoringOutputs": [
                              {
                                 "S3Output": {
                                    "LocalPath": "string",
                                    "S3UploadMode": "string",
                                    "S3Uri": "string"
                                 }
                              }
                           ]
                        },
                        "MonitoringResources": {
                           "ClusterConfig": {
                              "InstanceCount": number,
                              "InstanceType": "string",
                              "VolumeKmsKeyId": "string",
                              "VolumeSizeInGB": number
                           }
                        },
                        "NetworkConfig": {
                           "EnableInterContainerTrafficEncryption": boolean,
                           "EnableNetworkIsolation": boolean,
                           "VpcConfig": {
                              "SecurityGroupIds": [ "string" ],
                              "Subnets": [ "string" ]
                           }
                        },
                        "RoleArn": "string",
                        "StoppingCondition": {
                           "MaxRuntimeInSeconds": number
                        }
                     },
                     "MonitoringJobDefinitionName": "string",
                     "MonitoringType": "string",
                     "ScheduleConfig": {
                        "DataAnalysisEndTime": "string",
                        "DataAnalysisStartTime": "string",
                        "ScheduleExpression": "string"
                     }
                  },
                  "MonitoringScheduleName": "string",
                  "MonitoringScheduleStatus": "string",
                  "MonitoringType": "string",
                  "Tags": [
                     {
                        "Key": "string",
                        "Value": "string"
                     }
                  ]
               }
            ],
            "ProductionVariants": [
               {
                  "CapacityReservationConfig": {
                     "AvailableInstanceCount": number,
                     "CapacityReservationPreference": "string",
                     "Ec2CapacityReservations": [
                        {
                           "AvailableInstanceCount": number,
                           "Ec2CapacityReservationId": "string",
                           "TotalInstanceCount": number,
                           "UsedByCurrentEndpoint": number
                        }
                     ],
                     "MlReservationArn": "string",
                     "TotalInstanceCount": number,
                     "UsedByCurrentEndpoint": number
                  },
                  "CurrentInstanceCount": number,
                  "CurrentServerlessConfig": {
                     "MaxConcurrency": number,
                     "MemorySizeInMB": number,
                     "ProvisionedConcurrency": number
                  },
                  "CurrentWeight": number,
                  "DeployedImages": [
                     {
                        "ResolutionTime": number,
                        "ResolvedImage": "string",
                        "SpecifiedImage": "string"
                     }
                  ],
                  "DesiredInstanceCount": number,
                  "DesiredServerlessConfig": {
                     "MaxConcurrency": number,
                     "MemorySizeInMB": number,
                     "ProvisionedConcurrency": number
                  },
                  "DesiredWeight": number,
                  "InstancePools": [
                     {
                        "CurrentInstanceCount": number,
                        "InstanceType": "string"
                     }
                  ],
                  "ManagedInstanceScaling": {
                     "MaxInstanceCount": number,
                     "MinInstanceCount": number,
                     "ScaleInPolicy": {
                        "CooldownInMinutes": number,
                        "MaximumStepSize": number,
                        "Strategy": "string"
                     },
                     "Status": "string"
                  },
                  "RoutingConfig": {
                     "PrefixAwareRoutingConfig": {
                        "ConcurrencyThreshold": number,
                        "PrefixLength": number
                     },
                     "RoutingStrategy": "string"
                  },
                  "VariantName": "string",
                  "VariantStatus": [
                     {
                        "StartTime": number,
                        "Status": "string",
                        "StatusMessage": "string"
                     }
                  ]
               }
            ],
            "ShadowProductionVariants": [
               {
                  "CapacityReservationConfig": {
                     "AvailableInstanceCount": number,
                     "CapacityReservationPreference": "string",
                     "Ec2CapacityReservations": [
                        {
                           "AvailableInstanceCount": number,
                           "Ec2CapacityReservationId": "string",
                           "TotalInstanceCount": number,
                           "UsedByCurrentEndpoint": number
                        }
                     ],
                     "MlReservationArn": "string",
                     "TotalInstanceCount": number,
                     "UsedByCurrentEndpoint": number
                  },
                  "CurrentInstanceCount": number,
                  "CurrentServerlessConfig": {
                     "MaxConcurrency": number,
                     "MemorySizeInMB": number,
                     "ProvisionedConcurrency": number
                  },
                  "CurrentWeight": number,
                  "DeployedImages": [
                     {
                        "ResolutionTime": number,
                        "ResolvedImage": "string",
                        "SpecifiedImage": "string"
                     }
                  ],
                  "DesiredInstanceCount": number,
                  "DesiredServerlessConfig": {
                     "MaxConcurrency": number,
                     "MemorySizeInMB": number,
                     "ProvisionedConcurrency": number
                  },
                  "DesiredWeight": number,
                  "InstancePools": [
                     {
                        "CurrentInstanceCount": number,
                        "InstanceType": "string"
                     }
                  ],
                  "ManagedInstanceScaling": {
                     "MaxInstanceCount": number,
                     "MinInstanceCount": number,
                     "ScaleInPolicy": {
                        "CooldownInMinutes": number,
                        "MaximumStepSize": number,
                        "Strategy": "string"
                     },
                     "Status": "string"
                  },
                  "RoutingConfig": {
                     "PrefixAwareRoutingConfig": {
                        "ConcurrencyThreshold": number,
                        "PrefixLength": number
                     },
                     "RoutingStrategy": "string"
                  },
                  "VariantName": "string",
                  "VariantStatus": [
                     {
                        "StartTime": number,
                        "Status": "string",
                        "StatusMessage": "string"
                     }
                  ]
               }
            ],
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "Experiment": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "Description": "string",
            "DisplayName": "string",
            "ExperimentArn": "string",
            "ExperimentName": "string",
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "Source": {
               "SourceArn": "string",
               "SourceType": "string"
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "FeatureGroup": {
            "CreationTime": number,
            "Description": "string",
            "EventTimeFeatureName": "string",
            "FailureReason": "string",
            "FeatureDefinitions": [
               {
                  "CollectionConfig": { ... },
                  "CollectionType": "string",
                  "FeatureName": "string",
                  "FeatureType": "string"
               }
            ],
            "FeatureGroupArn": "string",
            "FeatureGroupName": "string",
            "FeatureGroupStatus": "string",
            "LastModifiedTime": number,
            "LastUpdateStatus": {
               "FailureReason": "string",
               "Status": "string"
            },
            "OfflineStoreConfig": {
               "DataCatalogConfig": {
                  "Catalog": "string",
                  "Database": "string",
                  "TableName": "string"
               },
               "DisableGlueTableCreation": boolean,
               "S3StorageConfig": {
                  "KmsKeyId": "string",
                  "ResolvedOutputS3Uri": "string",
                  "S3Uri": "string"
               },
               "TableFormat": "string"
            },
            "OfflineStoreStatus": {
               "BlockedReason": "string",
               "Status": "string"
            },
            "OnlineStoreConfig": {
               "EnableOnlineStore": boolean,
               "SecurityConfig": {
                  "KmsKeyId": "string"
               },
               "StorageType": "string",
               "TtlDuration": {
                  "Unit": "string",
                  "Value": number
               }
            },
            "RecordIdentifierFeatureName": "string",
            "RoleArn": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "FeatureMetadata": {
            "CreationTime": number,
            "Description": "string",
            "FeatureGroupArn": "string",
            "FeatureGroupName": "string",
            "FeatureName": "string",
            "FeatureType": "string",
            "LastModifiedTime": number,
            "Parameters": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "HyperParameterTuningJob": {
            "BestTrainingJob": {
               "CreationTime": number,
               "FailureReason": "string",
               "FinalHyperParameterTuningJobObjectiveMetric": {
                  "MetricName": "string",
                  "Type": "string",
                  "Value": number
               },
               "ObjectiveStatus": "string",
               "TrainingEndTime": number,
               "TrainingJobArn": "string",
               "TrainingJobDefinitionName": "string",
               "TrainingJobName": "string",
               "TrainingJobStatus": "string",
               "TrainingStartTime": number,
               "TunedHyperParameters": {
                  "string" : "string"
               },
               "TuningJobName": "string"
            },
            "ConsumedResources": {
               "RuntimeInSeconds": number
            },
            "CreationTime": number,
            "FailureReason": "string",
            "HyperParameterTuningEndTime": number,
            "HyperParameterTuningJobArn": "string",
            "HyperParameterTuningJobConfig": {
               "HyperParameterTuningJobObjective": {
                  "MetricName": "string",
                  "Type": "string"
               },
               "ParameterRanges": {
                  "AutoParameters": [
                     {
                        "Name": "string",
                        "ValueHint": "string"
                     }
                  ],
                  "CategoricalParameterRanges": [
                     {
                        "Name": "string",
                        "Values": [ "string" ]
                     }
                  ],
                  "ContinuousParameterRanges": [
                     {
                        "MaxValue": "string",
                        "MinValue": "string",
                        "Name": "string",
                        "ScalingType": "string"
                     }
                  ],
                  "IntegerParameterRanges": [
                     {
                        "MaxValue": "string",
                        "MinValue": "string",
                        "Name": "string",
                        "ScalingType": "string"
                     }
                  ]
               },
               "RandomSeed": number,
               "ResourceLimits": {
                  "MaxNumberOfTrainingJobs": number,
                  "MaxParallelTrainingJobs": number,
                  "MaxRuntimeInSeconds": number
               },
               "Strategy": "string",
               "StrategyConfig": {
                  "HyperbandStrategyConfig": {
                     "MaxResource": number,
                     "MinResource": number
                  }
               },
               "TrainingJobEarlyStoppingType": "string",
               "TuningJobCompletionCriteria": {
                  "BestObjectiveNotImproving": {
                     "MaxNumberOfTrainingJobsNotImproving": number
                  },
                  "ConvergenceDetected": {
                     "CompleteOnConvergence": "string"
                  },
                  "TargetObjectiveMetricValue": number
               }
            },
            "HyperParameterTuningJobName": "string",
            "HyperParameterTuningJobStatus": "string",
            "LastModifiedTime": number,
            "ObjectiveStatusCounters": {
               "Failed": number,
               "Pending": number,
               "Succeeded": number
            },
            "OverallBestTrainingJob": {
               "CreationTime": number,
               "FailureReason": "string",
               "FinalHyperParameterTuningJobObjectiveMetric": {
                  "MetricName": "string",
                  "Type": "string",
                  "Value": number
               },
               "ObjectiveStatus": "string",
               "TrainingEndTime": number,
               "TrainingJobArn": "string",
               "TrainingJobDefinitionName": "string",
               "TrainingJobName": "string",
               "TrainingJobStatus": "string",
               "TrainingStartTime": number,
               "TunedHyperParameters": {
                  "string" : "string"
               },
               "TuningJobName": "string"
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "TrainingJobDefinition": {
               "AlgorithmSpecification": {
                  "AlgorithmName": "string",
                  "MetricDefinitions": [
                     {
                        "Name": "string",
                        "Regex": "string"
                     }
                  ],
                  "TrainingImage": "string",
                  "TrainingInputMode": "string"
               },
               "CheckpointConfig": {
                  "LocalPath": "string",
                  "S3Uri": "string"
               },
               "DefinitionName": "string",
               "EnableInterContainerTrafficEncryption": boolean,
               "EnableManagedSpotTraining": boolean,
               "EnableNetworkIsolation": boolean,
               "Environment": {
                  "string" : "string"
               },
               "HyperParameterRanges": {
                  "AutoParameters": [
                     {
                        "Name": "string",
                        "ValueHint": "string"
                     }
                  ],
                  "CategoricalParameterRanges": [
                     {
                        "Name": "string",
                        "Values": [ "string" ]
                     }
                  ],
                  "ContinuousParameterRanges": [
                     {
                        "MaxValue": "string",
                        "MinValue": "string",
                        "Name": "string",
                        "ScalingType": "string"
                     }
                  ],
                  "IntegerParameterRanges": [
                     {
                        "MaxValue": "string",
                        "MinValue": "string",
                        "Name": "string",
                        "ScalingType": "string"
                     }
                  ]
               },
               "HyperParameterTuningResourceConfig": {
                  "AllocationStrategy": "string",
                  "InstanceConfigs": [
                     {
                        "InstanceCount": number,
                        "InstanceType": "string",
                        "VolumeSizeInGB": number
                     }
                  ],
                  "InstanceCount": number,
                  "InstanceType": "string",
                  "VolumeKmsKeyId": "string",
                  "VolumeSizeInGB": number
               },
               "InputDataConfig": [
                  {
                     "ChannelName": "string",
                     "CompressionType": "string",
                     "ContentType": "string",
                     "DataSource": {
                        "DatasetSource": {
                           "DatasetArn": "string"
                        },
                        "FileSystemDataSource": {
                           "DirectoryPath": "string",
                           "FileSystemAccessMode": "string",
                           "FileSystemId": "string",
                           "FileSystemType": "string"
                        },
                        "S3DataSource": {
                           "AttributeNames": [ "string" ],
                           "HubAccessConfig": {
                              "HubContentArn": "string"
                           },
                           "InstanceGroupNames": [ "string" ],
                           "ModelAccessConfig": {
                              "AcceptEula": boolean
                           },
                           "S3DataDistributionType": "string",
                           "S3DataType": "string",
                           "S3Uri": "string"
                        }
                     },
                     "InputMode": "string",
                     "RecordWrapperType": "string",
                     "ShuffleConfig": {
                        "Seed": number
                     }
                  }
               ],
               "OutputDataConfig": {
                  "CompressionType": "string",
                  "KmsKeyId": "string",
                  "S3OutputPath": "string"
               },
               "ResourceConfig": {
                  "InstanceCount": number,
                  "InstanceGroups": [
                     {
                        "InstanceCount": number,
                        "InstanceGroupName": "string",
                        "InstanceType": "string"
                     }
                  ],
                  "InstancePlacementConfig": {
                     "EnableMultipleJobs": boolean,
                     "PlacementSpecifications": [
                        {
                           "InstanceCount": number,
                           "UltraServerId": "string"
                        }
                     ]
                  },
                  "InstanceType": "string",
                  "KeepAlivePeriodInSeconds": number,
                  "TrainingPlanArn": "string",
                  "VolumeKmsKeyId": "string",
                  "VolumeSizeInGB": number
               },
               "RetryStrategy": {
                  "MaximumRetryAttempts": number
               },
               "RoleArn": "string",
               "StaticHyperParameters": {
                  "string" : "string"
               },
               "StoppingCondition": {
                  "MaxPendingTimeInSeconds": number,
                  "MaxRuntimeInSeconds": number,
                  "MaxWaitTimeInSeconds": number
               },
               "TuningObjective": {
                  "MetricName": "string",
                  "Type": "string"
               },
               "VpcConfig": {
                  "SecurityGroupIds": [ "string" ],
                  "Subnets": [ "string" ]
               }
            },
            "TrainingJobDefinitions": [
               {
                  "AlgorithmSpecification": {
                     "AlgorithmName": "string",
                     "MetricDefinitions": [
                        {
                           "Name": "string",
                           "Regex": "string"
                        }
                     ],
                     "TrainingImage": "string",
                     "TrainingInputMode": "string"
                  },
                  "CheckpointConfig": {
                     "LocalPath": "string",
                     "S3Uri": "string"
                  },
                  "DefinitionName": "string",
                  "EnableInterContainerTrafficEncryption": boolean,
                  "EnableManagedSpotTraining": boolean,
                  "EnableNetworkIsolation": boolean,
                  "Environment": {
                     "string" : "string"
                  },
                  "HyperParameterRanges": {
                     "AutoParameters": [
                        {
                           "Name": "string",
                           "ValueHint": "string"
                        }
                     ],
                     "CategoricalParameterRanges": [
                        {
                           "Name": "string",
                           "Values": [ "string" ]
                        }
                     ],
                     "ContinuousParameterRanges": [
                        {
                           "MaxValue": "string",
                           "MinValue": "string",
                           "Name": "string",
                           "ScalingType": "string"
                        }
                     ],
                     "IntegerParameterRanges": [
                        {
                           "MaxValue": "string",
                           "MinValue": "string",
                           "Name": "string",
                           "ScalingType": "string"
                        }
                     ]
                  },
                  "HyperParameterTuningResourceConfig": {
                     "AllocationStrategy": "string",
                     "InstanceConfigs": [
                        {
                           "InstanceCount": number,
                           "InstanceType": "string",
                           "VolumeSizeInGB": number
                        }
                     ],
                     "InstanceCount": number,
                     "InstanceType": "string",
                     "VolumeKmsKeyId": "string",
                     "VolumeSizeInGB": number
                  },
                  "InputDataConfig": [
                     {
                        "ChannelName": "string",
                        "CompressionType": "string",
                        "ContentType": "string",
                        "DataSource": {
                           "DatasetSource": {
                              "DatasetArn": "string"
                           },
                           "FileSystemDataSource": {
                              "DirectoryPath": "string",
                              "FileSystemAccessMode": "string",
                              "FileSystemId": "string",
                              "FileSystemType": "string"
                           },
                           "S3DataSource": {
                              "AttributeNames": [ "string" ],
                              "HubAccessConfig": {
                                 "HubContentArn": "string"
                              },
                              "InstanceGroupNames": [ "string" ],
                              "ModelAccessConfig": {
                                 "AcceptEula": boolean
                              },
                              "S3DataDistributionType": "string",
                              "S3DataType": "string",
                              "S3Uri": "string"
                           }
                        },
                        "InputMode": "string",
                        "RecordWrapperType": "string",
                        "ShuffleConfig": {
                           "Seed": number
                        }
                     }
                  ],
                  "OutputDataConfig": {
                     "CompressionType": "string",
                     "KmsKeyId": "string",
                     "S3OutputPath": "string"
                  },
                  "ResourceConfig": {
                     "InstanceCount": number,
                     "InstanceGroups": [
                        {
                           "InstanceCount": number,
                           "InstanceGroupName": "string",
                           "InstanceType": "string"
                        }
                     ],
                     "InstancePlacementConfig": {
                        "EnableMultipleJobs": boolean,
                        "PlacementSpecifications": [
                           {
                              "InstanceCount": number,
                              "UltraServerId": "string"
                           }
                        ]
                     },
                     "InstanceType": "string",
                     "KeepAlivePeriodInSeconds": number,
                     "TrainingPlanArn": "string",
                     "VolumeKmsKeyId": "string",
                     "VolumeSizeInGB": number
                  },
                  "RetryStrategy": {
                     "MaximumRetryAttempts": number
                  },
                  "RoleArn": "string",
                  "StaticHyperParameters": {
                     "string" : "string"
                  },
                  "StoppingCondition": {
                     "MaxPendingTimeInSeconds": number,
                     "MaxRuntimeInSeconds": number,
                     "MaxWaitTimeInSeconds": number
                  },
                  "TuningObjective": {
                     "MetricName": "string",
                     "Type": "string"
                  },
                  "VpcConfig": {
                     "SecurityGroupIds": [ "string" ],
                     "Subnets": [ "string" ]
                  }
               }
            ],
            "TrainingJobStatusCounters": {
               "Completed": number,
               "InProgress": number,
               "NonRetryableError": number,
               "RetryableError": number,
               "Stopped": number
            },
            "TuningJobCompletionDetails": {
               "ConvergenceDetectedTime": number,
               "NumberOfTrainingJobsObjectiveNotImproving": number
            },
            "WarmStartConfig": {
               "ParentHyperParameterTuningJobs": [
                  {
                     "HyperParameterTuningJobName": "string"
                  }
               ],
               "WarmStartType": "string"
            }
         },
         "Job": {
            "CreationTime": number,
            "EndTime": number,
            "FailureReason": "string",
            "JobArn": "string",
            "JobCategory": "string",
            "JobConfigDocument": "string",
            "JobConfigSchemaVersion": "string",
            "JobName": "string",
            "JobStatus": "string",
            "LastModifiedTime": number,
            "RoleArn": "string",
            "SecondaryStatus": "string",
            "SecondaryStatusTransitions": [
               {
                  "EndTime": number,
                  "StartTime": number,
                  "Status": "string",
                  "StatusMessage": "string"
               }
            ],
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "Model": {
            "Endpoints": [
               {
                  "CreationTime": number,
                  "EndpointArn": "string",
                  "EndpointName": "string",
                  "EndpointStatus": "string",
                  "LastModifiedTime": number
               }
            ],
            "LastBatchTransformJob": {
               "AutoMLJobArn": "string",
               "BatchStrategy": "string",
               "CreationTime": number,
               "DataCaptureConfig": {
                  "DestinationS3Uri": "string",
                  "GenerateInferenceId": boolean,
                  "KmsKeyId": "string"
               },
               "DataProcessing": {
                  "InputFilter": "string",
                  "JoinSource": "string",
                  "OutputFilter": "string"
               },
               "Environment": {
                  "string" : "string"
               },
               "ExperimentConfig": {
                  "ExperimentName": "string",
                  "RunName": "string",
                  "TrialComponentDisplayName": "string",
                  "TrialName": "string"
               },
               "FailureReason": "string",
               "LabelingJobArn": "string",
               "MaxConcurrentTransforms": number,
               "MaxPayloadInMB": number,
               "ModelClientConfig": {
                  "InvocationsMaxRetries": number,
                  "InvocationsTimeoutInSeconds": number
               },
               "ModelName": "string",
               "Tags": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ],
               "TransformEndTime": number,
               "TransformInput": {
                  "CompressionType": "string",
                  "ContentType": "string",
                  "DataSource": {
                     "S3DataSource": {
                        "S3DataType": "string",
                        "S3Uri": "string"
                     }
                  },
                  "SplitType": "string"
               },
               "TransformJobArn": "string",
               "TransformJobName": "string",
               "TransformJobStatus": "string",
               "TransformOutput": {
                  "Accept": "string",
                  "AssembleWith": "string",
                  "KmsKeyId": "string",
                  "S3OutputPath": "string"
               },
               "TransformResources": {
                  "InstanceCount": number,
                  "InstanceType": "string",
                  "TransformAmiVersion": "string",
                  "VolumeKmsKeyId": "string"
               },
               "TransformStartTime": number
            },
            "Model": {
               "Containers": [
                  {
                     "AdditionalModelDataSources": [
                        {
                           "ChannelName": "string",
                           "S3DataSource": {
                              "CompressionType": "string",
                              "ETag": "string",
                              "HubAccessConfig": {
                                 "HubContentArn": "string"
                              },
                              "ManifestEtag": "string",
                              "ManifestS3Uri": "string",
                              "ModelAccessConfig": {
                                 "AcceptEula": boolean
                              },
                              "S3DataType": "string",
                              "S3Uri": "string"
                           }
                        }
                     ],
                     "ContainerHostname": "string",
                     "ContainerMetricsConfig": {
                        "MetricsEndpoints": [
                           {
                              "MetricPublishFrequencyInSeconds": number,
                              "MetricsEndpointPath": "string"
                           }
                        ]
                     },
                     "Environment": {
                        "string" : "string"
                     },
                     "Image": "string",
                     "ImageConfig": {
                        "RepositoryAccessMode": "string",
                        "RepositoryAuthConfig": {
                           "RepositoryCredentialsProviderArn": "string"
                        }
                     },
                     "InferenceSpecificationName": "string",
                     "Mode": "string",
                     "ModelDataSource": {
                        "S3DataSource": {
                           "CompressionType": "string",
                           "ETag": "string",
                           "HubAccessConfig": {
                              "HubContentArn": "string"
                           },
                           "ManifestEtag": "string",
                           "ManifestS3Uri": "string",
                           "ModelAccessConfig": {
                              "AcceptEula": boolean
                           },
                           "S3DataType": "string",
                           "S3Uri": "string"
                        }
                     },
                     "ModelDataUrl": "string",
                     "ModelPackageName": "string",
                     "MultiModelConfig": {
                        "ModelCacheSetting": "string"
                     }
                  }
               ],
               "CreationTime": number,
               "DeploymentRecommendation": {
                  "RealTimeInferenceRecommendations": [
                     {
                        "Environment": {
                           "string" : "string"
                        },
                        "InstanceType": "string",
                        "RecommendationId": "string"
                     }
                  ],
                  "RecommendationStatus": "string"
               },
               "EnableNetworkIsolation": boolean,
               "ExecutionRoleArn": "string",
               "InferenceExecutionConfig": {
                  "Mode": "string"
               },
               "ModelArn": "string",
               "ModelName": "string",
               "PrimaryContainer": {
                  "AdditionalModelDataSources": [
                     {
                        "ChannelName": "string",
                        "S3DataSource": {
                           "CompressionType": "string",
                           "ETag": "string",
                           "HubAccessConfig": {
                              "HubContentArn": "string"
                           },
                           "ManifestEtag": "string",
                           "ManifestS3Uri": "string",
                           "ModelAccessConfig": {
                              "AcceptEula": boolean
                           },
                           "S3DataType": "string",
                           "S3Uri": "string"
                        }
                     }
                  ],
                  "ContainerHostname": "string",
                  "ContainerMetricsConfig": {
                     "MetricsEndpoints": [
                        {
                           "MetricPublishFrequencyInSeconds": number,
                           "MetricsEndpointPath": "string"
                        }
                     ]
                  },
                  "Environment": {
                     "string" : "string"
                  },
                  "Image": "string",
                  "ImageConfig": {
                     "RepositoryAccessMode": "string",
                     "RepositoryAuthConfig": {
                        "RepositoryCredentialsProviderArn": "string"
                     }
                  },
                  "InferenceSpecificationName": "string",
                  "Mode": "string",
                  "ModelDataSource": {
                     "S3DataSource": {
                        "CompressionType": "string",
                        "ETag": "string",
                        "HubAccessConfig": {
                           "HubContentArn": "string"
                        },
                        "ManifestEtag": "string",
                        "ManifestS3Uri": "string",
                        "ModelAccessConfig": {
                           "AcceptEula": boolean
                        },
                        "S3DataType": "string",
                        "S3Uri": "string"
                     }
                  },
                  "ModelDataUrl": "string",
                  "ModelPackageName": "string",
                  "MultiModelConfig": {
                     "ModelCacheSetting": "string"
                  }
               },
               "Tags": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ],
               "VpcConfig": {
                  "SecurityGroupIds": [ "string" ],
                  "Subnets": [ "string" ]
               }
            },
            "ModelCard": {
               "CreatedBy": {
                  "DomainId": "string",
                  "IamIdentity": {
                     "Arn": "string",
                     "PrincipalId": "string",
                     "SourceIdentity": "string"
                  },
                  "UserProfileArn": "string",
                  "UserProfileName": "string"
               },
               "CreationTime": number,
               "LastModifiedBy": {
                  "DomainId": "string",
                  "IamIdentity": {
                     "Arn": "string",
                     "PrincipalId": "string",
                     "SourceIdentity": "string"
                  },
                  "UserProfileArn": "string",
                  "UserProfileName": "string"
               },
               "LastModifiedTime": number,
               "ModelCardArn": "string",
               "ModelCardName": "string",
               "ModelCardStatus": "string",
               "ModelCardVersion": number,
               "ModelId": "string",
               "RiskRating": "string",
               "SecurityConfig": {
                  "KmsKeyId": "string"
               },
               "Tags": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ]
            },
            "MonitoringSchedules": [
               {
                  "BatchTransformInput": {
                     "DataCapturedDestinationS3Uri": "string",
                     "DatasetFormat": {
                        "Csv": {
                           "Header": boolean
                        },
                        "Json": {
                           "Line": boolean
                        },
                        "Parquet": {
                        }
                     },
                     "EndTimeOffset": "string",
                     "ExcludeFeaturesAttribute": "string",
                     "FeaturesAttribute": "string",
                     "InferenceAttribute": "string",
                     "LocalPath": "string",
                     "ProbabilityAttribute": "string",
                     "ProbabilityThresholdAttribute": number,
                     "S3DataDistributionType": "string",
                     "S3InputMode": "string",
                     "StartTimeOffset": "string"
                  },
                  "CreationTime": number,
                  "EndpointName": "string",
                  "FailureReason": "string",
                  "LastModifiedTime": number,
                  "LastMonitoringExecutionSummary": {
                     "CreationTime": number,
                     "EndpointName": "string",
                     "FailureReason": "string",
                     "LastModifiedTime": number,
                     "MonitoringExecutionStatus": "string",
                     "MonitoringJobDefinitionName": "string",
                     "MonitoringScheduleName": "string",
                     "MonitoringType": "string",
                     "ProcessingJobArn": "string",
                     "ScheduledTime": number
                  },
                  "MonitoringAlertSummaries": [
                     {
                        "Actions": {
                           "ModelDashboardIndicator": {
                              "Enabled": boolean
                           }
                        },
                        "AlertStatus": "string",
                        "CreationTime": number,
                        "DatapointsToAlert": number,
                        "EvaluationPeriod": number,
                        "LastModifiedTime": number,
                        "MonitoringAlertName": "string"
                     }
                  ],
                  "MonitoringScheduleArn": "string",
                  "MonitoringScheduleConfig": {
                     "MonitoringJobDefinition": {
                        "BaselineConfig": {
                           "BaseliningJobName": "string",
                           "ConstraintsResource": {
                              "S3Uri": "string"
                           },
                           "StatisticsResource": {
                              "S3Uri": "string"
                           }
                        },
                        "Environment": {
                           "string" : "string"
                        },
                        "MonitoringAppSpecification": {
                           "ContainerArguments": [ "string" ],
                           "ContainerEntrypoint": [ "string" ],
                           "ImageUri": "string",
                           "PostAnalyticsProcessorSourceUri": "string",
                           "RecordPreprocessorSourceUri": "string"
                        },
                        "MonitoringInputs": [
                           {
                              "BatchTransformInput": {
                                 "DataCapturedDestinationS3Uri": "string",
                                 "DatasetFormat": {
                                    "Csv": {
                                       "Header": boolean
                                    },
                                    "Json": {
                                       "Line": boolean
                                    },
                                    "Parquet": {
                                    }
                                 },
                                 "EndTimeOffset": "string",
                                 "ExcludeFeaturesAttribute": "string",
                                 "FeaturesAttribute": "string",
                                 "InferenceAttribute": "string",
                                 "LocalPath": "string",
                                 "ProbabilityAttribute": "string",
                                 "ProbabilityThresholdAttribute": number,
                                 "S3DataDistributionType": "string",
                                 "S3InputMode": "string",
                                 "StartTimeOffset": "string"
                              },
                              "EndpointInput": {
                                 "EndpointName": "string",
                                 "EndTimeOffset": "string",
                                 "ExcludeFeaturesAttribute": "string",
                                 "FeaturesAttribute": "string",
                                 "InferenceAttribute": "string",
                                 "LocalPath": "string",
                                 "ProbabilityAttribute": "string",
                                 "ProbabilityThresholdAttribute": number,
                                 "S3DataDistributionType": "string",
                                 "S3InputMode": "string",
                                 "StartTimeOffset": "string"
                              }
                           }
                        ],
                        "MonitoringOutputConfig": {
                           "KmsKeyId": "string",
                           "MonitoringOutputs": [
                              {
                                 "S3Output": {
                                    "LocalPath": "string",
                                    "S3UploadMode": "string",
                                    "S3Uri": "string"
                                 }
                              }
                           ]
                        },
                        "MonitoringResources": {
                           "ClusterConfig": {
                              "InstanceCount": number,
                              "InstanceType": "string",
                              "VolumeKmsKeyId": "string",
                              "VolumeSizeInGB": number
                           }
                        },
                        "NetworkConfig": {
                           "EnableInterContainerTrafficEncryption": boolean,
                           "EnableNetworkIsolation": boolean,
                           "VpcConfig": {
                              "SecurityGroupIds": [ "string" ],
                              "Subnets": [ "string" ]
                           }
                        },
                        "RoleArn": "string",
                        "StoppingCondition": {
                           "MaxRuntimeInSeconds": number
                        }
                     },
                     "MonitoringJobDefinitionName": "string",
                     "MonitoringType": "string",
                     "ScheduleConfig": {
                        "DataAnalysisEndTime": "string",
                        "DataAnalysisStartTime": "string",
                        "ScheduleExpression": "string"
                     }
                  },
                  "MonitoringScheduleName": "string",
                  "MonitoringScheduleStatus": "string",
                  "MonitoringType": "string"
               }
            ]
         },
         "ModelCard": {
            "Content": "string",
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "ModelCardArn": "string",
            "ModelCardName": "string",
            "ModelCardStatus": "string",
            "ModelCardVersion": number,
            "ModelId": "string",
            "ModelPackageGroupName": "string",
            "RiskRating": "string",
            "SecurityConfig": {
               "KmsKeyId": "string"
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "ModelPackage": {
            "AdditionalInferenceSpecifications": [
               {
                  "Containers": [
                     {
                        "AdditionalModelDataSources": [
                           {
                              "ChannelName": "string",
                              "S3DataSource": {
                                 "CompressionType": "string",
                                 "ETag": "string",
                                 "HubAccessConfig": {
                                    "HubContentArn": "string"
                                 },
                                 "ManifestEtag": "string",
                                 "ManifestS3Uri": "string",
                                 "ModelAccessConfig": {
                                    "AcceptEula": boolean
                                 },
                                 "S3DataType": "string",
                                 "S3Uri": "string"
                              }
                           }
                        ],
                        "AdditionalS3DataSource": {
                           "CompressionType": "string",
                           "ETag": "string",
                           "S3DataType": "string",
                           "S3Uri": "string"
                        },
                        "BaseModel": {
                           "HubContentName": "string",
                           "HubContentVersion": "string",
                           "RecipeName": "string"
                        },
                        "ContainerHostname": "string",
                        "Environment": {
                           "string" : "string"
                        },
                        "Framework": "string",
                        "FrameworkVersion": "string",
                        "Image": "string",
                        "ImageDigest": "string",
                        "IsCheckpoint": boolean,
                        "ModelDataETag": "string",
                        "ModelDataSource": {
                           "S3DataSource": {
                              "CompressionType": "string",
                              "ETag": "string",
                              "HubAccessConfig": {
                                 "HubContentArn": "string"
                              },
                              "ManifestEtag": "string",
                              "ManifestS3Uri": "string",
                              "ModelAccessConfig": {
                                 "AcceptEula": boolean
                              },
                              "S3DataType": "string",
                              "S3Uri": "string"
                           }
                        },
                        "ModelDataUrl": "string",
                        "ModelInput": {
                           "DataInputConfig": "string"
                        },
                        "NearestModelName": "string",
                        "ProductId": "string"
                     }
                  ],
                  "Description": "string",
                  "Name": "string",
                  "SupportedContentTypes": [ "string" ],
                  "SupportedRealtimeInferenceInstanceTypes": [ "string" ],
                  "SupportedResponseMIMETypes": [ "string" ],
                  "SupportedTransformInstanceTypes": [ "string" ]
               }
            ],
            "ApprovalDescription": "string",
            "CertifyForMarketplace": boolean,
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "CustomerMetadataProperties": {
               "string" : "string"
            },
            "Domain": "string",
            "DriftCheckBaselines": {
               "Bias": {
                  "ConfigFile": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "PostTrainingConstraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "PreTrainingConstraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               },
               "Explainability": {
                  "ConfigFile": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "Constraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               },
               "ModelDataQuality": {
                  "Constraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "Statistics": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               },
               "ModelQuality": {
                  "Constraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "Statistics": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               }
            },
            "InferenceSpecification": {
               "Containers": [
                  {
                     "AdditionalModelDataSources": [
                        {
                           "ChannelName": "string",
                           "S3DataSource": {
                              "CompressionType": "string",
                              "ETag": "string",
                              "HubAccessConfig": {
                                 "HubContentArn": "string"
                              },
                              "ManifestEtag": "string",
                              "ManifestS3Uri": "string",
                              "ModelAccessConfig": {
                                 "AcceptEula": boolean
                              },
                              "S3DataType": "string",
                              "S3Uri": "string"
                           }
                        }
                     ],
                     "AdditionalS3DataSource": {
                        "CompressionType": "string",
                        "ETag": "string",
                        "S3DataType": "string",
                        "S3Uri": "string"
                     },
                     "BaseModel": {
                        "HubContentName": "string",
                        "HubContentVersion": "string",
                        "RecipeName": "string"
                     },
                     "ContainerHostname": "string",
                     "Environment": {
                        "string" : "string"
                     },
                     "Framework": "string",
                     "FrameworkVersion": "string",
                     "Image": "string",
                     "ImageDigest": "string",
                     "IsCheckpoint": boolean,
                     "ModelDataETag": "string",
                     "ModelDataSource": {
                        "S3DataSource": {
                           "CompressionType": "string",
                           "ETag": "string",
                           "HubAccessConfig": {
                              "HubContentArn": "string"
                           },
                           "ManifestEtag": "string",
                           "ManifestS3Uri": "string",
                           "ModelAccessConfig": {
                              "AcceptEula": boolean
                           },
                           "S3DataType": "string",
                           "S3Uri": "string"
                        }
                     },
                     "ModelDataUrl": "string",
                     "ModelInput": {
                        "DataInputConfig": "string"
                     },
                     "NearestModelName": "string",
                     "ProductId": "string"
                  }
               ],
               "SupportedContentTypes": [ "string" ],
               "SupportedRealtimeInferenceInstanceTypes": [ "string" ],
               "SupportedResponseMIMETypes": [ "string" ],
               "SupportedTransformInstanceTypes": [ "string" ]
            },
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "MetadataProperties": {
               "CommitId": "string",
               "GeneratedBy": "string",
               "ProjectId": "string",
               "Repository": "string"
            },
            "ModelApprovalStatus": "string",
            "ModelCard": {
               "ModelCardContent": "string",
               "ModelCardStatus": "string"
            },
            "ModelLifeCycle": {
               "Stage": "string",
               "StageDescription": "string",
               "StageStatus": "string"
            },
            "ModelMetrics": {
               "Bias": {
                  "PostTrainingReport": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "PreTrainingReport": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "Report": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               },
               "Explainability": {
                  "Report": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               },
               "ModelDataQuality": {
                  "Constraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "Statistics": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               },
               "ModelQuality": {
                  "Constraints": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  },
                  "Statistics": {
                     "ContentDigest": "string",
                     "ContentType": "string",
                     "S3Uri": "string"
                  }
               }
            },
            "ModelPackageArn": "string",
            "ModelPackageDescription": "string",
            "ModelPackageGroupName": "string",
            "ModelPackageName": "string",
            "ModelPackageRegistrationType": "string",
            "ModelPackageStatus": "string",
            "ModelPackageStatusDetails": {
               "ImageScanStatuses": [
                  {
                     "FailureReason": "string",
                     "Name": "string",
                     "Status": "string"
                  }
               ],
               "ValidationStatuses": [
                  {
                     "FailureReason": "string",
                     "Name": "string",
                     "Status": "string"
                  }
               ]
            },
            "ModelPackageVersion": number,
            "SamplePayloadUrl": "string",
            "SecurityConfig": {
               "KmsKeyId": "string"
            },
            "SkipModelValidation": "string",
            "SourceAlgorithmSpecification": {
               "SourceAlgorithms": [
                  {
                     "AlgorithmName": "string",
                     "ModelDataETag": "string",
                     "ModelDataSource": {
                        "S3DataSource": {
                           "CompressionType": "string",
                           "ETag": "string",
                           "HubAccessConfig": {
                              "HubContentArn": "string"
                           },
                           "ManifestEtag": "string",
                           "ManifestS3Uri": "string",
                           "ModelAccessConfig": {
                              "AcceptEula": boolean
                           },
                           "S3DataType": "string",
                           "S3Uri": "string"
                        }
                     },
                     "ModelDataUrl": "string"
                  }
               ]
            },
            "SourceUri": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "Task": "string",
            "ValidationSpecification": {
               "ValidationProfiles": [
                  {
                     "ProfileName": "string",
                     "TransformJobDefinition": {
                        "BatchStrategy": "string",
                        "Environment": {
                           "string" : "string"
                        },
                        "MaxConcurrentTransforms": number,
                        "MaxPayloadInMB": number,
                        "TransformInput": {
                           "CompressionType": "string",
                           "ContentType": "string",
                           "DataSource": {
                              "S3DataSource": {
                                 "S3DataType": "string",
                                 "S3Uri": "string"
                              }
                           },
                           "SplitType": "string"
                        },
                        "TransformOutput": {
                           "Accept": "string",
                           "AssembleWith": "string",
                           "KmsKeyId": "string",
                           "S3OutputPath": "string"
                        },
                        "TransformResources": {
                           "InstanceCount": number,
                           "InstanceType": "string",
                           "TransformAmiVersion": "string",
                           "VolumeKmsKeyId": "string"
                        }
                     }
                  }
               ],
               "ValidationRole": "string"
            }
         },
         "ModelPackageGroup": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "ModelPackageGroupArn": "string",
            "ModelPackageGroupDescription": "string",
            "ModelPackageGroupName": "string",
            "ModelPackageGroupStatus": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "Pipeline": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "LastRunTime": number,
            "ParallelismConfiguration": {
               "MaxParallelExecutionSteps": number
            },
            "PipelineArn": "string",
            "PipelineDescription": "string",
            "PipelineDisplayName": "string",
            "PipelineName": "string",
            "PipelineStatus": "string",
            "RoleArn": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "PipelineExecution": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "FailureReason": "string",
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "ParallelismConfiguration": {
               "MaxParallelExecutionSteps": number
            },
            "PipelineArn": "string",
            "PipelineExecutionArn": "string",
            "PipelineExecutionDescription": "string",
            "PipelineExecutionDisplayName": "string",
            "PipelineExecutionStatus": "string",
            "PipelineExperimentConfig": {
               "ExperimentName": "string",
               "TrialName": "string"
            },
            "PipelineParameters": [
               {
                  "Name": "string",
                  "Value": "string"
               }
            ],
            "PipelineVersionDisplayName": "string",
            "PipelineVersionId": number,
            "SelectiveExecutionConfig": {
               "SelectedSteps": [
                  {
                     "StepName": "string"
                  }
               ],
               "SourcePipelineExecutionArn": "string"
            }
         },
         "PipelineVersion": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "LastExecutedPipelineExecutionArn": "string",
            "LastExecutedPipelineExecutionDisplayName": "string",
            "LastExecutedPipelineExecutionStatus": "string",
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "PipelineArn": "string",
            "PipelineVersionDescription": "string",
            "PipelineVersionDisplayName": "string",
            "PipelineVersionId": number
         },
         "Project": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "ProjectArn": "string",
            "ProjectDescription": "string",
            "ProjectId": "string",
            "ProjectName": "string",
            "ProjectStatus": "string",
            "ServiceCatalogProvisionedProductDetails": {
               "ProvisionedProductId": "string",
               "ProvisionedProductStatusMessage": "string"
            },
            "ServiceCatalogProvisioningDetails": {
               "PathId": "string",
               "ProductId": "string",
               "ProvisioningArtifactId": "string",
               "ProvisioningParameters": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ]
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "TemplateProviderDetails": [
               {
                  "CfnTemplateProviderDetail": {
                     "Parameters": [
                        {
                           "Key": "string",
                           "Value": "string"
                        }
                     ],
                     "RoleARN": "string",
                     "StackDetail": {
                        "Id": "string",
                        "Name": "string",
                        "StatusMessage": "string"
                     },
                     "TemplateName": "string",
                     "TemplateURL": "string"
                  }
               }
            ]
         },
         "TrainingJob": {
            "AlgorithmSpecification": {
               "AlgorithmName": "string",
               "ContainerArguments": [ "string" ],
               "ContainerEntrypoint": [ "string" ],
               "EnableSageMakerMetricsTimeSeries": boolean,
               "MetricDefinitions": [
                  {
                     "Name": "string",
                     "Regex": "string"
                  }
               ],
               "TrainingImage": "string",
               "TrainingImageConfig": {
                  "TrainingRepositoryAccessMode": "string",
                  "TrainingRepositoryAuthConfig": {
                     "TrainingRepositoryCredentialsProviderArn": "string"
                  }
               },
               "TrainingInputMode": "string"
            },
            "AutoMLJobArn": "string",
            "BillableTimeInSeconds": number,
            "CheckpointConfig": {
               "LocalPath": "string",
               "S3Uri": "string"
            },
            "CreationTime": number,
            "DebugHookConfig": {
               "CollectionConfigurations": [
                  {
                     "CollectionName": "string",
                     "CollectionParameters": {
                        "string" : "string"
                     }
                  }
               ],
               "HookParameters": {
                  "string" : "string"
               },
               "LocalPath": "string",
               "S3OutputPath": "string"
            },
            "DebugRuleConfigurations": [
               {
                  "InstanceType": "string",
                  "LocalPath": "string",
                  "RuleConfigurationName": "string",
                  "RuleEvaluatorImage": "string",
                  "RuleParameters": {
                     "string" : "string"
                  },
                  "S3OutputPath": "string",
                  "VolumeSizeInGB": number
               }
            ],
            "DebugRuleEvaluationStatuses": [
               {
                  "LastModifiedTime": number,
                  "RuleConfigurationName": "string",
                  "RuleEvaluationJobArn": "string",
                  "RuleEvaluationStatus": "string",
                  "StatusDetails": "string"
               }
            ],
            "EnableInterContainerTrafficEncryption": boolean,
            "EnableManagedSpotTraining": boolean,
            "EnableNetworkIsolation": boolean,
            "Environment": {
               "string" : "string"
            },
            "ExperimentConfig": {
               "ExperimentName": "string",
               "RunName": "string",
               "TrialComponentDisplayName": "string",
               "TrialName": "string"
            },
            "FailureReason": "string",
            "FinalMetricDataList": [
               {
                  "MetricName": "string",
                  "Timestamp": number,
                  "Value": number
               }
            ],
            "HyperParameters": {
               "string" : "string"
            },
            "InputDataConfig": [
               {
                  "ChannelName": "string",
                  "CompressionType": "string",
                  "ContentType": "string",
                  "DataSource": {
                     "DatasetSource": {
                        "DatasetArn": "string"
                     },
                     "FileSystemDataSource": {
                        "DirectoryPath": "string",
                        "FileSystemAccessMode": "string",
                        "FileSystemId": "string",
                        "FileSystemType": "string"
                     },
                     "S3DataSource": {
                        "AttributeNames": [ "string" ],
                        "HubAccessConfig": {
                           "HubContentArn": "string"
                        },
                        "InstanceGroupNames": [ "string" ],
                        "ModelAccessConfig": {
                           "AcceptEula": boolean
                        },
                        "S3DataDistributionType": "string",
                        "S3DataType": "string",
                        "S3Uri": "string"
                     }
                  },
                  "InputMode": "string",
                  "RecordWrapperType": "string",
                  "ShuffleConfig": {
                     "Seed": number
                  }
               }
            ],
            "LabelingJobArn": "string",
            "LastModifiedTime": number,
            "ModelArtifacts": {
               "S3ModelArtifacts": "string"
            },
            "ModelPackageConfig": {
               "ModelPackageGroupArn": "string",
               "SourceModelPackageArn": "string"
            },
            "OutputDataConfig": {
               "CompressionType": "string",
               "KmsKeyId": "string",
               "S3OutputPath": "string"
            },
            "OutputModelPackageArn": "string",
            "ProfilerConfig": {
               "DisableProfiler": boolean,
               "ProfilingIntervalInMilliseconds": number,
               "ProfilingParameters": {
                  "string" : "string"
               },
               "S3OutputPath": "string"
            },
            "ResourceConfig": {
               "InstanceCount": number,
               "InstanceGroups": [
                  {
                     "InstanceCount": number,
                     "InstanceGroupName": "string",
                     "InstanceType": "string"
                  }
               ],
               "InstancePlacementConfig": {
                  "EnableMultipleJobs": boolean,
                  "PlacementSpecifications": [
                     {
                        "InstanceCount": number,
                        "UltraServerId": "string"
                     }
                  ]
               },
               "InstanceType": "string",
               "KeepAlivePeriodInSeconds": number,
               "TrainingPlanArn": "string",
               "VolumeKmsKeyId": "string",
               "VolumeSizeInGB": number
            },
            "RetryStrategy": {
               "MaximumRetryAttempts": number
            },
            "RoleArn": "string",
            "SecondaryStatus": "string",
            "SecondaryStatusTransitions": [
               {
                  "EndTime": number,
                  "StartTime": number,
                  "Status": "string",
                  "StatusMessage": "string"
               }
            ],
            "StoppingCondition": {
               "MaxPendingTimeInSeconds": number,
               "MaxRuntimeInSeconds": number,
               "MaxWaitTimeInSeconds": number
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "TensorBoardOutputConfig": {
               "LocalPath": "string",
               "S3OutputPath": "string"
            },
            "TrainingEndTime": number,
            "TrainingJobArn": "string",
            "TrainingJobName": "string",
            "TrainingJobStatus": "string",
            "TrainingStartTime": number,
            "TrainingTimeInSeconds": number,
            "TuningJobArn": "string",
            "VpcConfig": {
               "SecurityGroupIds": [ "string" ],
               "Subnets": [ "string" ]
            },
            "WarmPoolStatus": {
               "ResourceRetainedBillableTimeInSeconds": number,
               "ReusedByJob": "string",
               "Status": "string"
            }
         },
         "Trial": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "DisplayName": "string",
            "ExperimentName": "string",
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "MetadataProperties": {
               "CommitId": "string",
               "GeneratedBy": "string",
               "ProjectId": "string",
               "Repository": "string"
            },
            "Source": {
               "SourceArn": "string",
               "SourceType": "string"
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "TrialArn": "string",
            "TrialComponentSummaries": [
               {
                  "CreatedBy": {
                     "DomainId": "string",
                     "IamIdentity": {
                        "Arn": "string",
                        "PrincipalId": "string",
                        "SourceIdentity": "string"
                     },
                     "UserProfileArn": "string",
                     "UserProfileName": "string"
                  },
                  "CreationTime": number,
                  "TrialComponentArn": "string",
                  "TrialComponentName": "string",
                  "TrialComponentSource": {
                     "SourceArn": "string",
                     "SourceType": "string"
                  }
               }
            ],
            "TrialName": "string"
         },
         "TrialComponent": {
            "CreatedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "CreationTime": number,
            "DisplayName": "string",
            "EndTime": number,
            "InputArtifacts": {
               "string" : {
                  "MediaType": "string",
                  "Value": "string"
               }
            },
            "LastModifiedBy": {
               "DomainId": "string",
               "IamIdentity": {
                  "Arn": "string",
                  "PrincipalId": "string",
                  "SourceIdentity": "string"
               },
               "UserProfileArn": "string",
               "UserProfileName": "string"
            },
            "LastModifiedTime": number,
            "LineageGroupArn": "string",
            "MetadataProperties": {
               "CommitId": "string",
               "GeneratedBy": "string",
               "ProjectId": "string",
               "Repository": "string"
            },
            "Metrics": [
               {
                  "Avg": number,
                  "Count": number,
                  "Last": number,
                  "Max": number,
                  "MetricName": "string",
                  "Min": number,
                  "SourceArn": "string",
                  "StdDev": number,
                  "TimeStamp": number
               }
            ],
            "OutputArtifacts": {
               "string" : {
                  "MediaType": "string",
                  "Value": "string"
               }
            },
            "Parameters": {
               "string" : {
                  "NumberValue": number,
                  "StringValue": "string"
               }
            },
            "Parents": [
               {
                  "ExperimentName": "string",
                  "TrialName": "string"
               }
            ],
            "RunName": "string",
            "Source": {
               "SourceArn": "string",
               "SourceType": "string"
            },
            "SourceDetail": {
               "ProcessingJob": {
                  "AppSpecification": {
                     "ContainerArguments": [ "string" ],
                     "ContainerEntrypoint": [ "string" ],
                     "ImageUri": "string"
                  },
                  "AutoMLJobArn": "string",
                  "CreationTime": number,
                  "Environment": {
                     "string" : "string"
                  },
                  "ExitMessage": "string",
                  "ExperimentConfig": {
                     "ExperimentName": "string",
                     "RunName": "string",
                     "TrialComponentDisplayName": "string",
                     "TrialName": "string"
                  },
                  "FailureReason": "string",
                  "LastModifiedTime": number,
                  "MonitoringScheduleArn": "string",
                  "NetworkConfig": {
                     "EnableInterContainerTrafficEncryption": boolean,
                     "EnableNetworkIsolation": boolean,
                     "VpcConfig": {
                        "SecurityGroupIds": [ "string" ],
                        "Subnets": [ "string" ]
                     }
                  },
                  "ProcessingEndTime": number,
                  "ProcessingInputs": [
                     {
                        "AppManaged": boolean,
                        "DatasetDefinition": {
                           "AthenaDatasetDefinition": {
                              "Catalog": "string",
                              "Database": "string",
                              "KmsKeyId": "string",
                              "OutputCompression": "string",
                              "OutputFormat": "string",
                              "OutputS3Uri": "string",
                              "QueryString": "string",
                              "WorkGroup": "string"
                           },
                           "DataDistributionType": "string",
                           "InputMode": "string",
                           "LocalPath": "string",
                           "RedshiftDatasetDefinition": {
                              "ClusterId": "string",
                              "ClusterRoleArn": "string",
                              "Database": "string",
                              "DbUser": "string",
                              "KmsKeyId": "string",
                              "OutputCompression": "string",
                              "OutputFormat": "string",
                              "OutputS3Uri": "string",
                              "QueryString": "string"
                           }
                        },
                        "InputName": "string",
                        "S3Input": {
                           "LocalPath": "string",
                           "S3CompressionType": "string",
                           "S3DataDistributionType": "string",
                           "S3DataType": "string",
                           "S3InputMode": "string",
                           "S3Uri": "string"
                        }
                     }
                  ],
                  "ProcessingJobArn": "string",
                  "ProcessingJobName": "string",
                  "ProcessingJobStatus": "string",
                  "ProcessingOutputConfig": {
                     "KmsKeyId": "string",
                     "Outputs": [
                        {
                           "AppManaged": boolean,
                           "FeatureStoreOutput": {
                              "FeatureGroupName": "string"
                           },
                           "OutputName": "string",
                           "S3Output": {
                              "LocalPath": "string",
                              "S3UploadMode": "string",
                              "S3Uri": "string"
                           }
                        }
                     ]
                  },
                  "ProcessingResources": {
                     "ClusterConfig": {
                        "InstanceCount": number,
                        "InstanceType": "string",
                        "VolumeKmsKeyId": "string",
                        "VolumeSizeInGB": number
                     }
                  },
                  "ProcessingStartTime": number,
                  "RoleArn": "string",
                  "StoppingCondition": {
                     "MaxRuntimeInSeconds": number
                  },
                  "Tags": [
                     {
                        "Key": "string",
                        "Value": "string"
                     }
                  ],
                  "TrainingJobArn": "string"
               },
               "SourceArn": "string",
               "TrainingJob": {
                  "AlgorithmSpecification": {
                     "AlgorithmName": "string",
                     "ContainerArguments": [ "string" ],
                     "ContainerEntrypoint": [ "string" ],
                     "EnableSageMakerMetricsTimeSeries": boolean,
                     "MetricDefinitions": [
                        {
                           "Name": "string",
                           "Regex": "string"
                        }
                     ],
                     "TrainingImage": "string",
                     "TrainingImageConfig": {
                        "TrainingRepositoryAccessMode": "string",
                        "TrainingRepositoryAuthConfig": {
                           "TrainingRepositoryCredentialsProviderArn": "string"
                        }
                     },
                     "TrainingInputMode": "string"
                  },
                  "AutoMLJobArn": "string",
                  "BillableTimeInSeconds": number,
                  "CheckpointConfig": {
                     "LocalPath": "string",
                     "S3Uri": "string"
                  },
                  "CreationTime": number,
                  "DebugHookConfig": {
                     "CollectionConfigurations": [
                        {
                           "CollectionName": "string",
                           "CollectionParameters": {
                              "string" : "string"
                           }
                        }
                     ],
                     "HookParameters": {
                        "string" : "string"
                     },
                     "LocalPath": "string",
                     "S3OutputPath": "string"
                  },
                  "DebugRuleConfigurations": [
                     {
                        "InstanceType": "string",
                        "LocalPath": "string",
                        "RuleConfigurationName": "string",
                        "RuleEvaluatorImage": "string",
                        "RuleParameters": {
                           "string" : "string"
                        },
                        "S3OutputPath": "string",
                        "VolumeSizeInGB": number
                     }
                  ],
                  "DebugRuleEvaluationStatuses": [
                     {
                        "LastModifiedTime": number,
                        "RuleConfigurationName": "string",
                        "RuleEvaluationJobArn": "string",
                        "RuleEvaluationStatus": "string",
                        "StatusDetails": "string"
                     }
                  ],
                  "EnableInterContainerTrafficEncryption": boolean,
                  "EnableManagedSpotTraining": boolean,
                  "EnableNetworkIsolation": boolean,
                  "Environment": {
                     "string" : "string"
                  },
                  "ExperimentConfig": {
                     "ExperimentName": "string",
                     "RunName": "string",
                     "TrialComponentDisplayName": "string",
                     "TrialName": "string"
                  },
                  "FailureReason": "string",
                  "FinalMetricDataList": [
                     {
                        "MetricName": "string",
                        "Timestamp": number,
                        "Value": number
                     }
                  ],
                  "HyperParameters": {
                     "string" : "string"
                  },
                  "InputDataConfig": [
                     {
                        "ChannelName": "string",
                        "CompressionType": "string",
                        "ContentType": "string",
                        "DataSource": {
                           "DatasetSource": {
                              "DatasetArn": "string"
                           },
                           "FileSystemDataSource": {
                              "DirectoryPath": "string",
                              "FileSystemAccessMode": "string",
                              "FileSystemId": "string",
                              "FileSystemType": "string"
                           },
                           "S3DataSource": {
                              "AttributeNames": [ "string" ],
                              "HubAccessConfig": {
                                 "HubContentArn": "string"
                              },
                              "InstanceGroupNames": [ "string" ],
                              "ModelAccessConfig": {
                                 "AcceptEula": boolean
                              },
                              "S3DataDistributionType": "string",
                              "S3DataType": "string",
                              "S3Uri": "string"
                           }
                        },
                        "InputMode": "string",
                        "RecordWrapperType": "string",
                        "ShuffleConfig": {
                           "Seed": number
                        }
                     }
                  ],
                  "LabelingJobArn": "string",
                  "LastModifiedTime": number,
                  "ModelArtifacts": {
                     "S3ModelArtifacts": "string"
                  },
                  "ModelPackageConfig": {
                     "ModelPackageGroupArn": "string",
                     "SourceModelPackageArn": "string"
                  },
                  "OutputDataConfig": {
                     "CompressionType": "string",
                     "KmsKeyId": "string",
                     "S3OutputPath": "string"
                  },
                  "OutputModelPackageArn": "string",
                  "ProfilerConfig": {
                     "DisableProfiler": boolean,
                     "ProfilingIntervalInMilliseconds": number,
                     "ProfilingParameters": {
                        "string" : "string"
                     },
                     "S3OutputPath": "string"
                  },
                  "ResourceConfig": {
                     "InstanceCount": number,
                     "InstanceGroups": [
                        {
                           "InstanceCount": number,
                           "InstanceGroupName": "string",
                           "InstanceType": "string"
                        }
                     ],
                     "InstancePlacementConfig": {
                        "EnableMultipleJobs": boolean,
                        "PlacementSpecifications": [
                           {
                              "InstanceCount": number,
                              "UltraServerId": "string"
                           }
                        ]
                     },
                     "InstanceType": "string",
                     "KeepAlivePeriodInSeconds": number,
                     "TrainingPlanArn": "string",
                     "VolumeKmsKeyId": "string",
                     "VolumeSizeInGB": number
                  },
                  "RetryStrategy": {
                     "MaximumRetryAttempts": number
                  },
                  "RoleArn": "string",
                  "SecondaryStatus": "string",
                  "SecondaryStatusTransitions": [
                     {
                        "EndTime": number,
                        "StartTime": number,
                        "Status": "string",
                        "StatusMessage": "string"
                     }
                  ],
                  "StoppingCondition": {
                     "MaxPendingTimeInSeconds": number,
                     "MaxRuntimeInSeconds": number,
                     "MaxWaitTimeInSeconds": number
                  },
                  "Tags": [
                     {
                        "Key": "string",
                        "Value": "string"
                     }
                  ],
                  "TensorBoardOutputConfig": {
                     "LocalPath": "string",
                     "S3OutputPath": "string"
                  },
                  "TrainingEndTime": number,
                  "TrainingJobArn": "string",
                  "TrainingJobName": "string",
                  "TrainingJobStatus": "string",
                  "TrainingStartTime": number,
                  "TrainingTimeInSeconds": number,
                  "TuningJobArn": "string",
                  "VpcConfig": {
                     "SecurityGroupIds": [ "string" ],
                     "Subnets": [ "string" ]
                  },
                  "WarmPoolStatus": {
                     "ResourceRetainedBillableTimeInSeconds": number,
                     "ReusedByJob": "string",
                     "Status": "string"
                  }
               },
               "TransformJob": {
                  "AutoMLJobArn": "string",
                  "BatchStrategy": "string",
                  "CreationTime": number,
                  "DataCaptureConfig": {
                     "DestinationS3Uri": "string",
                     "GenerateInferenceId": boolean,
                     "KmsKeyId": "string"
                  },
                  "DataProcessing": {
                     "InputFilter": "string",
                     "JoinSource": "string",
                     "OutputFilter": "string"
                  },
                  "Environment": {
                     "string" : "string"
                  },
                  "ExperimentConfig": {
                     "ExperimentName": "string",
                     "RunName": "string",
                     "TrialComponentDisplayName": "string",
                     "TrialName": "string"
                  },
                  "FailureReason": "string",
                  "LabelingJobArn": "string",
                  "MaxConcurrentTransforms": number,
                  "MaxPayloadInMB": number,
                  "ModelClientConfig": {
                     "InvocationsMaxRetries": number,
                     "InvocationsTimeoutInSeconds": number
                  },
                  "ModelName": "string",
                  "Tags": [
                     {
                        "Key": "string",
                        "Value": "string"
                     }
                  ],
                  "TransformEndTime": number,
                  "TransformInput": {
                     "CompressionType": "string",
                     "ContentType": "string",
                     "DataSource": {
                        "S3DataSource": {
                           "S3DataType": "string",
                           "S3Uri": "string"
                        }
                     },
                     "SplitType": "string"
                  },
                  "TransformJobArn": "string",
                  "TransformJobName": "string",
                  "TransformJobStatus": "string",
                  "TransformOutput": {
                     "Accept": "string",
                     "AssembleWith": "string",
                     "KmsKeyId": "string",
                     "S3OutputPath": "string"
                  },
                  "TransformResources": {
                     "InstanceCount": number,
                     "InstanceType": "string",
                     "TransformAmiVersion": "string",
                     "VolumeKmsKeyId": "string"
                  },
                  "TransformStartTime": number
               }
            },
            "StartTime": number,
            "Status": {
               "Message": "string",
               "PrimaryStatus": "string"
            },
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "TrialComponentArn": "string",
            "TrialComponentName": "string"
         }
      }
   ],
   "TotalHits": {
      "Relation": "string",
      "Value": number
   }
}
```

## Response Elements
<a name="API_Search_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_Search_ResponseSyntax) **   <a name="sagemaker-Search-response-NextToken"></a>
If the result of the previous `Search` request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [Results](#API_Search_ResponseSyntax) **   <a name="sagemaker-Search-response-Results"></a>
A list of `SearchRecord` objects.
Type: Array of [SearchRecord](API_SearchRecord.md) objects

 ** [TotalHits](#API_Search_ResponseSyntax) **   <a name="sagemaker-Search-response-TotalHits"></a>
The total number of matching results.
Type: [TotalHits](API_TotalHits.md) object

## Errors
<a name="API_Search_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_Search_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/Search)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/Search)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Search)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/Search)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Search)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/Search)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/Search)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/Search)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/Search)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Search)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

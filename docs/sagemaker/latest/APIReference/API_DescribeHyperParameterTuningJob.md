---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHyperParameterTuningJob.html
---

# DescribeHyperParameterTuningJob
<a name="API_DescribeHyperParameterTuningJob"></a>

Returns a description of a hyperparameter tuning job, depending on the fields selected. These fields can include the name, Amazon Resource Name (ARN), job status of your tuning job and more.

## Request Syntax
<a name="API_DescribeHyperParameterTuningJob_RequestSyntax"></a>

```
{
   "HyperParameterTuningJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeHyperParameterTuningJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HyperParameterTuningJobName](#API_DescribeHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-request-HyperParameterTuningJobName"></a>
The name of the tuning job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

## Response Syntax
<a name="API_DescribeHyperParameterTuningJob_ResponseSyntax"></a>

```
{
   "Autotune": {
      "Mode": "string"
   },
   "BestTrainingJob": {
      "FailureReason": "string",
      "FinalHyperParameterTuningJobObjectiveMetric": {
         "MetricName": "string",
         "Type": "string",
         "Value": number
      },
      "ObjectiveStatus": "string",
      "TrainingJobArn": "string",
      "TrainingJobDefinitionName": "string",
      "TrainingJobName": "string",
      "TrainingJobStatus": "string",
      "TunedHyperParameters": {
         "string" : "string"
      },
      "TuningJobName": "string"
   },
   "ConsumedResources": {
      "RuntimeInSeconds": number
   },
   "FailureReason": "string",
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
   "ObjectiveStatusCounters": {
      "Failed": number,
      "Pending": number,
      "Succeeded": number
   },
   "OverallBestTrainingJob": {
      "FailureReason": "string",
      "FinalHyperParameterTuningJobObjectiveMetric": {
         "MetricName": "string",
         "Type": "string",
         "Value": number
      },
      "ObjectiveStatus": "string",
      "TrainingJobArn": "string",
      "TrainingJobDefinitionName": "string",
      "TrainingJobName": "string",
      "TrainingJobStatus": "string",
      "TunedHyperParameters": {
         "string" : "string"
      },
      "TuningJobName": "string"
   },
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
         "InstancePreferences": [
            {
               "InstanceCount": number,
               "InstanceType": "string",
               "TrainingPlanArns": [ "string" ]
            }
         ],
         "InstanceType": "string",
         "KeepAlivePeriodInSeconds": number,
         "SelectedInstanceCount": number,
         "SelectedInstanceType": "string",
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
            "InstancePreferences": [
               {
                  "InstanceCount": number,
                  "InstanceType": "string",
                  "TrainingPlanArns": [ "string" ]
               }
            ],
            "InstanceType": "string",
            "KeepAlivePeriodInSeconds": number,
            "SelectedInstanceCount": number,
            "SelectedInstanceType": "string",
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
}
```

## Response Elements
<a name="API_DescribeHyperParameterTuningJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Autotune](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-Autotune"></a>
A flag to indicate if autotune is enabled for the hyperparameter tuning job.
Type: [Autotune](API_Autotune.md) object

 ** [BestTrainingJob](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-BestTrainingJob"></a>
A [TrainingJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html) object that describes the training job that completed with the best current [HyperParameterTuningJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html).
Type: [HyperParameterTrainingJobSummary](API_HyperParameterTrainingJobSummary.md) object

 ** [ConsumedResources](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-ConsumedResources"></a>
The total resources consumed by your hyperparameter tuning job.
Type: [HyperParameterTuningJobConsumedResources](API_HyperParameterTuningJobConsumedResources.md) object

 ** [FailureReason](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-FailureReason"></a>
If the tuning job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HyperParameterTuningJobArn](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobArn"></a>
The Amazon Resource Name (ARN) of the tuning job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:hyper-parameter-tuning-job/.*`

 ** [HyperParameterTuningJobConfig](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobConfig"></a>
The [HyperParameterTuningJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html) object that specifies the configuration of the tuning job.
Type: [HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md) object

 ** [HyperParameterTuningJobName](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobName"></a>
The name of the hyperparameter tuning job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`

 ** [HyperParameterTuningJobStatus](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus"></a>
The status of the tuning job.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping | Deleting | DeleteFailed`

 ** [ObjectiveStatusCounters](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-ObjectiveStatusCounters"></a>
The [ObjectiveStatusCounters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ObjectiveStatusCounters.html) object that specifies the number of training jobs, categorized by the status of their final objective metric, that this tuning job launched.
Type: [ObjectiveStatusCounters](API_ObjectiveStatusCounters.md) object

 ** [OverallBestTrainingJob](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-OverallBestTrainingJob"></a>
If the hyperparameter tuning job is an warm start tuning job with a `WarmStartType` of `IDENTICAL_DATA_AND_ALGORITHM`, this is the [TrainingJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html) for the training job with the best objective metric value of all training jobs launched by this tuning job and all parent jobs specified for the warm start tuning job.
Type: [HyperParameterTrainingJobSummary](API_HyperParameterTrainingJobSummary.md) object

 ** [TrainingJobDefinition](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-TrainingJobDefinition"></a>
The [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) object that specifies the definition of the training jobs that this tuning job launches.
Type: [HyperParameterTrainingJobDefinition](API_HyperParameterTrainingJobDefinition.md) object

 ** [TrainingJobDefinitions](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-TrainingJobDefinitions"></a>
A list of the [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) objects launched for this tuning job.
Type: Array of [HyperParameterTrainingJobDefinition](API_HyperParameterTrainingJobDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [TrainingJobStatusCounters](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-TrainingJobStatusCounters"></a>
The [TrainingJobStatusCounters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobStatusCounters.html) object that specifies the number of training jobs, categorized by status, that this tuning job launched.
Type: [TrainingJobStatusCounters](API_TrainingJobStatusCounters.md) object

 ** [TuningJobCompletionDetails](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-TuningJobCompletionDetails"></a>
Tuning job completion information returned as the response from a hyperparameter tuning job. This information tells if your tuning job has or has not converged. It also includes the number of training jobs that have not improved model performance as evaluated against the objective function.
Type: [HyperParameterTuningJobCompletionDetails](API_HyperParameterTuningJobCompletionDetails.md) object

 ** [WarmStartConfig](#API_DescribeHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-DescribeHyperParameterTuningJob-response-WarmStartConfig"></a>
The configuration for starting the hyperparameter parameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.
Type: [HyperParameterTuningJobWarmStartConfig](API_HyperParameterTuningJobWarmStartConfig.md) object

## Errors
<a name="API_DescribeHyperParameterTuningJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeHyperParameterTuningJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeHyperParameterTuningJob)

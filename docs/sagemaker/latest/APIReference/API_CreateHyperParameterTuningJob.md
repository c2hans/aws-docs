---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html
---

# CreateHyperParameterTuningJob
<a name="API_CreateHyperParameterTuningJob"></a>

Starts a hyperparameter tuning job. A hyperparameter tuning job finds the best version of a model by running many training jobs on your dataset using the algorithm you choose and values for hyperparameters within ranges that you specify. It then chooses the hyperparameter values that result in a model that performs the best, as measured by an objective metric that you choose.

A hyperparameter tuning job automatically creates Amazon SageMaker experiments, trials, and trial components for each training job that it runs. You can view these entities in Amazon SageMaker Studio. For more information, see [View Experiments, Trials, and Trial Components](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-view-compare.html#experiments-view).

**Important**
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request hyperparameter variable or plain text fields..

## Request Syntax
<a name="API_CreateHyperParameterTuningJob_RequestSyntax"></a>

```
{
   "Autotune": {
      "Mode": "{{string}}"
   },
   "HyperParameterTuningJobConfig": {
      "HyperParameterTuningJobObjective": {
         "MetricName": "{{string}}",
         "Type": "{{string}}"
      },
      "ParameterRanges": {
         "AutoParameters": [
            {
               "Name": "{{string}}",
               "ValueHint": "{{string}}"
            }
         ],
         "CategoricalParameterRanges": [
            {
               "Name": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "ContinuousParameterRanges": [
            {
               "MaxValue": "{{string}}",
               "MinValue": "{{string}}",
               "Name": "{{string}}",
               "ScalingType": "{{string}}"
            }
         ],
         "IntegerParameterRanges": [
            {
               "MaxValue": "{{string}}",
               "MinValue": "{{string}}",
               "Name": "{{string}}",
               "ScalingType": "{{string}}"
            }
         ]
      },
      "RandomSeed": {{number}},
      "ResourceLimits": {
         "MaxNumberOfTrainingJobs": {{number}},
         "MaxParallelTrainingJobs": {{number}},
         "MaxRuntimeInSeconds": {{number}}
      },
      "Strategy": "{{string}}",
      "StrategyConfig": {
         "HyperbandStrategyConfig": {
            "MaxResource": {{number}},
            "MinResource": {{number}}
         }
      },
      "TrainingJobEarlyStoppingType": "{{string}}",
      "TuningJobCompletionCriteria": {
         "BestObjectiveNotImproving": {
            "MaxNumberOfTrainingJobsNotImproving": {{number}}
         },
         "ConvergenceDetected": {
            "CompleteOnConvergence": "{{string}}"
         },
         "TargetObjectiveMetricValue": {{number}}
      }
   },
   "HyperParameterTuningJobName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrainingJobDefinition": {
      "AlgorithmSpecification": {
         "AlgorithmName": "{{string}}",
         "MetricDefinitions": [
            {
               "Name": "{{string}}",
               "Regex": "{{string}}"
            }
         ],
         "TrainingImage": "{{string}}",
         "TrainingInputMode": "{{string}}"
      },
      "CheckpointConfig": {
         "LocalPath": "{{string}}",
         "S3Uri": "{{string}}"
      },
      "DefinitionName": "{{string}}",
      "EnableInterContainerTrafficEncryption": {{boolean}},
      "EnableManagedSpotTraining": {{boolean}},
      "EnableNetworkIsolation": {{boolean}},
      "Environment": {
         "{{string}}" : "{{string}}"
      },
      "HyperParameterRanges": {
         "AutoParameters": [
            {
               "Name": "{{string}}",
               "ValueHint": "{{string}}"
            }
         ],
         "CategoricalParameterRanges": [
            {
               "Name": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "ContinuousParameterRanges": [
            {
               "MaxValue": "{{string}}",
               "MinValue": "{{string}}",
               "Name": "{{string}}",
               "ScalingType": "{{string}}"
            }
         ],
         "IntegerParameterRanges": [
            {
               "MaxValue": "{{string}}",
               "MinValue": "{{string}}",
               "Name": "{{string}}",
               "ScalingType": "{{string}}"
            }
         ]
      },
      "HyperParameterTuningResourceConfig": {
         "AllocationStrategy": "{{string}}",
         "InstanceConfigs": [
            {
               "InstanceCount": {{number}},
               "InstanceType": "{{string}}",
               "VolumeSizeInGB": {{number}}
            }
         ],
         "InstanceCount": {{number}},
         "InstanceType": "{{string}}",
         "VolumeKmsKeyId": "{{string}}",
         "VolumeSizeInGB": {{number}}
      },
      "InputDataConfig": [
         {
            "ChannelName": "{{string}}",
            "CompressionType": "{{string}}",
            "ContentType": "{{string}}",
            "DataSource": {
               "DatasetSource": {
                  "DatasetArn": "{{string}}"
               },
               "FileSystemDataSource": {
                  "DirectoryPath": "{{string}}",
                  "FileSystemAccessMode": "{{string}}",
                  "FileSystemId": "{{string}}",
                  "FileSystemType": "{{string}}"
               },
               "S3DataSource": {
                  "AttributeNames": [ "{{string}}" ],
                  "HubAccessConfig": {
                     "HubContentArn": "{{string}}"
                  },
                  "InstanceGroupNames": [ "{{string}}" ],
                  "ModelAccessConfig": {
                     "AcceptEula": {{boolean}}
                  },
                  "S3DataDistributionType": "{{string}}",
                  "S3DataType": "{{string}}",
                  "S3Uri": "{{string}}"
               }
            },
            "InputMode": "{{string}}",
            "RecordWrapperType": "{{string}}",
            "ShuffleConfig": {
               "Seed": {{number}}
            }
         }
      ],
      "OutputDataConfig": {
         "CompressionType": "{{string}}",
         "KmsKeyId": "{{string}}",
         "S3OutputPath": "{{string}}"
      },
      "ResourceConfig": {
         "InstanceCount": {{number}},
         "InstanceGroups": [
            {
               "InstanceCount": {{number}},
               "InstanceGroupName": "{{string}}",
               "InstanceType": "{{string}}"
            }
         ],
         "InstancePlacementConfig": {
            "EnableMultipleJobs": {{boolean}},
            "PlacementSpecifications": [
               {
                  "InstanceCount": {{number}},
                  "UltraServerId": "{{string}}"
               }
            ]
         },
         "InstancePreferences": [
            {
               "InstanceCount": {{number}},
               "InstanceType": "{{string}}",
               "TrainingPlanArns": [ "{{string}}" ]
            }
         ],
         "InstanceType": "{{string}}",
         "KeepAlivePeriodInSeconds": {{number}},
         "SelectedInstanceCount": {{number}},
         "SelectedInstanceType": "{{string}}",
         "TrainingPlanArn": "{{string}}",
         "VolumeKmsKeyId": "{{string}}",
         "VolumeSizeInGB": {{number}}
      },
      "RetryStrategy": {
         "MaximumRetryAttempts": {{number}}
      },
      "RoleArn": "{{string}}",
      "StaticHyperParameters": {
         "{{string}}" : "{{string}}"
      },
      "StoppingCondition": {
         "MaxPendingTimeInSeconds": {{number}},
         "MaxRuntimeInSeconds": {{number}},
         "MaxWaitTimeInSeconds": {{number}}
      },
      "TuningObjective": {
         "MetricName": "{{string}}",
         "Type": "{{string}}"
      },
      "VpcConfig": {
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "TrainingJobDefinitions": [
      {
         "AlgorithmSpecification": {
            "AlgorithmName": "{{string}}",
            "MetricDefinitions": [
               {
                  "Name": "{{string}}",
                  "Regex": "{{string}}"
               }
            ],
            "TrainingImage": "{{string}}",
            "TrainingInputMode": "{{string}}"
         },
         "CheckpointConfig": {
            "LocalPath": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "DefinitionName": "{{string}}",
         "EnableInterContainerTrafficEncryption": {{boolean}},
         "EnableManagedSpotTraining": {{boolean}},
         "EnableNetworkIsolation": {{boolean}},
         "Environment": {
            "{{string}}" : "{{string}}"
         },
         "HyperParameterRanges": {
            "AutoParameters": [
               {
                  "Name": "{{string}}",
                  "ValueHint": "{{string}}"
               }
            ],
            "CategoricalParameterRanges": [
               {
                  "Name": "{{string}}",
                  "Values": [ "{{string}}" ]
               }
            ],
            "ContinuousParameterRanges": [
               {
                  "MaxValue": "{{string}}",
                  "MinValue": "{{string}}",
                  "Name": "{{string}}",
                  "ScalingType": "{{string}}"
               }
            ],
            "IntegerParameterRanges": [
               {
                  "MaxValue": "{{string}}",
                  "MinValue": "{{string}}",
                  "Name": "{{string}}",
                  "ScalingType": "{{string}}"
               }
            ]
         },
         "HyperParameterTuningResourceConfig": {
            "AllocationStrategy": "{{string}}",
            "InstanceConfigs": [
               {
                  "InstanceCount": {{number}},
                  "InstanceType": "{{string}}",
                  "VolumeSizeInGB": {{number}}
               }
            ],
            "InstanceCount": {{number}},
            "InstanceType": "{{string}}",
            "VolumeKmsKeyId": "{{string}}",
            "VolumeSizeInGB": {{number}}
         },
         "InputDataConfig": [
            {
               "ChannelName": "{{string}}",
               "CompressionType": "{{string}}",
               "ContentType": "{{string}}",
               "DataSource": {
                  "DatasetSource": {
                     "DatasetArn": "{{string}}"
                  },
                  "FileSystemDataSource": {
                     "DirectoryPath": "{{string}}",
                     "FileSystemAccessMode": "{{string}}",
                     "FileSystemId": "{{string}}",
                     "FileSystemType": "{{string}}"
                  },
                  "S3DataSource": {
                     "AttributeNames": [ "{{string}}" ],
                     "HubAccessConfig": {
                        "HubContentArn": "{{string}}"
                     },
                     "InstanceGroupNames": [ "{{string}}" ],
                     "ModelAccessConfig": {
                        "AcceptEula": {{boolean}}
                     },
                     "S3DataDistributionType": "{{string}}",
                     "S3DataType": "{{string}}",
                     "S3Uri": "{{string}}"
                  }
               },
               "InputMode": "{{string}}",
               "RecordWrapperType": "{{string}}",
               "ShuffleConfig": {
                  "Seed": {{number}}
               }
            }
         ],
         "OutputDataConfig": {
            "CompressionType": "{{string}}",
            "KmsKeyId": "{{string}}",
            "S3OutputPath": "{{string}}"
         },
         "ResourceConfig": {
            "InstanceCount": {{number}},
            "InstanceGroups": [
               {
                  "InstanceCount": {{number}},
                  "InstanceGroupName": "{{string}}",
                  "InstanceType": "{{string}}"
               }
            ],
            "InstancePlacementConfig": {
               "EnableMultipleJobs": {{boolean}},
               "PlacementSpecifications": [
                  {
                     "InstanceCount": {{number}},
                     "UltraServerId": "{{string}}"
                  }
               ]
            },
            "InstancePreferences": [
               {
                  "InstanceCount": {{number}},
                  "InstanceType": "{{string}}",
                  "TrainingPlanArns": [ "{{string}}" ]
               }
            ],
            "InstanceType": "{{string}}",
            "KeepAlivePeriodInSeconds": {{number}},
            "SelectedInstanceCount": {{number}},
            "SelectedInstanceType": "{{string}}",
            "TrainingPlanArn": "{{string}}",
            "VolumeKmsKeyId": "{{string}}",
            "VolumeSizeInGB": {{number}}
         },
         "RetryStrategy": {
            "MaximumRetryAttempts": {{number}}
         },
         "RoleArn": "{{string}}",
         "StaticHyperParameters": {
            "{{string}}" : "{{string}}"
         },
         "StoppingCondition": {
            "MaxPendingTimeInSeconds": {{number}},
            "MaxRuntimeInSeconds": {{number}},
            "MaxWaitTimeInSeconds": {{number}}
         },
         "TuningObjective": {
            "MetricName": "{{string}}",
            "Type": "{{string}}"
         },
         "VpcConfig": {
            "SecurityGroupIds": [ "{{string}}" ],
            "Subnets": [ "{{string}}" ]
         }
      }
   ],
   "WarmStartConfig": {
      "ParentHyperParameterTuningJobs": [
         {
            "HyperParameterTuningJobName": "{{string}}"
         }
      ],
      "WarmStartType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateHyperParameterTuningJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Autotune](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-Autotune"></a>
Configures SageMaker Automatic model tuning (AMT) to automatically find optimal parameters for the following fields:
+  [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges): The names and ranges of parameters that a hyperparameter tuning job can optimize.
+  [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html): The maximum resources that can be used for a training job. These resources include the maximum number of training jobs, the maximum runtime of a tuning job, and the maximum number of training jobs to run at the same time.
+  [TrainingJobEarlyStoppingType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType): A flag that specifies whether or not to use early stopping for training jobs launched by a hyperparameter tuning job.
+  [RetryStrategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy): The number of times to retry a training job.
+  [Strategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html): Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training jobs that it launches.
+  [ConvergenceDetected](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html): A flag to indicate that Automatic model tuning (AMT) has detected model convergence.
Type: [Autotune](API_Autotune.md) object
Required: No

 ** [HyperParameterTuningJobConfig](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-HyperParameterTuningJobConfig"></a>
The [HyperParameterTuningJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html) object that describes the tuning job, including the search strategy, the objective metric used to evaluate training jobs, ranges of parameters to search, and resource limits for the tuning job. For more information, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html).
Type: [HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md) object
Required: Yes

 ** [HyperParameterTuningJobName](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-HyperParameterTuningJobName"></a>
The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same AWS account and AWS Region. The name must have 1 to 32 characters. Valid characters are a-z, A-Z, 0-9, and : \+ = @ \_ % - (hyphen). The name is not case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** [Tags](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Tags that you specify for the tuning job are also added to all training jobs that the tuning job launches.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrainingJobDefinition](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-TrainingJobDefinition"></a>
The [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) object that describes the training jobs that this tuning job launches, including static hyperparameters, input data configuration, output data configuration, resource configuration, and stopping condition.
Type: [HyperParameterTrainingJobDefinition](API_HyperParameterTrainingJobDefinition.md) object
Required: No

 ** [TrainingJobDefinitions](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-TrainingJobDefinitions"></a>
A list of the [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) objects launched for this tuning job.
Type: Array of [HyperParameterTrainingJobDefinition](API_HyperParameterTrainingJobDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [WarmStartConfig](#API_CreateHyperParameterTuningJob_RequestSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-request-WarmStartConfig"></a>
Specifies the configuration for starting the hyperparameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.
All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric. If you specify `IDENTICAL_DATA_AND_ALGORITHM` as the `WarmStartType` value for the warm start configuration, the training job that performs the best in the new tuning job is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.
All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.
Type: [HyperParameterTuningJobWarmStartConfig](API_HyperParameterTuningJobWarmStartConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateHyperParameterTuningJob_ResponseSyntax"></a>

```
{
   "HyperParameterTuningJobArn": "string"
}
```

## Response Elements
<a name="API_CreateHyperParameterTuningJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HyperParameterTuningJobArn](#API_CreateHyperParameterTuningJob_ResponseSyntax) **   <a name="sagemaker-CreateHyperParameterTuningJob-response-HyperParameterTuningJobArn"></a>
The Amazon Resource Name (ARN) of the tuning job. SageMaker assigns an ARN to a hyperparameter tuning job when you create it.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:hyper-parameter-tuning-job/.*`

## Errors
<a name="API_CreateHyperParameterTuningJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateHyperParameterTuningJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateHyperParameterTuningJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateHyperParameterTuningJob)

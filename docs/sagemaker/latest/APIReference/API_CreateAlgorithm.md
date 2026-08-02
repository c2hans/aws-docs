---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAlgorithm.html
---

# CreateAlgorithm
<a name="API_CreateAlgorithm"></a>

Create a machine learning algorithm that you can use in SageMaker and list in the AWS Marketplace.

## Request Syntax
<a name="API_CreateAlgorithm_RequestSyntax"></a>

```
{
   "AlgorithmDescription": "{{string}}",
   "AlgorithmName": "{{string}}",
   "CertifyForMarketplace": {{boolean}},
   "InferenceSpecification": {
      "Containers": [
         {
            "AdditionalModelDataSources": [
               {
                  "ChannelName": "{{string}}",
                  "S3DataSource": {
                     "CompressionType": "{{string}}",
                     "ETag": "{{string}}",
                     "HubAccessConfig": {
                        "HubContentArn": "{{string}}"
                     },
                     "ManifestEtag": "{{string}}",
                     "ManifestS3Uri": "{{string}}",
                     "ModelAccessConfig": {
                        "AcceptEula": {{boolean}}
                     },
                     "S3DataType": "{{string}}",
                     "S3Uri": "{{string}}"
                  }
               }
            ],
            "AdditionalS3DataSource": {
               "CompressionType": "{{string}}",
               "ETag": "{{string}}",
               "S3DataType": "{{string}}",
               "S3Uri": "{{string}}"
            },
            "BaseModel": {
               "HubContentName": "{{string}}",
               "HubContentVersion": "{{string}}",
               "RecipeName": "{{string}}"
            },
            "ContainerHostname": "{{string}}",
            "Environment": {
               "{{string}}" : "{{string}}"
            },
            "Framework": "{{string}}",
            "FrameworkVersion": "{{string}}",
            "Image": "{{string}}",
            "ImageDigest": "{{string}}",
            "IsCheckpoint": {{boolean}},
            "ModelDataETag": "{{string}}",
            "ModelDataSource": {
               "S3DataSource": {
                  "CompressionType": "{{string}}",
                  "ETag": "{{string}}",
                  "HubAccessConfig": {
                     "HubContentArn": "{{string}}"
                  },
                  "ManifestEtag": "{{string}}",
                  "ManifestS3Uri": "{{string}}",
                  "ModelAccessConfig": {
                     "AcceptEula": {{boolean}}
                  },
                  "S3DataType": "{{string}}",
                  "S3Uri": "{{string}}"
               }
            },
            "ModelDataUrl": "{{string}}",
            "ModelInput": {
               "DataInputConfig": "{{string}}"
            },
            "NearestModelName": "{{string}}",
            "ProductId": "{{string}}"
         }
      ],
      "SupportedContentTypes": [ "{{string}}" ],
      "SupportedRealtimeInferenceInstanceTypes": [ "{{string}}" ],
      "SupportedResponseMIMETypes": [ "{{string}}" ],
      "SupportedTransformInstanceTypes": [ "{{string}}" ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrainingSpecification": {
      "AdditionalS3DataSource": {
         "CompressionType": "{{string}}",
         "ETag": "{{string}}",
         "S3DataType": "{{string}}",
         "S3Uri": "{{string}}"
      },
      "MetricDefinitions": [
         {
            "Name": "{{string}}",
            "Regex": "{{string}}"
         }
      ],
      "SupportedHyperParameters": [
         {
            "DefaultValue": "{{string}}",
            "Description": "{{string}}",
            "IsRequired": {{boolean}},
            "IsTunable": {{boolean}},
            "Name": "{{string}}",
            "Range": {
               "CategoricalParameterRangeSpecification": {
                  "Values": [ "{{string}}" ]
               },
               "ContinuousParameterRangeSpecification": {
                  "MaxValue": "{{string}}",
                  "MinValue": "{{string}}"
               },
               "IntegerParameterRangeSpecification": {
                  "MaxValue": "{{string}}",
                  "MinValue": "{{string}}"
               }
            },
            "Type": "{{string}}"
         }
      ],
      "SupportedTrainingInstanceTypes": [ "{{string}}" ],
      "SupportedTuningJobObjectiveMetrics": [
         {
            "MetricName": "{{string}}",
            "Type": "{{string}}"
         }
      ],
      "SupportsDistributedTraining": {{boolean}},
      "TrainingChannels": [
         {
            "Description": "{{string}}",
            "IsRequired": {{boolean}},
            "Name": "{{string}}",
            "SupportedCompressionTypes": [ "{{string}}" ],
            "SupportedContentTypes": [ "{{string}}" ],
            "SupportedInputModes": [ "{{string}}" ]
         }
      ],
      "TrainingImage": "{{string}}",
      "TrainingImageDigest": "{{string}}"
   },
   "ValidationSpecification": {
      "ValidationProfiles": [
         {
            "ProfileName": "{{string}}",
            "TrainingJobDefinition": {
               "HyperParameters": {
                  "{{string}}" : "{{string}}"
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
                  "InstanceType": "{{string}}",
                  "KeepAlivePeriodInSeconds": {{number}},
                  "TrainingPlanArn": "{{string}}",
                  "VolumeKmsKeyId": "{{string}}",
                  "VolumeSizeInGB": {{number}}
               },
               "StoppingCondition": {
                  "MaxPendingTimeInSeconds": {{number}},
                  "MaxRuntimeInSeconds": {{number}},
                  "MaxWaitTimeInSeconds": {{number}}
               },
               "TrainingInputMode": "{{string}}"
            },
            "TransformJobDefinition": {
               "BatchStrategy": "{{string}}",
               "Environment": {
                  "{{string}}" : "{{string}}"
               },
               "MaxConcurrentTransforms": {{number}},
               "MaxPayloadInMB": {{number}},
               "TransformInput": {
                  "CompressionType": "{{string}}",
                  "ContentType": "{{string}}",
                  "DataSource": {
                     "S3DataSource": {
                        "S3DataType": "{{string}}",
                        "S3Uri": "{{string}}"
                     }
                  },
                  "SplitType": "{{string}}"
               },
               "TransformOutput": {
                  "Accept": "{{string}}",
                  "AssembleWith": "{{string}}",
                  "KmsKeyId": "{{string}}",
                  "S3OutputPath": "{{string}}"
               },
               "TransformResources": {
                  "InstanceCount": {{number}},
                  "InstanceType": "{{string}}",
                  "TransformAmiVersion": "{{string}}",
                  "VolumeKmsKeyId": "{{string}}"
               }
            }
         }
      ],
      "ValidationRole": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateAlgorithm_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlgorithmDescription](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-AlgorithmDescription"></a>
A description of the algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** [AlgorithmName](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-AlgorithmName"></a>
The name of the algorithm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [CertifyForMarketplace](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-CertifyForMarketplace"></a>
Whether to certify the algorithm so that it can be listed in AWS Marketplace.
Type: Boolean
Required: No

 ** [InferenceSpecification](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-InferenceSpecification"></a>
Specifies details about inference jobs that the algorithm runs, including the following:
+ The Amazon ECR paths of containers that contain the inference code and model artifacts.
+ The instance types that the algorithm supports for transform jobs and real-time endpoints used for inference.
+ The input and output content formats that the algorithm supports for inference.
Type: [InferenceSpecification](API_InferenceSpecification.md) object
Required: No

 ** [Tags](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrainingSpecification](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-TrainingSpecification"></a>
Specifies details about training jobs run by this algorithm, including the following:
+ The Amazon ECR path of the container and the version digest of the algorithm.
+ The hyperparameters that the algorithm supports.
+ The instance types that the algorithm supports for training.
+ Whether the algorithm supports distributed training.
+ The metrics that the algorithm emits to Amazon CloudWatch.
+ Which metrics that the algorithm emits can be used as the objective metric for hyperparameter tuning jobs.
+ The input channels that the algorithm supports for training data. For example, an algorithm might support `train`, `validation`, and `test` channels.
Type: [TrainingSpecification](API_TrainingSpecification.md) object
Required: Yes

 ** [ValidationSpecification](#API_CreateAlgorithm_RequestSyntax) **   <a name="sagemaker-CreateAlgorithm-request-ValidationSpecification"></a>
Specifies configurations for one or more training jobs and that SageMaker runs to test the algorithm's training code and, optionally, one or more batch transform jobs that SageMaker runs to test the algorithm's inference code.
Type: [AlgorithmValidationSpecification](API_AlgorithmValidationSpecification.md) object
Required: No

## Response Syntax
<a name="API_CreateAlgorithm_ResponseSyntax"></a>

```
{
   "AlgorithmArn": "string"
}
```

## Response Elements
<a name="API_CreateAlgorithm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlgorithmArn](#API_CreateAlgorithm_ResponseSyntax) **   <a name="sagemaker-CreateAlgorithm-response-AlgorithmArn"></a>
The Amazon Resource Name (ARN) of the new algorithm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:algorithm/[\S]{1,2048}`

## Errors
<a name="API_CreateAlgorithm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateAlgorithm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAlgorithm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAlgorithm)

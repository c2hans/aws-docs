---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAlgorithm.html
---

# DescribeAlgorithm
<a name="API_DescribeAlgorithm"></a>

Returns a description of the specified algorithm that is in your account.

## Request Syntax
<a name="API_DescribeAlgorithm_RequestSyntax"></a>

```
{
   "AlgorithmName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAlgorithm_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlgorithmName](#API_DescribeAlgorithm_RequestSyntax) **   <a name="sagemaker-DescribeAlgorithm-request-AlgorithmName"></a>
The name of the algorithm to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: Yes

## Response Syntax
<a name="API_DescribeAlgorithm_ResponseSyntax"></a>

```
{
   "AlgorithmArn": "string",
   "AlgorithmDescription": "string",
   "AlgorithmName": "string",
   "AlgorithmStatus": "string",
   "AlgorithmStatusDetails": {
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
   "CertifyForMarketplace": boolean,
   "CreationTime": number,
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
   "ProductId": "string",
   "TrainingSpecification": {
      "AdditionalS3DataSource": {
         "CompressionType": "string",
         "ETag": "string",
         "S3DataType": "string",
         "S3Uri": "string"
      },
      "MetricDefinitions": [
         {
            "Name": "string",
            "Regex": "string"
         }
      ],
      "SupportedHyperParameters": [
         {
            "DefaultValue": "string",
            "Description": "string",
            "IsRequired": boolean,
            "IsTunable": boolean,
            "Name": "string",
            "Range": {
               "CategoricalParameterRangeSpecification": {
                  "Values": [ "string" ]
               },
               "ContinuousParameterRangeSpecification": {
                  "MaxValue": "string",
                  "MinValue": "string"
               },
               "IntegerParameterRangeSpecification": {
                  "MaxValue": "string",
                  "MinValue": "string"
               }
            },
            "Type": "string"
         }
      ],
      "SupportedTrainingInstanceTypes": [ "string" ],
      "SupportedTuningJobObjectiveMetrics": [
         {
            "MetricName": "string",
            "Type": "string"
         }
      ],
      "SupportsDistributedTraining": boolean,
      "TrainingChannels": [
         {
            "Description": "string",
            "IsRequired": boolean,
            "Name": "string",
            "SupportedCompressionTypes": [ "string" ],
            "SupportedContentTypes": [ "string" ],
            "SupportedInputModes": [ "string" ]
         }
      ],
      "TrainingImage": "string",
      "TrainingImageDigest": "string"
   },
   "ValidationSpecification": {
      "ValidationProfiles": [
         {
            "ProfileName": "string",
            "TrainingJobDefinition": {
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
               "StoppingCondition": {
                  "MaxPendingTimeInSeconds": number,
                  "MaxRuntimeInSeconds": number,
                  "MaxWaitTimeInSeconds": number
               },
               "TrainingInputMode": "string"
            },
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
}
```

## Response Elements
<a name="API_DescribeAlgorithm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlgorithmArn](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-AlgorithmArn"></a>
The Amazon Resource Name (ARN) of the algorithm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:algorithm/[\S]{1,2048}`

 ** [AlgorithmDescription](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-AlgorithmDescription"></a>
A brief summary about the algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

 ** [AlgorithmName](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-AlgorithmName"></a>
The name of the algorithm being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AlgorithmStatus](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-AlgorithmStatus"></a>
The current status of the algorithm.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting`

 ** [AlgorithmStatusDetails](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-AlgorithmStatusDetails"></a>
Details about the current status of the algorithm.
Type: [AlgorithmStatusDetails](API_AlgorithmStatusDetails.md) object

 ** [CertifyForMarketplace](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-CertifyForMarketplace"></a>
Whether the algorithm is certified to be listed in AWS Marketplace.
Type: Boolean

 ** [CreationTime](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-CreationTime"></a>
A timestamp specifying when the algorithm was created.
Type: Timestamp

 ** [InferenceSpecification](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-InferenceSpecification"></a>
Details about inference jobs that the algorithm runs.
Type: [InferenceSpecification](API_InferenceSpecification.md) object

 ** [ProductId](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-ProductId"></a>
The product identifier of the algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [TrainingSpecification](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-TrainingSpecification"></a>
Details about training jobs run by this algorithm.
Type: [TrainingSpecification](API_TrainingSpecification.md) object

 ** [ValidationSpecification](#API_DescribeAlgorithm_ResponseSyntax) **   <a name="sagemaker-DescribeAlgorithm-response-ValidationSpecification"></a>
Details about configurations for one or more training jobs that SageMaker runs to test the algorithm.
Type: [AlgorithmValidationSpecification](API_AlgorithmValidationSpecification.md) object

## Errors
<a name="API_DescribeAlgorithm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeAlgorithm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAlgorithm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAlgorithm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

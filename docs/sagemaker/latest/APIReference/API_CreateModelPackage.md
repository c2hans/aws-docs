---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html
---

# CreateModelPackage
<a name="API_CreateModelPackage"></a>

Creates a model package that you can use to create SageMaker models or list on AWS Marketplace, or a versioned model that is part of a model group. Buyers can subscribe to model packages listed on AWS Marketplace to create models in SageMaker.

To create a model package by specifying a Docker container that contains your inference code and the Amazon S3 location of your model artifacts, provide values for `InferenceSpecification`. To create a model from an algorithm resource that you created or subscribed to in AWS Marketplace, provide a value for `SourceAlgorithmSpecification`.

**Note**
There are two types of model packages:
Versioned - a model that is part of a model group in the model registry.
Unversioned - a model package that is not part of a model group.

## Request Syntax
<a name="API_CreateModelPackage_RequestSyntax"></a>

```
{
   "AdditionalInferenceSpecifications": [
      {
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
         "Description": "{{string}}",
         "Name": "{{string}}",
         "SupportedContentTypes": [ "{{string}}" ],
         "SupportedRealtimeInferenceInstanceTypes": [ "{{string}}" ],
         "SupportedResponseMIMETypes": [ "{{string}}" ],
         "SupportedTransformInstanceTypes": [ "{{string}}" ]
      }
   ],
   "CertifyForMarketplace": {{boolean}},
   "ClientToken": "{{string}}",
   "CustomerMetadataProperties": {
      "{{string}}" : "{{string}}"
   },
   "Domain": "{{string}}",
   "DriftCheckBaselines": {
      "Bias": {
         "ConfigFile": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "PostTrainingConstraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "PreTrainingConstraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "Explainability": {
         "ConfigFile": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "Constraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "ModelDataQuality": {
         "Constraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "Statistics": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "ModelQuality": {
         "Constraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "Statistics": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      }
   },
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
   "ManagedStorageType": "{{string}}",
   "MetadataProperties": {
      "CommitId": "{{string}}",
      "GeneratedBy": "{{string}}",
      "ProjectId": "{{string}}",
      "Repository": "{{string}}"
   },
   "ModelApprovalStatus": "{{string}}",
   "ModelCard": {
      "ModelCardContent": "{{string}}",
      "ModelCardStatus": "{{string}}"
   },
   "ModelLifeCycle": {
      "Stage": "{{string}}",
      "StageDescription": "{{string}}",
      "StageStatus": "{{string}}"
   },
   "ModelMetrics": {
      "Bias": {
         "PostTrainingReport": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "PreTrainingReport": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "Report": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "Explainability": {
         "Report": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "ModelDataQuality": {
         "Constraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "Statistics": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "ModelQuality": {
         "Constraints": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "Statistics": {
            "ContentDigest": "{{string}}",
            "ContentType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      }
   },
   "ModelPackageDescription": "{{string}}",
   "ModelPackageGroupName": "{{string}}",
   "ModelPackageName": "{{string}}",
   "ModelPackageRegistrationType": "{{string}}",
   "SamplePayloadUrl": "{{string}}",
   "SecurityConfig": {
      "KmsKeyId": "{{string}}"
   },
   "SkipModelValidation": "{{string}}",
   "SourceAlgorithmSpecification": {
      "SourceAlgorithms": [
         {
            "AlgorithmName": "{{string}}",
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
            "ModelDataUrl": "{{string}}"
         }
      ]
   },
   "SourceUri": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Task": "{{string}}",
   "ValidationSpecification": {
      "ValidationProfiles": [
         {
            "ProfileName": "{{string}}",
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
<a name="API_CreateModelPackage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdditionalInferenceSpecifications](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-AdditionalInferenceSpecifications"></a>
An array of additional Inference Specification objects. Each additional Inference Specification specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.
Type: Array of [AdditionalInferenceSpecificationDefinition](API_AdditionalInferenceSpecificationDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** [CertifyForMarketplace](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-CertifyForMarketplace"></a>
Whether to certify the model package for listing on AWS Marketplace.
This parameter is optional for unversioned models, and does not apply to versioned models.
Type: Boolean
Required: No

 ** [ClientToken](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [CustomerMetadataProperties](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-CustomerMetadataProperties"></a>
The metadata properties associated with the model package versions.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,128}`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,256}`
Required: No

 ** [Domain](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-Domain"></a>
The machine learning domain of your model package and its components. Common machine learning domains include computer vision and natural language processing.
Type: String
Required: No

 ** [DriftCheckBaselines](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-DriftCheckBaselines"></a>
Represents the drift check baselines that can be used when the model monitor is set using the model package. For more information, see the topic on [Drift Detection against Previous Baselines in SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html#pipelines-quality-clarify-baseline-drift-detection) in the *Amazon SageMaker Developer Guide*.
Type: [DriftCheckBaselines](API_DriftCheckBaselines.md) object
Required: No

 ** [InferenceSpecification](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-InferenceSpecification"></a>
Specifies details about inference jobs that you can run with models based on this model package, including the following information:
+ The Amazon ECR paths of containers that contain the inference code and model artifacts.
+ The instance types that the model package supports for transform jobs and real-time endpoints used for inference.
+ The input and output content formats that the model package supports for inference.
Type: [InferenceSpecification](API_InferenceSpecification.md) object
Required: No

 ** [ManagedStorageType](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ManagedStorageType"></a>
The storage type of the model package.
Type: String
Valid Values: `Restricted`
Required: No

 ** [MetadataProperties](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** [ModelApprovalStatus](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelApprovalStatus"></a>
Whether the model is approved for deployment.
This parameter is optional for versioned models, and does not apply to unversioned models.
For versioned models, the value of this parameter must be set to `Approved` to deploy the model.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`
Required: No

 ** [ModelCard](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelCard"></a>
The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard`. The `ModelPackageModelCard` schema does not include `model_package_details`, and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema). For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html).
Type: [ModelPackageModelCard](API_ModelPackageModelCard.md) object
Required: No

 ** [ModelLifeCycle](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelLifeCycle"></a>
 A structure describing the current state of the model in its life cycle.
Type: [ModelLifeCycle](API_ModelLifeCycle.md) object
Required: No

 ** [ModelMetrics](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelMetrics"></a>
A structure that contains model metrics reports.
Type: [ModelMetrics](API_ModelMetrics.md) object
Required: No

 ** [ModelPackageDescription](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelPackageDescription"></a>
A description of the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** [ModelPackageGroupName](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelPackageGroupName"></a>
The name or Amazon Resource Name (ARN) of the model package group that this model version belongs to.
This parameter is required for versioned models, and does not apply to unversioned models.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: No

 ** [ModelPackageName](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelPackageName"></a>
The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
This parameter is required for unversioned models. It is not applicable to versioned models.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [ModelPackageRegistrationType](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ModelPackageRegistrationType"></a>
 The package registration type of the model package input.
Type: String
Valid Values: `Logged | Registered`
Required: No

 ** [SamplePayloadUrl](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-SamplePayloadUrl"></a>
The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). This archive can hold multiple files that are all equally used in the load test. Each file in the archive must satisfy the size constraints of the [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html#API_runtime_InvokeEndpoint_RequestSyntax) call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** [SecurityConfig](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-SecurityConfig"></a>
The AWS KMS Key ID (`KMSKeyId`) used for encryption of model package information.
Type: [ModelPackageSecurityConfig](API_ModelPackageSecurityConfig.md) object
Required: No

 ** [SkipModelValidation](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-SkipModelValidation"></a>
Indicates if you want to skip model validation.
Type: String
Valid Values: `All | None`
Required: No

 ** [SourceAlgorithmSpecification](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-SourceAlgorithmSpecification"></a>
Details about the algorithm that was used to create the model package.
Type: [SourceAlgorithmSpecification](API_SourceAlgorithmSpecification.md) object
Required: No

 ** [SourceUri](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-SourceUri"></a>
The URI of the source for the model package. If you want to clone a model package, set it to the model package Amazon Resource Name (ARN). If you want to register a model, set it to the model ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{N}\p{P}]{0,1024}`
Required: No

 ** [Tags](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-Tags"></a>
A list of key value pairs associated with the model. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
If you supply `ModelPackageGroupName`, your model package belongs to the model group you specify and uses the tags associated with the model group. In this case, you cannot supply a `tag` argument.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Task](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-Task"></a>
The machine learning task your model package accomplishes. Common machine learning tasks include object detection and image classification. The following tasks are supported by Inference Recommender: `"IMAGE_CLASSIFICATION"` \| `"OBJECT_DETECTION"` \| `"TEXT_GENERATION"` \|`"IMAGE_SEGMENTATION"` \| `"FILL_MASK"` \| `"CLASSIFICATION"` \| `"REGRESSION"` \| `"OTHER"`.
Specify "OTHER" if none of the tasks listed fit your use case.
Type: String
Required: No

 ** [ValidationSpecification](#API_CreateModelPackage_RequestSyntax) **   <a name="sagemaker-CreateModelPackage-request-ValidationSpecification"></a>
Specifies configurations for one or more transform jobs that SageMaker runs to test the model package.
Type: [ModelPackageValidationSpecification](API_ModelPackageValidationSpecification.md) object
Required: No

## Response Syntax
<a name="API_CreateModelPackage_ResponseSyntax"></a>

```
{
   "ModelPackageArn": "string"
}
```

## Response Elements
<a name="API_CreateModelPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelPackageArn](#API_CreateModelPackage_ResponseSyntax) **   <a name="sagemaker-CreateModelPackage-response-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the new model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

## Errors
<a name="API_CreateModelPackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateModelPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateModelPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateModelPackage)

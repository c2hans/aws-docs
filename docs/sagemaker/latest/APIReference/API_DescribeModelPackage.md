---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelPackage.html
---

# DescribeModelPackage
<a name="API_DescribeModelPackage"></a>

Returns a description of the specified model package, which is used to create SageMaker models or list them on AWS Marketplace.

**Important**
If you provided a AWS KMS Key ID when you created your model package, you will see the [KMS Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) API call in your CloudTrail logs when you use this API. To call this operation without requiring `kms:Decrypt` permission on the customer-managed key, set `IncludedData` to `MetadataOnly`; the response is returned with the embedded `ModelCard.ModelCardContent` field sanitized.

To create models in SageMaker, buyers can subscribe to model packages listed on AWS Marketplace.

## Request Syntax
<a name="API_DescribeModelPackage_RequestSyntax"></a>

```
{
   "IncludedData": "{{string}}",
   "ModelPackageName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelPackage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludedData](#API_DescribeModelPackage_RequestSyntax) **   <a name="sagemaker-DescribeModelPackage-request-IncludedData"></a>
Specifies the level of model package data to include in the response. Use this parameter to call `DescribeModelPackage` on a model package that has an associated model card without requiring `kms:Decrypt` permission on the customer-managed AWS KMS key associated with the embedded model card.
+  `AllData`: Returns the full model package response, including the unredacted `ModelCard.ModelCardContent`. This option requires `kms:Decrypt` permission on the customer-managed key, if one is associated with the embedded model card. This is the default.
+  `MetadataOnly`: Returns the full model package response, but with the embedded `ModelCard.ModelCardContent` sanitized to include only a small set of unencrypted metadata fields. This option does not require `kms:Decrypt` permission. All other top-level response fields, including `InferenceSpecification`, `ModelMetrics`, `DriftCheckBaselines`, and `SecurityConfig`, are returned unchanged. For the list of fields preserved within `ModelCardContent`, see [ModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelPackage.html#sagemaker-DescribeModelPackage-response-ModelCard).
If you don't specify a value, SageMaker returns `AllData`.
Type: String
Valid Values: `AllData | MetadataOnly`
Required: No

 ** [ModelPackageName](#API_DescribeModelPackage_RequestSyntax) **   <a name="sagemaker-DescribeModelPackage-request-ModelPackageName"></a>
The name or Amazon Resource Name (ARN) of the model package to describe.
When you specify a name, the name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 176.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)(\/[0-9]{1,9})?`
Required: Yes

## Response Syntax
<a name="API_DescribeModelPackage_ResponseSyntax"></a>

```
{
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
   "ManagedStorageType": "string",
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
}
```

## Response Elements
<a name="API_DescribeModelPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdditionalInferenceSpecifications](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-AdditionalInferenceSpecifications"></a>
An array of additional Inference Specification objects. Each additional Inference Specification specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.
Type: Array of [AdditionalInferenceSpecificationDefinition](API_AdditionalInferenceSpecificationDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.

 ** [ApprovalDescription](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ApprovalDescription"></a>
A description provided for the model approval.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`

 ** [CertifyForMarketplace](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-CertifyForMarketplace"></a>
Whether the model package is certified for listing on AWS Marketplace.
Type: Boolean

 ** [CreatedBy](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-CreationTime"></a>
A timestamp specifying when the model package was created.
Type: Timestamp

 ** [CustomerMetadataProperties](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-CustomerMetadataProperties"></a>
The metadata properties associated with the model package versions.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,128}`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,256}`

 ** [Domain](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-Domain"></a>
The machine learning domain of the model package you specified. Common machine learning domains include computer vision and natural language processing.
Type: String

 ** [DriftCheckBaselines](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-DriftCheckBaselines"></a>
Represents the drift check baselines that can be used when the model monitor is set using the model package. For more information, see the topic on [Drift Detection against Previous Baselines in SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html#pipelines-quality-clarify-baseline-drift-detection) in the *Amazon SageMaker Developer Guide*.
Type: [DriftCheckBaselines](API_DriftCheckBaselines.md) object

 ** [InferenceSpecification](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-InferenceSpecification"></a>
Details about inference jobs that you can run with models based on this model package.
Type: [InferenceSpecification](API_InferenceSpecification.md) object

 ** [LastModifiedBy](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [ManagedStorageType](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ManagedStorageType"></a>
The storage type of the model package.
Type: String
Valid Values: `Restricted`

 ** [MetadataProperties](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object

 ** [ModelApprovalStatus](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelApprovalStatus"></a>
The approval status of the model package.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`

 ** [ModelCard](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelCard"></a>
The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard`. The `ModelPackageModelCard` schema does not include `model_package_details`, and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema). For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html).
When you set `IncludedData` to `MetadataOnly` in the request, `ModelCardStatus` is preserved and `ModelCardContent` is sanitized to include only the following JSON paths, when present in the model card:
+  `model_overview.model_id`
+  `model_overview.model_name`
+  `intended_uses.risk_rating`
+  `model_package_details.model_package_group_name`
+  `model_package_details.model_package_arn`
Because the `ModelPackageModelCard` schema does not include `model_package_details` and limits `model_overview` to `model_creator` and `model_artifact`, the sanitized `ModelCardContent` for a model package typically contains only `intended_uses.risk_rating` if it was provided when the model card was created. To retrieve the complete `ModelCardContent`, set `IncludedData` to `AllData` or omit the parameter.
Type: [ModelPackageModelCard](API_ModelPackageModelCard.md) object

 ** [ModelLifeCycle](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelLifeCycle"></a>
 A structure describing the current state of the model in its life cycle.
Type: [ModelLifeCycle](API_ModelLifeCycle.md) object

 ** [ModelMetrics](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelMetrics"></a>
Metrics for the model.
Type: [ModelMetrics](API_ModelMetrics.md) object

 ** [ModelPackageArn](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

 ** [ModelPackageDescription](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageDescription"></a>
A brief summary of the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

 ** [ModelPackageGroupName](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageGroupName"></a>
If the model is a versioned model, the name of the model group that the versioned model belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelPackageName](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageName"></a>
The name of the model package being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelPackageRegistrationType](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageRegistrationType"></a>
 The package registration type of the model package output.
Type: String
Valid Values: `Logged | Registered`

 ** [ModelPackageStatus](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageStatus"></a>
The current status of the model package.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting`

 ** [ModelPackageStatusDetails](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageStatusDetails"></a>
Details about the current status of the model package.
Type: [ModelPackageStatusDetails](API_ModelPackageStatusDetails.md) object

 ** [ModelPackageVersion](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ModelPackageVersion"></a>
The version of the model package.
Type: Integer
Valid Range: Minimum value of 1.

 ** [SamplePayloadUrl](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-SamplePayloadUrl"></a>
The Amazon Simple Storage Service (Amazon S3) path where the sample payload are stored. This path points to a single gzip compressed tar archive (.tar.gz suffix).
Type: String

 ** [SecurityConfig](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-SecurityConfig"></a>
The AWS KMS Key ID (`KMSKeyId`) used for encryption of model package information.
Type: [ModelPackageSecurityConfig](API_ModelPackageSecurityConfig.md) object

 ** [SkipModelValidation](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-SkipModelValidation"></a>
Indicates if you want to skip model validation.
Type: String
Valid Values: `All | None`

 ** [SourceAlgorithmSpecification](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-SourceAlgorithmSpecification"></a>
Details about the algorithm that was used to create the model package.
Type: [SourceAlgorithmSpecification](API_SourceAlgorithmSpecification.md) object

 ** [SourceUri](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-SourceUri"></a>
The URI of the source for the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{N}\p{P}]{0,1024}`

 ** [Task](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-Task"></a>
The machine learning task you specified that your model package accomplishes. Common machine learning tasks include object detection and image classification.
Type: String

 ** [ValidationSpecification](#API_DescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackage-response-ValidationSpecification"></a>
Configurations for one or more transform jobs that SageMaker runs to test the model package.
Type: [ModelPackageValidationSpecification](API_ModelPackageValidationSpecification.md) object

## Errors
<a name="API_DescribeModelPackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeModelPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelPackage)

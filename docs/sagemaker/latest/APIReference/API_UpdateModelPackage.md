---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelPackage.html
---

# UpdateModelPackage
<a name="API_UpdateModelPackage"></a>

Updates a versioned model.

## Request Syntax
<a name="API_UpdateModelPackage_RequestSyntax"></a>

```
{
   "AdditionalInferenceSpecificationsToAdd": [
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
   "ApprovalDescription": "{{string}}",
   "ClientToken": "{{string}}",
   "CustomerMetadataProperties": {
      "{{string}}" : "{{string}}"
   },
   "CustomerMetadataPropertiesToRemove": [ "{{string}}" ],
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
   "ModelPackageArn": "{{string}}",
   "ModelPackageRegistrationType": "{{string}}",
   "SourceUri": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateModelPackage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdditionalInferenceSpecificationsToAdd](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-AdditionalInferenceSpecificationsToAdd"></a>
An array of additional Inference Specification objects to be added to the existing array additional Inference Specification. Total number of additional Inference Specifications can not exceed 15. Each additional Inference Specification specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.
Type: Array of [AdditionalInferenceSpecificationDefinition](API_AdditionalInferenceSpecificationDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** [ApprovalDescription](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ApprovalDescription"></a>
A description for the approval status of the model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [ClientToken](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ClientToken"></a>
 A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [CustomerMetadataProperties](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-CustomerMetadataProperties"></a>
The metadata properties associated with the model package versions.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,128}`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,256}`
Required: No

 ** [CustomerMetadataPropertiesToRemove](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-CustomerMetadataPropertiesToRemove"></a>
The metadata properties associated with the model package versions to remove.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,128}`
Required: No

 ** [InferenceSpecification](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-InferenceSpecification"></a>
Specifies details about inference jobs that you can run with models based on this model package, including the following information:
+ The Amazon ECR paths of containers that contain the inference code and model artifacts.
+ The instance types that the model package supports for transform jobs and real-time endpoints used for inference.
+ The input and output content formats that the model package supports for inference.
Type: [InferenceSpecification](API_InferenceSpecification.md) object
Required: No

 ** [ModelApprovalStatus](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ModelApprovalStatus"></a>
The approval status of the model.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`
Required: No

 ** [ModelCard](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ModelCard"></a>
The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard`. The `ModelPackageModelCard` schema does not include `model_package_details`, and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema). For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html).
Type: [ModelPackageModelCard](API_ModelPackageModelCard.md) object
Required: No

 ** [ModelLifeCycle](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ModelLifeCycle"></a>
 A structure describing the current state of the model in its life cycle.
Type: [ModelLifeCycle](API_ModelLifeCycle.md) object
Required: No

 ** [ModelPackageArn](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: Yes

 ** [ModelPackageRegistrationType](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-ModelPackageRegistrationType"></a>
 The package registration type of the model package input.
Type: String
Valid Values: `Logged | Registered`
Required: No

 ** [SourceUri](#API_UpdateModelPackage_RequestSyntax) **   <a name="sagemaker-UpdateModelPackage-request-SourceUri"></a>
The URI of the source for the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{N}\p{P}]{0,1024}`
Required: No

## Response Syntax
<a name="API_UpdateModelPackage_ResponseSyntax"></a>

```
{
   "ModelPackageArn": "string"
}
```

## Response Elements
<a name="API_UpdateModelPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelPackageArn](#API_UpdateModelPackage_ResponseSyntax) **   <a name="sagemaker-UpdateModelPackage-response-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

## Errors
<a name="API_UpdateModelPackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

## See Also
<a name="API_UpdateModelPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateModelPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateModelPackage)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDescribeModelPackage.html
---

# BatchDescribeModelPackage
<a name="API_BatchDescribeModelPackage"></a>

This action batch describes a list of versioned model packages

## Request Syntax
<a name="API_BatchDescribeModelPackage_RequestSyntax"></a>

```
{
   "ModelPackageArnList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDescribeModelPackage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelPackageArnList](#API_BatchDescribeModelPackage_RequestSyntax) **   <a name="sagemaker-BatchDescribeModelPackage-request-ModelPackageArnList"></a>
The list of Amazon Resource Name (ARN) of the model package groups.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: Yes

## Response Syntax
<a name="API_BatchDescribeModelPackage_ResponseSyntax"></a>

```
{
   "BatchDescribeModelPackageErrorMap": {
      "string" : {
         "ErrorCode": "string",
         "ErrorResponse": "string"
      }
   },
   "ModelPackageSummaries": {
      "string" : {
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
         "ModelApprovalStatus": "string",
         "ModelPackageArn": "string",
         "ModelPackageDescription": "string",
         "ModelPackageGroupName": "string",
         "ModelPackageRegistrationType": "string",
         "ModelPackageStatus": "string",
         "ModelPackageVersion": number
      }
   }
}
```

## Response Elements
<a name="API_BatchDescribeModelPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BatchDescribeModelPackageErrorMap](#API_BatchDescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-BatchDescribeModelPackage-response-BatchDescribeModelPackageErrorMap"></a>
A map of the resource and BatchDescribeModelPackageError objects reporting the error associated with describing the model package.
Type: String to [BatchDescribeModelPackageError](API_BatchDescribeModelPackageError.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Key Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

 ** [ModelPackageSummaries](#API_BatchDescribeModelPackage_ResponseSyntax) **   <a name="sagemaker-BatchDescribeModelPackage-response-ModelPackageSummaries"></a>
The summaries for the model package versions
Type: String to [BatchDescribeModelPackageSummary](API_BatchDescribeModelPackageSummary.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Key Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

## Errors
<a name="API_BatchDescribeModelPackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchDescribeModelPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/BatchDescribeModelPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchDescribeModelPackage)

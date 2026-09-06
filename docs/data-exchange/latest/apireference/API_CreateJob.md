---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateJob.html
---

# CreateJob
<a name="API_CreateJob"></a>

This operation creates a job.

## Request Syntax
<a name="API_CreateJob_RequestSyntax"></a>

```
POST /v1/jobs HTTP/1.1
Content-type: application/json

{
   "AssetConfiguration": {
      "Tags": [
         {
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "Details": {
      "CreateS3DataAccessFromS3Bucket": {
         "AssetSource": {
            "Bucket": "{{string}}",
            "KeyPrefixes": [ "{{string}}" ],
            "Keys": [ "{{string}}" ],
            "KmsKeysToGrant": [
               {
                  "KmsKeyArn": "{{string}}"
               }
            ]
         },
         "DataSetId": "{{string}}",
         "RevisionId": "{{string}}"
      },
      "ExportAssetsToS3": {
         "AssetDestinations": [
            {
               "AssetId": "{{string}}",
               "Bucket": "{{string}}",
               "Key": "{{string}}"
            }
         ],
         "DataSetId": "{{string}}",
         "Encryption": {
            "KmsKeyArn": "{{string}}",
            "Type": "{{string}}"
         },
         "RevisionId": "{{string}}"
      },
      "ExportAssetToSignedUrl": {
         "AssetId": "{{string}}",
         "DataSetId": "{{string}}",
         "RevisionId": "{{string}}"
      },
      "ExportRevisionsToS3": {
         "DataSetId": "{{string}}",
         "Encryption": {
            "KmsKeyArn": "{{string}}",
            "Type": "{{string}}"
         },
         "RevisionDestinations": [
            {
               "Bucket": "{{string}}",
               "KeyPattern": "{{string}}",
               "RevisionId": "{{string}}"
            }
         ]
      },
      "ImportAssetFromApiGatewayApi": {
         "ApiDescription": "{{string}}",
         "ApiId": "{{string}}",
         "ApiKey": "{{string}}",
         "ApiName": "{{string}}",
         "ApiSpecificationMd5Hash": "{{string}}",
         "DataSetId": "{{string}}",
         "ProtocolType": "{{string}}",
         "RevisionId": "{{string}}",
         "Stage": "{{string}}"
      },
      "ImportAssetFromSignedUrl": {
         "AssetName": "{{string}}",
         "DataSetId": "{{string}}",
         "Md5Hash": "{{string}}",
         "RevisionId": "{{string}}"
      },
      "ImportAssetsFromLakeFormationTagPolicy": {
         "CatalogId": "{{string}}",
         "Database": {
            "Expression": [
               {
                  "TagKey": "{{string}}",
                  "TagValues": [ "{{string}}" ]
               }
            ],
            "Permissions": [ "{{string}}" ]
         },
         "DataSetId": "{{string}}",
         "RevisionId": "{{string}}",
         "RoleArn": "{{string}}",
         "Table": {
            "Expression": [
               {
                  "TagKey": "{{string}}",
                  "TagValues": [ "{{string}}" ]
               }
            ],
            "Permissions": [ "{{string}}" ]
         }
      },
      "ImportAssetsFromRedshiftDataShares": {
         "AssetSources": [
            {
               "DataShareArn": "{{string}}"
            }
         ],
         "DataSetId": "{{string}}",
         "RevisionId": "{{string}}"
      },
      "ImportAssetsFromS3": {
         "AssetSources": [
            {
               "Bucket": "{{string}}",
               "Key": "{{string}}"
            }
         ],
         "DataSetId": "{{string}}",
         "RevisionId": "{{string}}"
      }
   },
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssetConfiguration](#API_CreateJob_RequestSyntax) **   <a name="dataexchange-CreateJob-request-AssetConfiguration"></a>
The configuration for the asset, including tags to be applied to assets created by the job.
Type: [AssetConfiguration](API_AssetConfiguration.md) object
Required: No

 ** [Details](#API_CreateJob_RequestSyntax) **   <a name="dataexchange-CreateJob-request-Details"></a>
The details for the CreateJob request.
Type: [RequestDetails](API_RequestDetails.md) object
Required: Yes

 ** [Type](#API_CreateJob_RequestSyntax) **   <a name="dataexchange-CreateJob-request-Type"></a>
The type of job to be created.
Type: String
Valid Values: `IMPORT_ASSETS_FROM_S3 | IMPORT_ASSET_FROM_SIGNED_URL | EXPORT_ASSETS_TO_S3 | EXPORT_ASSET_TO_SIGNED_URL | EXPORT_REVISIONS_TO_S3 | IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES | IMPORT_ASSET_FROM_API_GATEWAY_API | CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET | IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY`
Required: Yes

## Response Syntax
<a name="API_CreateJob_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "AssetConfiguration": {
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "CreatedAt": "string",
   "Details": {
      "CreateS3DataAccessFromS3Bucket": {
         "AssetSource": {
            "Bucket": "string",
            "KeyPrefixes": [ "string" ],
            "Keys": [ "string" ],
            "KmsKeysToGrant": [
               {
                  "KmsKeyArn": "string"
               }
            ]
         },
         "DataSetId": "string",
         "RevisionId": "string"
      },
      "ExportAssetsToS3": {
         "AssetDestinations": [
            {
               "AssetId": "string",
               "Bucket": "string",
               "Key": "string"
            }
         ],
         "DataSetId": "string",
         "Encryption": {
            "KmsKeyArn": "string",
            "Type": "string"
         },
         "RevisionId": "string"
      },
      "ExportAssetToSignedUrl": {
         "AssetId": "string",
         "DataSetId": "string",
         "RevisionId": "string",
         "SignedUrl": "string",
         "SignedUrlExpiresAt": "string"
      },
      "ExportRevisionsToS3": {
         "DataSetId": "string",
         "Encryption": {
            "KmsKeyArn": "string",
            "Type": "string"
         },
         "EventActionArn": "string",
         "RevisionDestinations": [
            {
               "Bucket": "string",
               "KeyPattern": "string",
               "RevisionId": "string"
            }
         ]
      },
      "ImportAssetFromApiGatewayApi": {
         "ApiDescription": "string",
         "ApiId": "string",
         "ApiKey": "string",
         "ApiName": "string",
         "ApiSpecificationMd5Hash": "string",
         "ApiSpecificationUploadUrl": "string",
         "ApiSpecificationUploadUrlExpiresAt": "string",
         "DataSetId": "string",
         "ProtocolType": "string",
         "RevisionId": "string",
         "Stage": "string"
      },
      "ImportAssetFromSignedUrl": {
         "AssetName": "string",
         "DataSetId": "string",
         "Md5Hash": "string",
         "RevisionId": "string",
         "SignedUrl": "string",
         "SignedUrlExpiresAt": "string"
      },
      "ImportAssetsFromLakeFormationTagPolicy": {
         "CatalogId": "string",
         "Database": {
            "Expression": [
               {
                  "TagKey": "string",
                  "TagValues": [ "string" ]
               }
            ],
            "Permissions": [ "string" ]
         },
         "DataSetId": "string",
         "RevisionId": "string",
         "RoleArn": "string",
         "Table": {
            "Expression": [
               {
                  "TagKey": "string",
                  "TagValues": [ "string" ]
               }
            ],
            "Permissions": [ "string" ]
         }
      },
      "ImportAssetsFromRedshiftDataShares": {
         "AssetSources": [
            {
               "DataShareArn": "string"
            }
         ],
         "DataSetId": "string",
         "RevisionId": "string"
      },
      "ImportAssetsFromS3": {
         "AssetSources": [
            {
               "Bucket": "string",
               "Key": "string"
            }
         ],
         "DataSetId": "string",
         "RevisionId": "string"
      }
   },
   "Errors": [
      {
         "Code": "string",
         "Details": {
            "ImportAssetFromSignedUrlJobErrorDetails": {
               "AssetName": "string"
            },
            "ImportAssetsFromS3JobErrorDetails": [
               {
                  "Bucket": "string",
                  "Key": "string"
               }
            ]
         },
         "LimitName": "string",
         "LimitValue": number,
         "Message": "string",
         "ResourceId": "string",
         "ResourceType": "string"
      }
   ],
   "Id": "string",
   "State": "string",
   "Type": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_CreateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-Arn"></a>
The ARN for the job.
Type: String

 ** [AssetConfiguration](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-AssetConfiguration"></a>
The configuration for the asset, including tags applied to assets created by the job.
Type: [AssetConfiguration](API_AssetConfiguration.md) object

 ** [CreatedAt](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-CreatedAt"></a>
The date and time that the job was created, in ISO 8601 format.
Type: Timestamp

 ** [Details](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-Details"></a>
Details about the job.
Type: [ResponseDetails](API_ResponseDetails.md) object

 ** [Errors](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-Errors"></a>
The errors associated with jobs.
Type: Array of [JobError](API_JobError.md) objects

 ** [Id](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-Id"></a>
The unique identifier for the job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [State](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-State"></a>
The state of the job.
Type: String
Valid Values: `WAITING | IN_PROGRESS | ERROR | COMPLETED | CANCELLED | TIMED_OUT`

 ** [Type](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-Type"></a>
The job type.
Type: String
Valid Values: `IMPORT_ASSETS_FROM_S3 | IMPORT_ASSET_FROM_SIGNED_URL | EXPORT_ASSETS_TO_S3 | EXPORT_ASSET_TO_SIGNED_URL | EXPORT_REVISIONS_TO_S3 | IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES | IMPORT_ASSET_FROM_API_GATEWAY_API | CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET | IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY`

 ** [UpdatedAt](#API_CreateJob_ResponseSyntax) **   <a name="dataexchange-CreateJob-response-UpdatedAt"></a>
The date and time that the job was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_CreateJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** Message **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** ResourceId **
The unique identifier for the resource with the conflict.
 ** ResourceType **
The type of the resource with the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/CreateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CreateJob)

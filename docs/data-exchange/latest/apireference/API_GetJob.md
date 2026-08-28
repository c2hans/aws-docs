---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetJob.html
---

# GetJob
<a name="API_GetJob"></a>

This operation returns information about a job.

## Request Syntax
<a name="API_GetJob_RequestSyntax"></a>

```
GET /v1/jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_GetJob_RequestSyntax) **   <a name="dataexchange-GetJob-request-uri-JobId"></a>
The unique identifier for a job.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_GetJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetJob_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-Arn"></a>
The ARN for the job.
Type: String

 ** [AssetConfiguration](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-AssetConfiguration"></a>
The configuration for the asset, including tags applied to assets created by the job.
Type: [AssetConfiguration](API_AssetConfiguration.md) object

 ** [CreatedAt](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-CreatedAt"></a>
The date and time that the job was created, in ISO 8601 format.
Type: Timestamp

 ** [Details](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-Details"></a>
Details about the job.
Type: [ResponseDetails](API_ResponseDetails.md) object

 ** [Errors](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-Errors"></a>
The errors associated with jobs.
Type: Array of [JobError](API_JobError.md) objects

 ** [Id](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-Id"></a>
The unique identifier for the job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [State](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-State"></a>
The state of the job.
Type: String
Valid Values: `WAITING | IN_PROGRESS | ERROR | COMPLETED | CANCELLED | TIMED_OUT`

 ** [Type](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-Type"></a>
The job type.
Type: String
Valid Values: `IMPORT_ASSETS_FROM_S3 | IMPORT_ASSET_FROM_SIGNED_URL | EXPORT_ASSETS_TO_S3 | EXPORT_ASSET_TO_SIGNED_URL | EXPORT_REVISIONS_TO_S3 | IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES | IMPORT_ASSET_FROM_API_GATEWAY_API | CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET | IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY`

 ** [UpdatedAt](#API_GetJob_ResponseSyntax) **   <a name="dataexchange-GetJob-response-UpdatedAt"></a>
The date and time that the job was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_GetJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/GetJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/GetJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

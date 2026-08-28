---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

This operation lists your jobs sorted by CreatedAt in descending order.

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
GET /v1/jobs?dataSetId={{DataSetId}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&revisionId={{RevisionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_ListJobs_RequestSyntax) **   <a name="dataexchange-ListJobs-request-uri-DataSetId"></a>
The unique identifier for a data set.

 ** [MaxResults](#API_ListJobs_RequestSyntax) **   <a name="dataexchange-ListJobs-request-uri-MaxResults"></a>
The maximum number of results returned by a single call.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [NextToken](#API_ListJobs_RequestSyntax) **   <a name="dataexchange-ListJobs-request-uri-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.

 ** [RevisionId](#API_ListJobs_RequestSyntax) **   <a name="dataexchange-ListJobs-request-uri-RevisionId"></a>
The unique identifier for a revision.

## Request Body
<a name="API_ListJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Jobs": [
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Jobs](#API_ListJobs_ResponseSyntax) **   <a name="dataexchange-ListJobs-response-Jobs"></a>
The jobs listed by the request.
Type: Array of [JobEntry](API_JobEntry.md) objects

 ** [NextToken](#API_ListJobs_ResponseSyntax) **   <a name="dataexchange-ListJobs-response-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Type: String

## Errors
<a name="API_ListJobs_Errors"></a>

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
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ListJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

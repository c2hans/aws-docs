---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListRevisionAssets.html
---

# ListRevisionAssets
<a name="API_ListRevisionAssets"></a>

This operation lists a revision's assets sorted alphabetically in descending order.

## Request Syntax
<a name="API_ListRevisionAssets_RequestSyntax"></a>

```
GET /v1/data-sets/{{DataSetId}}/revisions/{{RevisionId}}/assets?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRevisionAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_ListRevisionAssets_RequestSyntax) **   <a name="dataexchange-ListRevisionAssets-request-uri-DataSetId"></a>
The unique identifier for a data set.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** [MaxResults](#API_ListRevisionAssets_RequestSyntax) **   <a name="dataexchange-ListRevisionAssets-request-uri-MaxResults"></a>
The maximum number of results returned by a single call.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [NextToken](#API_ListRevisionAssets_RequestSyntax) **   <a name="dataexchange-ListRevisionAssets-request-uri-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.

 ** [RevisionId](#API_ListRevisionAssets_RequestSyntax) **   <a name="dataexchange-ListRevisionAssets-request-uri-RevisionId"></a>
The unique identifier for a revision.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_ListRevisionAssets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRevisionAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Assets": [
      {
         "Arn": "string",
         "AssetDetails": {
            "ApiGatewayApiAsset": {
               "ApiDescription": "string",
               "ApiEndpoint": "string",
               "ApiId": "string",
               "ApiKey": "string",
               "ApiName": "string",
               "ApiSpecificationDownloadUrl": "string",
               "ApiSpecificationDownloadUrlExpiresAt": "string",
               "ProtocolType": "string",
               "Stage": "string"
            },
            "LakeFormationDataPermissionAsset": {
               "LakeFormationDataPermissionDetails": {
                  "LFTagPolicy": {
                     "CatalogId": "string",
                     "ResourceDetails": {
                        "Database": {
                           "Expression": [
                              {
                                 "TagKey": "string",
                                 "TagValues": [ "string" ]
                              }
                           ]
                        },
                        "Table": {
                           "Expression": [
                              {
                                 "TagKey": "string",
                                 "TagValues": [ "string" ]
                              }
                           ]
                        }
                     },
                     "ResourceType": "string"
                  }
               },
               "LakeFormationDataPermissionType": "string",
               "Permissions": [ "string" ],
               "RoleArn": "string"
            },
            "RedshiftDataShareAsset": {
               "Arn": "string"
            },
            "S3DataAccessAsset": {
               "Bucket": "string",
               "KeyPrefixes": [ "string" ],
               "Keys": [ "string" ],
               "KmsKeysToGrant": [
                  {
                     "KmsKeyArn": "string"
                  }
               ],
               "S3AccessPointAlias": "string",
               "S3AccessPointArn": "string"
            },
            "S3SnapshotAsset": {
               "Size": number
            }
         },
         "AssetType": "string",
         "CreatedAt": "string",
         "DataSetId": "string",
         "Id": "string",
         "Name": "string",
         "RevisionId": "string",
         "SourceId": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListRevisionAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Assets](#API_ListRevisionAssets_ResponseSyntax) **   <a name="dataexchange-ListRevisionAssets-response-Assets"></a>
The asset objects listed by the request.
Type: Array of [AssetEntry](API_AssetEntry.md) objects

 ** [NextToken](#API_ListRevisionAssets_ResponseSyntax) **   <a name="dataexchange-ListRevisionAssets-response-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Type: String

## Errors
<a name="API_ListRevisionAssets_Errors"></a>

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
<a name="API_ListRevisionAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/ListRevisionAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ListRevisionAssets)

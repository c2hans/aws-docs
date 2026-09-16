---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataIntegrationFlows.html
---

# ListDataIntegrationFlows
<a name="API_ListDataIntegrationFlows"></a>

Enables you to programmatically list all data pipelines for the provided AWS Supply Chain instance.

## Request Syntax
<a name="API_ListDataIntegrationFlows_RequestSyntax"></a>

```
GET /api/data-integration/instance/{{instanceId}}/data-integration-flows?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataIntegrationFlows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_ListDataIntegrationFlows_RequestSyntax) **   <a name="supplychain-ListDataIntegrationFlows-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [maxResults](#API_ListDataIntegrationFlows_RequestSyntax) **   <a name="supplychain-ListDataIntegrationFlows-request-uri-maxResults"></a>
Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.
Valid Range: Minimum value of 0. Maximum value of 20.

 ** [nextToken](#API_ListDataIntegrationFlows_RequestSyntax) **   <a name="supplychain-ListDataIntegrationFlows-request-uri-nextToken"></a>
The pagination token to fetch the next page of the DataIntegrationFlows.
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Request Body
<a name="API_ListDataIntegrationFlows_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataIntegrationFlows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flows": [
      {
         "createdTime": number,
         "instanceId": "string",
         "lastModifiedTime": number,
         "name": "string",
         "sources": [
            {
               "datasetSource": {
                  "datasetIdentifier": "string",
                  "options": {
                     "dedupeRecords": boolean,
                     "dedupeStrategy": {
                        "fieldPriority": {
                           "fields": [
                              {
                                 "name": "string",
                                 "sortOrder": "string"
                              }
                           ]
                        },
                        "type": "string"
                     },
                     "loadType": "string"
                  }
               },
               "s3Source": {
                  "bucketName": "string",
                  "options": {
                     "fileType": "string"
                  },
                  "prefix": "string"
               },
               "sourceName": "string",
               "sourceType": "string"
            }
         ],
         "target": {
            "datasetTarget": {
               "datasetIdentifier": "string",
               "options": {
                  "dedupeRecords": boolean,
                  "dedupeStrategy": {
                     "fieldPriority": {
                        "fields": [
                           {
                              "name": "string",
                              "sortOrder": "string"
                           }
                        ]
                     },
                     "type": "string"
                  },
                  "loadType": "string"
               }
            },
            "s3Target": {
               "bucketName": "string",
               "options": {
                  "fileType": "string"
               },
               "prefix": "string"
            },
            "targetType": "string"
         },
         "transformation": {
            "sqlTransformation": {
               "query": "string"
            },
            "transformationType": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataIntegrationFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flows](#API_ListDataIntegrationFlows_ResponseSyntax) **   <a name="supplychain-ListDataIntegrationFlows-response-flows"></a>
The response parameters for ListDataIntegrationFlows.
Type: Array of [DataIntegrationFlow](API_DataIntegrationFlow.md) objects

 ** [nextToken](#API_ListDataIntegrationFlows_ResponseSyntax) **   <a name="supplychain-ListDataIntegrationFlows-response-nextToken"></a>
The pagination token to fetch the next page of the DataIntegrationFlows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Errors
<a name="API_ListDataIntegrationFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDataIntegrationFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/ListDataIntegrationFlows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/ListDataIntegrationFlows)

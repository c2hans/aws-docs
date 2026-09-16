---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataIntegrationFlow.html
---

# GetDataIntegrationFlow
<a name="API_GetDataIntegrationFlow"></a>

Enables you to programmatically view a specific data pipeline for the provided AWS Supply Chain instance and DataIntegrationFlow name.

## Request Syntax
<a name="API_GetDataIntegrationFlow_RequestSyntax"></a>

```
GET /api/data-integration/instance/{{instanceId}}/data-integration-flows/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataIntegrationFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_GetDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-GetDataIntegrationFlow-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_GetDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-GetDataIntegrationFlow-request-uri-name"></a>
The name of the DataIntegrationFlow created.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetDataIntegrationFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataIntegrationFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flow": {
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
}
```

## Response Elements
<a name="API_GetDataIntegrationFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flow](#API_GetDataIntegrationFlow_ResponseSyntax) **   <a name="supplychain-GetDataIntegrationFlow-response-flow"></a>
The details of the DataIntegrationFlow returned.
Type: [DataIntegrationFlow](API_DataIntegrationFlow.md) object

## Errors
<a name="API_GetDataIntegrationFlow_Errors"></a>

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
<a name="API_GetDataIntegrationFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/GetDataIntegrationFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/GetDataIntegrationFlow)

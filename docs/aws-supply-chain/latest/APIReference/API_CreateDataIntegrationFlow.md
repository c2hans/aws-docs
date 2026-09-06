---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateDataIntegrationFlow.html
---

# CreateDataIntegrationFlow
<a name="API_CreateDataIntegrationFlow"></a>

Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined AWS Supply Chain dataset (product, inbound\_order) or a temporary dataset along with the data transformation query provided with the API.

## Request Syntax
<a name="API_CreateDataIntegrationFlow_RequestSyntax"></a>

```
PUT /api/data-integration/instance/{{instanceId}}/data-integration-flows/{{name}} HTTP/1.1
Content-type: application/json

{
   "sources": [
      {
         "datasetSource": {
            "datasetIdentifier": "{{string}}",
            "options": {
               "dedupeRecords": {{boolean}},
               "dedupeStrategy": {
                  "fieldPriority": {
                     "fields": [
                        {
                           "name": "{{string}}",
                           "sortOrder": "{{string}}"
                        }
                     ]
                  },
                  "type": "{{string}}"
               },
               "loadType": "{{string}}"
            }
         },
         "s3Source": {
            "bucketName": "{{string}}",
            "options": {
               "fileType": "{{string}}"
            },
            "prefix": "{{string}}"
         },
         "sourceName": "{{string}}",
         "sourceType": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "target": {
      "datasetTarget": {
         "datasetIdentifier": "{{string}}",
         "options": {
            "dedupeRecords": {{boolean}},
            "dedupeStrategy": {
               "fieldPriority": {
                  "fields": [
                     {
                        "name": "{{string}}",
                        "sortOrder": "{{string}}"
                     }
                  ]
               },
               "type": "{{string}}"
            },
            "loadType": "{{string}}"
         }
      },
      "s3Target": {
         "bucketName": "{{string}}",
         "options": {
            "fileType": "{{string}}"
         },
         "prefix": "{{string}}"
      },
      "targetType": "{{string}}"
   },
   "transformation": {
      "sqlTransformation": {
         "query": "{{string}}"
      },
      "transformationType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataIntegrationFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_CreateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_CreateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-request-uri-name"></a>
Name of the DataIntegrationFlow.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

## Request Body
<a name="API_CreateDataIntegrationFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sources](#API_CreateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-request-sources"></a>
The source configurations for DataIntegrationFlow.
Type: Array of [DataIntegrationFlowSource](API_DataIntegrationFlowSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: Yes

 ** [tags](#API_CreateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-request-tags"></a>
The tags of the DataIntegrationFlow to be created
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [target](#API_CreateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-request-target"></a>
The target configurations for DataIntegrationFlow.
Type: [DataIntegrationFlowTarget](API_DataIntegrationFlowTarget.md) object
Required: Yes

 ** [transformation](#API_CreateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-request-transformation"></a>
The transformation configurations for DataIntegrationFlow.
Type: [DataIntegrationFlowTransformation](API_DataIntegrationFlowTransformation.md) object
Required: Yes

## Response Syntax
<a name="API_CreateDataIntegrationFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "instanceId": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateDataIntegrationFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceId](#API_CreateDataIntegrationFlow_ResponseSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-response-instanceId"></a>
The AWS Supply Chain instance identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_CreateDataIntegrationFlow_ResponseSyntax) **   <a name="supplychain-CreateDataIntegrationFlow-response-name"></a>
The name of the DataIntegrationFlow created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_CreateDataIntegrationFlow_Errors"></a>

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
<a name="API_CreateDataIntegrationFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/CreateDataIntegrationFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/CreateDataIntegrationFlow)

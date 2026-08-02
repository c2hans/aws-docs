---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UpdateDataIntegrationFlow.html
---

# UpdateDataIntegrationFlow
<a name="API_UpdateDataIntegrationFlow"></a>

Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined AWS Supply Chain dataset (product, inbound\_order) or a temporary dataset along with the data transformation query provided with the API.

## Request Syntax
<a name="API_UpdateDataIntegrationFlow_RequestSyntax"></a>

```
PATCH /api/data-integration/instance/{{instanceId}}/data-integration-flows/{{name}} HTTP/1.1
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
<a name="API_UpdateDataIntegrationFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_UpdateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-UpdateDataIntegrationFlow-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_UpdateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-UpdateDataIntegrationFlow-request-uri-name"></a>
The name of the DataIntegrationFlow to be updated.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

## Request Body
<a name="API_UpdateDataIntegrationFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sources](#API_UpdateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-UpdateDataIntegrationFlow-request-sources"></a>
The new source configurations for the DataIntegrationFlow.
Type: Array of [DataIntegrationFlowSource](API_DataIntegrationFlowSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: No

 ** [target](#API_UpdateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-UpdateDataIntegrationFlow-request-target"></a>
The new target configurations for the DataIntegrationFlow.
Type: [DataIntegrationFlowTarget](API_DataIntegrationFlowTarget.md) object
Required: No

 ** [transformation](#API_UpdateDataIntegrationFlow_RequestSyntax) **   <a name="supplychain-UpdateDataIntegrationFlow-request-transformation"></a>
The new transformation configurations for the DataIntegrationFlow.
Type: [DataIntegrationFlowTransformation](API_DataIntegrationFlowTransformation.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataIntegrationFlow_ResponseSyntax"></a>

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
<a name="API_UpdateDataIntegrationFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flow](#API_UpdateDataIntegrationFlow_ResponseSyntax) **   <a name="supplychain-UpdateDataIntegrationFlow-response-flow"></a>
The details of the updated DataIntegrationFlow.
Type: [DataIntegrationFlow](API_DataIntegrationFlow.md) object

## Errors
<a name="API_UpdateDataIntegrationFlow_Errors"></a>

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
<a name="API_UpdateDataIntegrationFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/UpdateDataIntegrationFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/UpdateDataIntegrationFlow)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetIntermediateTable.html
---

# GetIntermediateTable
<a name="API_GetIntermediateTable"></a>

Retrieves an intermediate table. Returns the full details of the intermediate table, including schema, table dependencies, inherited constraints, child resources, and status. Only the intermediate table owner can call this operation.

## Request Syntax
<a name="API_GetIntermediateTable_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/intermediateTables/{{intermediateTableIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIntermediateTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [intermediateTableIdentifier](#API_GetIntermediateTable_RequestSyntax) **   <a name="API-GetIntermediateTable-request-uri-intermediateTableIdentifier"></a>
The unique identifier of the intermediate table to retrieve.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_GetIntermediateTable_RequestSyntax) **   <a name="API-GetIntermediateTable-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the intermediate table.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetIntermediateTable_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIntermediateTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "intermediateTable": {
      "analysisRuleTypes": [ "string" ],
      "arn": "string",
      "childResources": [
         {
            "ownerAccountId": "string",
            "resourceId": "string",
            "resourceName": "string",
            "resourceStatus": "string",
            "resourceType": "string"
         }
      ],
      "collaborationArn": "string",
      "collaborationId": "string",
      "createTime": number,
      "description": "string",
      "id": "string",
      "intermediateTableVersion": {
         "analysisId": "string",
         "analysisType": "string",
         "expirationTime": number,
         "inheritedConstraints": {
            "additionalAnalyses": {
               "sources": [
                  {
                     "id": "string",
                     "name": "string",
                     "sourceAccountId": "string",
                     "type": "string",
                     "value": "string"
                  }
               ],
               "value": "string"
            },
            "allowedAdditionalAnalyses": {
               "sources": [
                  {
                     "id": "string",
                     "name": "string",
                     "sourceAccountId": "string",
                     "type": "string",
                     "value": [ "string" ]
                  }
               ],
               "value": [ "string" ]
            },
            "allowedResultReceivers": {
               "sources": [
                  {
                     "id": "string",
                     "name": "string",
                     "sourceAccountId": "string",
                     "type": "string",
                     "value": [ "string" ]
                  }
               ],
               "value": [ "string" ]
            },
            "disallowedOutputColumns": {
               "columnLineage": [
                  {
                     "column": "string",
                     "sourceAccountId": "string",
                     "sourceColumn": "string",
                     "sourceId": "string",
                     "sourceName": "string",
                     "sourceType": "string"
                  }
               ],
               "value": [ "string" ]
            }
         },
         "kmsKeyArn": "string",
         "parameters": {
            "string" : "string"
         },
         "versionId": "string"
      },
      "kmsKeyArn": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "name": "string",
      "populationAnalysisConfiguration": { ... },
      "retentionInDays": number,
      "schema": {
         "columns": [
            {
               "name": "string",
               "type": "string"
            }
         ]
      },
      "status": "string",
      "statusReason": "string",
      "tableDependencies": [
         {
            "creatorAccountId": "string",
            "id": "string",
            "name": "string",
            "parentType": "string",
            "type": "string"
         }
      ],
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_GetIntermediateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [intermediateTable](#API_GetIntermediateTable_ResponseSyntax) **   <a name="API-GetIntermediateTable-response-intermediateTable"></a>
The intermediate table retrieved.
Type: [IntermediateTable](API_IntermediateTable.md) object

## Errors
<a name="API_GetIntermediateTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetIntermediateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/GetIntermediateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/GetIntermediateTable)

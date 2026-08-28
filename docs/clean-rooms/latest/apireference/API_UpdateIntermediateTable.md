---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIntermediateTable.html
---

# UpdateIntermediateTable
<a name="API_UpdateIntermediateTable"></a>

Updates an intermediate table. You can update the description, KMS key ARN, and column types of existing columns. Only the intermediate table owner can call this operation.

## Request Syntax
<a name="API_UpdateIntermediateTable_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/intermediateTables/{{intermediateTableIdentifier}} HTTP/1.1
Content-type: application/json

{
   "columns": [
      {
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIntermediateTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [intermediateTableIdentifier](#API_UpdateIntermediateTable_RequestSyntax) **   <a name="API-UpdateIntermediateTable-request-uri-intermediateTableIdentifier"></a>
The unique identifier of the intermediate table to update.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_UpdateIntermediateTable_RequestSyntax) **   <a name="API-UpdateIntermediateTable-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the intermediate table.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateIntermediateTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [columns](#API_UpdateIntermediateTable_RequestSyntax) **   <a name="API-UpdateIntermediateTable-request-columns"></a>
The list of columns with updated type definitions. Only the type of existing columns can be updated.
Type: Array of [IntermediateTableColumn](API_IntermediateTableColumn.md) objects
Required: No

 ** [description](#API_UpdateIntermediateTable_RequestSyntax) **   <a name="API-UpdateIntermediateTable-request-description"></a>
A new description for the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [kmsKeyArn](#API_UpdateIntermediateTable_RequestSyntax) **   <a name="API-UpdateIntermediateTable-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer-managed KMS key to use for encrypting future population data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
Required: No

## Response Syntax
<a name="API_UpdateIntermediateTable_ResponseSyntax"></a>

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
<a name="API_UpdateIntermediateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [intermediateTable](#API_UpdateIntermediateTable_ResponseSyntax) **   <a name="API-UpdateIntermediateTable-response-intermediateTable"></a>
The updated intermediate table.
Type: [IntermediateTable](API_IntermediateTable.md) object

## Errors
<a name="API_UpdateIntermediateTable_Errors"></a>

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
<a name="API_UpdateIntermediateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateIntermediateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateIntermediateTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

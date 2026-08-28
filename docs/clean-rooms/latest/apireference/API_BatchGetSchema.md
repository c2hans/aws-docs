---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BatchGetSchema.html
---

# BatchGetSchema
<a name="API_BatchGetSchema"></a>

Retrieves multiple schemas by their identifiers.

## Request Syntax
<a name="API_BatchGetSchema_RequestSyntax"></a>

```
POST /collaborations/{{collaborationIdentifier}}/batch-schema HTTP/1.1
Content-type: application/json

{
   "names": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetSchema_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_BatchGetSchema_RequestSyntax) **   <a name="API-BatchGetSchema-request-uri-collaborationIdentifier"></a>
A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_BatchGetSchema_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [names](#API_BatchGetSchema_RequestSyntax) **   <a name="API-BatchGetSchema-request-names"></a>
The names for the schema objects to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

## Response Syntax
<a name="API_BatchGetSchema_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "message": "string",
         "name": "string"
      }
   ],
   "schemas": [
      {
         "analysisMethod": "string",
         "analysisRuleTypes": [ "string" ],
         "collaborationArn": "string",
         "collaborationId": "string",
         "columns": [
            {
               "name": "string",
               "type": "string"
            }
         ],
         "createTime": number,
         "creatorAccountId": "string",
         "description": "string",
         "name": "string",
         "partitionKeys": [
            {
               "name": "string",
               "type": "string"
            }
         ],
         "resourceArn": "string",
         "schemaStatusDetails": [
            {
               "analysisRuleType": "string",
               "analysisType": "string",
               "configurations": [ "string" ],
               "reasons": [
                  {
                     "code": "string",
                     "message": "string"
                  }
               ],
               "status": "string"
            }
         ],
         "schemaTypeProperties": { ... },
         "selectedAnalysisMethods": [ "string" ],
         "type": "string",
         "updateTime": number
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetSchema_ResponseSyntax) **   <a name="API-BatchGetSchema-response-errors"></a>
Error reasons for schemas that could not be retrieved. One error is returned for every schema that could not be retrieved.
Type: Array of [BatchGetSchemaError](API_BatchGetSchemaError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [schemas](#API_BatchGetSchema_ResponseSyntax) **   <a name="API-BatchGetSchema-response-schemas"></a>
The retrieved list of schemas.
Type: Array of [Schema](API_Schema.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_BatchGetSchema_Errors"></a>

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
<a name="API_BatchGetSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/BatchGetSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/BatchGetSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateSchemaMapping.html
---

# UpdateSchemaMapping
<a name="API_UpdateSchemaMapping"></a>

Updates a schema mapping.

**Note**
A schema is immutable if it is being used by a workflow. Therefore, you can't update a schema mapping if it's associated with a workflow.

## Request Syntax
<a name="API_UpdateSchemaMapping_RequestSyntax"></a>

```
PUT /schemas/{{schemaName}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "mappedInputFields": [
      {
         "fieldName": "{{string}}",
         "groupName": "{{string}}",
         "hashed": {{boolean}},
         "matchKey": "{{string}}",
         "subType": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateSchemaMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [schemaName](#API_UpdateSchemaMapping_RequestSyntax) **   <a name="API-UpdateSchemaMapping-request-uri-schemaName"></a>
The name of the schema. There can't be multiple `SchemaMappings` with the same name.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_UpdateSchemaMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateSchemaMapping_RequestSyntax) **   <a name="API-UpdateSchemaMapping-request-description"></a>
A description of the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [mappedInputFields](#API_UpdateSchemaMapping_RequestSyntax) **   <a name="API-UpdateSchemaMapping-request-mappedInputFields"></a>
A list of `MappedInputFields`. Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
Type: Array of [SchemaInputAttribute](API_SchemaInputAttribute.md) objects
Array Members: Minimum number of 2 items. Maximum number of 60 items.
Required: Yes

## Response Syntax
<a name="API_UpdateSchemaMapping_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "mappedInputFields": [
      {
         "fieldName": "string",
         "groupName": "string",
         "hashed": boolean,
         "matchKey": "string",
         "subType": "string",
         "type": "string"
      }
   ],
   "schemaArn": "string",
   "schemaName": "string"
}
```

## Response Elements
<a name="API_UpdateSchemaMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateSchemaMapping_ResponseSyntax) **   <a name="API-UpdateSchemaMapping-response-description"></a>
A description of the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [mappedInputFields](#API_UpdateSchemaMapping_ResponseSyntax) **   <a name="API-UpdateSchemaMapping-response-mappedInputFields"></a>
A list of `MappedInputFields`. Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
Type: Array of [SchemaInputAttribute](API_SchemaInputAttribute.md) objects
Array Members: Minimum number of 2 items. Maximum number of 60 items.

 ** [schemaArn](#API_UpdateSchemaMapping_ResponseSyntax) **   <a name="API-UpdateSchemaMapping-response-schemaArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `SchemaMapping`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(schemamapping/[a-zA-Z_0-9-]{1,255})`

 ** [schemaName](#API_UpdateSchemaMapping_ResponseSyntax) **   <a name="API-UpdateSchemaMapping-response-schemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_UpdateSchemaMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSchemaMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/UpdateSchemaMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/UpdateSchemaMapping)

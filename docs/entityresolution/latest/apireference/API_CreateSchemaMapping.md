---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateSchemaMapping.html
---

# CreateSchemaMapping
<a name="API_CreateSchemaMapping"></a>

Creates a schema mapping, which defines the schema of the input customer records table. The `SchemaMapping` also provides AWS Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.

## Request Syntax
<a name="API_CreateSchemaMapping_RequestSyntax"></a>

```
POST /schemas HTTP/1.1
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
   ],
   "schemaName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSchemaMapping_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSchemaMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateSchemaMapping_RequestSyntax) **   <a name="API-CreateSchemaMapping-request-description"></a>
A description of the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [mappedInputFields](#API_CreateSchemaMapping_RequestSyntax) **   <a name="API-CreateSchemaMapping-request-mappedInputFields"></a>
A list of `MappedInputFields`. Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
Type: Array of [SchemaInputAttribute](API_SchemaInputAttribute.md) objects
Array Members: Minimum number of 2 items. Maximum number of 35 items.
Required: Yes

 ** [schemaName](#API_CreateSchemaMapping_RequestSyntax) **   <a name="API-CreateSchemaMapping-request-schemaName"></a>
The name of the schema. There can't be multiple `SchemaMappings` with the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** [tags](#API_CreateSchemaMapping_RequestSyntax) **   <a name="API-CreateSchemaMapping-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSchemaMapping_ResponseSyntax"></a>

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
<a name="API_CreateSchemaMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateSchemaMapping_ResponseSyntax) **   <a name="API-CreateSchemaMapping-response-description"></a>
A description of the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [mappedInputFields](#API_CreateSchemaMapping_ResponseSyntax) **   <a name="API-CreateSchemaMapping-response-mappedInputFields"></a>
A list of `MappedInputFields`. Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
Type: Array of [SchemaInputAttribute](API_SchemaInputAttribute.md) objects
Array Members: Minimum number of 2 items. Maximum number of 35 items.

 ** [schemaArn](#API_CreateSchemaMapping_ResponseSyntax) **   <a name="API-CreateSchemaMapping-response-schemaArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `SchemaMapping`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(schemamapping/[a-zA-Z_0-9-]{1,255})`

 ** [schemaName](#API_CreateSchemaMapping_ResponseSyntax) **   <a name="API-CreateSchemaMapping-response-schemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_CreateSchemaMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** ExceedsLimitException **
The request was rejected because it attempted to create resources beyond the current AWS Entity Resolution account limits. The error message describes the limit exceeded.
 ** quotaName **
The name of the quota that has been breached.
 ** quotaValue **
The current quota value for the customers.
HTTP Status Code: 402

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_CreateSchemaMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/CreateSchemaMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/CreateSchemaMapping)

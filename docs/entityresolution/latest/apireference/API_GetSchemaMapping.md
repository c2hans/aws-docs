---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetSchemaMapping.html
---

# GetSchemaMapping
<a name="API_GetSchemaMapping"></a>

Returns the SchemaMapping of a given name.

## Request Syntax
<a name="API_GetSchemaMapping_RequestSyntax"></a>

```
GET /schemas/{{schemaName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSchemaMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [schemaName](#API_GetSchemaMapping_RequestSyntax) **   <a name="API-GetSchemaMapping-request-uri-schemaName"></a>
The name of the schema to be retrieved.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_GetSchemaMapping_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSchemaMapping_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "description": "string",
   "hasWorkflows": boolean,
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
   "schemaName": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetSchemaMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-createdAt"></a>
The timestamp of when the `SchemaMapping` was created.
Type: Timestamp

 ** [description](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-description"></a>
A description of the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [hasWorkflows](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-hasWorkflows"></a>
Specifies whether the schema mapping has been applied to a workflow.
Type: Boolean

 ** [mappedInputFields](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-mappedInputFields"></a>
A list of `MappedInputFields`. Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information AWS Entity Resolution uses for matching.
Type: Array of [SchemaInputAttribute](API_SchemaInputAttribute.md) objects
Array Members: Minimum number of 2 items. Maximum number of 60 items.

 ** [schemaArn](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-schemaArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the SchemaMapping.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(schemamapping/[a-zA-Z_0-9-]{1,255})`

 ** [schemaName](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-schemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

 ** [tags](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updatedAt](#API_GetSchemaMapping_ResponseSyntax) **   <a name="API-GetSchemaMapping-response-updatedAt"></a>
The timestamp of when the `SchemaMapping` was last updated.
Type: Timestamp

## Errors
<a name="API_GetSchemaMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetSchemaMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetSchemaMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetSchemaMapping)

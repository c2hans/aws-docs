---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTable.html
---

# UpdateConfiguredTable
<a name="API_UpdateConfiguredTable"></a>

Updates a configured table.

## Request Syntax
<a name="API_UpdateConfiguredTable_RequestSyntax"></a>

```
PATCH /configuredTables/{{configuredTableIdentifier}} HTTP/1.1
Content-type: application/json

{
   "allowedColumns": [ "{{string}}" ],
   "analysisMethod": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "selectedAnalysisMethods": [ "{{string}}" ],
   "tableReference": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateConfiguredTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredTableIdentifier](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-uri-configuredTableIdentifier"></a>
The identifier for the configured table to update. Currently accepts the configured table ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateConfiguredTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedColumns](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-allowedColumns"></a>
The columns of the underlying table that can be used by collaborations or analysis rules.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: No

 ** [analysisMethod](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-analysisMethod"></a>
 The analysis method for the configured table.
 `DIRECT_QUERY` allows SQL queries to be run directly on this table.
 `DIRECT_JOB` allows PySpark jobs to be run directly on this table.
 `MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.
Type: String
Valid Values: `DIRECT_QUERY | DIRECT_JOB | MULTIPLE`
Required: No

 ** [description](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-description"></a>
A new description for the configured table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [name](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-name"></a>
A new name for the configured table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: No

 ** [selectedAnalysisMethods](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-selectedAnalysisMethods"></a>
 The selected analysis methods for the table configuration update.
Type: Array of strings
Valid Values: `DIRECT_QUERY | DIRECT_JOB`
Required: No

 ** [tableReference](#API_UpdateConfiguredTable_RequestSyntax) **   <a name="API-UpdateConfiguredTable-request-tableReference"></a>
A pointer to the dataset that underlies this table.
Type: [TableReference](API_TableReference.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateConfiguredTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredTable": {
      "allowedColumns": [ "string" ],
      "analysisMethod": "string",
      "analysisRuleTypes": [ "string" ],
      "arn": "string",
      "createTime": number,
      "description": "string",
      "id": "string",
      "name": "string",
      "selectedAnalysisMethods": [ "string" ],
      "tableReference": { ... },
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_UpdateConfiguredTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredTable](#API_UpdateConfiguredTable_ResponseSyntax) **   <a name="API-UpdateConfiguredTable-response-configuredTable"></a>
The updated configured table.
Type: [ConfiguredTable](API_ConfiguredTable.md) object

## Errors
<a name="API_UpdateConfiguredTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

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
<a name="API_UpdateConfiguredTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateConfiguredTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateConfiguredTable)

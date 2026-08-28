---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DisallowIntermediateTable.html
---

# DisallowIntermediateTable
<a name="API_DisallowIntermediateTable"></a>

Marks an intermediate table as invalid when it references the caller's base table. The data provider (base table owner) calls this operation, not the intermediate table owner. By default, the operation also marks all descendant intermediate tables as invalid.

## Request Syntax
<a name="API_DisallowIntermediateTable_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/disallowIntermediateTable HTTP/1.1
Content-type: application/json

{
   "includeDescendants": {{boolean}},
   "intermediateTableName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisallowIntermediateTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_DisallowIntermediateTable_RequestSyntax) **   <a name="API-DisallowIntermediateTable-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the intermediate table to disallow.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_DisallowIntermediateTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [includeDescendants](#API_DisallowIntermediateTable_RequestSyntax) **   <a name="API-DisallowIntermediateTable-request-includeDescendants"></a>
Specifies whether to cascade the disallow action to descendant intermediate tables. Default is `true`.
Type: Boolean
Required: No

 ** [intermediateTableName](#API_DisallowIntermediateTable_RequestSyntax) **   <a name="API-DisallowIntermediateTable-request-intermediateTableName"></a>
The name of the intermediate table to disallow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_DisallowIntermediateTable_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisallowIntermediateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisallowIntermediateTable_Errors"></a>

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
<a name="API_DisallowIntermediateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/DisallowIntermediateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DisallowIntermediateTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

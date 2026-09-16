---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ExecuteQuery.html
---

# ExecuteQuery
<a name="API_ExecuteQuery"></a>

Run queries to access information from your knowledge graph of entities within individual workspaces.

**Note**
The ExecuteQuery action only works with [AWS Java SDK2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html). ExecuteQuery will not work with any AWS Java SDK version < 2.x.

## Request Syntax
<a name="API_ExecuteQuery_RequestSyntax"></a>

```
POST /queries/execution HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryStatement": "{{string}}",
   "workspaceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExecuteQuery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExecuteQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ExecuteQuery_RequestSyntax) **   <a name="tm-ExecuteQuery-request-maxResults"></a>
The maximum number of results to return at one time. The default is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ExecuteQuery_RequestSyntax) **   <a name="tm-ExecuteQuery-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

 ** [queryStatement](#API_ExecuteQuery_RequestSyntax) **   <a name="tm-ExecuteQuery-request-queryStatement"></a>
The query statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\s\S]+`
Required: Yes

 ** [workspaceId](#API_ExecuteQuery_RequestSyntax) **   <a name="tm-ExecuteQuery-request-workspaceId"></a>
The ID of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_ExecuteQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "columnDescriptions": [
      {
         "name": "string",
         "type": "string"
      }
   ],
   "nextToken": "string",
   "rows": [
      {
         "rowData": [ JSON value ]
      }
   ]
}
```

## Response Elements
<a name="API_ExecuteQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [columnDescriptions](#API_ExecuteQuery_ResponseSyntax) **   <a name="tm-ExecuteQuery-response-columnDescriptions"></a>
A list of ColumnDescription objects.
Type: Array of [ColumnDescription](API_ColumnDescription.md) objects

 ** [nextToken](#API_ExecuteQuery_ResponseSyntax) **   <a name="tm-ExecuteQuery-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [rows](#API_ExecuteQuery_ResponseSyntax) **   <a name="tm-ExecuteQuery-response-rows"></a>
Represents a single row in the query results.
Type: Array of [Row](API_Row.md) objects

## Errors
<a name="API_ExecuteQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** QueryTimeoutException **
The query timeout exception.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ExecuteQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ExecuteQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ExecuteQuery)

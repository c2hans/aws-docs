---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListConfiguredTables.html
---

# ListConfiguredTables
<a name="API_ListConfiguredTables"></a>

Lists configured tables.

## Request Syntax
<a name="API_ListConfiguredTables_RequestSyntax"></a>

```
GET /configuredTables?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConfiguredTables_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListConfiguredTables_RequestSyntax) **   <a name="API-ListConfiguredTables-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListConfiguredTables_RequestSyntax) **   <a name="API-ListConfiguredTables-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Request Body
<a name="API_ListConfiguredTables_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConfiguredTables_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredTableSummaries": [
      {
         "analysisMethod": "string",
         "analysisRuleTypes": [ "string" ],
         "arn": "string",
         "createTime": number,
         "id": "string",
         "name": "string",
         "selectedAnalysisMethods": [ "string" ],
         "updateTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConfiguredTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredTableSummaries](#API_ListConfiguredTables_ResponseSyntax) **   <a name="API-ListConfiguredTables-response-configuredTableSummaries"></a>
The configured tables listed by the request.
Type: Array of [ConfiguredTableSummary](API_ConfiguredTableSummary.md) objects

 ** [nextToken](#API_ListConfiguredTables_ResponseSyntax) **   <a name="API-ListConfiguredTables-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Errors
<a name="API_ListConfiguredTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

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
<a name="API_ListConfiguredTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListConfiguredTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListConfiguredTables)

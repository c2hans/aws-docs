---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html
---

# ListAnalyzers
<a name="API_ListAnalyzers"></a>

Retrieves a list of analyzers.

## Request Syntax
<a name="API_ListAnalyzers_RequestSyntax"></a>

```
GET /analyzer?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAnalyzers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAnalyzers_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzers-request-uri-maxResults"></a>
The maximum number of results to return in the response.

 ** [nextToken](#API_ListAnalyzers_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzers-request-uri-nextToken"></a>
A token used for pagination of results returned.

 ** [type](#API_ListAnalyzers_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzers-request-uri-type"></a>
The type of analyzer.
Valid Values: `ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ORGANIZATION_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS`

## Request Body
<a name="API_ListAnalyzers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAnalyzers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analyzers": [
      {
         "arn": "string",
         "configuration": { ... },
         "createdAt": "string",
         "lastResourceAnalyzed": "string",
         "lastResourceAnalyzedAt": "string",
         "name": "string",
         "status": "string",
         "statusReason": {
            "code": "string"
         },
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnalyzers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analyzers](#API_ListAnalyzers_ResponseSyntax) **   <a name="accessanalyzer-ListAnalyzers-response-analyzers"></a>
The analyzers retrieved.
Type: Array of [AnalyzerSummary](API_AnalyzerSummary.md) objects

 ** [nextToken](#API_ListAnalyzers_ResponseSyntax) **   <a name="accessanalyzer-ListAnalyzers-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

## Errors
<a name="API_ListAnalyzers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListAnalyzers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAnalyzers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAnalyzers)

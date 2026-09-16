---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListArchiveRules.html
---

# ListArchiveRules
<a name="API_ListArchiveRules"></a>

Retrieves a list of archive rules created for the specified analyzer.

## Request Syntax
<a name="API_ListArchiveRules_RequestSyntax"></a>

```
GET /analyzer/{{analyzerName}}/archive-rule?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListArchiveRules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerName](#API_ListArchiveRules_RequestSyntax) **   <a name="accessanalyzer-ListArchiveRules-request-uri-analyzerName"></a>
The name of the analyzer to retrieve rules from.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

 ** [maxResults](#API_ListArchiveRules_RequestSyntax) **   <a name="accessanalyzer-ListArchiveRules-request-uri-maxResults"></a>
The maximum number of results to return in the request.

 ** [nextToken](#API_ListArchiveRules_RequestSyntax) **   <a name="accessanalyzer-ListArchiveRules-request-uri-nextToken"></a>
A token used for pagination of results returned.

## Request Body
<a name="API_ListArchiveRules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListArchiveRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "archiveRules": [
      {
         "createdAt": "string",
         "filter": {
            "string" : {
               "contains": [ "string" ],
               "eq": [ "string" ],
               "exists": boolean,
               "neq": [ "string" ]
            }
         },
         "ruleName": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListArchiveRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [archiveRules](#API_ListArchiveRules_ResponseSyntax) **   <a name="accessanalyzer-ListArchiveRules-response-archiveRules"></a>
A list of archive rules created for the specified analyzer.
Type: Array of [ArchiveRuleSummary](API_ArchiveRuleSummary.md) objects

 ** [nextToken](#API_ListArchiveRules_ResponseSyntax) **   <a name="accessanalyzer-ListArchiveRules-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

## Errors
<a name="API_ListArchiveRules_Errors"></a>

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
<a name="API_ListArchiveRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListArchiveRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListArchiveRules)

---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html
---

# GetAnalyzer
<a name="API_GetAnalyzer"></a>

Retrieves information about the specified analyzer.

## Request Syntax
<a name="API_GetAnalyzer_RequestSyntax"></a>

```
GET /analyzer/{{analyzerName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAnalyzer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerName](#API_GetAnalyzer_RequestSyntax) **   <a name="accessanalyzer-GetAnalyzer-request-uri-analyzerName"></a>
The name of the analyzer retrieved.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

## Request Body
<a name="API_GetAnalyzer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAnalyzer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analyzer": {
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
}
```

## Response Elements
<a name="API_GetAnalyzer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analyzer](#API_GetAnalyzer_ResponseSyntax) **   <a name="accessanalyzer-GetAnalyzer-response-analyzer"></a>
An `AnalyzerSummary` object that contains information about the analyzer.
Type: [AnalyzerSummary](API_AnalyzerSummary.md) object

## Errors
<a name="API_GetAnalyzer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

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
<a name="API_GetAnalyzer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetAnalyzer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetAnalyzer)

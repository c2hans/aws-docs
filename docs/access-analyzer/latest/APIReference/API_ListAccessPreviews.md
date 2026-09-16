---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviews.html
---

# ListAccessPreviews
<a name="API_ListAccessPreviews"></a>

Retrieves a list of access previews for the specified analyzer.

## Request Syntax
<a name="API_ListAccessPreviews_RequestSyntax"></a>

```
GET /access-preview?analyzerArn={{analyzerArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccessPreviews_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerArn](#API_ListAccessPreviews_RequestSyntax) **   <a name="accessanalyzer-ListAccessPreviews-request-uri-analyzerArn"></a>
The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access preview.
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** [maxResults](#API_ListAccessPreviews_RequestSyntax) **   <a name="accessanalyzer-ListAccessPreviews-request-uri-maxResults"></a>
The maximum number of results to return in the response.

 ** [nextToken](#API_ListAccessPreviews_RequestSyntax) **   <a name="accessanalyzer-ListAccessPreviews-request-uri-nextToken"></a>
A token used for pagination of results returned.

## Request Body
<a name="API_ListAccessPreviews_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccessPreviews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessPreviews": [
      {
         "analyzerArn": "string",
         "createdAt": "string",
         "id": "string",
         "status": "string",
         "statusReason": {
            "code": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccessPreviews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessPreviews](#API_ListAccessPreviews_ResponseSyntax) **   <a name="accessanalyzer-ListAccessPreviews-response-accessPreviews"></a>
A list of access previews retrieved for the analyzer.
Type: Array of [AccessPreviewSummary](API_AccessPreviewSummary.md) objects

 ** [nextToken](#API_ListAccessPreviews_ResponseSyntax) **   <a name="accessanalyzer-ListAccessPreviews-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

## Errors
<a name="API_ListAccessPreviews_Errors"></a>

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
<a name="API_ListAccessPreviews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAccessPreviews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAccessPreviews)

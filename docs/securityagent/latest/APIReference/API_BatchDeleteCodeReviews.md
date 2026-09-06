---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchDeleteCodeReviews.html
---

# BatchDeleteCodeReviews
<a name="API_BatchDeleteCodeReviews"></a>

Deletes one or more code reviews from an agent space.

## Request Syntax
<a name="API_BatchDeleteCodeReviews_RequestSyntax"></a>

```
POST /BatchDeleteCodeReviews HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteCodeReviews_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteCodeReviews_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchDeleteCodeReviews_RequestSyntax) **   <a name="securityagent-BatchDeleteCodeReviews-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the code reviews to delete.
Type: String
Required: Yes

 ** [codeReviewIds](#API_BatchDeleteCodeReviews_RequestSyntax) **   <a name="securityagent-BatchDeleteCodeReviews-request-codeReviewIds"></a>
The list of code review identifiers to delete.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchDeleteCodeReviews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deleted": [ "string" ],
   "failed": [
      {
         "codeReviewId": "string",
         "reason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteCodeReviews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deleted](#API_BatchDeleteCodeReviews_ResponseSyntax) **   <a name="securityagent-BatchDeleteCodeReviews-response-deleted"></a>
The list of identifiers of the code reviews that were successfully deleted.
Type: Array of strings

 ** [failed](#API_BatchDeleteCodeReviews_ResponseSyntax) **   <a name="securityagent-BatchDeleteCodeReviews-response-failed"></a>
The list of code reviews that failed to delete, including the reason for each failure.
Type: Array of [DeleteCodeReviewFailure](API_DeleteCodeReviewFailure.md) objects

## Errors
<a name="API_BatchDeleteCodeReviews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchDeleteCodeReviews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchDeleteCodeReviews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchDeleteCodeReviews)

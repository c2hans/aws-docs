---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_PutFeedPolicy.html
---

# PutFeedPolicy
<a name="API_PutFeedPolicy"></a>

Attaches or replaces a resource-based policy on the specified feed. A resource-based policy grants cross-account access to the feed.

## Request Syntax
<a name="API_PutFeedPolicy_RequestSyntax"></a>

```
PUT /v1/feed/{{id}}/policy HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutFeedPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_PutFeedPolicy_RequestSyntax) **   <a name="elementalinference-PutFeedPolicy-request-uri-id"></a>
The ID of the feed to attach the policy to.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_PutFeedPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_PutFeedPolicy_RequestSyntax) **   <a name="elementalinference-PutFeedPolicy-request-policy"></a>
The resource-based policy document to attach to the feed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_PutFeedPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutFeedPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutFeedPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict.
HTTP Status Code: 409

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the action doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_PutFeedPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/PutFeedPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/PutFeedPolicy)

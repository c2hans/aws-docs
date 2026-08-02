---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CancelPolicyGeneration.html
---

# CancelPolicyGeneration
<a name="API_CancelPolicyGeneration"></a>

Cancels the requested policy generation.

## Request Syntax
<a name="API_CancelPolicyGeneration_RequestSyntax"></a>

```
PUT /policy/generation/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelPolicyGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_CancelPolicyGeneration_RequestSyntax) **   <a name="accessanalyzer-CancelPolicyGeneration-request-uri-jobId"></a>
The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.
Required: Yes

## Request Body
<a name="API_CancelPolicyGeneration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelPolicyGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelPolicyGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelPolicyGeneration_Errors"></a>

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
<a name="API_CancelPolicyGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CancelPolicyGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CancelPolicyGeneration)

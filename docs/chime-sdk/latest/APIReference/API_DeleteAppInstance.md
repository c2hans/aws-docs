---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstance.html
---

# DeleteAppInstance
<a name="API_DeleteAppInstance"></a>

Deletes an `AppInstance` and all associated data asynchronously.

## Request Syntax
<a name="API_DeleteAppInstance_RequestSyntax"></a>

```
DELETE /app-instances/{{appInstanceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAppInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceArn](#API_DeleteAppInstance_RequestSyntax) **   <a name="chimesdk-DeleteAppInstance-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_DeleteAppInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAppInstance_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAppInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAppInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_DeleteAppInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/DeleteAppInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/DeleteAppInstance)

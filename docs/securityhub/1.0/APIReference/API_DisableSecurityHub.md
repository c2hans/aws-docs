---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHub.html
---

# DisableSecurityHub
<a name="API_DisableSecurityHub"></a>

Disables Security Hub CSPM in your account only in the current AWS Region. To disable Security Hub CSPM in all Regions, you must submit one request per Region where you have enabled Security Hub CSPM.

You can't disable Security Hub CSPM in an account that is currently the Security Hub CSPM administrator.

When you disable Security Hub CSPM, your existing findings and insights and any Security Hub CSPM configuration settings are deleted after 90 days and cannot be recovered. Any standards that were enabled are disabled, and your administrator and member account associations are removed.

If you want to save your existing findings, you must export them before you disable Security Hub CSPM.

## Request Syntax
<a name="API_DisableSecurityHub_RequestSyntax"></a>

```
DELETE /accounts HTTP/1.1
```

## URI Request Parameters
<a name="API_DisableSecurityHub_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisableSecurityHub_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisableSecurityHub_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisableSecurityHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableSecurityHub_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_DisableSecurityHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DisableSecurityHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DisableSecurityHub)

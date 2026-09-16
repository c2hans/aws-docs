---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateTrustedTokenIssuer.html
---

# UpdateTrustedTokenIssuer
<a name="API_UpdateTrustedTokenIssuer"></a>

Updates the name of the trusted token issuer, or the path of a source attribute or destination attribute for a trusted token issuer configuration.

**Note**
Updating this trusted token issuer configuration might cause users to lose access to any applications that are configured to use the trusted token issuer.

## Request Syntax
<a name="API_UpdateTrustedTokenIssuer_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "TrustedTokenIssuerArn": "{{string}}",
   "TrustedTokenIssuerConfiguration": { ... }
}
```

## Request Parameters
<a name="API_UpdateTrustedTokenIssuer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-UpdateTrustedTokenIssuer-request-Name"></a>
Specifies the updated name to be applied to the trusted token issuer configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w+=,.@-]+`
Required: No

 ** [TrustedTokenIssuerArn](#API_UpdateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-UpdateTrustedTokenIssuer-request-TrustedTokenIssuerArn"></a>
Specifies the ARN of the trusted token issuer configuration that you want to update.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [TrustedTokenIssuerConfiguration](#API_UpdateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-UpdateTrustedTokenIssuer-request-TrustedTokenIssuerConfiguration"></a>
Specifies a structure with settings to apply to the specified trusted token issuer. The settings that you can provide are determined by the type of the trusted token issuer that you are updating.
Type: [TrustedTokenIssuerUpdateConfiguration](API_TrustedTokenIssuerUpdateConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Elements
<a name="API_UpdateTrustedTokenIssuer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTrustedTokenIssuer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrustedTokenIssuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/UpdateTrustedTokenIssuer)

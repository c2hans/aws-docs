---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateTrustedTokenIssuer.html
---

# CreateTrustedTokenIssuer
<a name="API_CreateTrustedTokenIssuer"></a>

Creates a connection to a trusted token issuer in an instance of IAM Identity Center. A trusted token issuer enables trusted identity propagation to be used with applications that authenticate outside of AWS.

This trusted token issuer describes an external identity provider (IdP) that can generate claims or assertions in the form of access tokens for a user. Applications enabled for IAM Identity Center can use these tokens for authentication.

## Request Syntax
<a name="API_CreateTrustedTokenIssuer_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "InstanceArn": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrustedTokenIssuerConfiguration": { ... },
   "TrustedTokenIssuerType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTrustedTokenIssuer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-request-ClientToken"></a>
Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [InstanceArn](#API_CreateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-request-InstanceArn"></a>
Specifies the ARN of the instance of IAM Identity Center to contain the new trusted token issuer configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [Name](#API_CreateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-request-Name"></a>
Specifies the name of the new trusted token issuer configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** [Tags](#API_CreateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-request-Tags"></a>
Specifies tags to be attached to the new trusted token issuer configuration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 75 items.
Required: No

 ** [TrustedTokenIssuerConfiguration](#API_CreateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-request-TrustedTokenIssuerConfiguration"></a>
Specifies settings that apply to the new trusted token issuer configuration. The settings that are available depend on what `TrustedTokenIssuerType` you specify.
Type: [TrustedTokenIssuerConfiguration](API_TrustedTokenIssuerConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [TrustedTokenIssuerType](#API_CreateTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-request-TrustedTokenIssuerType"></a>
Specifies the type of the new trusted token issuer.
Type: String
Valid Values: `OIDC_JWT`
Required: Yes

## Response Syntax
<a name="API_CreateTrustedTokenIssuer_ResponseSyntax"></a>

```
{
   "TrustedTokenIssuerArn": "string"
}
```

## Response Elements
<a name="API_CreateTrustedTokenIssuer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrustedTokenIssuerArn](#API_CreateTrustedTokenIssuer_ResponseSyntax) **   <a name="singlesignon-CreateTrustedTokenIssuer-response-TrustedTokenIssuerArn"></a>
The ARN of the new trusted token issuer configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateTrustedTokenIssuer_Errors"></a>

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

 ** ServiceQuotaExceededException **
Indicates that the principal has crossed the permitted number of resources that can be created.
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
<a name="API_CreateTrustedTokenIssuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/CreateTrustedTokenIssuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/CreateTrustedTokenIssuer)

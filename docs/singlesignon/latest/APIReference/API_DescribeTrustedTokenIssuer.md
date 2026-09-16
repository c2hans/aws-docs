---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeTrustedTokenIssuer.html
---

# DescribeTrustedTokenIssuer
<a name="API_DescribeTrustedTokenIssuer"></a>

Retrieves details about a trusted token issuer configuration stored in an instance of IAM Identity Center. Details include the name of the trusted token issuer, the issuer URL, and the path of the source attribute and the destination attribute for a trusted token issuer configuration.

## Request Syntax
<a name="API_DescribeTrustedTokenIssuer_RequestSyntax"></a>

```
{
   "TrustedTokenIssuerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrustedTokenIssuer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrustedTokenIssuerArn](#API_DescribeTrustedTokenIssuer_RequestSyntax) **   <a name="singlesignon-DescribeTrustedTokenIssuer-request-TrustedTokenIssuerArn"></a>
Specifies the ARN of the trusted token issuer configuration that you want details about.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeTrustedTokenIssuer_ResponseSyntax"></a>

```
{
   "Name": "string",
   "TrustedTokenIssuerArn": "string",
   "TrustedTokenIssuerConfiguration": { ... },
   "TrustedTokenIssuerType": "string"
}
```

## Response Elements
<a name="API_DescribeTrustedTokenIssuer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DescribeTrustedTokenIssuer_ResponseSyntax) **   <a name="singlesignon-DescribeTrustedTokenIssuer-response-Name"></a>
The name of the trusted token issuer configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w+=,.@-]+`

 ** [TrustedTokenIssuerArn](#API_DescribeTrustedTokenIssuer_ResponseSyntax) **   <a name="singlesignon-DescribeTrustedTokenIssuer-response-TrustedTokenIssuerArn"></a>
The ARN of the trusted token issuer configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [TrustedTokenIssuerConfiguration](#API_DescribeTrustedTokenIssuer_ResponseSyntax) **   <a name="singlesignon-DescribeTrustedTokenIssuer-response-TrustedTokenIssuerConfiguration"></a>
A structure the describes the settings that apply of this trusted token issuer.
Type: [TrustedTokenIssuerConfiguration](API_TrustedTokenIssuerConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [TrustedTokenIssuerType](#API_DescribeTrustedTokenIssuer_ResponseSyntax) **   <a name="singlesignon-DescribeTrustedTokenIssuer-response-TrustedTokenIssuerType"></a>
The type of the trusted token issuer.
Type: String
Valid Values: `OIDC_JWT`

## Errors
<a name="API_DescribeTrustedTokenIssuer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
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
<a name="API_DescribeTrustedTokenIssuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeTrustedTokenIssuer)

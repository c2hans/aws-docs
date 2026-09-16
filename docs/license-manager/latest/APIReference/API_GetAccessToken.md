---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetAccessToken.html
---

# GetAccessToken
<a name="API_GetAccessToken"></a>

Gets a temporary access token to use with AssumeRoleWithWebIdentity. Access tokens are valid for one hour.

## Request Syntax
<a name="API_GetAccessToken_RequestSyntax"></a>

```
{
   "Token": "{{string}}",
   "TokenProperties": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetAccessToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Token](#API_GetAccessToken_RequestSyntax) **   <a name="licensemanager-GetAccessToken-request-Token"></a>
Refresh token, encoded as a JWT token.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: Yes

 ** [TokenProperties](#API_GetAccessToken_RequestSyntax) **   <a name="licensemanager-GetAccessToken-request-TokenProperties"></a>
Token properties to validate against those present in the JWT token.
Type: Array of strings
Array Members: Maximum number of 3 items.
Required: No

## Response Syntax
<a name="API_GetAccessToken_ResponseSyntax"></a>

```
{
   "AccessToken": "string"
}
```

## Response Elements
<a name="API_GetAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessToken](#API_GetAccessToken_ResponseSyntax) **   <a name="licensemanager-GetAccessToken-response-AccessToken"></a>
Temporary access token.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`

## Errors
<a name="API_GetAccessToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_GetAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/GetAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/GetAccessToken)

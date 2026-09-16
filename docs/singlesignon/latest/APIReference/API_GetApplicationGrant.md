---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationGrant.html
---

# GetApplicationGrant
<a name="API_GetApplicationGrant"></a>

Retrieves details about an application grant.

## Request Syntax
<a name="API_GetApplicationGrant_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "GrantType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetApplicationGrant_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_GetApplicationGrant_RequestSyntax) **   <a name="singlesignon-GetApplicationGrant-request-ApplicationArn"></a>
Specifies the ARN of the application that contains the grant.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [GrantType](#API_GetApplicationGrant_RequestSyntax) **   <a name="singlesignon-GetApplicationGrant-request-GrantType"></a>
Specifies the type of grant.
Type: String
Valid Values: `authorization_code | refresh_token | urn:ietf:params:oauth:grant-type:jwt-bearer | urn:ietf:params:oauth:grant-type:token-exchange`
Required: Yes

## Response Syntax
<a name="API_GetApplicationGrant_ResponseSyntax"></a>

```
{
   "Grant": { ... }
}
```

## Response Elements
<a name="API_GetApplicationGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Grant](#API_GetApplicationGrant_ResponseSyntax) **   <a name="singlesignon-GetApplicationGrant-response-Grant"></a>
A structure that describes the requested grant.
Type: [Grant](API_Grant.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetApplicationGrant_Errors"></a>

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
<a name="API_GetApplicationGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/GetApplicationGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/GetApplicationGrant)

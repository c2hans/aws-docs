---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationGrant.html
---

# PutApplicationGrant
<a name="API_PutApplicationGrant"></a>

Creates a configuration for an application to use grants. Conceptually grants are authorization to request actions related to tokens. This configuration will be used when parties are requesting and receiving tokens during the trusted identity propagation process. For more information on the IAM Identity Center supported grant workflows, see [SAML 2.0 and OAuth 2.0](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html).

A grant is created between your applications and Identity Center instance which enables an application to use specified mechanisms to obtain tokens. These tokens are used by your applications to gain access to AWS resources on behalf of users. The following elements are within these exchanges:
+  **Requester** - The application requesting access to AWS resources.
+  **Subject** - Typically the user that is requesting access to AWS resources.
+  **Grant** - Conceptually, a grant is authorization to access AWS resources. These grants authorize token generation for authenticating access to the requester and for the request to make requests on behalf of the subjects. There are four types of grants:
  +  **AuthorizationCode** - Allows an application to request authorization through a series of user-agent redirects.
  +  **JWT bearer ** - Authorizes an application to exchange a JSON Web Token that came from an external identity provider. To learn more, see [RFC 6479](https://datatracker.ietf.org/doc/html/rfc6749).
  +  **Refresh token** - Enables application to request new access tokens to replace expiring or expired access tokens.
  +  **Exchange token** - A grant that requests tokens from the authorization server by providing a ‘subject’ token with access scope authorizing trusted identity propagation to this application. To learn more, see [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693).
+  **Authorization server** - IAM Identity Center requests tokens.

User credentials are never shared directly within these exchanges. Instead, applications use grants to request access tokens from IAM Identity Center. For more information, see [RFC 6479](https://datatracker.ietf.org/doc/html/rfc6749).

**Use cases**
+ Connecting to custom applications.
+ Configuring an AWS service to make calls to another AWS services using JWT tokens.

## Request Syntax
<a name="API_PutApplicationGrant_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "Grant": { ... },
   "GrantType": "{{string}}"
}
```

## Request Parameters
<a name="API_PutApplicationGrant_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_PutApplicationGrant_RequestSyntax) **   <a name="singlesignon-PutApplicationGrant-request-ApplicationArn"></a>
Specifies the ARN of the application to update.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [Grant](#API_PutApplicationGrant_RequestSyntax) **   <a name="singlesignon-PutApplicationGrant-request-Grant"></a>
Specifies a structure that describes the grant to update.
Type: [Grant](API_Grant.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [GrantType](#API_PutApplicationGrant_RequestSyntax) **   <a name="singlesignon-PutApplicationGrant-request-GrantType"></a>
Specifies the type of grant to update.
Type: String
Valid Values: `authorization_code | refresh_token | urn:ietf:params:oauth:grant-type:jwt-bearer | urn:ietf:params:oauth:grant-type:token-exchange`
Required: Yes

## Response Elements
<a name="API_PutApplicationGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutApplicationGrant_Errors"></a>

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
<a name="API_PutApplicationGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/PutApplicationGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/PutApplicationGrant)

---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.html
---

# GetIdentityProviderByIdentifier
<a name="API_GetIdentityProviderByIdentifier"></a>

Given the identifier of an identity provider (IdP), for example `examplecorp`, returns information about the user pool configuration for that IdP. For more information about IdPs, see [Third-party IdP sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html).

## Request Syntax
<a name="API_GetIdentityProviderByIdentifier_RequestSyntax"></a>

```
{
   "IdpIdentifier": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIdentityProviderByIdentifier_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdpIdentifier](#API_GetIdentityProviderByIdentifier_RequestSyntax) **   <a name="CognitoUserPools-GetIdentityProviderByIdentifier-request-IdpIdentifier"></a>
The identifier that you assigned to your user pool. The identifier is an alternative name for an IdP that is distinct from the IdP name. For example, an IdP with a name of `MyIdP` might have an identifier of the email domain `example.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[\w\s+=.@-]+`
Required: Yes

 ** [UserPoolId](#API_GetIdentityProviderByIdentifier_RequestSyntax) **   <a name="CognitoUserPools-GetIdentityProviderByIdentifier-request-UserPoolId"></a>
The ID of the user pool where you want to get information about the IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_GetIdentityProviderByIdentifier_ResponseSyntax"></a>

```
{
   "IdentityProvider": {
      "AttributeMapping": {
         "string" : "string"
      },
      "CreationDate": number,
      "IdpIdentifiers": [ "string" ],
      "LastModifiedDate": number,
      "ProviderDetails": {
         "string" : "string"
      },
      "ProviderName": "string",
      "ProviderType": "string",
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_GetIdentityProviderByIdentifier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProvider](#API_GetIdentityProviderByIdentifier_ResponseSyntax) **   <a name="CognitoUserPools-GetIdentityProviderByIdentifier-response-IdentityProvider"></a>
The configuration of the IdP in your user pool. Includes additional identifiers, the IdP name and type, and trust-relationship details like the issuer URL.
Type: [IdentityProviderType](API_IdentityProviderType.md) object

## Errors
<a name="API_GetIdentityProviderByIdentifier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_GetIdentityProviderByIdentifier_Examples"></a>

### Example
<a name="API_GetIdentityProviderByIdentifier_Example_1"></a>

The following example request returns the details of the IdP with the identifier `MySSO`.

#### Sample Request
<a name="API_GetIdentityProviderByIdentifier_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.GetIdentityProviderByIdentifier
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "IdpIdentifier": "MySSO",
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_GetIdentityProviderByIdentifier_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "IdentityProvider": {
        "AttributeMapping": {
            "email": "idp_email"
        },
        "CreationDate": 1643741231.169,
        "IdpIdentifiers": [
            "MySSO"
        ],
        "LastModifiedDate": 1703798328.069,
        "ProviderDetails": {
            "ActiveEncryptionCertificate": "[Certificate text]",
            "IDPSignout": "false",
            "MetadataFile": "<md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"http://www.example.com/saml\"><md:IDPSSODescriptor WantAuthnRequestsSigned=\"false\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:KeyDescriptor use=\"signing\"><ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:X509Data><ds:X509Certificate>CERTIFICATE_DATA</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://example.com/slo/saml\"/><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://example.com/slo/saml\"/><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://example.com/sso/saml\"/><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://example.com/sso/saml\"/></md:IDPSSODescriptor></md:EntityDescriptor>",
            "SLORedirectBindingURI": "https://example.com/slo/saml",
            "SSORedirectBindingURI": "https://example.com/sso/saml"
        },
        "ProviderName": "Corp-SSO",
        "ProviderType": "SAML",
        "UserPoolId": "us-west-2_EXAMPLE"
    }
}
```

## See Also
<a name="API_GetIdentityProviderByIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier)

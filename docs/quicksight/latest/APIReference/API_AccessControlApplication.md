---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccessControlApplication.html
---

# AccessControlApplication

An access control application. It defines how an external client signs in to Quick Sight with OAuth 2.0. Client secret values are never included.

## Contents
<a name="API_AccessControlApplication_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplicationId **   <a name="QS-Type-AccessControlApplication-ApplicationId"></a>
The ID of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Arn **   <a name="QS-Type-AccessControlApplication-Arn"></a>
The ARN of the access control application.
Type: String
Required: Yes

 ** AuthenticationType **   <a name="QS-Type-AccessControlApplication-AuthenticationType"></a>
The authentication protocol that the access control application uses.
Type: String
Valid Values: `OIDC`
Required: Yes

 ** CreatedTime **   <a name="QS-Type-AccessControlApplication-CreatedTime"></a>
The time when the access control application was created.
Type: Timestamp
Required: Yes

 ** LastUpdatedTime **   <a name="QS-Type-AccessControlApplication-LastUpdatedTime"></a>
The time when the access control application was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-AccessControlApplication-Name"></a>
The name of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Namespace **   <a name="QS-Type-AccessControlApplication-Namespace"></a>
The Quick Sight namespace that the access control application belongs to.
Type: String
Required: Yes

 ** Status **   <a name="QS-Type-AccessControlApplication-Status"></a>
The status of the access control application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** TenantUrl **   <a name="QS-Type-AccessControlApplication-TenantUrl"></a>
The tenant URL of the access control application. This URL hosts the OAuth 2.0 and OpenID Connect endpoints for the application, such as `/authorize`, `/token`, `/.well-known/openid-configuration`, and `/jwks`.
Type: String
Required: Yes

 ** Description **   <a name="QS-Type-AccessControlApplication-Description"></a>
The description of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** IdcApplicationArn **   <a name="QS-Type-AccessControlApplication-IdcApplicationArn"></a>
The ARN of the AWS IAM Identity Center application that Quick Sight manages for this access control application. This value is present when the `IdpAuthorizingType` is `IDC_AUTH_CODE`, or when a trusted token issuer is configured.
Type: String
Required: No

 ** IdpAuthorizingConfiguration **   <a name="QS-Type-AccessControlApplication-IdpAuthorizingConfiguration"></a>
The identity provider configuration of the access control application. Client secret values are never included.
Type: [IdpAuthorizingConfig](API_IdpAuthorizingConfig.md) object
Required: No

 ** QuickAuthenticationConfiguration **   <a name="QS-Type-AccessControlApplication-QuickAuthenticationConfiguration"></a>
The Quick Sight authentication configuration of the access control application. Client secret values are never included.
Type: [QuickAuthenticationConfig](API_QuickAuthenticationConfig.md) object
Required: No

## See Also
<a name="API_AccessControlApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AccessControlApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AccessControlApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AccessControlApplication)

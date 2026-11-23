---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccessControlApplicationSummary.html
---

# AccessControlApplicationSummary

A summary of an access control application, including its ID, ARN, name, namespace, authentication type, status, and timestamps.

## Contents
<a name="API_AccessControlApplicationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplicationId **   <a name="QS-Type-AccessControlApplicationSummary-ApplicationId"></a>
The ID of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Arn **   <a name="QS-Type-AccessControlApplicationSummary-Arn"></a>
The ARN of the access control application.
Type: String
Required: Yes

 ** AuthenticationType **   <a name="QS-Type-AccessControlApplicationSummary-AuthenticationType"></a>
The authentication protocol that the access control application uses.
Type: String
Valid Values: `OIDC`
Required: Yes

 ** CreatedTime **   <a name="QS-Type-AccessControlApplicationSummary-CreatedTime"></a>
The time when the access control application was created.
Type: Timestamp
Required: Yes

 ** LastUpdatedTime **   <a name="QS-Type-AccessControlApplicationSummary-LastUpdatedTime"></a>
The time when the access control application was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-AccessControlApplicationSummary-Name"></a>
The name of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Namespace **   <a name="QS-Type-AccessControlApplicationSummary-Namespace"></a>
The Quick Sight namespace that the access control application belongs to.
Type: String
Required: Yes

 ** Status **   <a name="QS-Type-AccessControlApplicationSummary-Status"></a>
The status of the access control application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** TenantUrl **   <a name="QS-Type-AccessControlApplicationSummary-TenantUrl"></a>
The tenant URL of the access control application. This URL hosts the OAuth 2.0 and OpenID Connect endpoints for the application, such as `/authorize`, `/token`, `/.well-known/openid-configuration`, and `/jwks`.
Type: String
Required: Yes

 ** Description **   <a name="QS-Type-AccessControlApplicationSummary-Description"></a>
The description of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** IdpAuthorizingConfiguration **   <a name="QS-Type-AccessControlApplicationSummary-IdpAuthorizingConfiguration"></a>
A summary of the identity provider configuration of the access control application, without client secret information.
Type: [IdpAuthorizingConfigSummary](API_IdpAuthorizingConfigSummary.md) object
Required: No

 ** QuickAuthenticationConfiguration **   <a name="QS-Type-AccessControlApplicationSummary-QuickAuthenticationConfiguration"></a>
The Quick Sight authentication configuration of the access control application. Client secret values are never included.
Type: [QuickAuthenticationConfig](API_QuickAuthenticationConfig.md) object
Required: No

## See Also
<a name="API_AccessControlApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AccessControlApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AccessControlApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AccessControlApplicationSummary)

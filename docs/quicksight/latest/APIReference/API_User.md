---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

A registered user of Quick Sight.

## Contents
<a name="API_User_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Active **   <a name="QS-Type-User-Active"></a>
The active status of user. When you create an Quick Sight user that's not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.
Type: Boolean
Required: No

 ** Arn **   <a name="QS-Type-User-Arn"></a>
The Amazon Resource Name (ARN) for the user.
Type: String
Required: No

 ** CustomPermissionsName **   <a name="QS-Type-User-CustomPermissionsName"></a>
The custom permissions profile associated with this user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`
Required: No

 ** Email **   <a name="QS-Type-User-Email"></a>
The user's email address.
Type: String
Required: No

 ** ExternalLoginFederationProviderType **   <a name="QS-Type-User-ExternalLoginFederationProviderType"></a>
The type of supported external login provider that provides identity to let the user federate into Quick Sight with an associated IAM role. The type can be one of the following.
+  `COGNITO`: Amazon Cognito. The provider URL is cognito-identity.amazonaws.com.
+  `CUSTOM_OIDC`: Custom OpenID Connect (OIDC) provider.
Type: String
Required: No

 ** ExternalLoginFederationProviderUrl **   <a name="QS-Type-User-ExternalLoginFederationProviderUrl"></a>
The URL of the external login provider.
Type: String
Required: No

 ** ExternalLoginId **   <a name="QS-Type-User-ExternalLoginId"></a>
The identity ID for the user in the external login provider.
Type: String
Required: No

 ** IdentityType **   <a name="QS-Type-User-IdentityType"></a>
The type of identity authentication used by the user.
Type: String
Valid Values: `IAM | QUICKSIGHT | IAM_IDENTITY_CENTER`
Required: No

 ** PrincipalId **   <a name="QS-Type-User-PrincipalId"></a>
The principal ID of the user.
Type: String
Required: No

 ** Role **   <a name="QS-Type-User-Role"></a>
The Quick Sight role for the user. The user role can be one of the following:.
+  `READER`: A user who has read-only access to dashboards.
+  `AUTHOR`: A user who can create data sources, datasets, analyses, and dashboards.
+  `ADMIN`: A user who is an author, who can also manage Amazon Quick Sight settings.
+  `READER_PRO`: Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Quick Sight, can build stories with Amazon Q, and can generate executive summaries from dashboards.
+  `AUTHOR_PRO`: Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.
+  `ADMIN_PRO`: Admin Pros are Author Pros who can also manage Quick Sight administrative settings. Admin Pro users are billed at Author Pro pricing.
+  `RESTRICTED_READER`: This role isn't currently available for use.
+  `RESTRICTED_AUTHOR`: This role isn't currently available for use.
Type: String
Valid Values: `ADMIN | AUTHOR | READER | RESTRICTED_AUTHOR | RESTRICTED_READER | ADMIN_PRO | AUTHOR_PRO | READER_PRO`
Required: No

 ** UserName **   <a name="QS-Type-User-UserName"></a>
The user's user name. This value is required if you are registering a user that will be managed in Quick Sight. In the output, the value for `UserName` is `N/A` when the value for `IdentityType` is `IAM` and the corresponding IAM user is deleted.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/User)

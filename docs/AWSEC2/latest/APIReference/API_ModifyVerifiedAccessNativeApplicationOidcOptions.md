---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessNativeApplicationOidcOptions.html
---

# ModifyVerifiedAccessNativeApplicationOidcOptions
<a name="API_ModifyVerifiedAccessNativeApplicationOidcOptions"></a>

Describes the OpenID Connect (OIDC) options.

## Contents
<a name="API_ModifyVerifiedAccessNativeApplicationOidcOptions_Contents"></a>

 ** AuthorizationEndpoint **
The authorization endpoint of the IdP.
Type: String
Required: No

 ** ClientId **
The OAuth 2.0 client identifier.
Type: String
Required: No

 ** ClientSecret **
The OAuth 2.0 client secret.
Type: String
Required: No

 ** Issuer **
The OIDC issuer identifier of the IdP.
Type: String
Required: No

 ** PublicSigningKeyEndpoint **
The public signing key endpoint.
Type: String
Required: No

 ** Scope **
The set of user claims to be requested from the IdP.
Type: String
Required: No

 ** TokenEndpoint **
The token endpoint of the IdP.
Type: String
Required: No

 ** UserInfoEndpoint **
The user info endpoint of the IdP.
Type: String
Required: No

## See Also
<a name="API_ModifyVerifiedAccessNativeApplicationOidcOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVerifiedAccessNativeApplicationOidcOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVerifiedAccessNativeApplicationOidcOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVerifiedAccessNativeApplicationOidcOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

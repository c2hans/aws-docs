---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessTrustProviderOidcOptions.html
---

# CreateVerifiedAccessTrustProviderOidcOptions
<a name="API_CreateVerifiedAccessTrustProviderOidcOptions"></a>

Describes the options when creating an AWS Verified Access trust provider using the `user` type.

## Contents
<a name="API_CreateVerifiedAccessTrustProviderOidcOptions_Contents"></a>

 ** AuthorizationEndpoint **
The OIDC authorization endpoint.
Type: String
Required: No

 ** ClientId **
The client identifier.
Type: String
Required: No

 ** ClientSecret **
The client secret.
Type: String
Required: No

 ** Issuer **
The OIDC issuer.
Type: String
Required: No

 ** Scope **
OpenID Connect (OIDC) scopes are used by an application during authentication to authorize access to a user's details. Each scope returns a specific set of user attributes.
Type: String
Required: No

 ** TokenEndpoint **
The OIDC token endpoint.
Type: String
Required: No

 ** UserInfoEndpoint **
The OIDC user info endpoint.
Type: String
Required: No

## See Also
<a name="API_CreateVerifiedAccessTrustProviderOidcOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVerifiedAccessTrustProviderOidcOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVerifiedAccessTrustProviderOidcOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVerifiedAccessTrustProviderOidcOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

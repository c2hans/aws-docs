---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessTrustProvider.html
---

# VerifiedAccessTrustProvider
<a name="API_VerifiedAccessTrustProvider"></a>

Describes a Verified Access trust provider.

## Contents
<a name="API_VerifiedAccessTrustProvider_Contents"></a>

 ** creationTime **
The creation time.
Type: String
Required: No

 ** description **
A description for the AWS Verified Access trust provider.
Type: String
Required: No

 ** deviceOptions **
The options for device-identity trust provider.
Type: [DeviceOptions](API_DeviceOptions.md) object
Required: No

 ** deviceTrustProviderType **
The type of device-based trust provider.
Type: String
Valid Values: `jamf | crowdstrike | jumpcloud`
Required: No

 ** lastUpdatedTime **
The last updated time.
Type: String
Required: No

 ** nativeApplicationOidcOptions **
The OpenID Connect (OIDC) options.
Type: [NativeApplicationOidcOptions](API_NativeApplicationOidcOptions.md) object
Required: No

 ** oidcOptions **
The options for an OpenID Connect-compatible user-identity trust provider.
Type: [OidcOptions](API_OidcOptions.md) object
Required: No

 ** policyReferenceName **
The identifier to be used when working with policy rules.
Type: String
Required: No

 ** sseSpecification **
The options in use for server side encryption.
Type: [VerifiedAccessSseSpecificationResponse](API_VerifiedAccessSseSpecificationResponse.md) object
Required: No

 ** TagSet.N **
The tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trustProviderType **
The type of Verified Access trust provider.
Type: String
Valid Values: `user | device`
Required: No

 ** userTrustProviderType **
The type of user-based trust provider.
Type: String
Valid Values: `iam-identity-center | oidc`
Required: No

 ** verifiedAccessTrustProviderId **
The ID of the AWS Verified Access trust provider.
Type: String
Required: No

## See Also
<a name="API_VerifiedAccessTrustProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessTrustProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessTrustProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessTrustProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

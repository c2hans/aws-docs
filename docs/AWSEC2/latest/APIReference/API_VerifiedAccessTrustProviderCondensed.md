---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessTrustProviderCondensed.html
---

# VerifiedAccessTrustProviderCondensed
<a name="API_VerifiedAccessTrustProviderCondensed"></a>

Condensed information about a trust provider.

## Contents
<a name="API_VerifiedAccessTrustProviderCondensed_Contents"></a>

 ** description **
The description of trust provider.
Type: String
Required: No

 ** deviceTrustProviderType **
The type of device-based trust provider.
Type: String
Valid Values: `jamf | crowdstrike | jumpcloud`
Required: No

 ** trustProviderType **
The type of trust provider (user- or device-based).
Type: String
Valid Values: `user | device`
Required: No

 ** userTrustProviderType **
The type of user-based trust provider.
Type: String
Valid Values: `iam-identity-center | oidc`
Required: No

 ** verifiedAccessTrustProviderId **
The ID of the trust provider.
Type: String
Required: No

## See Also
<a name="API_VerifiedAccessTrustProviderCondensed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessTrustProviderCondensed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessTrustProviderCondensed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessTrustProviderCondensed)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

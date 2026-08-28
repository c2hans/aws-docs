---
source_url: https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_AwsAdditionalDetails.html
---

# AwsAdditionalDetails
<a name="API_AwsAdditionalDetails"></a>

This structure contains AWS-specific parameter extensions and the [identity context](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html).

## Contents
<a name="API_AwsAdditionalDetails_Contents"></a>

 ** identityContext **   <a name="singlesignon-Type-AwsAdditionalDetails-identityContext"></a>
The trusted context assertion is signed and encrypted by AWS STS. It provides access to `sts:identity_context` claim in the `idToken` without JWT parsing
Identity context comprises information that AWS services use to make authorization decisions when they receive requests.
Type: String
Required: No

## See Also
<a name="API_AwsAdditionalDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-oidc-2019-06-10/AwsAdditionalDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-oidc-2019-06-10/AwsAdditionalDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-oidc-2019-06-10/AwsAdditionalDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrustedIdentityPropagationSettings.html
---

# TrustedIdentityPropagationSettings
<a name="API_TrustedIdentityPropagationSettings"></a>

The Trusted Identity Propagation (TIP) settings for the SageMaker domain. These settings determine how user identities from IAM Identity Center are propagated through the domain to TIP enabled AWS services.

## Contents
<a name="API_TrustedIdentityPropagationSettings_Contents"></a>

 ** Status **   <a name="sagemaker-Type-TrustedIdentityPropagationSettings-Status"></a>
The status of Trusted Identity Propagation (TIP) at the SageMaker domain level.
When disabled, standard IAM role-based access is used.
When enabled:
+ User identities from IAM Identity Center are propagated through the application to TIP enabled AWS services.
+ New applications or existing applications that are automatically patched, will use the domain level configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_TrustedIdentityPropagationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrustedIdentityPropagationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrustedIdentityPropagationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrustedIdentityPropagationSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

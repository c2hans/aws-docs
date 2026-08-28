---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ContinuousDeploymentPolicyConfig.html
---

# ContinuousDeploymentPolicyConfig
<a name="API_ContinuousDeploymentPolicyConfig"></a>

Contains the configuration for a continuous deployment policy.

## Contents
<a name="API_ContinuousDeploymentPolicyConfig_Contents"></a>

 ** Enabled **   <a name="cloudfront-Type-ContinuousDeploymentPolicyConfig-Enabled"></a>
A Boolean that indicates whether this continuous deployment policy is enabled (in effect). When this value is `true`, this policy is enabled and in effect. When this value is `false`, this policy is not enabled and has no effect.
Type: Boolean
Required: Yes

 ** StagingDistributionDnsNames **   <a name="cloudfront-Type-ContinuousDeploymentPolicyConfig-StagingDistributionDnsNames"></a>
The CloudFront domain name of the staging distribution. For example: `d111111abcdef8.cloudfront.net`.
Type: [StagingDistributionDnsNames](API_StagingDistributionDnsNames.md) object
Required: Yes

 ** TrafficConfig **   <a name="cloudfront-Type-ContinuousDeploymentPolicyConfig-TrafficConfig"></a>
Contains the parameters for routing production traffic from your primary to staging distributions.
Type: [TrafficConfig](API_TrafficConfig.md) object
Required: No

## See Also
<a name="API_ContinuousDeploymentPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

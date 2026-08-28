---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ContinuousDeploymentSingleWeightConfig.html
---

# ContinuousDeploymentSingleWeightConfig
<a name="API_ContinuousDeploymentSingleWeightConfig"></a>

Contains the percentage of traffic to send to a staging distribution.

## Contents
<a name="API_ContinuousDeploymentSingleWeightConfig_Contents"></a>

 ** Weight **   <a name="cloudfront-Type-ContinuousDeploymentSingleWeightConfig-Weight"></a>
The percentage of traffic to send to a staging distribution, expressed as a decimal number between 0 and 0.15. For example, a value of 0.10 means 10% of traffic is sent to the staging distribution.
Type: Float
Required: Yes

 ** SessionStickinessConfig **   <a name="cloudfront-Type-ContinuousDeploymentSingleWeightConfig-SessionStickinessConfig"></a>
Session stickiness provides the ability to define multiple requests from a single viewer as a single session. This prevents the potentially inconsistent experience of sending some of a given user's requests to your staging distribution, while others are sent to your primary distribution. Define the session duration using TTL values.
Type: [SessionStickinessConfig](API_SessionStickinessConfig.md) object
Required: No

## See Also
<a name="API_ContinuousDeploymentSingleWeightConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

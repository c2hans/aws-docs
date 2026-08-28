---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TrafficConfig.html
---

# TrafficConfig
<a name="API_TrafficConfig"></a>

The traffic configuration of your continuous deployment.

## Contents
<a name="API_TrafficConfig_Contents"></a>

 ** Type **   <a name="cloudfront-Type-TrafficConfig-Type"></a>
The type of traffic configuration.
Type: String
Valid Values: `SingleWeight | SingleHeader`
Required: Yes

 ** SingleHeaderConfig **   <a name="cloudfront-Type-TrafficConfig-SingleHeaderConfig"></a>
Determines which HTTP requests are sent to the staging distribution.
Type: [ContinuousDeploymentSingleHeaderConfig](API_ContinuousDeploymentSingleHeaderConfig.md) object
Required: No

 ** SingleWeightConfig **   <a name="cloudfront-Type-TrafficConfig-SingleWeightConfig"></a>
Contains the percentage of traffic to send to the staging distribution.
Type: [ContinuousDeploymentSingleWeightConfig](API_ContinuousDeploymentSingleWeightConfig.md) object
Required: No

## See Also
<a name="API_TrafficConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TrafficConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TrafficConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TrafficConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

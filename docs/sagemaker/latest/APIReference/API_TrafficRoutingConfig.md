---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrafficRoutingConfig.html
---

# TrafficRoutingConfig
<a name="API_TrafficRoutingConfig"></a>

Defines the traffic routing strategy during an endpoint deployment to shift traffic from the old fleet to the new fleet.

## Contents
<a name="API_TrafficRoutingConfig_Contents"></a>

 ** Type **   <a name="sagemaker-Type-TrafficRoutingConfig-Type"></a>
Traffic routing strategy type.
+  `ALL_AT_ONCE`: Endpoint traffic shifts to the new fleet in a single step.
+  `CANARY`: Endpoint traffic shifts to the new fleet in two steps. The first step is the canary, which is a small portion of the traffic. The second step is the remainder of the traffic.
+  `LINEAR`: Endpoint traffic shifts to the new fleet in n steps of a configurable size.
Type: String
Valid Values: `ALL_AT_ONCE | CANARY | LINEAR`
Required: Yes

 ** WaitIntervalInSeconds **   <a name="sagemaker-Type-TrafficRoutingConfig-WaitIntervalInSeconds"></a>
The waiting time (in seconds) between incremental steps to turn on traffic on the new endpoint fleet.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: Yes

 ** CanarySize **   <a name="sagemaker-Type-TrafficRoutingConfig-CanarySize"></a>
Batch size for the first step to turn on traffic on the new endpoint fleet. `Value` must be less than or equal to 50% of the variant's total instance count.
Type: [CapacitySize](API_CapacitySize.md) object
Required: No

 ** LinearStepSize **   <a name="sagemaker-Type-TrafficRoutingConfig-LinearStepSize"></a>
Batch size for each step to turn on traffic on the new endpoint fleet. `Value` must be 10-50% of the variant's total instance count.
Type: [CapacitySize](API_CapacitySize.md) object
Required: No

## See Also
<a name="API_TrafficRoutingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrafficRoutingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrafficRoutingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrafficRoutingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

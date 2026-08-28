---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentAvailabilityZoneBalance.html
---

# InferenceComponentAvailabilityZoneBalance
<a name="API_InferenceComponentAvailabilityZoneBalance"></a>

Configuration for balancing inference component copies across Availability Zones.

## Contents
<a name="API_InferenceComponentAvailabilityZoneBalance_Contents"></a>

 ** EnforcementMode **   <a name="sagemaker-Type-InferenceComponentAvailabilityZoneBalance-EnforcementMode"></a>
Determines how strictly the Availability Zone balance constraint is enforced.
PERMISSIVE
The endpoint attempts to balance copies across Availability Zones but proceeds with scheduling even if balance can't be achieved due to available capacity or instance distribution across Availability Zones.
Type: String
Valid Values: `PERMISSIVE`
Required: Yes

 ** MaxImbalance **   <a name="sagemaker-Type-InferenceComponentAvailabilityZoneBalance-MaxImbalance"></a>
The maximum allowed difference in the number of inference component copies between any two Availability Zones. This parameter applies only when the endpoint has instances across two or more Availability Zones. A copy placement is allowed if it reduces imbalance or the resulting imbalance is within this value.
Default value: `0`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_InferenceComponentAvailabilityZoneBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentAvailabilityZoneBalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentAvailabilityZoneBalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentAvailabilityZoneBalance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

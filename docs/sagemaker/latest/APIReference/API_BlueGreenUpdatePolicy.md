---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BlueGreenUpdatePolicy.html
---

# BlueGreenUpdatePolicy
<a name="API_BlueGreenUpdatePolicy"></a>

Update policy for a blue/green deployment. If this update policy is specified, SageMaker creates a new fleet during the deployment while maintaining the old fleet. SageMaker flips traffic to the new fleet according to the specified traffic routing configuration. Only one update policy should be used in the deployment configuration. If no update policy is specified, SageMaker uses a blue/green deployment strategy with all at once traffic shifting by default.

## Contents
<a name="API_BlueGreenUpdatePolicy_Contents"></a>

 ** TrafficRoutingConfiguration **   <a name="sagemaker-Type-BlueGreenUpdatePolicy-TrafficRoutingConfiguration"></a>
Defines the traffic routing strategy to shift traffic from the old fleet to the new fleet during an endpoint deployment.
Type: [TrafficRoutingConfig](API_TrafficRoutingConfig.md) object
Required: Yes

 ** MaximumExecutionTimeoutInSeconds **   <a name="sagemaker-Type-BlueGreenUpdatePolicy-MaximumExecutionTimeoutInSeconds"></a>
Maximum execution timeout for the deployment. Note that the timeout value should be larger than the total waiting time specified in `TerminationWaitInSeconds` and `WaitIntervalInSeconds`.
Type: Integer
Valid Range: Minimum value of 600. Maximum value of 28800.
Required: No

 ** TerminationWaitInSeconds **   <a name="sagemaker-Type-BlueGreenUpdatePolicy-TerminationWaitInSeconds"></a>
Additional waiting time in seconds after the completion of an endpoint deployment before terminating the old endpoint fleet. Default is 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

## See Also
<a name="API_BlueGreenUpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BlueGreenUpdatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BlueGreenUpdatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BlueGreenUpdatePolicy)

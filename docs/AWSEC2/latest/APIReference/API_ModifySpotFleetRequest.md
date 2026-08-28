---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest.html
---

# ModifySpotFleetRequest
<a name="API_ModifySpotFleetRequest"></a>

Modifies the specified Spot Fleet request.

You can only modify a Spot Fleet request of type `maintain`.

While the Spot Fleet request is being modified, it is in the `modifying` state.

To scale up your Spot Fleet, increase its target capacity. The Spot Fleet launches the additional Spot Instances according to the allocation strategy for the Spot Fleet request. If the allocation strategy is `lowestPrice`, the Spot Fleet launches instances using the Spot Instance pool with the lowest price. If the allocation strategy is `diversified`, the Spot Fleet distributes the instances across the Spot Instance pools. If the allocation strategy is `capacityOptimized`, Spot Fleet launches instances from Spot Instance pools with optimal capacity for the number of instances that are launching.

To scale down your Spot Fleet, decrease its target capacity. First, the Spot Fleet cancels any open requests that exceed the new target capacity. You can request that the Spot Fleet terminate Spot Instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is `lowestPrice`, the Spot Fleet terminates the instances with the highest price per unit. If the allocation strategy is `capacityOptimized`, the Spot Fleet terminates the instances in the Spot Instance pools that have the least available Spot Instance capacity. If the allocation strategy is `diversified`, the Spot Fleet terminates instances across the Spot Instance pools. Alternatively, you can request that the Spot Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually.

If you are finished with your Spot Fleet for now, but will use it again later, you can set the target capacity to 0.

## Request Parameters
<a name="API_ModifySpotFleetRequest_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Context**
Reserved.
Type: String
Required: No

 **ExcessCapacityTerminationPolicy**
Indicates whether running instances should be terminated if the target capacity of the Spot Fleet request is decreased below the current size of the Spot Fleet.
Supported only for fleets of type `maintain`.
Type: String
Valid Values: `noTermination | default`
Required: No

 **LaunchTemplateConfig.N**
The launch template and overrides. You can only use this parameter if you specified a launch template (`LaunchTemplateConfigs`) in your Spot Fleet request. If you specified `LaunchSpecifications` in your Spot Fleet request, then omit this parameter.
Type: Array of [LaunchTemplateConfig](API_LaunchTemplateConfig.md) objects
Required: No

 **OnDemandTargetCapacity**
The number of On-Demand Instances in the fleet.
Type: Integer
Required: No

 **SpotFleetRequestId**
The ID of the Spot Fleet request.
Type: String
Required: Yes

 **TargetCapacity**
The size of the fleet.
Type: Integer
Required: No

## Response Elements
<a name="API_ModifySpotFleetRequest_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
If the request succeeds, the response returns `true`. If the request fails, no response is returned, and instead an error message is returned.
Type: Boolean

## Errors
<a name="API_ModifySpotFleetRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifySpotFleetRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifySpotFleetRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifySpotFleetRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

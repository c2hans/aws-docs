---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyCapacityReservation.html
---

# ModifyCapacityReservation
<a name="API_ModifyCapacityReservation"></a>

Modifies the capacity reservation of the specified load balancer.

When modifying capacity reservation, you must include at least one `MinimumLoadBalancerCapacity` or `ResetCapacityReservation`.

## Request Parameters
<a name="API_ModifyCapacityReservation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

 ** MinimumLoadBalancerCapacity **
The minimum load balancer capacity reserved.
Type: [MinimumLoadBalancerCapacity](API_MinimumLoadBalancerCapacity.md) object
Required: No

 ** ResetCapacityReservation **
Resets the capacity reservation.
Type: Boolean
Required: No

## Response Elements
<a name="API_ModifyCapacityReservation_ResponseElements"></a>

The following elements are returned by the service.

 **CapacityReservationState.member.N**
The state of the capacity reservation.
Type: Array of [ZonalCapacityReservationState](API_ZonalCapacityReservationState.md) objects

 ** DecreaseRequestsRemaining **
The amount of daily capacity decreases remaining.
Type: Integer

 ** LastModifiedTime **
The last time the capacity reservation was modified.
Type: Timestamp

 ** MinimumLoadBalancerCapacity **
The requested minimum capacity reservation for the load balancer
Type: [MinimumLoadBalancerCapacity](API_MinimumLoadBalancerCapacity.md) object

## Errors
<a name="API_ModifyCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CapacityDecreaseRequestLimitExceeded **
You've exceeded the daily capacity decrease limit for this reservation.
HTTP Status Code: 400

 ** CapacityReservationPending **
There is a pending capacity reservation.
HTTP Status Code: 400

 ** CapacityUnitsLimitExceeded **
You've exceeded the capacity units limit.
HTTP Status Code: 400

 ** InsufficientCapacity **
There is insufficient capacity to reserve.
HTTP Status Code: 500

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** OperationNotPermitted **
This operation is not allowed.
HTTP Status Code: 400

 ** PriorRequestNotComplete **
This operation is not allowed while a prior request has not been completed.
HTTP Status Code: 429

## See Also
<a name="API_ModifyCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyCapacityReservation)

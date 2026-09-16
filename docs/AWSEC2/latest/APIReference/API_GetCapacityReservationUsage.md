---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityReservationUsage.html
---

# GetCapacityReservationUsage
<a name="API_GetCapacityReservationUsage"></a>

Gets usage information about a Capacity Reservation. If the Capacity Reservation is shared, it shows usage information for the Capacity Reservation owner and each AWS account that is currently using the shared capacity. If the Capacity Reservation is not shared, it shows only the Capacity Reservation owner's usage.

## Request Parameters
<a name="API_GetCapacityReservationUsage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityReservationId**
The ID of the Capacity Reservation.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_GetCapacityReservationUsage_ResponseElements"></a>

The following elements are returned by the service.

 **availableInstanceCount**
The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.
Type: Integer

 **capacityReservationId**
The ID of the Capacity Reservation.
Type: String

 **instanceType**
The type of instance for which the Capacity Reservation reserves capacity.
Type: String

 **instanceUsageSet**
Information about the Capacity Reservation usage.
Type: Array of [InstanceUsage](API_InstanceUsage.md) objects

 **interruptible**
 Indicates whether the Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims capacity.
Type: Boolean

 **interruptibleCapacityAllocation**
 Information about the capacity allocated to the interruptible Capacity Reservation, including instance counts and allocation status.
Type: [InterruptibleCapacityAllocation](API_InterruptibleCapacityAllocation.md) object

 **interruptionInfo**
 Details about the interruption configuration and source reservation for interruptible Capacity Reservations.
Type: [InterruptionInfo](API_InterruptionInfo.md) object

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **state**
The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:
+  `active` - The capacity is available for use.
+  `expired` - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.
+  `cancelled` - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.
+  `pending` - The Capacity Reservation request was successful but the capacity provisioning is still pending.
+  `failed` - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.
+  `scheduled` - (*Future-dated Capacity Reservations*) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.
+  `payment-pending` - (*Capacity Blocks*) The upfront payment has not been processed yet.
+  `payment-failed` - (*Capacity Blocks*) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.
+  `assessing` - (*Future-dated Capacity Reservations*) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.
+  `delayed` - (*Future-dated Capacity Reservations*) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.
+  `unsupported` - (*Future-dated Capacity Reservations*) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.
+  `cancelling` - (*Future-dated Capacity Reservations*) The Capacity Reservation is being cancelled. Capacity has been released but charges continue for the commitment wind-down period. The reservation transitions to `cancelled` when the wind-down completes.
Type: String
Valid Values: `active | expired | cancelled | pending | failed | scheduled | payment-pending | payment-failed | assessing | delayed | unsupported | cancelling | unavailable`

 **totalInstanceCount**
The number of instances for which the Capacity Reservation reserves capacity.
Type: Integer

## Errors
<a name="API_GetCapacityReservationUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetCapacityReservationUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetCapacityReservationUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetCapacityReservationUsage)

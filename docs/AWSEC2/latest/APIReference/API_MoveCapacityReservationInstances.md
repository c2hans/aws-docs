---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveCapacityReservationInstances.html
---

# MoveCapacityReservationInstances
<a name="API_MoveCapacityReservationInstances"></a>

Move available capacity from a source Capacity Reservation to a destination Capacity Reservation. The source Capacity Reservation and the destination Capacity Reservation must be `active`, owned by your AWS account, and share the following:
+ Instance type
+ Platform
+ Availability Zone
+ Tenancy
+ Placement group
+ Capacity Reservation end time - `At specific time` or `Manually`.

## Request Parameters
<a name="API_MoveCapacityReservationInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DestinationCapacityReservationId**
 The ID of the Capacity Reservation that you want to move capacity into.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceCount**
The number of instances that you want to move from the source Capacity Reservation.
Type: Integer
Required: Yes

 **SourceCapacityReservationId**
 The ID of the Capacity Reservation from which you want to move capacity.
Type: String
Required: Yes

## Response Elements
<a name="API_MoveCapacityReservationInstances_ResponseElements"></a>

The following elements are returned by the service.

 **destinationCapacityReservation**
 Information about the destination Capacity Reservation.
Type: [CapacityReservation](API_CapacityReservation.md) object

 **instanceCount**
 The number of instances that were moved from the source Capacity Reservation to the destination Capacity Reservation.
Type: Integer

 **requestId**
The ID of the request.
Type: String

 **sourceCapacityReservation**
 Information about the source Capacity Reservation.
Type: [CapacityReservation](API_CapacityReservation.md) object

## Errors
<a name="API_MoveCapacityReservationInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_MoveCapacityReservationInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/MoveCapacityReservationInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MoveCapacityReservationInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

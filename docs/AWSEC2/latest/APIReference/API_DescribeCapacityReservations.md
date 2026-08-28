---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html
---

# DescribeCapacityReservations
<a name="API_DescribeCapacityReservations"></a>

Describes one or more of your Capacity Reservations. The results describe only the Capacity Reservations in the AWS Region that you're currently using.

## Request Parameters
<a name="API_DescribeCapacityReservations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityReservationId.N**
The ID of the Capacity Reservation.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `instance-type` - The type of instance for which the Capacity Reservation reserves capacity.
+  `owner-id` - The ID of the AWS account that owns the Capacity Reservation.
+  `instance-platform` - The type of operating system for which the Capacity Reservation reserves capacity.
+  `availability-zone` - The Availability Zone of the Capacity Reservation.
+  `tenancy` - Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:
  +  `default` - The Capacity Reservation is created on hardware that is shared with other AWS accounts.
  +  `dedicated` - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single AWS account.
+  `outpost-arn` - The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.
+  `state` - The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:
  +  `active`- The Capacity Reservation is active and the capacity is available for your use.
  +  `expired` - The Capacity Reservation expired automatically at the date and time specified in your request. The reserved capacity is no longer available for your use.
  +  `cancelled` - The Capacity Reservation was cancelled. The reserved capacity is no longer available for your use.
  +  `pending` - The Capacity Reservation request was successful but the capacity provisioning is still pending.
  +  `failed` - The Capacity Reservation request has failed. A request might fail due to invalid request parameters, capacity constraints, or instance limit constraints. Failed requests are retained for 60 minutes.
+  `start-date` - The date and time at which the Capacity Reservation was started.
+  `end-date` - The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to expired when it reaches its end date and time.
+  `end-date-type` - Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:
  +  `unlimited` - The Capacity Reservation remains active until you explicitly cancel it.
  +  `limited` - The Capacity Reservation expires automatically at a specified date and time.
+  `instance-match-criteria` - Indicates the type of instance launches that the Capacity Reservation accepts. The options include:
  +  `open` - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.
  +  `targeted` - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.
+  `placement-group-arn` - The ARN of the cluster placement group in which the Capacity Reservation was created.
Type: Array of [Filter](API_Filter.md) objects
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
<a name="API_DescribeCapacityReservations_ResponseElements"></a>

The following elements are returned by the service.

 **capacityReservationSet**
Information about the Capacity Reservations.
Type: Array of [CapacityReservation](API_CapacityReservation.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeCapacityReservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeCapacityReservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeCapacityReservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeCapacityReservations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

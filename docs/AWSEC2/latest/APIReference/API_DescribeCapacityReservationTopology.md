---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservationTopology.html
---

# DescribeCapacityReservationTopology
<a name="API_DescribeCapacityReservationTopology"></a>

Describes a tree-based hierarchy that represents the physical host placement of your pending or active Capacity Reservations within an Availability Zone or Local Zone. You can use this information to determine the relative proximity of your capacity within the AWS network before it is launched and use this information to allocate capacity together to support your tightly coupled workloads.

Capacity Reservation topology is supported for specific instance types only. For more information, see [Prerequisites for Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.html) in the *Amazon EC2 User Guide*.

**Note**
The Amazon EC2 API follows an eventual consistency model due to the distributed nature of the system supporting it. As a result, when you call the DescribeCapacityReservationTopology API command immediately after launching instances, the response might return a `null` value for `capacityBlockId` because the data might not have fully propagated across all subsystems. For more information, see [Eventual consistency in the Amazon EC2 API](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) in the *Amazon EC2 Developer Guide*.

For more information, see [Amazon EC2 topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeCapacityReservationTopology_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityReservationId.N**
The Capacity Reservation IDs.
Default: Describes all your Capacity Reservations.
Constraints: Maximum 10 explicitly specified Capacity Reservation IDs.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone` - The name of the Availability Zone (for example, `us-west-2a`) or Local Zone (for example, `us-west-2-lax-1b`) that the Capacity Reservation is in.
+  `instance-type` - The instance type (for example, `p4d.24xlarge`) or instance family (for example, `p4d*`). You can use the `*` wildcard to match zero or more characters, or the `?` wildcard to match zero or one character.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
You can't specify this parameter and the Capacity Reservation IDs parameter in the same request.
Default: `10`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeCapacityReservationTopology_ResponseElements"></a>

The following elements are returned by the service.

 **capacityReservationSet**
Information about the topology of each Capacity Reservation.
Type: Array of [CapacityReservationTopology](API_CapacityReservationTopology.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeCapacityReservationTopology_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeCapacityReservationTopology_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeCapacityReservationTopology)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeCapacityReservationTopology)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

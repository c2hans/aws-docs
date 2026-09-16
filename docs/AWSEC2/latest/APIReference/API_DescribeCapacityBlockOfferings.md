---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityBlockOfferings.html
---

# DescribeCapacityBlockOfferings
<a name="API_DescribeCapacityBlockOfferings"></a>

Describes Capacity Block offerings available for purchase in the AWS Region that you're currently using. With Capacity Blocks, you can purchase a specific GPU instance type or EC2 UltraServer for a period of time.

To search for an available Capacity Block offering, you specify a reservation duration and instance count.

## Request Parameters
<a name="API_DescribeCapacityBlockOfferings_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllAvailabilityZones**
 Include all Availability Zones and Local Zones, regardless of your opt-in status. If you do not use this parameter, the results include available offerings from all Availability Zones in the AWS Region and Local Zones you are opted into.
Type: Boolean
Required: No

 **CapacityDurationHours**
The reservation duration for the Capacity Block, in hours. You must specify the duration in 1-day increments up 14 days, and in 7-day increments up to 182 days.
Type: Integer
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndDateRange**
The latest end date for the Capacity Block offering.
Type: Timestamp
Required: No

 **InstanceCount**
The number of instances for which to reserve capacity. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.
Type: Integer
Required: No

 **InstanceType**
The type of instance for which the Capacity Block offering reserves capacity.
Type: String
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

 **StartDateRange**
The earliest start date for the Capacity Block offering.
Type: Timestamp
Required: No

 **UltraserverCount**
The number of EC2 UltraServers in the offerings.
Type: Integer
Required: No

 **UltraserverType**
The EC2 UltraServer type of the Capacity Block offerings.
Type: String
Required: No

## Response Elements
<a name="API_DescribeCapacityBlockOfferings_ResponseElements"></a>

The following elements are returned by the service.

 **capacityBlockOfferingSet**
The recommended Capacity Block offering for the dates specified.
Type: Array of [CapacityBlockOffering](API_CapacityBlockOffering.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeCapacityBlockOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeCapacityBlockOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeCapacityBlockOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeCapacityBlockOfferings)

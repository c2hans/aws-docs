---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTopology.html
---

# DescribeInstanceTopology
<a name="API_DescribeInstanceTopology"></a>

Describes a tree-based hierarchy that represents the physical host placement of your EC2 instances within an Availability Zone or Local Zone. You can use this information to determine the relative proximity of your EC2 instances within the AWS network to support your tightly coupled workloads.

Instance topology is supported for specific instance types only. For more information, see [Prerequisites for Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.html) in the *Amazon EC2 User Guide*.

**Note**
The Amazon EC2 API follows an eventual consistency model due to the distributed nature of the system supporting it. As a result, when you call the DescribeInstanceTopology API command immediately after launching instances, the response might return a `null` value for `capacityBlockId` because the data might not have fully propagated across all subsystems. For more information, see [Eventual consistency in the Amazon EC2 API](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) in the *Amazon EC2 Developer Guide*.

For more information, see [Amazon EC2 topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeInstanceTopology_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone` - The name of the Availability Zone (for example, `us-west-2a`) or Local Zone (for example, `us-west-2-lax-1b`) that the instance is in.
+  `instance-type` - The instance type (for example, `p4d.24xlarge`) or instance family (for example, `p4d*`). You can use the `*` wildcard to match zero or more characters, or the `?` wildcard to match zero or one character.
+  `zone-id` - The ID of the Availability Zone (for example, `usw2-az2`) or Local Zone (for example, `usw2-lax1-az1`) that the instance is in.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **GroupName.N**
The name of the placement group that each instance is in.
Constraints: Maximum 100 explicitly specified placement group names.
Type: Array of strings
Required: No

 **InstanceId.N**
The instance IDs.
Default: Describes all your instances.
Constraints: Maximum 100 explicitly specified instance IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
You can't specify this parameter and the instance IDs parameter in the same request.
Default: `20`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeInstanceTopology_ResponseElements"></a>

The following elements are returned by the service.

 **instanceSet**
Information about the topology of each instance.
Type: Array of [InstanceTopology](API_InstanceTopology.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceTopology_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeInstanceTopology_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceTopology)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceTopology)

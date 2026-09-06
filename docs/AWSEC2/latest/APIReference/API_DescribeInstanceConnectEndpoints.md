---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceConnectEndpoints.html
---

# DescribeInstanceConnectEndpoints
<a name="API_DescribeInstanceConnectEndpoints"></a>

Describes the specified EC2 Instance Connect Endpoints or all EC2 Instance Connect Endpoints.

## Request Parameters
<a name="API_DescribeInstanceConnectEndpoints_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `instance-connect-endpoint-id` - The ID of the EC2 Instance Connect Endpoint.
+  `state` - The state of the EC2 Instance Connect Endpoint (`create-in-progress` \| `create-complete` \| `create-failed` \| `delete-in-progress` \| `delete-complete` \| `delete-failed`).
+  `subnet-id` - The ID of the subnet in which the EC2 Instance Connect Endpoint was created.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `tag-value` - The value of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific value, regardless of tag key.
+  `vpc-id` - The ID of the VPC in which the EC2 Instance Connect Endpoint was created.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **InstanceConnectEndpointId.N**
One or more EC2 Instance Connect Endpoint IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeInstanceConnectEndpoints_ResponseElements"></a>

The following elements are returned by the service.

 **instanceConnectEndpointSet**
Information about the EC2 Instance Connect Endpoints.
Type: Array of [Ec2InstanceConnectEndpoint](API_Ec2InstanceConnectEndpoint.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceConnectEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeInstanceConnectEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceConnectEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceConnectEndpoints)

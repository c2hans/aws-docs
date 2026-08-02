---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcBlockPublicAccessExclusions.html
---

# DescribeVpcBlockPublicAccessExclusions
<a name="API_DescribeVpcBlockPublicAccessExclusions"></a>

Describe VPC Block Public Access (BPA) exclusions. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_DescribeVpcBlockPublicAccessExclusions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ExclusionId.N**
IDs of exclusions.
Type: Array of strings
Required: No

 **Filter.N**
Filters for the request:
+  `resource-arn` - The Amazon Resource Name (ARN) of a exclusion.
+  `internet-gateway-exclusion-mode` - The mode of a VPC BPA exclusion. Possible values: `allow-bidirectional | allow-egress`.
+  `state` - The state of VPC BPA. Possible values: `create-in-progress | create-complete | update-in-progress | update-complete | delete-in-progress | deleted-complete | disable-in-progress | disable-complete`
+  `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `tag-value`: The value of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific value, regardless of the tag key.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeVpcBlockPublicAccessExclusions_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **vpcBlockPublicAccessExclusionSet**
Details related to the exclusions.
Type: Array of [VpcBlockPublicAccessExclusion](API_VpcBlockPublicAccessExclusion.md) objects

## Errors
<a name="API_DescribeVpcBlockPublicAccessExclusions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeVpcBlockPublicAccessExclusions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcBlockPublicAccessExclusions)

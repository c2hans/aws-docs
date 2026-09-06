---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypeOfferings.html
---

# DescribeInstanceTypeOfferings
<a name="API_DescribeInstanceTypeOfferings"></a>

Lists the instance types that are offered for the specified location. If no location is specified, the default is to list the instance types that are offered in the current Region.

## Request Parameters
<a name="API_DescribeInstanceTypeOfferings_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `instance-type` - The instance type. For a list of possible values, see [Instance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Instance.html).
+  `location` - The location. For a list of possible identifiers, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **LocationType**
The location type.
+  `availability-zone` - The Availability Zone. When you specify a location filter, it must be an Availability Zone for the current Region.
+  `availability-zone-id` - The AZ ID. When you specify a location filter, it must be an AZ ID for the current Region.
+  `outpost` - The Outpost ARN. When you specify a location filter, it must be an Outpost ARN for the current Region.
+  `region` - The current Region. If you specify a location filter, it must match the current Region.
Type: String
Valid Values: `region | availability-zone | availability-zone-id | outpost`
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
<a name="API_DescribeInstanceTypeOfferings_ResponseElements"></a>

The following elements are returned by the service.

 **instanceTypeOfferingSet**
The instance types offered in the location.
Type: Array of [InstanceTypeOffering](API_InstanceTypeOffering.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceTypeOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeInstanceTypeOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceTypeOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceTypeOfferings)

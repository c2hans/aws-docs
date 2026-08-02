---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamPoolAllocations.html
---

# GetIpamPoolAllocations
<a name="API_GetIpamPoolAllocations"></a>

Get a list of all the CIDR allocations in an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the AWS Region where this IPAM pool is available for allocations.

**Note**
If you use this action after [AllocateIpamPoolCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateIpamPoolCidr.html) or [ReleaseIpamPoolAllocation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseIpamPoolAllocation.html), note that all EC2 API actions follow an [eventual consistency](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) model.

## Request Parameters
<a name="API_GetIpamPoolAllocations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters for the request. For more information about filtering, see [Filtering CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IpamPoolAllocationId**
The ID of the allocation.
Type: String
Required: No

 **IpamPoolId**
The ID of the IPAM pool you want to see the allocations for.
Type: String
Required: Yes

 **MaxResults**
The maximum number of results you would like returned per page.
Type: Integer
Valid Range: Minimum value of 1000. Maximum value of 100000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_GetIpamPoolAllocations_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPoolAllocationSet**
The IPAM pool allocations you want information on.
Type: Array of [IpamPoolAllocation](API_IpamPoolAllocation.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetIpamPoolAllocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamPoolAllocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamPoolAllocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamPoolAllocations)

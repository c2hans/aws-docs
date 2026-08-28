---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamDiscoveredResourceCidrs.html
---

# GetIpamDiscoveredResourceCidrs
<a name="API_GetIpamDiscoveredResourceCidrs"></a>

Returns the resource CIDRs that are monitored as part of a resource discovery. A discovered resource is a resource CIDR monitored under a resource discovery. The following resources can be discovered: VPCs, Public IPv4 pools, VPC subnets, and Elastic IP addresses.

## Request Parameters
<a name="API_GetIpamDiscoveredResourceCidrs_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
Filters.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IpamResourceDiscoveryId**
A resource discovery ID.
Type: String
Required: Yes

 **MaxResults**
The maximum number of discovered resource CIDRs to return in one page of results.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String
Required: No

 **ResourceRegion**
A resource Region.
Type: String
Required: Yes

## Response Elements
<a name="API_GetIpamDiscoveredResourceCidrs_ResponseElements"></a>

The following elements are returned by the service.

 **ipamDiscoveredResourceCidrSet**
Discovered resource CIDRs.
Type: Array of [IpamDiscoveredResourceCidr](API_IpamDiscoveredResourceCidr.md) objects

 **nextToken**
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetIpamDiscoveredResourceCidrs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamDiscoveredResourceCidrs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamDiscoveredResourceCidrs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

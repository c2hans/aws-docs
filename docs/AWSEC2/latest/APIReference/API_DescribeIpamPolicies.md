---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamPolicies.html
---

# DescribeIpamPolicies
<a name="API_DescribeIpamPolicies"></a>

Describes one or more IPAM policies.

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations.

## Request Parameters
<a name="API_DescribeIpamPolicies_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters for the IPAM policy description.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IpamPolicyId.N**
The IDs of the IPAM policies to describe.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeIpamPolicies_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPolicySet**
Information about the IPAM policies.
An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations.
Type: Array of [IpamPolicy](API_IpamPolicy.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeIpamPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeIpamPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeIpamPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeIpamPolicies)

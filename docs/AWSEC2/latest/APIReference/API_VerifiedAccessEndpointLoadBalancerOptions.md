---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessEndpointLoadBalancerOptions.html
---

# VerifiedAccessEndpointLoadBalancerOptions
<a name="API_VerifiedAccessEndpointLoadBalancerOptions"></a>

Describes a load balancer when creating an AWS Verified Access endpoint using the `load-balancer` type.

## Contents
<a name="API_VerifiedAccessEndpointLoadBalancerOptions_Contents"></a>

 ** loadBalancerArn **
The ARN of the load balancer.
Type: String
Required: No

 ** port **
The IP port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PortRangeSet.N **
The port ranges.
Type: Array of [VerifiedAccessEndpointPortRange](API_VerifiedAccessEndpointPortRange.md) objects
Required: No

 ** protocol **
The IP protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

 ** SubnetIdSet.N **
The IDs of the subnets.
Type: Array of strings
Required: No

## See Also
<a name="API_VerifiedAccessEndpointLoadBalancerOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessEndpointLoadBalancerOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessEndpointLoadBalancerOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessEndpointLoadBalancerOptions)

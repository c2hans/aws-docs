---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessEndpointLoadBalancerOptions.html
---

# CreateVerifiedAccessEndpointLoadBalancerOptions
<a name="API_CreateVerifiedAccessEndpointLoadBalancerOptions"></a>

Describes the load balancer options when creating an AWS Verified Access endpoint using the `load-balancer` type.

## Contents
<a name="API_CreateVerifiedAccessEndpointLoadBalancerOptions_Contents"></a>

 ** LoadBalancerArn **
The ARN of the load balancer.
Type: String
Required: No

 ** Port **
The IP port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PortRange.N **
The port ranges.
Type: Array of [CreateVerifiedAccessEndpointPortRange](API_CreateVerifiedAccessEndpointPortRange.md) objects
Required: No

 ** Protocol **
The IP protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

 ** SubnetId.N **
The IDs of the subnets. You can specify only one subnet per Availability Zone.
Type: Array of strings
Required: No

## See Also
<a name="API_CreateVerifiedAccessEndpointLoadBalancerOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVerifiedAccessEndpointLoadBalancerOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVerifiedAccessEndpointLoadBalancerOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVerifiedAccessEndpointLoadBalancerOptions)

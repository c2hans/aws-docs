---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerListener.html
---

# AwsElbLoadBalancerListener
<a name="API_AwsElbLoadBalancerListener"></a>

Information about a load balancer listener.

## Contents
<a name="API_AwsElbLoadBalancerListener_Contents"></a>

 ** InstancePort **   <a name="securityhub-Type-AwsElbLoadBalancerListener-InstancePort"></a>
The port on which the instance is listening.
Type: Integer
Required: No

 ** InstanceProtocol **   <a name="securityhub-Type-AwsElbLoadBalancerListener-InstanceProtocol"></a>
The protocol to use to route traffic to instances.
Valid values: `HTTP` \| `HTTPS` \| `TCP` \| `SSL`
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoadBalancerPort **   <a name="securityhub-Type-AwsElbLoadBalancerListener-LoadBalancerPort"></a>
The port on which the load balancer is listening.
On EC2-VPC, you can specify any port from the range 1-65535.
On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
Type: Integer
Required: No

 ** Protocol **   <a name="securityhub-Type-AwsElbLoadBalancerListener-Protocol"></a>
The load balancer transport protocol to use for routing.
Valid values: `HTTP` \| `HTTPS` \| `TCP` \| `SSL`
Type: String
Pattern: `.*\S.*`
Required: No

 ** SslCertificateId **   <a name="securityhub-Type-AwsElbLoadBalancerListener-SslCertificateId"></a>
The ARN of the server certificate.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLoadBalancerListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerListener)

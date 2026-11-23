---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_SubnetConfiguration.html
---

# SubnetConfiguration

A complex type that identifies one subnet for a health check source and the security groups that Route 53 associates with the network interfaces that it creates in that subnet.

## Contents
<a name="API_SubnetConfiguration_Contents"></a>

 ** AvailabilityZoneId **   <a name="Route53-Type-SubnetConfiguration-AvailabilityZoneId"></a>
The ID of the Availability Zone that contains the subnet, for example `use1-az1`. Specify the Availability Zone ID, not the Availability Zone name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SecurityGroupIdList **   <a name="Route53-Type-SubnetConfiguration-SecurityGroupIdList"></a>
The IDs of the security groups in the same virtual private cloud (VPC) to associate with the network interfaces that Route 53 creates in this subnet. The security groups must allow outbound traffic to the endpoints that the health checks monitor.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SubnetId **   <a name="Route53-Type-SubnetConfiguration-SubnetId"></a>
The ID of the subnet that Route 53 uses to send health check requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_SubnetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/SubnetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/SubnetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/SubnetConfiguration)

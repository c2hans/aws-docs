---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxyVpcConfiguration.html
---

# ProxyVpcConfiguration

The VPC configuration for a proxy.

## Contents
<a name="API_ProxyVpcConfiguration_Contents"></a>

 ** availabilityZones **   <a name="elasticloadbalancing-Type-ProxyVpcConfiguration-availabilityZones"></a>
The Availability Zones used by the proxy.
Type: Array of [SubnetAndZone](API_SubnetAndZone.md) objects
Required: Yes

 ** securityGroups **   <a name="elasticloadbalancing-Type-ProxyVpcConfiguration-securityGroups"></a>
The security groups used by the proxy.
Type: Array of [SecurityGroupDetails](API_SecurityGroupDetails.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** vpcId **   <a name="elasticloadbalancing-Type-ProxyVpcConfiguration-vpcId"></a>
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_ProxyVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxyVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxyVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxyVpcConfiguration)

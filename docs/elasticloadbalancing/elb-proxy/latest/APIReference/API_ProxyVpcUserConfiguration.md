---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxyVpcUserConfiguration.html
---

# ProxyVpcUserConfiguration

The VPC configuration for a proxy, used by mutating operations.

## Contents
<a name="API_ProxyVpcUserConfiguration_Contents"></a>

 ** securityGroups **   <a name="elasticloadbalancing-Type-ProxyVpcUserConfiguration-securityGroups"></a>
The security groups used by the proxy.
Type: Array of [SecurityGroupDetails](API_SecurityGroupDetails.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** subnets **   <a name="elasticloadbalancing-Type-ProxyVpcUserConfiguration-subnets"></a>
The subnets used by the proxy.
Type: Array of [SubnetDetails](API_SubnetDetails.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_ProxyVpcUserConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxyVpcUserConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxyVpcUserConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxyVpcUserConfiguration)

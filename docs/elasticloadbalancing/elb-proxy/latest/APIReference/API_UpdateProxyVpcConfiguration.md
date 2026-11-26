---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_UpdateProxyVpcConfiguration.html
---

# UpdateProxyVpcConfiguration

The updated VPC configuration for a proxy. You must provide at least one of `subnets` or `securityGroups`.

## Contents
<a name="API_UpdateProxyVpcConfiguration_Contents"></a>

 ** securityGroups **   <a name="elasticloadbalancing-Type-UpdateProxyVpcConfiguration-securityGroups"></a>
The updated security groups for the proxy.
Type: Array of [SecurityGroupDetails](API_SecurityGroupDetails.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** subnets **   <a name="elasticloadbalancing-Type-UpdateProxyVpcConfiguration-subnets"></a>
The updated subnets for the proxy.
Type: Array of [SubnetDetails](API_SubnetDetails.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_UpdateProxyVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/UpdateProxyVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/UpdateProxyVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/UpdateProxyVpcConfiguration)

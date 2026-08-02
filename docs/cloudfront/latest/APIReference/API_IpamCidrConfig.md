---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_IpamCidrConfig.html
---

# IpamCidrConfig
<a name="API_IpamCidrConfig"></a>

Configuration for an IPAM CIDR that defines a specific IP address range, IPAM pool, and associated Anycast IP address.

## Contents
<a name="API_IpamCidrConfig_Contents"></a>

 ** Cidr **   <a name="cloudfront-Type-IpamCidrConfig-Cidr"></a>
The CIDR that specifies the IP address range for this IPAM configuration.
Type: String
Required: Yes

 ** IpamPoolArn **   <a name="cloudfront-Type-IpamCidrConfig-IpamPoolArn"></a>
The Amazon Resource Name (ARN) of the IPAM pool that the CIDR block is assigned to.
Type: String
Required: Yes

 ** AnycastIp **   <a name="cloudfront-Type-IpamCidrConfig-AnycastIp"></a>
The specified Anycast IP address allocated from the IPAM pool for this CIDR configuration.
Type: String
Required: No

 ** Status **   <a name="cloudfront-Type-IpamCidrConfig-Status"></a>
The current status of the IPAM CIDR configuration.
Type: String
Valid Values: `provisioned | failed-provision | provisioning | deprovisioned | failed-deprovision | deprovisioning | advertised | failed-advertise | advertising | withdrawn | failed-withdraw | withdrawing`
Required: No

## See Also
<a name="API_IpamCidrConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/IpamCidrConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/IpamCidrConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/IpamCidrConfig)

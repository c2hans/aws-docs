---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_IpamConfig.html
---

# IpamConfig
<a name="API_IpamConfig"></a>

The configuration IPAM settings that includes the quantity of CIDR configurations and the list of IPAM CIDR configurations.

## Contents
<a name="API_IpamConfig_Contents"></a>

 ** IpamCidrConfigs **   <a name="cloudfront-Type-IpamConfig-IpamCidrConfigs"></a>
A list of IPAM CIDR configurations that define the IP address ranges, IPAM pools, and associated Anycast IP addresses.
Type: Array of [IpamCidrConfig](API_IpamCidrConfig.md) objects
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-IpamConfig-Quantity"></a>
The number of IPAM CIDR configurations in the `IpamCidrConfigs` list.
Type: Integer
Required: Yes

## See Also
<a name="API_IpamConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/IpamConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/IpamConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/IpamConfig)

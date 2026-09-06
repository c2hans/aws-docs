---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

The network type (IPv4-only, Dual-Stack, PrivateLink) of the ingress endpoint resource.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** PrivateNetworkConfiguration **   <a name="sesmailmanager-Type-NetworkConfiguration-PrivateNetworkConfiguration"></a>
Specifies the network configuration for the private ingress point.
Type: [PrivateNetworkConfiguration](API_PrivateNetworkConfiguration.md) object
Required: No

 ** PublicNetworkConfiguration **   <a name="sesmailmanager-Type-NetworkConfiguration-PublicNetworkConfiguration"></a>
Specifies the network configuration for the public ingress point.
Type: [PublicNetworkConfiguration](API_PublicNetworkConfiguration.md) object
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/NetworkConfiguration)

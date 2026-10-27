---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_PublicSourceEndpointNetworkingConfiguration.html
---

# PublicSourceEndpointNetworkingConfiguration
<a name="API_PublicSourceEndpointNetworkingConfiguration"></a>

The networking configuration for a publicly accessible source endpoint, including the CIDR blocks that are allowed to connect.

## Contents
<a name="API_PublicSourceEndpointNetworkingConfiguration_Contents"></a>

 ** sourceAllowRules **   <a name="mediaconnect-Type-PublicSourceEndpointNetworkingConfiguration-sourceAllowRules"></a>
The rules that specify which CIDR blocks can connect to the source endpoint. You can specify up to 10 rules.
Type: Array of [PublicSourceEndpointNetworkingConfigurationAllowRule](API_PublicSourceEndpointNetworkingConfigurationAllowRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_PublicSourceEndpointNetworkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/PublicSourceEndpointNetworkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/PublicSourceEndpointNetworkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/PublicSourceEndpointNetworkingConfiguration)

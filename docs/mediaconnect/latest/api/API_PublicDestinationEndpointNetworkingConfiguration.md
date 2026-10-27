---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_PublicDestinationEndpointNetworkingConfiguration.html
---

# PublicDestinationEndpointNetworkingConfiguration
<a name="API_PublicDestinationEndpointNetworkingConfiguration"></a>

The networking configuration for a publicly accessible destination endpoint, including the CIDR blocks that are allowed to connect.

## Contents
<a name="API_PublicDestinationEndpointNetworkingConfiguration_Contents"></a>

 ** destinationAllowRules **   <a name="mediaconnect-Type-PublicDestinationEndpointNetworkingConfiguration-destinationAllowRules"></a>
The rules that specify which CIDR blocks can connect to the destination endpoint. You can specify up to 10 rules.
Type: Array of [PublicDestinationEndpointNetworkingConfigurationAllowRule](API_PublicDestinationEndpointNetworkingConfigurationAllowRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_PublicDestinationEndpointNetworkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/PublicDestinationEndpointNetworkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/PublicDestinationEndpointNetworkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/PublicDestinationEndpointNetworkingConfiguration)

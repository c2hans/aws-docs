---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_VpcDestinationEndpointNetworkingConfiguration.html
---

# VpcDestinationEndpointNetworkingConfiguration
<a name="API_VpcDestinationEndpointNetworkingConfiguration"></a>

The networking configuration for a destination endpoint in a virtual private cloud (VPC).

## Contents
<a name="API_VpcDestinationEndpointNetworkingConfiguration_Contents"></a>

 ** securityGroupIds **   <a name="mediaconnect-Type-VpcDestinationEndpointNetworkingConfiguration-securityGroupIds"></a>
The IDs of the security groups to associate with the destination endpoint. You can specify from 1 to 5 security groups.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** subnetId **   <a name="mediaconnect-Type-VpcDestinationEndpointNetworkingConfiguration-subnetId"></a>
The ID of the subnet to use for the destination endpoint.
Type: String
Required: Yes

## See Also
<a name="API_VpcDestinationEndpointNetworkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/VpcDestinationEndpointNetworkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/VpcDestinationEndpointNetworkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/VpcDestinationEndpointNetworkingConfiguration)

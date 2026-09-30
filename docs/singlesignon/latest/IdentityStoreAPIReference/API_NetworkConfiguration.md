---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

The network configuration that controls how an identity store can be accessed. You provide this object in a request.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** VpceAccessRequired **   <a name="singlesignon-Type-NetworkConfiguration-VpceAccessRequired"></a>
Specifies whether the identity store can be accessed only through a virtual private cloud (VPC) endpoint. When set to `true`, requests must originate from a VPC endpoint.
This value must be set to either `true` or `false` when you provide `NetworkConfiguration` in a request.
Type: Boolean
Required: Yes

 ** ApiAllowSourceIps **   <a name="singlesignon-Type-NetworkConfiguration-ApiAllowSourceIps"></a>
A list of IP address CIDR ranges that are allowed to access the identity store API operations. A request from an IP address in this list bypasses the identity store's other API network controls: it's permitted even if it doesn't come through a VPC endpoint required by `VpceAccessRequired`, and even if it doesn't originate from a VPC in `ApiRestrictSourceVpcs`. If you don't specify a value, no such IP address exception applies.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 2. Maximum length of 43.
Pattern: `((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))?|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(:[0-9a-fA-F]{1,4}){1,6}|:((:[0-9a-fA-F]{1,4}){1,7}|:))(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))?)`
Required: No

 ** ApiRestrictSourceVpcs **   <a name="singlesignon-Type-NetworkConfiguration-ApiRestrictSourceVpcs"></a>
A list of virtual private cloud (VPC) IDs that are allowed to access the identity store API operations. A request is denied unless it originates from a VPC in this list, or from an IP address in `ApiAllowSourceIps` if you specified one. If you don't specify a value, access isn't restricted to specific VPCs, but the VPC endpoint requirement set by `VpceAccessRequired` still applies.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`
Required: No

 ** ScimAllowSourceIps **   <a name="singlesignon-Type-NetworkConfiguration-ScimAllowSourceIps"></a>
A list of IP address CIDR ranges that are allowed to access the identity store through the System for Cross-domain Identity Management (SCIM) protocol. Requests from IP addresses outside these ranges are denied. If you don't specify a value, SCIM requests remain subject to the identity store's other network controls, such as the VPC endpoint requirement set by `VpceAccessRequired`.
For example, to allow SCIM traffic from the public internet while still requiring the identity store API operations to be accessed through a VPC endpoint, set `VpceAccessRequired` to `true` and set this value to `0.0.0.0/0`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 2. Maximum length of 43.
Pattern: `((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))?|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(:[0-9a-fA-F]{1,4}){1,6}|:((:[0-9a-fA-F]{1,4}){1,7}|:))(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))?)`
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/NetworkConfiguration)

---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_NetworkConfigurationDetails.html
---

# NetworkConfigurationDetails
<a name="API_NetworkConfigurationDetails"></a>

The network configuration that controls how an identity store can be accessed. This object is returned as part of service API responses.

## Contents
<a name="API_NetworkConfigurationDetails_Contents"></a>

 ** VpceAccessRequired **   <a name="singlesignon-Type-NetworkConfigurationDetails-VpceAccessRequired"></a>
Specifies whether the identity store can be accessed only through a virtual private cloud (VPC) endpoint. When set to `true`, requests must originate from a VPC endpoint.
Type: Boolean
Required: Yes

 ** ApiAllowSourceIps **   <a name="singlesignon-Type-NetworkConfigurationDetails-ApiAllowSourceIps"></a>
A list of IP address CIDR ranges that are allowed to access the identity store API operations. A request from an IP address in this list bypasses the identity store's other API network controls: it's permitted even if it doesn't come through a VPC endpoint required by `VpceAccessRequired`, and even if it doesn't originate from a VPC in `ApiRestrictSourceVpcs`. If this field is empty, no such IP address exception applies.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 2. Maximum length of 43.
Pattern: `((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))?|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(:[0-9a-fA-F]{1,4}){1,6}|:((:[0-9a-fA-F]{1,4}){1,7}|:))(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))?)`
Required: No

 ** ApiRestrictSourceVpcs **   <a name="singlesignon-Type-NetworkConfigurationDetails-ApiRestrictSourceVpcs"></a>
A list of virtual private cloud (VPC) IDs that are allowed to access the identity store API operations. A request is denied unless it originates from a VPC in this list, or from an IP address in `ApiAllowSourceIps` if one is configured. If this field is empty, access isn't restricted to specific VPCs, but the VPC endpoint requirement from `VpceAccessRequired` still applies.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`
Required: No

 ** ScimAllowSourceIps **   <a name="singlesignon-Type-NetworkConfigurationDetails-ScimAllowSourceIps"></a>
A list of IP address CIDR ranges that are allowed to access the identity store through the System for Cross-domain Identity Management (SCIM) protocol. Requests from IP addresses outside these ranges are denied. If this field is empty, SCIM requests remain subject to the identity store's other network controls, such as the VPC endpoint requirement.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 2. Maximum length of 43.
Pattern: `((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))?|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(:[0-9a-fA-F]{1,4}){1,6}|:((:[0-9a-fA-F]{1,4}){1,7}|:))(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))?)`
Required: No

## See Also
<a name="API_NetworkConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/NetworkConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/NetworkConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/NetworkConfigurationDetails)

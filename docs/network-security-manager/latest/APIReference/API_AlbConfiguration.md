---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AlbConfiguration.html
---

# AlbConfiguration
<a name="API_AlbConfiguration"></a>

Filter criteria specific to Application Load Balancers.

## Contents
<a name="API_AlbConfiguration_Contents"></a>

 ** ipAddressType **   <a name="networksecuritymanager-Type-AlbConfiguration-ipAddressType"></a>
The IP address type of the Application Load Balancer.
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`
Required: No

 ** scheme **   <a name="networksecuritymanager-Type-AlbConfiguration-scheme"></a>
The scheme of the Application Load Balancer, either `internet-facing` or `internal`.
Type: String
Valid Values: `internet-facing | internal`
Required: No

## See Also
<a name="API_AlbConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AlbConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AlbConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AlbConfiguration)

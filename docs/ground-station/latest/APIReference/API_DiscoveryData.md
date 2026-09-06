---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DiscoveryData.html
---

# DiscoveryData
<a name="API_DiscoveryData"></a>

Data for agent discovery.

## Contents
<a name="API_DiscoveryData_Contents"></a>

 ** capabilityArns **   <a name="groundstation-Type-DiscoveryData-capabilityArns"></a>
List of capabilities to associate with agent.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** privateIpAddresses **   <a name="groundstation-Type-DiscoveryData-privateIpAddresses"></a>
List of private IP addresses to associate with agent.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 7. Maximum length of 16.
Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
Required: Yes

 ** publicIpAddresses **   <a name="groundstation-Type-DiscoveryData-publicIpAddresses"></a>
List of public IP addresses to associate with agent.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 7. Maximum length of 16.
Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
Required: Yes

## See Also
<a name="API_DiscoveryData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DiscoveryData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DiscoveryData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DiscoveryData)

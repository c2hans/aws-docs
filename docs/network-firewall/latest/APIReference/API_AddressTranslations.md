---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AddressTranslations.html
---

# AddressTranslations

The public IP addresses that an internet gateway firewall uses for network address translation in one Availability Zone. Resources that don't have a public IP address reach the internet through these addresses. Network Firewall manages the addresses for you: it allocates them in your account and adds or removes addresses automatically based on traffic.

## Contents
<a name="API_AddressTranslations_Contents"></a>

 ** PublicIPv4Addresses **   <a name="networkfirewall-Type-AddressTranslations-PublicIPv4Addresses"></a>
The public IPv4 addresses that the internet gateway firewall uses for network address translation in this Availability Zone.
Type: Array of strings
Pattern: `^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)(/([0-9]|[12]\d|3[0-2]))?$`
Required: No

 ** PublicIPv6Addresses **   <a name="networkfirewall-Type-AddressTranslations-PublicIPv6Addresses"></a>
The public IPv6 addresses that the internet gateway firewall uses for network address translation in this Availability Zone.
Type: Array of strings
Pattern: `^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]+|::(ffff(:0{1,4})?:)?((25[0-5]|(2[0-4]|1?\d)?\d)\.){3}(25[0-5]|(2[0-4]|1?\d)?\d)|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1?\d)?\d)\.){3}(25[0-5]|(2[0-4]|1?\d)?\d))(/(12[0-8]|1[01]\d|[1-9]?\d))?$`
Required: No

## See Also
<a name="API_AddressTranslations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AddressTranslations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AddressTranslations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AddressTranslations)

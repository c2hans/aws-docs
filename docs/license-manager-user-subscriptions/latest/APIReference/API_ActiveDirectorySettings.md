---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ActiveDirectorySettings.html
---

# ActiveDirectorySettings
<a name="API_ActiveDirectorySettings"></a>

Contains network access and credential details that are needed for user administration in the Active Directory.

## Contents
<a name="API_ActiveDirectorySettings_Contents"></a>

 ** DomainCredentialsProvider **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectorySettings-DomainCredentialsProvider"></a>
Points to the `CredentialsProvider` resource that contains information about the credential provider for user administration.
Type: [CredentialsProvider](API_CredentialsProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** DomainIpv4List **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectorySettings-DomainIpv4List"></a>
A list of domain IPv4 addresses that are used for the Active Directory.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Pattern: `(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}`
Required: No

 ** DomainIpv6List **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectorySettings-DomainIpv6List"></a>
A list of domain IPv6 addresses that are used for the Active Directory.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Pattern: `([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|::|::[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}`
Required: No

 ** DomainName **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectorySettings-DomainName"></a>
The domain name for the Active Directory.
Type: String
Required: No

 ** DomainNetworkSettings **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectorySettings-DomainNetworkSettings"></a>
The `DomainNetworkSettings` resource contains an array of subnets that apply for the Active Directory.
Type: [DomainNetworkSettings](API_DomainNetworkSettings.md) object
Required: No

## See Also
<a name="API_ActiveDirectorySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/ActiveDirectorySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/ActiveDirectorySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/ActiveDirectorySettings)

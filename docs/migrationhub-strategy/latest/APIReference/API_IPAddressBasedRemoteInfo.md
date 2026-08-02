---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_IPAddressBasedRemoteInfo.html
---

# IPAddressBasedRemoteInfo
<a name="API_IPAddressBasedRemoteInfo"></a>

IP address based configurations.

## Contents
<a name="API_IPAddressBasedRemoteInfo_Contents"></a>

 ** authType **   <a name="migrationhubstrategy-Type-IPAddressBasedRemoteInfo-authType"></a>
The type of authorization.
Type: String
Valid Values: `NTLM | SSH | CERT`
Required: No

 ** ipAddressConfigurationTimeStamp **   <a name="migrationhubstrategy-Type-IPAddressBasedRemoteInfo-ipAddressConfigurationTimeStamp"></a>
The time stamp of the configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** osType **   <a name="migrationhubstrategy-Type-IPAddressBasedRemoteInfo-osType"></a>
The type of the operating system.
Type: String
Valid Values: `LINUX | WINDOWS`
Required: No

## See Also
<a name="API_IPAddressBasedRemoteInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/IPAddressBasedRemoteInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/IPAddressBasedRemoteInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/IPAddressBasedRemoteInfo)

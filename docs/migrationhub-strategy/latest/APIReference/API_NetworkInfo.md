---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_NetworkInfo.html
---

# NetworkInfo
<a name="API_NetworkInfo"></a>

 Information about the server's network for which the assessment was run.

## Contents
<a name="API_NetworkInfo_Contents"></a>

 ** interfaceName **   <a name="migrationhubstrategy-Type-NetworkInfo-interfaceName"></a>
 Information about the name of the interface of the server for which the assessment was run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: Yes

 ** ipAddress **   <a name="migrationhubstrategy-Type-NetworkInfo-ipAddress"></a>
 Information about the IP address of the server for which the assessment was run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])`
Required: Yes

 ** macAddress **   <a name="migrationhubstrategy-Type-NetworkInfo-macAddress"></a>
 Information about the MAC address of the server for which the assessment was run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17.
Pattern: `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\\.[0-9a-fA-F]{4}\\.[0-9a-fA-F]{4})$”`
Required: Yes

 ** netMask **   <a name="migrationhubstrategy-Type-NetworkInfo-netMask"></a>
 Information about the subnet mask of the server for which the assessment was run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_NetworkInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/NetworkInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/NetworkInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/NetworkInfo)

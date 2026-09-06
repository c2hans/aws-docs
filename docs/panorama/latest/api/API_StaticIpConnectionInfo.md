---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_StaticIpConnectionInfo.html
---

# StaticIpConnectionInfo
<a name="API_StaticIpConnectionInfo"></a>

A static IP configuration.

## Contents
<a name="API_StaticIpConnectionInfo_Contents"></a>

 ** DefaultGateway **   <a name="panorama-Type-StaticIpConnectionInfo-DefaultGateway"></a>
The connection's default gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Dns **   <a name="panorama-Type-StaticIpConnectionInfo-Dns"></a>
The connection's DNS address.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** IpAddress **   <a name="panorama-Type-StaticIpConnectionInfo-IpAddress"></a>
The connection's IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(:(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}))?`
Required: Yes

 ** Mask **   <a name="panorama-Type-StaticIpConnectionInfo-Mask"></a>
The connection's DNS mask.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

## See Also
<a name="API_StaticIpConnectionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/StaticIpConnectionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/StaticIpConnectionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/StaticIpConnectionInfo)

---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NtpPayload.html
---

# NtpPayload
<a name="API_NtpPayload"></a>

Network time protocol (NTP) server settings. Use this option to connect to local NTP servers instead of `pool.ntp.org`.

## Contents
<a name="API_NtpPayload_Contents"></a>

 ** NtpServers **   <a name="panorama-Type-NtpPayload-NtpServers"></a>
NTP servers to use, in order of preference.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*(^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$)|(^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(:(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}))?$).*`
Required: Yes

## See Also
<a name="API_NtpPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NtpPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NtpPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NtpPayload)

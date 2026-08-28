---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NtpStatus.html
---

# NtpStatus
<a name="API_NtpStatus"></a>

Details about an NTP server connection.

## Contents
<a name="API_NtpStatus_Contents"></a>

 ** ConnectionStatus **   <a name="panorama-Type-NtpStatus-ConnectionStatus"></a>
The connection's status.
Type: String
Valid Values: `CONNECTED | NOT_CONNECTED | CONNECTING`
Required: No

 ** IpAddress **   <a name="panorama-Type-NtpStatus-IpAddress"></a>
The IP address of the server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(:(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}))?`
Required: No

 ** NtpServerName **   <a name="panorama-Type-NtpStatus-NtpServerName"></a>
The domain name of the server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_NtpStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NtpStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NtpStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NtpStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

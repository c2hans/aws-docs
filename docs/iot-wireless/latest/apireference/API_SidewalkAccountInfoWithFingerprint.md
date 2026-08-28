---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkAccountInfoWithFingerprint.html
---

# SidewalkAccountInfoWithFingerprint
<a name="API_SidewalkAccountInfoWithFingerprint"></a>

Information about a Sidewalk account.

## Contents
<a name="API_SidewalkAccountInfoWithFingerprint_Contents"></a>

 ** AmazonId **   <a name="iotwireless-Type-SidewalkAccountInfoWithFingerprint-AmazonId"></a>
The Sidewalk Amazon ID.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** Arn **   <a name="iotwireless-Type-SidewalkAccountInfoWithFingerprint-Arn"></a>
The Amazon Resource Name of the resource.
Type: String
Required: No

 ** Fingerprint **   <a name="iotwireless-Type-SidewalkAccountInfoWithFingerprint-Fingerprint"></a>
The fingerprint of the Sidewalk application server private key.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[a-fA-F0-9]{64}`
Required: No

## See Also
<a name="API_SidewalkAccountInfoWithFingerprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkAccountInfoWithFingerprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkAccountInfoWithFingerprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkAccountInfoWithFingerprint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

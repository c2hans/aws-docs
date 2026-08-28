---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkGetDeviceProfile.html
---

# SidewalkGetDeviceProfile
<a name="API_SidewalkGetDeviceProfile"></a>

Gets information about a Sidewalk device profile.

## Contents
<a name="API_SidewalkGetDeviceProfile_Contents"></a>

 ** ApplicationServerPublicKey **   <a name="iotwireless-Type-SidewalkGetDeviceProfile-ApplicationServerPublicKey"></a>
The Sidewalk application server public key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[a-fA-F0-9]{64}`
Required: No

 ** DakCertificateMetadata **   <a name="iotwireless-Type-SidewalkGetDeviceProfile-DakCertificateMetadata"></a>
The DAK certificate information of the Sidewalk device profile.
Type: Array of [DakCertificateMetadata](API_DakCertificateMetadata.md) objects
Required: No

 ** QualificationStatus **   <a name="iotwireless-Type-SidewalkGetDeviceProfile-QualificationStatus"></a>
Gets information about the certification status of a Sidewalk device profile.
Type: Boolean
Required: No

## See Also
<a name="API_SidewalkGetDeviceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkGetDeviceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkGetDeviceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkGetDeviceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

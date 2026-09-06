---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_LocalTimeZoneConfig.html
---

# LocalTimeZoneConfig
<a name="API_connect-outbound-campaigns-v2_LocalTimeZoneConfig"></a>

The configuration of timezone of the recipient.

## Contents
<a name="API_connect-outbound-campaigns-v2_LocalTimeZoneConfig_Contents"></a>

 ** defaultTimeZone **   <a name="connect-Type-connect-outbound-campaigns-v2_LocalTimeZoneConfig-defaultTimeZone"></a>
The timezone to use for all recipients.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[a-zA-Z0-9_\-/]*`
Required: No

 ** localTimeZoneDetection **   <a name="connect-Type-connect-outbound-campaigns-v2_LocalTimeZoneConfig-localTimeZoneDetection"></a>
Detect methods for the recipient timezone.
Type: Array of strings
Valid Values: `ZIP_CODE | AREA_CODE`
Required: No

 ** localTimeZoneDetectionScope **   <a name="connect-Type-connect-outbound-campaigns-v2_LocalTimeZoneConfig-localTimeZoneDetectionScope"></a>
The scope of profile attributes used for timezone detection.
Type: String
Valid Values: `PRIMARY_ONLY | ALL_AVAILABLE`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_LocalTimeZoneConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/LocalTimeZoneConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/LocalTimeZoneConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/LocalTimeZoneConfig)

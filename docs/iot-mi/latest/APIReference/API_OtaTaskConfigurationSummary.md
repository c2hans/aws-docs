---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OtaTaskConfigurationSummary.html
---

# OtaTaskConfigurationSummary
<a name="API_OtaTaskConfigurationSummary"></a>

Structure representing one over-the-air (OTA) task configuration.

## Contents
<a name="API_OtaTaskConfigurationSummary_Contents"></a>

 ** CreatedAt **   <a name="managedintegrations-Type-OtaTaskConfigurationSummary-CreatedAt"></a>
The timestamp value of when the over-the-air (OTA) task configuration was created at.
Type: Timestamp
Required: No

 ** Name **   <a name="managedintegrations-Type-OtaTaskConfigurationSummary-Name"></a>
The name of the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** TaskConfigurationId **   <a name="managedintegrations-Type-OtaTaskConfigurationSummary-TaskConfigurationId"></a>
The id of the over-the-air (OTA) task configuration
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_OtaTaskConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OtaTaskConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OtaTaskConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OtaTaskConfigurationSummary)

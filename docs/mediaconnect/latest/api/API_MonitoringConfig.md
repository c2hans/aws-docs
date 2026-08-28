---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MonitoringConfig.html
---

# MonitoringConfig
<a name="API_MonitoringConfig"></a>

 The settings for source monitoring.

## Contents
<a name="API_MonitoringConfig_Contents"></a>

 ** audioMonitoringSettings **   <a name="mediaconnect-Type-MonitoringConfig-audioMonitoringSettings"></a>
 Contains the settings for audio stream metrics monitoring.
Type: Array of [AudioMonitoringSetting](API_AudioMonitoringSetting.md) objects
Required: No

 ** contentQualityAnalysisState **   <a name="mediaconnect-Type-MonitoringConfig-contentQualityAnalysisState"></a>
 Indicates whether content quality analysis is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** thumbnailState **   <a name="mediaconnect-Type-MonitoringConfig-thumbnailState"></a>
 Indicates whether thumbnails are enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** videoMonitoringSettings **   <a name="mediaconnect-Type-MonitoringConfig-videoMonitoringSettings"></a>
 Contains the settings for video stream metrics monitoring.
Type: Array of [VideoMonitoringSetting](API_VideoMonitoringSetting.md) objects
Required: No

## See Also
<a name="API_MonitoringConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MonitoringConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MonitoringConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MonitoringConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

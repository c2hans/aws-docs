---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MetricsExportConfig.html
---

# MetricsExportConfig
<a name="API_MetricsExportConfig"></a>

Set configurations for metrics export.

## Contents
<a name="API_MetricsExportConfig_Contents"></a>

 ** mqttTopic **   <a name="iot-Type-MetricsExportConfig-mqttTopic"></a>
The MQTT topic that Device Defender Detect should publish messages to for metrics export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** roleArn **   <a name="iot-Type-MetricsExportConfig-roleArn"></a>
This role ARN has permission to publish MQTT messages, after which Device Defender Detect can assume the role and publish messages on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_MetricsExportConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MetricsExportConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MetricsExportConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MetricsExportConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkEchoConfig.html
---

# UplinkEchoConfig
<a name="API_UplinkEchoConfig"></a>

Information about an uplink echo `Config`.

Parameters from the `AntennaUplinkConfig`, corresponding to the specified ` AntennaUplinkConfigArn`, are used when this `UplinkEchoConfig` is used in a contact.

## Contents
<a name="API_UplinkEchoConfig_Contents"></a>

 ** antennaUplinkConfigArn **   <a name="groundstation-Type-UplinkEchoConfig-antennaUplinkConfigArn"></a>
ARN of an uplink `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: Yes

 ** enabled **   <a name="groundstation-Type-UplinkEchoConfig-enabled"></a>
Whether or not an uplink `Config` is enabled.
Type: Boolean
Required: Yes

## See Also
<a name="API_UplinkEchoConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UplinkEchoConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UplinkEchoConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UplinkEchoConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

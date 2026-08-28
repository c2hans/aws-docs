---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_IotTwinMakerSourceConfiguration.html
---

# IotTwinMakerSourceConfiguration
<a name="API_IotTwinMakerSourceConfiguration"></a>

The metadata transfer job AWS IoT TwinMaker source configuration.

## Contents
<a name="API_IotTwinMakerSourceConfiguration_Contents"></a>

 ** workspace **   <a name="tm-Type-IotTwinMakerSourceConfiguration-workspace"></a>
The IoT TwinMaker workspace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: Yes

 ** filters **   <a name="tm-Type-IotTwinMakerSourceConfiguration-filters"></a>
The metadata transfer job AWS IoT TwinMaker source configuration filters.
Type: Array of [IotTwinMakerSourceConfigurationFilter](API_IotTwinMakerSourceConfigurationFilter.md) objects
Required: No

## See Also
<a name="API_IotTwinMakerSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/IotTwinMakerSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/IotTwinMakerSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/IotTwinMakerSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

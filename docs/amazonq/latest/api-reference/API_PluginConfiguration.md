---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PluginConfiguration.html
---

# PluginConfiguration
<a name="API_PluginConfiguration"></a>

Configuration information required to invoke chat in `PLUGIN_MODE`.

For more information, see [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html), [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html), and [Conversation settings](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope).

## Contents
<a name="API_PluginConfiguration_Contents"></a>

 ** pluginId **   <a name="qbusiness-Type-PluginConfiguration-pluginId"></a>
 The identifier of the plugin you want to use.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_PluginConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PluginConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PluginConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PluginConfiguration)

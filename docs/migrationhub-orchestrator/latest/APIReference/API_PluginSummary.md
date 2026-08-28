---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_PluginSummary.html
---

# PluginSummary
<a name="API_PluginSummary"></a>

The summary of the Migration Hub Orchestrator plugin.

## Contents
<a name="API_PluginSummary_Contents"></a>

 ** hostname **   <a name="migrationhuborchestrator-Type-PluginSummary-hostname"></a>
The name of the host.
Type: String
Required: No

 ** ipAddress **   <a name="migrationhuborchestrator-Type-PluginSummary-ipAddress"></a>
The IP address at which the plugin is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])`
Required: No

 ** pluginId **   <a name="migrationhuborchestrator-Type-PluginSummary-pluginId"></a>
The ID of the plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `.*\S.*`
Required: No

 ** registeredTime **   <a name="migrationhuborchestrator-Type-PluginSummary-registeredTime"></a>
The time at which the plugin was registered.
Type: String
Required: No

 ** status **   <a name="migrationhuborchestrator-Type-PluginSummary-status"></a>
The status of the plugin.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** version **   <a name="migrationhuborchestrator-Type-PluginSummary-version"></a>
The version of the plugin.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_PluginSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/PluginSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/PluginSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/PluginSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_NewRelicApiKeyConfig.html
---

# NewRelicApiKeyConfig
<a name="API_NewRelicApiKeyConfig"></a>

API key authentication configuration for New Relic service.

## Contents
<a name="API_NewRelicApiKeyConfig_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-NewRelicApiKeyConfig-accountId"></a>
New Relic Account ID
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `[0-9]+`
Required: Yes

 ** apiKey **   <a name="devopsagent-Type-NewRelicApiKeyConfig-apiKey"></a>
New Relic User API Key
Type: String
Pattern: `NRAK-[A-Z0-9]+`
Required: Yes

 ** region **   <a name="devopsagent-Type-NewRelicApiKeyConfig-region"></a>
New Relic region (US or EU)
Type: String
Valid Values: `US | EU | JP`
Required: Yes

 ** alertPolicyIds **   <a name="devopsagent-Type-NewRelicApiKeyConfig-alertPolicyIds"></a>
List of alert policy IDs grouping related conditions
Type: Array of strings
Pattern: `[0-9]+`
Required: No

 ** applicationIds **   <a name="devopsagent-Type-NewRelicApiKeyConfig-applicationIds"></a>
List of monitored APM application IDs in New Relic
Type: Array of strings
Pattern: `[0-9]+`
Required: No

 ** entityGuids **   <a name="devopsagent-Type-NewRelicApiKeyConfig-entityGuids"></a>
List of globally unique IDs for New Relic resources (apps, hosts, services)
Type: Array of strings
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_NewRelicApiKeyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/NewRelicApiKeyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/NewRelicApiKeyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/NewRelicApiKeyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

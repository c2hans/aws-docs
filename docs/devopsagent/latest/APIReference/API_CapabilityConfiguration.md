---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CapabilityConfiguration.html
---

# CapabilityConfiguration
<a name="API_CapabilityConfiguration"></a>

Capability configuration for the AWS DevOps Agent.

## Contents
<a name="API_CapabilityConfiguration_Contents"></a>

 ** enabled **   <a name="devopsagent-Type-CapabilityConfiguration-enabled"></a>
Whether the capability is enabled.
Type: Boolean
Required: No

 ** triggerFilterGroups **   <a name="devopsagent-Type-CapabilityConfiguration-triggerFilterGroups"></a>
Optional trigger filter groups. Evaluated only when enabled=true; retained while the capability is disabled, so re-enabling restores the prior trigger behavior.
Type: Array of [TriggerFilterGroup](API_TriggerFilterGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_CapabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/CapabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/CapabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/CapabilityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

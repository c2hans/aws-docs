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

---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_TriggerFilterGroup.html
---

# TriggerFilterGroup
<a name="API_TriggerFilterGroup"></a>

A group of trigger conditions. The group matches when ALL present conditions pass. A group cannot be empty: at least one condition must be present.

## Contents
<a name="API_TriggerFilterGroup_Contents"></a>

 ** events **   <a name="devopsagent-Type-TriggerFilterGroup-events"></a>
Passes when the webhook event is one of the listed events.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `PULL_REQUEST_READY_FOR_REVIEW | PULL_REQUEST_DRAFT`
Required: No

 ** targetBranches **   <a name="devopsagent-Type-TriggerFilterGroup-targetBranches"></a>
Passes when the change request target branch matches. Applicable to RELEASE\_READINESS\_REVIEW only.
Type: [PatternFilter](API_PatternFilter.md) object
Required: No

## See Also
<a name="API_TriggerFilterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/TriggerFilterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/TriggerFilterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/TriggerFilterGroup)

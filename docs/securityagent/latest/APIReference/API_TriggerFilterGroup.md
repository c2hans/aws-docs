---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_TriggerFilterGroup.html
---

# TriggerFilterGroup
<a name="API_TriggerFilterGroup"></a>

A set of conditions that start an automatic code review when they all pass. A filter group must include `events`, `filters`, or both.

## Contents
<a name="API_TriggerFilterGroup_Contents"></a>

 ** events **   <a name="securityagent-Type-TriggerFilterGroup-events"></a>
Passes when the pull request event is one of the listed events. If you omit this, the group matches `PULL_REQUEST_READY_FOR_REVIEW` and `PULL_REQUEST_DRAFT` events only.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `PULL_REQUEST_READY_FOR_REVIEW | PULL_REQUEST_DRAFT | PULL_REQUEST_LABEL_ADDED`
Required: No

 ** filters **   <a name="securityagent-Type-TriggerFilterGroup-filters"></a>
Passes when every filter passes. If you omit this, the group matches its events on any target branch and with any labels.
Type: Array of [TriggerFilter](API_TriggerFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_TriggerFilterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/TriggerFilterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/TriggerFilterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/TriggerFilterGroup)

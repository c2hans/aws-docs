---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CronSchedule.html
---

# CronSchedule
<a name="API_CronSchedule"></a>

Cron or rate schedule. Trigger-created custom-agent schedules use an EventBridge flexible window of up to 30 minutes for load distribution.

## Contents
<a name="API_CronSchedule_Contents"></a>

 ** expression **   <a name="devopsagent-Type-CronSchedule-expression"></a>
EventBridge cron or rate expression that anchors the flexible window
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_CronSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/CronSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/CronSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/CronSchedule)

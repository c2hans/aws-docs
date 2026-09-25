---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_NotificationRule.html
---

# NotificationRule
<a name="API_NotificationRule"></a>

Single notification rule: which transitions trigger this rule and where the resulting notification should be sent.

## Contents
<a name="API_NotificationRule_Contents"></a>

 ** target **   <a name="cloudwatchomni-Type-NotificationRule-target"></a>
The destination for notifications from this rule.
Type: [NotificationTarget](API_NotificationTarget.md) object
Required: Yes

 ** trigger **   <a name="cloudwatchomni-Type-NotificationRule-trigger"></a>
The conditions that trigger this notification rule.
Type: [NotificationTrigger](API_NotificationTrigger.md) object
Required: Yes

## See Also
<a name="API_NotificationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/NotificationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/NotificationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/NotificationRule)

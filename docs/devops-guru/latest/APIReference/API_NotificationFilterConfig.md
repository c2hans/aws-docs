---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_NotificationFilterConfig.html
---

# NotificationFilterConfig
<a name="API_NotificationFilterConfig"></a>

 The filter configurations for the Amazon SNS notification topic you use with DevOps Guru. You can choose to specify which events or message types to receive notifications for. You can also choose to specify which severity levels to receive notifications for.

## Contents
<a name="API_NotificationFilterConfig_Contents"></a>

 ** MessageTypes **   <a name="DevOpsGuru-Type-NotificationFilterConfig-MessageTypes"></a>
 The events that you want to receive notifications for. For example, you can choose to receive notifications only when the severity level is upgraded or a new insight is created.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `NEW_INSIGHT | CLOSED_INSIGHT | NEW_ASSOCIATION | SEVERITY_UPGRADED | NEW_RECOMMENDATION`
Required: No

 ** Severities **   <a name="DevOpsGuru-Type-NotificationFilterConfig-Severities"></a>
 The severity levels that you want to receive notifications for. For example, you can choose to receive notifications only for insights with `HIGH` and `MEDIUM` severity levels. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

## See Also
<a name="API_NotificationFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/NotificationFilterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/NotificationFilterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/NotificationFilterConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

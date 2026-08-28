---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html
---

# OffPeakWindow
<a name="API_OffPeakWindow"></a>

A custom 10-hour, low-traffic window during which OpenSearch Service can perform mandatory configuration changes on the domain. These actions can include scheduled service software updates and blue/green Auto-Tune enhancements. OpenSearch Service will schedule these actions during the window that you specify.

If you don't specify a window start time, it defaults to 10:00 P.M. local time.

For more information, see [Defining off-peak maintenance windows for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html).

## Contents
<a name="API_OffPeakWindow_Contents"></a>

 ** WindowStartTime **   <a name="opensearchservice-Type-OffPeakWindow-WindowStartTime"></a>
A custom start time for the off-peak window, in Coordinated Universal Time (UTC). The window length will always be 10 hours, so you can't specify an end time. For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M.
Type: [WindowStartTime](API_WindowStartTime.md) object
Required: No

## See Also
<a name="API_OffPeakWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/OffPeakWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/OffPeakWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/OffPeakWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_InsightsConfiguration.html
---

# InsightsConfiguration
<a name="API_InsightsConfiguration"></a>

The structure containing configurations related to insights.

## Contents
<a name="API_InsightsConfiguration_Contents"></a>

 ** InsightsEnabled **   <a name="xray-Type-InsightsConfiguration-InsightsEnabled"></a>
Set the InsightsEnabled value to true to enable insights or false to disable insights.
Type: Boolean
Required: No

 ** NotificationsEnabled **   <a name="xray-Type-InsightsConfiguration-NotificationsEnabled"></a>
Set the NotificationsEnabled value to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.
Type: Boolean
Required: No

## See Also
<a name="API_InsightsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/InsightsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/InsightsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/InsightsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

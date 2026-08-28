---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GroupSummary.html
---

# GroupSummary
<a name="API_GroupSummary"></a>

Details for a group without metadata.

## Contents
<a name="API_GroupSummary_Contents"></a>

 ** FilterExpression **   <a name="xray-Type-GroupSummary-FilterExpression"></a>
The filter expression defining the parameters to include traces.
Type: String
Required: No

 ** GroupARN **   <a name="xray-Type-GroupSummary-GroupARN"></a>
The ARN of the group generated based on the GroupName.
Type: String
Required: No

 ** GroupName **   <a name="xray-Type-GroupSummary-GroupName"></a>
The unique case-sensitive name of the group.
Type: String
Required: No

 ** InsightsConfiguration **   <a name="xray-Type-GroupSummary-InsightsConfiguration"></a>
The structure containing configurations related to insights.
+ The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group.
+ The NotificationsEnabled boolean can be set to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.
Type: [InsightsConfiguration](API_InsightsConfiguration.md) object
Required: No

## See Also
<a name="API_GroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

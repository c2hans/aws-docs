---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NotificationRecipientType.html
---

# NotificationRecipientType
<a name="API_NotificationRecipientType"></a>

The type of notification recipient.

## Contents
<a name="API_NotificationRecipientType_Contents"></a>

 ** UserIds **   <a name="connect-Type-NotificationRecipientType-UserIds"></a>
A list of user IDs. Supports variable injection of `$.ContactLens.ContactEvaluation.Agent.AgentId` for `OnContactEvaluationSubmit` event source.
Type: Array of strings
Required: No

 ** UserTags **   <a name="connect-Type-NotificationRecipientType-UserTags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }. Connect Customer users with the specified tags will be notified.
Type: String to string map
Required: No

## See Also
<a name="API_NotificationRecipientType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NotificationRecipientType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NotificationRecipientType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NotificationRecipientType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaFlowSummary.html
---

# MetaFlowSummary
<a name="API_MetaFlowSummary"></a>

Contains summary information about a WhatsApp Flow, including its ID, name, status, and categories.

## Contents
<a name="API_MetaFlowSummary_Contents"></a>

 ** flowCategories **   <a name="Social-Type-MetaFlowSummary-flowCategories"></a>
The categories that classify the business purpose of the Flow.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 9 items.
Valid Values: `SIGN_UP | SIGN_IN | APPOINTMENT_BOOKING | LEAD_GENERATION | SHOPPING | CONTACT_US | CUSTOMER_SUPPORT | SURVEY | OTHER`
Required: Yes

 ** flowId **   <a name="Social-Type-MetaFlowSummary-flowId"></a>
The unique identifier of the Flow assigned by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** flowName **   <a name="Social-Type-MetaFlowSummary-flowName"></a>
The name of the Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** flowStatus **   <a name="Social-Type-MetaFlowSummary-flowStatus"></a>
The lifecycle status of the Flow (DRAFT, PUBLISHED, DEPRECATED, BLOCKED, or THROTTLED).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: Yes

 ** validationErrors **   <a name="Social-Type-MetaFlowSummary-validationErrors"></a>
A list of validation errors from Meta, if any.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1048576.
Required: Yes

## See Also
<a name="API_MetaFlowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaFlowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaFlowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaFlowSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

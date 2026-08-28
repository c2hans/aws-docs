---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowSummary.html
---

# ContactFlowSummary
<a name="API_ContactFlowSummary"></a>

Contains summary information about a flow.

You can also create and update flows using the [Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html).

## Contents
<a name="API_ContactFlowSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-ContactFlowSummary-Arn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String
Required: No

 ** ContactFlowState **   <a name="connect-Type-ContactFlowSummary-ContactFlowState"></a>
The type of flow.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** ContactFlowStatus **   <a name="connect-Type-ContactFlowSummary-ContactFlowStatus"></a>
The status of the flow.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** ContactFlowType **   <a name="connect-Type-ContactFlowSummary-ContactFlowType"></a>
The type of flow.
Type: String
Valid Values: `CONTACT_FLOW | CUSTOMER_QUEUE | CUSTOMER_HOLD | CUSTOMER_WHISPER | AGENT_HOLD | AGENT_WHISPER | OUTBOUND_WHISPER | AGENT_TRANSFER | QUEUE_TRANSFER | CAMPAIGN`
Required: No

 ** Id **   <a name="connect-Type-ContactFlowSummary-Id"></a>
The identifier of the flow.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** Name **   <a name="connect-Type-ContactFlowSummary-Name"></a>
The name of the flow.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ContactFlowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

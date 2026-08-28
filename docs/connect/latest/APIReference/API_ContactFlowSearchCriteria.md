---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowSearchCriteria.html
---

# ContactFlowSearchCriteria
<a name="API_ContactFlowSearchCriteria"></a>

The search criteria to be used to return flows.

## Contents
<a name="API_ContactFlowSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-ContactFlowSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: Array of [ContactFlowSearchCriteria](#API_ContactFlowSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-ContactFlowSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [ContactFlowSearchCriteria](#API_ContactFlowSearchCriteria) objects
Required: No

 ** StateCondition **   <a name="connect-Type-ContactFlowSearchCriteria-StateCondition"></a>
The state of the flow.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** StatusCondition **   <a name="connect-Type-ContactFlowSearchCriteria-StatusCondition"></a>
The status of the flow.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** StringCondition **   <a name="connect-Type-ContactFlowSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

 ** TypeCondition **   <a name="connect-Type-ContactFlowSearchCriteria-TypeCondition"></a>
The type of flow.
Type: String
Valid Values: `CONTACT_FLOW | CUSTOMER_QUEUE | CUSTOMER_HOLD | CUSTOMER_WHISPER | AGENT_HOLD | AGENT_WHISPER | OUTBOUND_WHISPER | AGENT_TRANSFER | QUEUE_TRANSFER | CAMPAIGN`
Required: No

## See Also
<a name="API_ContactFlowSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowSearchCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

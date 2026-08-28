---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowModuleSummary.html
---

# ContactFlowModuleSummary
<a name="API_ContactFlowModuleSummary"></a>

Contains summary information about a flow.

## Contents
<a name="API_ContactFlowModuleSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-ContactFlowModuleSummary-Arn"></a>
The Amazon Resource Name (ARN) of the flow module.
Type: String
Required: No

 ** Id **   <a name="connect-Type-ContactFlowModuleSummary-Id"></a>
The identifier of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Name **   <a name="connect-Type-ContactFlowModuleSummary-Name"></a>
The name of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`
Required: No

 ** State **   <a name="connect-Type-ContactFlowModuleSummary-State"></a>
The type of flow module.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

## See Also
<a name="API_ContactFlowModuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowModuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowModuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowModuleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

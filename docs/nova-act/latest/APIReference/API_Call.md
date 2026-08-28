---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Call.html
---

# Call
<a name="API_Call"></a>

A request for the client to execute a specific tool with given parameters.

## Contents
<a name="API_Call_Contents"></a>

 ** callId **   <a name="novaact-Type-Call-callId"></a>
A unique identifier for this tool call, used to match results back to requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** input **   <a name="novaact-Type-Call-input"></a>
The input parameters for the tool call, formatted according to the tool's schema.
Type: JSON value
Required: Yes

 ** name **   <a name="novaact-Type-Call-name"></a>
The name of the tool to invoke, following the pattern 'tool.{toolName}' or 'browser.{browserAction}'.
Type: String
Required: Yes

## See Also
<a name="API_Call_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/Call)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/Call)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/Call)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

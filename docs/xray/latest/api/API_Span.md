---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Span.html
---

# Span
<a name="API_Span"></a>

 A span from a trace that has been ingested by the X-Ray service. A span represents a unit of work or an operation performed by a service.

## Contents
<a name="API_Span_Contents"></a>

 ** Document **   <a name="xray-Type-Span-Document"></a>
 The span document.
Type: String
Length Constraints: Maximum length of 204800.
Required: No

 ** Id **   <a name="xray-Type-Span-Id"></a>
The span ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## See Also
<a name="API_Span_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Span)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Span)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Span)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

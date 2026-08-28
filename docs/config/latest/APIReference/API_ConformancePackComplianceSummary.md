---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackComplianceSummary.html
---

# ConformancePackComplianceSummary
<a name="API_ConformancePackComplianceSummary"></a>

Summary includes the name and status of the conformance pack.

## Contents
<a name="API_ConformancePackComplianceSummary_Contents"></a>

 ** ConformancePackComplianceStatus **   <a name="config-Type-ConformancePackComplianceSummary-ConformancePackComplianceStatus"></a>
The status of the conformance pack.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: Yes

 ** ConformancePackName **   <a name="config-Type-ConformancePackComplianceSummary-ConformancePackName"></a>
The name of the conformance pack name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

## See Also
<a name="API_ConformancePackComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackComplianceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackComplianceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackComplianceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

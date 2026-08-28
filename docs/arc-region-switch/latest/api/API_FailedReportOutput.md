---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_FailedReportOutput.html
---

# FailedReportOutput
<a name="API_FailedReportOutput"></a>

Information about a report generation that failed.

## Contents
<a name="API_FailedReportOutput_Contents"></a>

 ** errorCode **   <a name="regionswitch-Type-FailedReportOutput-errorCode"></a>
The error code for the failed report generation.
Type: String
Valid Values: `insufficientPermissions | invalidResource | configurationError`
Required: No

 ** errorMessage **   <a name="regionswitch-Type-FailedReportOutput-errorMessage"></a>
The error message for the failed report generation.
Type: String
Required: No

## See Also
<a name="API_FailedReportOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/FailedReportOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/FailedReportOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/FailedReportOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

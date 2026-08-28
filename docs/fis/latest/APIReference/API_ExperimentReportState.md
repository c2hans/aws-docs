---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportState.html
---

# ExperimentReportState
<a name="API_ExperimentReportState"></a>

Describes the state of the experiment report generation.

## Contents
<a name="API_ExperimentReportState_Contents"></a>

 ** error **   <a name="fis-Type-ExperimentReportState-error"></a>
The error information of the experiment when the experiment report generation has failed.
Type: [ExperimentReportError](API_ExperimentReportError.md) object
Required: No

 ** reason **   <a name="fis-Type-ExperimentReportState-reason"></a>
The reason for the state of the experiment report generation.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** status **   <a name="fis-Type-ExperimentReportState-status"></a>
The state of the experiment report generation.
Type: String
Valid Values: `pending | running | completed | cancelled | failed`
Required: No

## See Also
<a name="API_ExperimentReportState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentReportState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentReportState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentReportState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

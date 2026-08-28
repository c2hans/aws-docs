---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfigurationOutputsS3Configuration.html
---

# ExperimentReportConfigurationOutputsS3Configuration
<a name="API_ExperimentReportConfigurationOutputsS3Configuration"></a>

Specifies the S3 destination for the experiment report.

## Contents
<a name="API_ExperimentReportConfigurationOutputsS3Configuration_Contents"></a>

 ** bucketName **   <a name="fis-Type-ExperimentReportConfigurationOutputsS3Configuration-bucketName"></a>
The name of the S3 bucket where the experiment report will be stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[\S]+`
Required: No

 ** prefix **   <a name="fis-Type-ExperimentReportConfigurationOutputsS3Configuration-prefix"></a>
The prefix of the S3 bucket where the experiment report will be stored.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentReportConfigurationOutputsS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentReportConfigurationOutputsS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentReportConfigurationOutputsS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentReportConfigurationOutputsS3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

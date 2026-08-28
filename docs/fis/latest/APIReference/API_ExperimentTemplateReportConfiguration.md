---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfiguration.html
---

# ExperimentTemplateReportConfiguration
<a name="API_ExperimentTemplateReportConfiguration"></a>

Describes the experiment report configuration. For more information, see [Experiment report configurations for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiment-report-configuration).

## Contents
<a name="API_ExperimentTemplateReportConfiguration_Contents"></a>

 ** dataSources **   <a name="fis-Type-ExperimentTemplateReportConfiguration-dataSources"></a>
The data sources for the experiment report.
Type: [ExperimentTemplateReportConfigurationDataSources](API_ExperimentTemplateReportConfigurationDataSources.md) object
Required: No

 ** outputs **   <a name="fis-Type-ExperimentTemplateReportConfiguration-outputs"></a>
Describes the output destinations of the experiment report.
Type: [ExperimentTemplateReportConfigurationOutputs](API_ExperimentTemplateReportConfigurationOutputs.md) object
Required: No

 ** postExperimentDuration **   <a name="fis-Type-ExperimentTemplateReportConfiguration-postExperimentDuration"></a>
The duration after the experiment end time for the data sources to include in the report.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `[\S]+`
Required: No

 ** preExperimentDuration **   <a name="fis-Type-ExperimentTemplateReportConfiguration-preExperimentDuration"></a>
The duration before the experiment start time for the data sources to include in the report.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTemplateReportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateReportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateReportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateReportConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfiguration.html
---

# ExperimentReportConfiguration
<a name="API_ExperimentReportConfiguration"></a>

Describes the report configuration for the experiment. For more information, see [Experiment report configurations for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiment-report-configuration).

## Contents
<a name="API_ExperimentReportConfiguration_Contents"></a>

 ** dataSources **   <a name="fis-Type-ExperimentReportConfiguration-dataSources"></a>
The data sources for the experiment report.
Type: [ExperimentReportConfigurationDataSources](API_ExperimentReportConfigurationDataSources.md) object
Required: No

 ** outputs **   <a name="fis-Type-ExperimentReportConfiguration-outputs"></a>
The output destinations of the experiment report.
Type: [ExperimentReportConfigurationOutputs](API_ExperimentReportConfigurationOutputs.md) object
Required: No

 ** postExperimentDuration **   <a name="fis-Type-ExperimentReportConfiguration-postExperimentDuration"></a>
The duration after the experiment end time for the data sources to include in the report.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `[\S]+`
Required: No

 ** preExperimentDuration **   <a name="fis-Type-ExperimentReportConfiguration-preExperimentDuration"></a>
The duration before the experiment start time for the data sources to include in the report.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentReportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentReportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentReportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentReportConfiguration)

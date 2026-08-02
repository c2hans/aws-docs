---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateReportConfigurationInput.html
---

# CreateExperimentTemplateReportConfigurationInput
<a name="API_CreateExperimentTemplateReportConfigurationInput"></a>

Specifies the configuration for experiment reports.

## Contents
<a name="API_CreateExperimentTemplateReportConfigurationInput_Contents"></a>

 ** dataSources **   <a name="fis-Type-CreateExperimentTemplateReportConfigurationInput-dataSources"></a>
The data sources for the experiment report.
Type: [ExperimentTemplateReportConfigurationDataSourcesInput](API_ExperimentTemplateReportConfigurationDataSourcesInput.md) object
Required: No

 ** outputs **   <a name="fis-Type-CreateExperimentTemplateReportConfigurationInput-outputs"></a>
The output destinations of the experiment report.
Type: [ExperimentTemplateReportConfigurationOutputsInput](API_ExperimentTemplateReportConfigurationOutputsInput.md) object
Required: No

 ** postExperimentDuration **   <a name="fis-Type-CreateExperimentTemplateReportConfigurationInput-postExperimentDuration"></a>
The duration after the experiment end time for the data sources to include in the report.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `[\S]+`
Required: No

 ** preExperimentDuration **   <a name="fis-Type-CreateExperimentTemplateReportConfigurationInput-preExperimentDuration"></a>
The duration before the experiment start time for the data sources to include in the report.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_CreateExperimentTemplateReportConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/CreateExperimentTemplateReportConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/CreateExperimentTemplateReportConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/CreateExperimentTemplateReportConfigurationInput)

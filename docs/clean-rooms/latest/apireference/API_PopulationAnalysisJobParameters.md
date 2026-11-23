---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulationAnalysisJobParameters.html
---

# PopulationAnalysisJobParameters

Contains the PySpark job parameters used to populate an intermediate table, including the ARN of the analysis template that defines the job. Use these parameters instead of SQL parameters when the analysis you use to populate the intermediate table is a PySpark analysis template.

## Contents
<a name="API_PopulationAnalysisJobParameters_Contents"></a>

 ** analysisTemplateArn **   <a name="API-Type-PopulationAnalysisJobParameters-analysisTemplateArn"></a>
Specifies the ARN of the PySpark analysis template that populates the intermediate table. Provide this ARN in `jobParameters` when you populate the intermediate table with results from a PySpark job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

## See Also
<a name="API_PopulationAnalysisJobParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PopulationAnalysisJobParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PopulationAnalysisJobParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PopulationAnalysisJobParameters)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulationAnalysisSqlParameters.html
---

# PopulationAnalysisSqlParameters
<a name="API_PopulationAnalysisSqlParameters"></a>

Contains the SQL parameters used to populate an intermediate table.

## Contents
<a name="API_PopulationAnalysisSqlParameters_Contents"></a>

 ** analysisTemplateArn **   <a name="API-Type-PopulationAnalysisSqlParameters-analysisTemplateArn"></a>
The Amazon Resource Name (ARN) of the analysis template to use for populating the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: No

 ** queryString **   <a name="API-Type-PopulationAnalysisSqlParameters-queryString"></a>
The SQL query string used to populate the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500000.
Required: No

## See Also
<a name="API_PopulationAnalysisSqlParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PopulationAnalysisSqlParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PopulationAnalysisSqlParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PopulationAnalysisSqlParameters)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulationAnalysisConfiguration.html
---

# PopulationAnalysisConfiguration
<a name="API_PopulationAnalysisConfiguration"></a>

Contains the configuration that defines the analysis used to populate an intermediate table.

## Contents
<a name="API_PopulationAnalysisConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** sqlParameters **   <a name="API-Type-PopulationAnalysisConfiguration-sqlParameters"></a>
The SQL parameters for the population analysis, including the query string or analysis template ARN.
Type: [PopulationAnalysisSqlParameters](API_PopulationAnalysisSqlParameters.md) object
Required: No

## See Also
<a name="API_PopulationAnalysisConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PopulationAnalysisConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PopulationAnalysisConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PopulationAnalysisConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

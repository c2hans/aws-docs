---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ContributionAnalysisDefault.html
---

# ContributionAnalysisDefault
<a name="API_ContributionAnalysisDefault"></a>

The contribution analysis visual display for a line, pie, or bar chart.

## Contents
<a name="API_ContributionAnalysisDefault_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContributorDimensions **   <a name="QS-Type-ContributionAnalysisDefault-ContributorDimensions"></a>
The dimensions columns that are used in the contribution analysis, usually a list of `ColumnIdentifiers`.
Type: Array of [ColumnIdentifier](API_ColumnIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: Yes

 ** MeasureFieldId **   <a name="QS-Type-ContributionAnalysisDefault-MeasureFieldId"></a>
The measure field that is used in the contribution analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## See Also
<a name="API_ContributionAnalysisDefault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ContributionAnalysisDefault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ContributionAnalysisDefault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ContributionAnalysisDefault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

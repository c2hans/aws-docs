---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnalysisSummary.html
---

# AnalysisSummary
<a name="API_AnalysisSummary"></a>

The summary metadata that describes an analysis.

## Contents
<a name="API_AnalysisSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnalysisId **   <a name="QS-Type-AnalysisSummary-AnalysisId"></a>
The ID of the analysis. This ID displays in the URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** Arn **   <a name="QS-Type-AnalysisSummary-Arn"></a>
The Amazon Resource Name (ARN) for the analysis.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-AnalysisSummary-CreatedTime"></a>
The time that the analysis was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-AnalysisSummary-LastUpdatedTime"></a>
The time that the analysis was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-AnalysisSummary-Name"></a>
The name of the analysis. This name is displayed in the Quick Sight console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Status **   <a name="QS-Type-AnalysisSummary-Status"></a>
The last known status for the analysis.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

## See Also
<a name="API_AnalysisSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnalysisSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnalysisSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnalysisSummary)

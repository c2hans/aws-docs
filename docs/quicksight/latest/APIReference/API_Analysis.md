---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Analysis.html
---

# Analysis
<a name="API_Analysis"></a>

Metadata structure for an analysis in Quick Sight

## Contents
<a name="API_Analysis_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnalysisId **   <a name="QS-Type-Analysis-AnalysisId"></a>
The ID of the analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** Arn **   <a name="QS-Type-Analysis-Arn"></a>
The Amazon Resource Name (ARN) of the analysis.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-Analysis-CreatedTime"></a>
The time that the analysis was created.
Type: Timestamp
Required: No

 ** DataSetArns **   <a name="QS-Type-Analysis-DataSetArns"></a>
The ARNs of the datasets of the analysis.
Type: Array of strings
Array Members: Maximum number of 100 items.
Required: No

 ** Errors **   <a name="QS-Type-Analysis-Errors"></a>
Errors associated with the analysis.
Type: Array of [AnalysisError](API_AnalysisError.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-Analysis-LastUpdatedTime"></a>
The time that the analysis was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-Analysis-Name"></a>
The descriptive name of the analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Sheets **   <a name="QS-Type-Analysis-Sheets"></a>
A list of the associated sheets with the unique identifier and name of each sheet.
Type: Array of [Sheet](API_Sheet.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** Status **   <a name="QS-Type-Analysis-Status"></a>
Status associated with the analysis.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** ThemeArn **   <a name="QS-Type-Analysis-ThemeArn"></a>
The ARN of the theme of the analysis.
Type: String
Required: No

## See Also
<a name="API_Analysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Analysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Analysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Analysis)

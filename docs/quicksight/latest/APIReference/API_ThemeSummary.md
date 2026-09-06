---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ThemeSummary.html
---

# ThemeSummary
<a name="API_ThemeSummary"></a>

The theme summary.

## Contents
<a name="API_ThemeSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-ThemeSummary-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-ThemeSummary-CreatedTime"></a>
The date and time that this theme was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-ThemeSummary-LastUpdatedTime"></a>
The last date and time that this theme was updated.
Type: Timestamp
Required: No

 ** LatestVersionNumber **   <a name="QS-Type-ThemeSummary-LatestVersionNumber"></a>
The latest version number for the theme.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** Name **   <a name="QS-Type-ThemeSummary-Name"></a>
the display name for the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ThemeId **   <a name="QS-Type-ThemeSummary-ThemeId"></a>
The ID of the theme. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_ThemeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ThemeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ThemeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ThemeSummary)

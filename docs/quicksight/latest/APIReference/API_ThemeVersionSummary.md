---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ThemeVersionSummary.html
---

# ThemeVersionSummary
<a name="API_ThemeVersionSummary"></a>

The theme version.

## Contents
<a name="API_ThemeVersionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-ThemeVersionSummary-Arn"></a>
The Amazon Resource Name (ARN) of the theme version.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-ThemeVersionSummary-CreatedTime"></a>
The date and time that this theme version was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-ThemeVersionSummary-Description"></a>
The description of the theme version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Status **   <a name="QS-Type-ThemeVersionSummary-Status"></a>
The status of the theme version.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** VersionNumber **   <a name="QS-Type-ThemeVersionSummary-VersionNumber"></a>
The version number of the theme version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ThemeVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ThemeVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ThemeVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ThemeVersionSummary)

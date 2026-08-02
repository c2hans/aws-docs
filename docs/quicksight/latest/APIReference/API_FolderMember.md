---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FolderMember.html
---

# FolderMember
<a name="API_FolderMember"></a>

An asset in a Quick Sight folder, such as a dashboard, analysis, or dataset.

## Contents
<a name="API_FolderMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MemberId **   <a name="QS-Type-FolderMember-MemberId"></a>
The ID of an asset in the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: No

 ** MemberType **   <a name="QS-Type-FolderMember-MemberType"></a>
The type of asset that it is.
Type: String
Valid Values: `DASHBOARD | ANALYSIS | DATASET | DATASOURCE | TOPIC`
Required: No

## See Also
<a name="API_FolderMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FolderMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FolderMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FolderMember)

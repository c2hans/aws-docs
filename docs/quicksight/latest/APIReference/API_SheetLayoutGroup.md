---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SheetLayoutGroup.html
---

# SheetLayoutGroup
<a name="API_SheetLayoutGroup"></a>

A group of elements within a sheet layout.

## Contents
<a name="API_SheetLayoutGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="QS-Type-SheetLayoutGroup-Id"></a>
A unique identifier for the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Members **   <a name="QS-Type-SheetLayoutGroup-Members"></a>
The members of the group.
Type: Array of [SheetLayoutGroupMember](API_SheetLayoutGroupMember.md) objects
Array Members: Minimum number of 2 items. Maximum number of 430 items.
Required: Yes

## See Also
<a name="API_SheetLayoutGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SheetLayoutGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SheetLayoutGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SheetLayoutGroup)

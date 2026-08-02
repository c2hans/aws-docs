---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Sheet.html
---

# Sheet
<a name="API_Sheet"></a>

A *sheet*, which is an object that contains a set of visuals that are viewed together on one page in Quick Sight. Every analysis and dashboard contains at least one sheet. Each sheet contains at least one visualization widget, for example a chart, pivot table, or narrative insight. Sheets can be associated with other components, such as controls, filters, and so on.

## Contents
<a name="API_Sheet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Images **   <a name="QS-Type-Sheet-Images"></a>
A list of images on a sheet.
Type: Array of [SheetImage](API_SheetImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Name **   <a name="QS-Type-Sheet-Name"></a>
The name of a sheet. This name is displayed on the sheet's tab in the Quick Sight console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** SheetId **   <a name="QS-Type-Sheet-SheetId"></a>
The unique identifier associated with a sheet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_Sheet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Sheet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Sheet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Sheet)

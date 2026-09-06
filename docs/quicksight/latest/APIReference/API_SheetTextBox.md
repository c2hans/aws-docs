---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SheetTextBox.html
---

# SheetTextBox
<a name="API_SheetTextBox"></a>

A text box.

## Contents
<a name="API_SheetTextBox_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SheetTextBoxId **   <a name="QS-Type-SheetTextBox-SheetTextBoxId"></a>
The unique identifier for a text box. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have text boxes that share identifiers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Content **   <a name="QS-Type-SheetTextBox-Content"></a>
The content that is displayed in the text box.
Type: String
Length Constraints: Maximum length of 150000.
Required: No

 ** Interactions **   <a name="QS-Type-SheetTextBox-Interactions"></a>
The general textbox interactions setup for a textbox.
Type: [TextBoxInteractionOptions](API_TextBoxInteractionOptions.md) object
Required: No

## See Also
<a name="API_SheetTextBox_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SheetTextBox)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SheetTextBox)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SheetTextBox)

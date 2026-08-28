---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TableCellStyle.html
---

# TableCellStyle
<a name="API_TableCellStyle"></a>

The table cell style for a cell in pivot table or table visual.

## Contents
<a name="API_TableCellStyle_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BackgroundColor **   <a name="QS-Type-TableCellStyle-BackgroundColor"></a>
The background color for the table cells.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Border **   <a name="QS-Type-TableCellStyle-Border"></a>
The borders for the table cells.
Type: [GlobalTableBorderOptions](API_GlobalTableBorderOptions.md) object
Required: No

 ** FontConfiguration **   <a name="QS-Type-TableCellStyle-FontConfiguration"></a>
The font configuration of the table cells.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** Height **   <a name="QS-Type-TableCellStyle-Height"></a>
The height color for the table cells.
Type: Integer
Valid Range: Minimum value of 8. Maximum value of 500.
Required: No

 ** HorizontalTextAlignment **   <a name="QS-Type-TableCellStyle-HorizontalTextAlignment"></a>
The horizontal text alignment (left, center, right, auto) for the table cells.
Type: String
Valid Values: `LEFT | CENTER | RIGHT | AUTO`
Required: No

 ** TextWrap **   <a name="QS-Type-TableCellStyle-TextWrap"></a>
The text wrap (none, wrap) for the table cells.
Type: String
Valid Values: `NONE | WRAP`
Required: No

 ** VerticalTextAlignment **   <a name="QS-Type-TableCellStyle-VerticalTextAlignment"></a>
The vertical text alignment (top, middle, bottom) for the table cells.
Type: String
Valid Values: `TOP | MIDDLE | BOTTOM | AUTO`
Required: No

 ** Visibility **   <a name="QS-Type-TableCellStyle-Visibility"></a>
The visibility of the table cells.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_TableCellStyle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TableCellStyle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TableCellStyle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TableCellStyle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

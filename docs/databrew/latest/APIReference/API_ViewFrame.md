---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ViewFrame.html
---

# ViewFrame
<a name="API_ViewFrame"></a>

Represents the data being transformed during an action.

## Contents
<a name="API_ViewFrame_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** StartColumnIndex **   <a name="databrew-Type-ViewFrame-StartColumnIndex"></a>
The starting index for the range of columns to return in the view frame.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Analytics **   <a name="databrew-Type-ViewFrame-Analytics"></a>
Controls if analytics computation is enabled or disabled. Enabled by default.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** ColumnRange **   <a name="databrew-Type-ViewFrame-ColumnRange"></a>
The number of columns to include in the view frame, beginning with the `StartColumnIndex` value and ignoring any columns in the `HiddenColumns` list.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** HiddenColumns **   <a name="databrew-Type-ViewFrame-HiddenColumns"></a>
A list of columns to hide in the view frame.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** RowRange **   <a name="databrew-Type-ViewFrame-RowRange"></a>
The number of rows to include in the view frame, beginning with the `StartRowIndex` value.
Type: Integer
Required: No

 ** StartRowIndex **   <a name="databrew-Type-ViewFrame-StartRowIndex"></a>
The starting index for the range of rows to return in the view frame.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ViewFrame_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ViewFrame)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ViewFrame)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ViewFrame)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

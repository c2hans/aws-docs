---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UploadSettings.html
---

# UploadSettings
<a name="API_UploadSettings"></a>

Information about the format for a source file or files.

## Contents
<a name="API_UploadSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainsHeader **   <a name="QS-Type-UploadSettings-ContainsHeader"></a>
Whether the file has a header row, or the files each have a header row.
Type: Boolean
Required: No

 ** CustomCellAddressRange **   <a name="QS-Type-UploadSettings-CustomCellAddressRange"></a>
A custom cell address range for Excel files, specifying which cells to import from the spreadsheet.
Type: String
Required: No

 ** Delimiter **   <a name="QS-Type-UploadSettings-Delimiter"></a>
The delimiter between values in the file.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** Format **   <a name="QS-Type-UploadSettings-Format"></a>
File format.
Type: String
Valid Values: `CSV | TSV | CLF | ELF | XLSX | JSON`
Required: No

 ** StartFromRow **   <a name="QS-Type-UploadSettings-StartFromRow"></a>
A row number to start reading data from.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TextQualifier **   <a name="QS-Type-UploadSettings-TextQualifier"></a>
Text qualifier.
Type: String
Valid Values: `DOUBLE_QUOTE | SINGLE_QUOTE`
Required: No

## See Also
<a name="API_UploadSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UploadSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UploadSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UploadSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

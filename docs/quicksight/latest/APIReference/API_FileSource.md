---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FileSource.html
---

# FileSource
<a name="API_FileSource"></a>

A physical table type that contains the schema and upload settings for a file-based data source.

## Contents
<a name="API_FileSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-FileSource-DataSourceArn"></a>
The Amazon Resource Name (ARN) for the data source.
Type: String
Required: Yes

 ** InputColumns **   <a name="QS-Type-FileSource-InputColumns"></a>
The column schema of the file.
Type: Array of [InputColumn](API_InputColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** SheetIndex **   <a name="QS-Type-FileSource-SheetIndex"></a>
The zero-based index of the sheet to use within the file. For files that contain multiple sheets, this identifies which sheet to read. Files that contain a single sheet, or that have no concept of sheets, use sheet 0.
Type: Integer
Required: Yes

 ** UploadSettings **   <a name="QS-Type-FileSource-UploadSettings"></a>
Information about the format for the source file.
Type: [UploadSettings](API_UploadSettings.md) object
Required: No

## See Also
<a name="API_FileSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FileSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FileSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FileSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotFile.html
---

# SnapshotFile
<a name="API_SnapshotFile"></a>

A structure that contains the information for the snapshot that you want to generate. This information is provided by you when you start a new snapshot job.

## Contents
<a name="API_SnapshotFile_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FormatType **   <a name="QS-Type-SnapshotFile-FormatType"></a>
The format of the snapshot file to be generated. You can choose between `CSV`, `Excel`, or `PDF`.
Type: String
Valid Values: `CSV | PDF | EXCEL`
Required: Yes

 ** SheetSelections **   <a name="QS-Type-SnapshotFile-SheetSelections"></a>
A list of `SnapshotFileSheetSelection` objects that contain information on the dashboard sheet that is exported. These objects provide information about the snapshot artifacts that are generated during the job. This structure can hold a maximum of 5 CSV configurations, 5 Excel configurations, or 1 configuration for PDF.
Type: Array of [SnapshotFileSheetSelection](API_SnapshotFileSheetSelection.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_SnapshotFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotFile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

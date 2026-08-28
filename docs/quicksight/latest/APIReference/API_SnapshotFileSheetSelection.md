---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotFileSheetSelection.html
---

# SnapshotFileSheetSelection
<a name="API_SnapshotFileSheetSelection"></a>

A structure that contains information that identifies the snapshot that needs to be generated.

## Contents
<a name="API_SnapshotFileSheetSelection_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SelectionScope **   <a name="QS-Type-SnapshotFileSheetSelection-SelectionScope"></a>
The selection scope of the visuals on a sheet of a dashboard that you are generating a snapthot of. You can choose one of the following options.
+  `ALL_VISUALS` - Selects all visuals that are on the sheet. This value is required if the snapshot is a PDF.
+  `SELECTED_VISUALS` - Select the visual that you want to add to the snapshot. This value is required if the snapshot is a CSV or Excel workbook.
Type: String
Valid Values: `ALL_VISUALS | SELECTED_VISUALS`
Required: Yes

 ** SheetId **   <a name="QS-Type-SnapshotFileSheetSelection-SheetId"></a>
The sheet ID of the dashboard to generate the snapshot artifact from. This value is required for CSV, Excel, and PDF format types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** VisualIds **   <a name="QS-Type-SnapshotFileSheetSelection-VisualIds"></a>
 A structure that lists the IDs of the visuals in the selected sheet. Supported visual types are table, pivot table visuals. This value is required if you are generating a CSV or Excel workbook. This value supports a maximum of 1 visual ID for CSV and 5 visual IDs across up to 5 sheet selections for Excel. If you are generating an Excel workbook, the order of the visual IDs provided in this structure determines the order of the worksheets in the Excel file.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_SnapshotFileSheetSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotFileSheetSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotFileSheetSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotFileSheetSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

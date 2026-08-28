---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Cell.html
---

# Cell
<a name="API_Cell"></a>

An occurrence of sensitive data detected in a Microsoft Excel workbook, comma-separated value (CSV) file, or tab-separated value (TSV) file.

## Contents
<a name="API_Cell_Contents"></a>

 ** CellReference **   <a name="securityhub-Type-Cell-CellReference"></a>
For a Microsoft Excel workbook, provides the location of the cell, as an absolute cell reference, that contains the data. For example, Sheet2\!C5 for cell C5 on Sheet2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Column **   <a name="securityhub-Type-Cell-Column"></a>
The column number of the column that contains the data. For a Microsoft Excel workbook, the column number corresponds to the alphabetical column identifiers. For example, a value of 1 for Column corresponds to the A column in the workbook.
Type: Long
Required: No

 ** ColumnName **   <a name="securityhub-Type-Cell-ColumnName"></a>
The name of the column that contains the data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Row **   <a name="securityhub-Type-Cell-Row"></a>
The row number of the row that contains the data.
Type: Long
Required: No

## See Also
<a name="API_Cell_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Cell)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Cell)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Cell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

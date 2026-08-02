---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ExcelOptions.html
---

# ExcelOptions
<a name="API_ExcelOptions"></a>

Represents a set of options that define how DataBrew will interpret a Microsoft Excel file when creating a dataset from that file.

## Contents
<a name="API_ExcelOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** HeaderRow **   <a name="databrew-Type-ExcelOptions-HeaderRow"></a>
A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.
Type: Boolean
Required: No

 ** SheetIndexes **   <a name="databrew-Type-ExcelOptions-SheetIndexes"></a>
One or more sheet numbers in the Excel file that will be included in the dataset.
Type: Array of integers
Array Members: Fixed number of 1 item.
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** SheetNames **   <a name="databrew-Type-ExcelOptions-SheetNames"></a>
One or more named sheets in the Excel file that will be included in the dataset.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 31.
Required: No

## See Also
<a name="API_ExcelOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ExcelOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ExcelOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ExcelOptions)

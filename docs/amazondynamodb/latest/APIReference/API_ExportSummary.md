---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportSummary.html
---

# ExportSummary
<a name="API_ExportSummary"></a>

Summary information about an export task.

## Contents
<a name="API_ExportSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ExportArn **   <a name="DDB-Type-ExportSummary-ExportArn"></a>
The Amazon Resource Name (ARN) of the export.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** ExportStatus **   <a name="DDB-Type-ExportSummary-ExportStatus"></a>
Export can be in one of the following states: IN\_PROGRESS, COMPLETED, or FAILED.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** ExportType **   <a name="DDB-Type-ExportSummary-ExportType"></a>
The type of export that was performed. Valid values are `FULL_EXPORT` or `INCREMENTAL_EXPORT`.
Type: String
Valid Values: `FULL_EXPORT | INCREMENTAL_EXPORT`
Required: No

## See Also
<a name="API_ExportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ExportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ExportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ExportSummary)

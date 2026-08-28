---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_IncrementalExportSpecification.html
---

# IncrementalExportSpecification
<a name="API_IncrementalExportSpecification"></a>

Optional object containing the parameters specific to an incremental export.

## Contents
<a name="API_IncrementalExportSpecification_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ExportFromTime **   <a name="DDB-Type-IncrementalExportSpecification-ExportFromTime"></a>
Time in the past which provides the inclusive start range for the export table's data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the table's state including and after this point in time.
Type: Timestamp
Required: No

 ** ExportToTime **   <a name="DDB-Type-IncrementalExportSpecification-ExportToTime"></a>
Time in the past which provides the exclusive end range for the export table's data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the table's state just prior to this point in time. If this is not provided, the latest time with data available will be used.
Type: Timestamp
Required: No

 ** ExportViewType **   <a name="DDB-Type-IncrementalExportSpecification-ExportViewType"></a>
The view type that was chosen for the export. Valid values are `NEW_AND_OLD_IMAGES` and `NEW_IMAGES`. The default value is `NEW_AND_OLD_IMAGES`.
 `NEW_AND_OLD_IMAGES` exports both the new and old images of each changed item, while `NEW_IMAGES` exports only the new (latest) image. The view type you choose determines the structure of each item in the output for `insert`, `update`, and `delete` operations. For details and examples of how each view type shapes the export output, see [DynamoDB table export output format](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.Output.html) in the *Amazon DynamoDB Developer Guide*.
Type: String
Valid Values: `NEW_IMAGE | NEW_AND_OLD_IMAGES`
Required: No

## See Also
<a name="API_IncrementalExportSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/IncrementalExportSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/IncrementalExportSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/IncrementalExportSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

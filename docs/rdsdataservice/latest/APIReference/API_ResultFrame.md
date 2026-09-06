---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ResultFrame.html
---

# ResultFrame
<a name="API_ResultFrame"></a>

The result set returned by a SQL statement.

**Note**
This data structure is only used with the deprecated `ExecuteSql` operation. Use the `BatchExecuteStatement` or `ExecuteStatement` operation instead.

## Contents
<a name="API_ResultFrame_Contents"></a>

 ** records **   <a name="rdsdtataservice-Type-ResultFrame-records"></a>
The records in the result set.
Type: Array of [Record](API_Record.md) objects
Required: No

 ** resultSetMetadata **   <a name="rdsdtataservice-Type-ResultFrame-resultSetMetadata"></a>
The result-set metadata in the result set.
Type: [ResultSetMetadata](API_ResultSetMetadata.md) object
Required: No

## See Also
<a name="API_ResultFrame_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/ResultFrame)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/ResultFrame)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/ResultFrame)

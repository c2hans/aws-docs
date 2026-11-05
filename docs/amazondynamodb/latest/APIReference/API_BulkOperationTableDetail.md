---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationTableDetail.html
---

# BulkOperationTableDetail
<a name="API_BulkOperationTableDetail"></a>

Contains identifying information for a table associated with a bulk operation.

## Contents
<a name="API_BulkOperationTableDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TableId **   <a name="DDB-Type-BulkOperationTableDetail-TableId"></a>
The unique identifier of the table associated with the bulk operation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** TableName **   <a name="DDB-Type-BulkOperationTableDetail-TableName"></a>
The name or ARN of the table associated with the bulk operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_BulkOperationTableDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BulkOperationTableDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BulkOperationTableDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BulkOperationTableDetail)

---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationSummary.html
---

# BulkOperationSummary
<a name="API_BulkOperationSummary"></a>

Contains summary information about a bulk operation.

## Contents
<a name="API_BulkOperationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BulkOperationArn **   <a name="DDB-Type-BulkOperationSummary-BulkOperationArn"></a>
The Amazon Resource Name (ARN) of the bulk operation.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

 ** BulkOperationStatus **   <a name="DDB-Type-BulkOperationSummary-BulkOperationStatus"></a>
The current status of the bulk operation.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | CANCELLING | CANCELLED | FAILED`
Required: Yes

 ** StartTime **   <a name="DDB-Type-BulkOperationSummary-StartTime"></a>
The time when DynamoDB accepted the start request.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="DDB-Type-BulkOperationSummary-EndTime"></a>
The time when the operation reached a terminal status. DynamoDB omits this value while the operation remains in progress.
Type: Timestamp
Required: No

## See Also
<a name="API_BulkOperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BulkOperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BulkOperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BulkOperationSummary)

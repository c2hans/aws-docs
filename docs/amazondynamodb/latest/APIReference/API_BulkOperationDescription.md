---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html
---

# BulkOperationDescription
<a name="API_BulkOperationDescription"></a>

Contains detailed information about a bulk operation.

## Contents
<a name="API_BulkOperationDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BulkOperationArn **   <a name="DDB-Type-BulkOperationDescription-BulkOperationArn"></a>
The Amazon Resource Name (ARN) of the bulk operation.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** BulkOperationStatus **   <a name="DDB-Type-BulkOperationDescription-BulkOperationStatus"></a>
The current status of the bulk operation can be one of the following values:
 `IN_PROGRESS`
DynamoDB is processing the input.
 `COMPLETED`
The bulk operation finished without parsing or validation errors. Condition-check failures do not cause the operation to complete with errors.
 `COMPLETED_WITH_ERRORS`
The bulk operation finished, but DynamoDB couldn't process at least one input item because of a parsing or validation error. When you enable `ERROR` output, DynamoDB writes the details to the configured Amazon S3 output location.
 `CANCELLING`
DynamoDB accepted a cancellation request and is stopping the operation.
 `CANCELLED`
DynamoDB stopped the operation after a cancellation request.
 `FAILED`
The bulk operation failed. DynamoDB might write some items before the operation reaches this status. See [FailureCode](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-FailureCode) and [FailureMessage](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-FailureMessage) for details.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | CANCELLING | CANCELLED | FAILED`
Required: No

 ** BulkOperationUsage **   <a name="DDB-Type-BulkOperationDescription-BulkOperationUsage"></a>
Usage information for the table and its indexes.
Type: Array of [BulkOperationUsage](API_BulkOperationUsage.md) objects
Required: No

 ** ClientToken **   <a name="DDB-Type-BulkOperationDescription-ClientToken"></a>
The idempotency token associated with the start request.
Type: String
Pattern: `^[^\$]+$`
Required: No

 ** EndTime **   <a name="DDB-Type-BulkOperationDescription-EndTime"></a>
The time when the operation reached a terminal status. DynamoDB omits this value while the operation remains in progress.
Type: Timestamp
Required: No

 ** FailedItemCount **   <a name="DDB-Type-BulkOperationDescription-FailedItemCount"></a>
The number of processed input items that failed because of parsing or validation errors. This count is included in `ProcessedItemCount`. Condition-check failures do not increase this count.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** FailureCode **   <a name="DDB-Type-BulkOperationDescription-FailureCode"></a>
A code that identifies why the bulk operation failed or was cancelled. DynamoDB returns this value only when `BulkOperationStatus` is `FAILED` or `CANCELLED`.
Type: String
Required: No

 ** FailureMessage **   <a name="DDB-Type-BulkOperationDescription-FailureMessage"></a>
A message that describes why the bulk operation failed or was cancelled. DynamoDB returns this value only when `BulkOperationStatus` is `FAILED` or `CANCELLED`.
Type: String
Required: No

 ** InputS3Configuration **   <a name="DDB-Type-BulkOperationDescription-InputS3Configuration"></a>
The Amazon S3 input configuration associated with the bulk operation.
Type: [InputS3Configuration](API_InputS3Configuration.md) object
Required: No

 ** MaxWriteRequestUnits **   <a name="DDB-Type-BulkOperationDescription-MaxWriteRequestUnits"></a>
The maximum write request unit rate configured for the bulk operation.
Type: Long
Valid Range: Minimum value of 1024.
Required: No

 ** OutputS3Configuration **   <a name="DDB-Type-BulkOperationDescription-OutputS3Configuration"></a>
The Amazon S3 output configuration associated with the bulk operation.
Type: [OutputS3Configuration](API_OutputS3Configuration.md) object
Required: No

 ** PerformanceTier **   <a name="DDB-Type-BulkOperationDescription-PerformanceTier"></a>
The performance tier selected for the bulk operation. Valid values are `STANDARD` and `ACCELERATED`. If the start request omitted this value, DynamoDB uses `STANDARD`.
Type: String
Valid Values: `STANDARD | ACCELERATED`
Required: No

 ** ProcessedInputBytes **   <a name="DDB-Type-BulkOperationDescription-ProcessedInputBytes"></a>
The number of bytes that DynamoDB has read from the Amazon S3 input objects.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ProcessedItemCount **   <a name="DDB-Type-BulkOperationDescription-ProcessedItemCount"></a>
The number of input items that DynamoDB has processed. This count includes successful writes, parsing or validation failures, and condition-check failures.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** StartTime **   <a name="DDB-Type-BulkOperationDescription-StartTime"></a>
The time when DynamoDB accepted the start request.
Type: Timestamp
Required: No

 ** TableDetails **   <a name="DDB-Type-BulkOperationDescription-TableDetails"></a>
A list containing identifying information for the table targeted by the bulk operation.
Type: Array of [BulkOperationTableDetail](API_BulkOperationTableDetail.md) objects
Required: No

 ** TotalInputBytes **   <a name="DDB-Type-BulkOperationDescription-TotalInputBytes"></a>
The total size, in bytes, of the Amazon S3 input objects. DynamoDB omits this value until the initial input-size calculation completes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_BulkOperationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BulkOperationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BulkOperationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BulkOperationDescription)

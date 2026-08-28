---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatchRequestEntry.html
---

# ChangeMessageVisibilityBatchRequestEntry
<a name="API_ChangeMessageVisibilityBatchRequestEntry"></a>

Encloses a receipt handle and an entry ID for each message in ` ChangeMessageVisibilityBatch.`

## Contents
<a name="API_ChangeMessageVisibilityBatchRequestEntry_Contents"></a>

 ** Id **   <a name="SQS-Type-ChangeMessageVisibilityBatchRequestEntry-Id"></a>
An identifier for this particular receipt handle used to communicate the result.
The `Id`s of a batch request need to be unique within a request.
This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (\_).
Type: String
Required: Yes

 ** ReceiptHandle **   <a name="SQS-Type-ChangeMessageVisibilityBatchRequestEntry-ReceiptHandle"></a>
A receipt handle.
Type: String
Required: Yes

 ** VisibilityTimeout **   <a name="SQS-Type-ChangeMessageVisibilityBatchRequestEntry-VisibilityTimeout"></a>
The new value (in seconds) for the message's visibility timeout.
Type: Integer
Required: No

## See Also
<a name="API_ChangeMessageVisibilityBatchRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ChangeMessageVisibilityBatchRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ChangeMessageVisibilityBatchRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ChangeMessageVisibilityBatchRequestEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

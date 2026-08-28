---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatchResponseEntry.html
---

# PutRecordBatchResponseEntry
<a name="API_PutRecordBatchResponseEntry"></a>

Contains the result for an individual record from a [PutRecordBatch](API_PutRecordBatch.md) request. If the record is successfully added to your Firehose stream, it receives a record ID. If the record fails to be added to your Firehose stream, the result includes an error code and an error message.

## Contents
<a name="API_PutRecordBatchResponseEntry_Contents"></a>

 ** ErrorCode **   <a name="Firehose-Type-PutRecordBatchResponseEntry-ErrorCode"></a>
The error code for an individual record result.
Type: String
Required: No

 ** ErrorMessage **   <a name="Firehose-Type-PutRecordBatchResponseEntry-ErrorMessage"></a>
The error message for an individual record result.
Type: String
Required: No

 ** RecordId **   <a name="Firehose-Type-PutRecordBatchResponseEntry-RecordId"></a>
The ID of the record.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_PutRecordBatchResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/PutRecordBatchResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/PutRecordBatchResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/PutRecordBatchResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecordsResultEntry.html
---

# PutRecordsResultEntry
<a name="API_PutRecordsResultEntry"></a>

Represents the result of an individual record from a `PutRecords` request. A record that is successfully added to a stream includes `SequenceNumber` and `ShardId` in the result. A record that fails to be added to the stream includes `ErrorCode` and `ErrorMessage` in the result.

## Contents
<a name="API_PutRecordsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="Streams-Type-PutRecordsResultEntry-ErrorCode"></a>
The error code for an individual record result. `ErrorCodes` can be either `ProvisionedThroughputExceededException` or `InternalFailure`.
Type: String
Required: No

 ** ErrorMessage **   <a name="Streams-Type-PutRecordsResultEntry-ErrorMessage"></a>
The error message for an individual record result. An `ErrorCode` value of `ProvisionedThroughputExceededException` has an error message that includes the account ID, stream name, and shard ID. An `ErrorCode` value of `InternalFailure` has the error message `"Internal Service Failure"`.
Type: String
Required: No

 ** SequenceNumber **   <a name="Streams-Type-PutRecordsResultEntry-SequenceNumber"></a>
The sequence number for an individual record result.
Type: String
Pattern: `0|([1-9]\d{0,128})`
Required: No

 ** ShardId **   <a name="Streams-Type-PutRecordsResultEntry-ShardId"></a>
The shard ID for an individual record result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_PutRecordsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/PutRecordsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/PutRecordsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/PutRecordsResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

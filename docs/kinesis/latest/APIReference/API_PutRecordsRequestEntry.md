---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecordsRequestEntry.html
---

# PutRecordsRequestEntry
<a name="API_PutRecordsRequestEntry"></a>

Represents the output for `PutRecords`.

## Contents
<a name="API_PutRecordsRequestEntry_Contents"></a>

 ** Data **   <a name="Streams-Type-PutRecordsRequestEntry-Data"></a>
The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 10485760.
Required: Yes

 ** PartitionKey **   <a name="Streams-Type-PutRecordsRequestEntry-PartitionKey"></a>
Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ExplicitHashKey **   <a name="Streams-Type-PutRecordsRequestEntry-ExplicitHashKey"></a>
The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.
Type: String
Pattern: `^(0|([1-9]\d{0,38}))$`
Required: No

## See Also
<a name="API_PutRecordsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/PutRecordsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/PutRecordsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/PutRecordsRequestEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

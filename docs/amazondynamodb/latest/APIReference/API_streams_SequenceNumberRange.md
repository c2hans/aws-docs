---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_SequenceNumberRange.html
---

# SequenceNumberRange
<a name="API_streams_SequenceNumberRange"></a>

The beginning and ending sequence numbers for the stream records contained within a shard.

## Contents
<a name="API_streams_SequenceNumberRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EndingSequenceNumber **   <a name="DDB-Type-streams_SequenceNumberRange-EndingSequenceNumber"></a>
The last sequence number for the stream records contained within a shard. String contains numeric characters only.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 40.
Required: No

 ** StartingSequenceNumber **   <a name="DDB-Type-streams_SequenceNumberRange-StartingSequenceNumber"></a>
The first sequence number for the stream records contained within a shard. String contains numeric characters only.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 40.
Required: No

## See Also
<a name="API_streams_SequenceNumberRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/streams-dynamodb-2012-08-10/SequenceNumberRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/streams-dynamodb-2012-08-10/SequenceNumberRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/streams-dynamodb-2012-08-10/SequenceNumberRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

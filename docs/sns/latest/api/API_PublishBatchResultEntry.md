---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_PublishBatchResultEntry.html
---

# PublishBatchResultEntry
<a name="API_PublishBatchResultEntry"></a>

Encloses data related to a successful message in a batch request for topic.

## Contents
<a name="API_PublishBatchResultEntry_Contents"></a>

 ** Id **
The `Id` of an entry in a batch request.
Type: String
Required: No

 ** MessageId **
An identifier for the message.
Type: String
Required: No

 ** SequenceNumber **
This parameter applies only to FIFO (first-in-first-out) topics.
The large, non-consecutive number that Amazon SNS assigns to each message.
The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to increase for a particular `MessageGroupId`.
Type: String
Required: No

## See Also
<a name="API_PublishBatchResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/PublishBatchResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/PublishBatchResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/PublishBatchResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

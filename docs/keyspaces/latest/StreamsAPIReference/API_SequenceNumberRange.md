---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_SequenceNumberRange.html
---

# SequenceNumberRange
<a name="API_SequenceNumberRange"></a>

Defines a range of sequence numbers within a change data capture stream's shard for Amazon Keyspaces.

## Contents
<a name="API_SequenceNumberRange_Contents"></a>

 ** endingSequenceNumber **   <a name="keyspaces-Type-SequenceNumberRange-endingSequenceNumber"></a>
The ending sequence number of the range, which may be null for open-ended ranges.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 48.
Required: No

 ** startingSequenceNumber **   <a name="keyspaces-Type-SequenceNumberRange-startingSequenceNumber"></a>
The starting sequence number of the range.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 48.
Required: No

## See Also
<a name="API_SequenceNumberRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/SequenceNumberRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/SequenceNumberRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/SequenceNumberRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

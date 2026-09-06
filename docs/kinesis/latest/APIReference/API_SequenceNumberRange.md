---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SequenceNumberRange.html
---

# SequenceNumberRange
<a name="API_SequenceNumberRange"></a>

The range of possible sequence numbers for the shard.

## Contents
<a name="API_SequenceNumberRange_Contents"></a>

 ** StartingSequenceNumber **   <a name="Streams-Type-SequenceNumberRange-StartingSequenceNumber"></a>
The starting sequence number for the range.
Type: String
Pattern: `^(0|([1-9]\d{0,128}))$`
Required: Yes

 ** EndingSequenceNumber **   <a name="Streams-Type-SequenceNumberRange-EndingSequenceNumber"></a>
The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of `null`.
Type: String
Pattern: `^(0|([1-9]\d{0,128}))$`
Required: No

## See Also
<a name="API_SequenceNumberRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/SequenceNumberRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/SequenceNumberRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/SequenceNumberRange)

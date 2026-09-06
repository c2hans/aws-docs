---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_HashKeyRange.html
---

# HashKeyRange
<a name="API_HashKeyRange"></a>

The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

## Contents
<a name="API_HashKeyRange_Contents"></a>

 ** EndingHashKey **   <a name="Streams-Type-HashKeyRange-EndingHashKey"></a>
The ending hash key of the hash key range.
Type: String
Pattern: `^(0|([1-9]\d{0,38}))$`
Required: Yes

 ** StartingHashKey **   <a name="Streams-Type-HashKeyRange-StartingHashKey"></a>
The starting hash key of the hash key range.
Type: String
Pattern: `^(0|([1-9]\d{0,38}))$`
Required: Yes

## See Also
<a name="API_HashKeyRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/HashKeyRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/HashKeyRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/HashKeyRange)

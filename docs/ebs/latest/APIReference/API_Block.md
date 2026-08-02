---
source_url: https://docs.aws.amazon.com/ebs/latest/APIReference/API_Block.html
---

# Block
<a name="API_Block"></a>

A block of data in an Amazon Elastic Block Store snapshot.

## Contents
<a name="API_Block_Contents"></a>

 ** BlockIndex **   <a name="ebs-Type-Block-BlockIndex"></a>
The block index.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** BlockToken **   <a name="ebs-Type-Block-BlockToken"></a>
The block token for the block index.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9+/=]+$`
Required: No

## See Also
<a name="API_Block_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ebs-2019-11-02/Block)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ebs-2019-11-02/Block)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ebs-2019-11-02/Block)

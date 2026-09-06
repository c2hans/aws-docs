---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TagSet.html
---

# TagSet
<a name="API_TagSet"></a>

A tag set contains tag key and tag value.

## Contents
<a name="API_TagSet_Contents"></a>

 ** key **   <a name="connect-Type-TagSet-key"></a>
The tag key in the TagSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Required: No

 ** value **   <a name="connect-Type-TagSet-value"></a>
The tag value in the tagSet.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_TagSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TagSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TagSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TagSet)

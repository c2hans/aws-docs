---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiTagFilter.html
---

# AmiTagFilter
<a name="API_AmiTagFilter"></a>

A filter that matches Amazon Machine Images (AMIs) by tag key and, optionally, tag value.

## Contents
<a name="API_AmiTagFilter_Contents"></a>

 ** key **   <a name="inspector2-Type-AmiTagFilter-key"></a>
The tag key to match against an AMI's tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="inspector2-Type-AmiTagFilter-value"></a>
The tag value to match against an AMI's tags. If omitted, the filter matches on the tag key alone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_AmiTagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AmiTagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AmiTagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AmiTagFilter)

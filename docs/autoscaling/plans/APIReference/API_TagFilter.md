---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

Represents a tag.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** Key **   <a name="autoscaling-Type-TagFilter-Key"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Values **   <a name="autoscaling-Type-TagFilter-Values"></a>
The tag values (0 to 20).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/TagFilter)

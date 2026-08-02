---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

Used to filter the workflow executions in visibility APIs based on a tag.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** tag **   <a name="SWF-Type-TagFilter-tag"></a>
 Specifies the tag that must be associated with the execution for it to meet the filter criteria.
Tags may only contain unicode letters, digits, whitespace, or these symbols: `_ . : / = + - @`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/TagFilter)

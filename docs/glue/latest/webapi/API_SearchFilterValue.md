---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchFilterValue.html
---

# SearchFilterValue
<a name="API_SearchFilterValue"></a>

A filter value. Exactly one of `stringValue` or `longValue` must be specified.

## Contents
<a name="API_SearchFilterValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** LongValue **   <a name="Glue-Type-SearchFilterValue-LongValue"></a>
A long integer filter value.
Type: Long
Required: No

 ** StringValue **   <a name="Glue-Type-SearchFilterValue-StringValue"></a>
A string filter value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SearchFilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchFilterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchFilterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchFilterValue)

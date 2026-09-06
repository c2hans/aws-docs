---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_StringFilter.html
---

# StringFilter
<a name="API_StringFilter"></a>

An object that describes the details of a string filter.

## Contents
<a name="API_StringFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-StringFilter-comparison"></a>
The operator to use when comparing values in the filter.
Type: String
Valid Values: `EQUALS | PREFIX | NOT_EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-StringFilter-value"></a>
The value to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_StringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/StringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/StringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/StringFilter)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_TagValue.html
---

# TagValue
<a name="API_connect-cases_TagValue"></a>

Object for case tag filter values.

## Contents
<a name="API_connect-cases_TagValue_Contents"></a>

 ** key **   <a name="connect-Type-connect-cases_TagValue-key"></a>
The tag key in the tag filter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]+`
Required: No

 ** value **   <a name="connect-Type-connect-cases_TagValue-value"></a>
The tag value in the tag filter value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([a-zA-Z0-9 _.:/=+\-@]*)`
Required: No

## See Also
<a name="API_connect-cases_TagValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/TagValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/TagValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/TagValue)

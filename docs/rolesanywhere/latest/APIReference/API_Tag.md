---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A label that consists of a key and value you define.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="rolesanywhere-Type-Tag-key"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[ a-zA-Z0-9_.:/=+@-]*`
Required: Yes

 ** value **   <a name="rolesanywhere-Type-Tag-value"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_.:/=+@-]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/Tag)

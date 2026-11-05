---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-contact-lens_TagCondition.html
---

# TagCondition
<a name="API_connect-contact-lens_TagCondition"></a>

A tag condition that consists of a tag key, a tag value, and a comparison operator.

## Contents
<a name="API_connect-contact-lens_TagCondition_Contents"></a>

 ** ComparisonType **   <a name="connect-Type-connect-contact-lens_TagCondition-ComparisonType"></a>
The comparison operator for the tag condition. Valid values: `EQUALS` \| `NOT_EQUALS`.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: No

 ** TagKey **   <a name="connect-Type-connect-contact-lens_TagCondition-TagKey"></a>
The tag key in the tag condition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagValue **   <a name="connect-Type-connect-contact-lens_TagCondition-TagValue"></a>
The tag value in the tag condition.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-contact-lens_TagCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/TagCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/TagCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/TagCondition)

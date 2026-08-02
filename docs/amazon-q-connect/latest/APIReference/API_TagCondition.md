---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_TagCondition.html
---

# TagCondition
<a name="API_amazon-q-connect_TagCondition"></a>

A leaf node condition which can be used to specify a tag condition.

## Contents
<a name="API_amazon-q-connect_TagCondition_Contents"></a>

 ** key **   <a name="connect-Type-amazon-q-connect_TagCondition-key"></a>
The tag key in the tag condition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Required: Yes

 ** value **   <a name="connect-Type-amazon-q-connect_TagCondition-value"></a>
The tag value in the tag condition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_TagCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/TagCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/TagCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/TagCondition)

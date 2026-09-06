---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceTag.html
---

# ResourceTag
<a name="API_ResourceTag"></a>

The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value. If you add more than one tag to a policy, you can specify whether to combine them using the logical AND operator or the logical OR operator. For more information, see [Working with Tag Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html).

Every resource tag must have a string value, either a non-empty string or an empty string. If you don't provide a value for a resource tag, Firewall Manager saves the value as an empty string: "". When Firewall Manager compares tags, it only matches two tags if they have the same key and the same value. A tag with an empty string value only matches with tags that also have an empty string value.

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** Key **   <a name="fms-Type-ResourceTag-Key"></a>
The resource tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@*\\]*)$`
Required: Yes

 ** Value **   <a name="fms-Type-ResourceTag-Value"></a>
The resource tag value. To specify an empty string value, either don't provide this or specify it as "".
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@*\\]*)$`
Required: No

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ResourceTag)

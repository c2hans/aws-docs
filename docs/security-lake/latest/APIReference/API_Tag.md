---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A *tag* is a label that you can define and associate with AWS resources, including certain types of Amazon Security Lake resources. Tags can help you identify, categorize, and manage resources in different ways, such as by owner, environment, or other criteria. You can associate tags with the following types of Security Lake resources: subscribers, and the data lake configuration for your AWS account in individual AWS Regions.

A resource can have up to 50 tags. Each tag consists of a required *tag key* and an associated *tag value*. A *tag key* is a general label that acts as a category for a more specific tag value. Each tag key must be unique and it can have only one tag value. A *tag value* acts as a descriptor for a tag key. Tag keys and values are case sensitive. They can contain letters, numbers, spaces, or the following symbols: \_ . : / = \+ @ -

For more information, see [Tagging Amazon Security Lake resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html) in the *Amazon Security Lake User Guide*.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="securitylake-Type-Tag-key"></a>
The name of the tag. This is a general label that acts as a category for a more specific tag value (`value`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="securitylake-Type-Tag-value"></a>
The value that’s associated with the specified tag key (`key`). This value acts as a descriptor for the tag key. A tag value cannot be null, but it can be an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

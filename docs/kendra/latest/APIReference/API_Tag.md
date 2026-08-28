---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource. TA tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="kendra-Type-Tag-Key"></a>
The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Value **   <a name="kendra-Type-Tag-Value"></a>
The value associated with the tag. The value may be an empty string but it can't be null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

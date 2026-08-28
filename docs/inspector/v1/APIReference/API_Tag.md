---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key and value pair. This data type is used as a request parameter in the [SetTagsForResource](API_SetTagsForResource.md) action and a response element in the [ListTagsForResource](API_ListTagsForResource.md) action.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="Inspector-Type-Tag-key"></a>
A tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="Inspector-Type-Tag-value"></a>
A value assigned to a tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

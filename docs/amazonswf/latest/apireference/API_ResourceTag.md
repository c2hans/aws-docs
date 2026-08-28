---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ResourceTag.html
---

# ResourceTag
<a name="API_ResourceTag"></a>

Tags are key-value pairs that can be associated with Amazon SWF state machines and activities.

Tags may only contain unicode letters, digits, whitespace, or these symbols: `_ . : / = + - @`.

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** key **   <a name="SWF-Type-ResourceTag-key"></a>
The key of a tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="SWF-Type-ResourceTag-value"></a>
The value of a tag.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ResourceTag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CustomEntityType.html
---

# CustomEntityType
<a name="API_CustomEntityType"></a>

An object representing a custom pattern for detecting sensitive data across the columns and rows of your structured data.

## Contents
<a name="API_CustomEntityType_Contents"></a>

 ** Name **   <a name="Glue-Type-CustomEntityType-Name"></a>
A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** RegexString **   <a name="Glue-Type-CustomEntityType-RegexString"></a>
A regular expression string that is used for detecting sensitive data in a custom pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** ContextWords **   <a name="Glue-Type-CustomEntityType-ContextWords"></a>
A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.
If no context words are passed only a regular expression is checked.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_CustomEntityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CustomEntityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CustomEntityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CustomEntityType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

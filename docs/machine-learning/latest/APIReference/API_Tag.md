---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A custom key-value pair associated with an ML object, such as an ML model.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="amazonml-Type-Tag-Key"></a>
A unique identifier for the tag. Valid characters include Unicode letters, digits, white space, \_, ., /, =, \+, -, %, and @.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Value **   <a name="amazonml-Type-Tag-Value"></a>
An optional string, typically used to describe or define the tag. Valid characters include Unicode letters, digits, white space, \_, ., /, =, \+, -, %, and @.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

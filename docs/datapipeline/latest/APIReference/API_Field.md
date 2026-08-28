---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Field.html
---

# Field
<a name="API_Field"></a>

A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (`StringValue`) or a reference to another object (`RefValue`) but not as both.

## Contents
<a name="API_Field_Contents"></a>

 ** key **   <a name="DP-Type-Field-key"></a>
The field identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** refValue **   <a name="DP-Type-Field-refValue"></a>
The field value, expressed as the identifier of another object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** stringValue **   <a name="DP-Type-Field-stringValue"></a>
The field value, expressed as a String.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/Field)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

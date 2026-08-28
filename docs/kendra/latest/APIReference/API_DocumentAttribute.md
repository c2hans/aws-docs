---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttribute.html
---

# DocumentAttribute
<a name="API_DocumentAttribute"></a>

A document attribute or metadata field. To create custom document attributes, see [Custom attributes](https://docs.aws.amazon.com/kendra/latest/dg/custom-attributes.html).

## Contents
<a name="API_DocumentAttribute_Contents"></a>

 ** Key **   <a name="kendra-Type-DocumentAttribute-Key"></a>
The identifier for the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: Yes

 ** Value **   <a name="kendra-Type-DocumentAttribute-Value"></a>
The value of the attribute.
Type: [DocumentAttributeValue](API_DocumentAttributeValue.md) object
Required: Yes

## See Also
<a name="API_DocumentAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DocumentAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DocumentAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DocumentAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_AdditionalResultAttribute.html
---

# AdditionalResultAttribute
<a name="API_AdditionalResultAttribute"></a>

An attribute returned from an index query.

## Contents
<a name="API_AdditionalResultAttribute_Contents"></a>

 ** Key **   <a name="kendra-Type-AdditionalResultAttribute-Key"></a>
The key that identifies the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Value **   <a name="kendra-Type-AdditionalResultAttribute-Value"></a>
An object that contains the attribute value.
Type: [AdditionalResultAttributeValue](API_AdditionalResultAttributeValue.md) object
Required: Yes

 ** ValueType **   <a name="kendra-Type-AdditionalResultAttribute-ValueType"></a>
The data type of the `Value` property.
Type: String
Valid Values: `TEXT_WITH_HIGHLIGHTS_VALUE`
Required: Yes

## See Also
<a name="API_AdditionalResultAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/AdditionalResultAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/AdditionalResultAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/AdditionalResultAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

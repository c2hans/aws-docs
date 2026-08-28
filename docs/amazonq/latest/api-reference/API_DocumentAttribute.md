---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttribute.html
---

# DocumentAttribute
<a name="API_DocumentAttribute"></a>

A document attribute or metadata field.

## Contents
<a name="API_DocumentAttribute_Contents"></a>

 ** name **   <a name="qbusiness-Type-DocumentAttribute-name"></a>
The identifier for the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: Yes

 ** value **   <a name="qbusiness-Type-DocumentAttribute-value"></a>
The value of the attribute.
Type: [DocumentAttributeValue](API_DocumentAttributeValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_DocumentAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

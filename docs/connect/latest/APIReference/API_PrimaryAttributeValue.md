---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PrimaryAttributeValue.html
---

# PrimaryAttributeValue
<a name="API_PrimaryAttributeValue"></a>

A primary attribute value.

## Contents
<a name="API_PrimaryAttributeValue_Contents"></a>

 ** AccessType **   <a name="connect-Type-PrimaryAttributeValue-AccessType"></a>
The value's access type.
Type: String
Valid Values: `ALLOW`
Required: No

 ** AttributeName **   <a name="connect-Type-PrimaryAttributeValue-AttributeName"></a>
The value's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `(?!aws:|connect:)[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+$`
Required: No

 ** Values **   <a name="connect-Type-PrimaryAttributeValue-Values"></a>
The value's values.
Type: Array of strings
Array Members: Maximum number of 2 items.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+$`
Required: No

## See Also
<a name="API_PrimaryAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PrimaryAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PrimaryAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PrimaryAttributeValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

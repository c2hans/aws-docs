---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PrimaryAttributeValueFilter.html
---

# PrimaryAttributeValueFilter
<a name="API_PrimaryAttributeValueFilter"></a>

A primary attribute value filter.

## Contents
<a name="API_PrimaryAttributeValueFilter_Contents"></a>

 ** AttributeName **   <a name="connect-Type-PrimaryAttributeValueFilter-AttributeName"></a>
The filter's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** Values **   <a name="connect-Type-PrimaryAttributeValueFilter-Values"></a>
The filter's values.
Type: Array of strings
Required: Yes

## See Also
<a name="API_PrimaryAttributeValueFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PrimaryAttributeValueFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PrimaryAttributeValueFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PrimaryAttributeValueFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PrimaryValue.html
---

# PrimaryValue
<a name="API_PrimaryValue"></a>

Represents a primary key value used to identify a specific record in a data table. Primary values are used in combination to create unique record identifiers when a table has multiple primary attributes.

## Contents
<a name="API_PrimaryValue_Contents"></a>

 ** AttributeName **   <a name="connect-Type-PrimaryValue-AttributeName"></a>
The name of the primary attribute that this value belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** Value **   <a name="connect-Type-PrimaryValue-Value"></a>
The actual value for the primary attribute. Must be provided as a string regardless of the attribute's value type. Primary values cannot be expressions and must be explicitly specified.
Type: String
Required: Yes

## See Also
<a name="API_PrimaryValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PrimaryValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PrimaryValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PrimaryValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

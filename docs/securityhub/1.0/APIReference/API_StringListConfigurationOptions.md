---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StringListConfigurationOptions.html
---

# StringListConfigurationOptions
<a name="API_StringListConfigurationOptions"></a>

 The options for customizing a security control parameter that is a list of strings.

## Contents
<a name="API_StringListConfigurationOptions_Contents"></a>

 ** DefaultValue **   <a name="securityhub-Type-StringListConfigurationOptions-DefaultValue"></a>
 The Security Hub CSPM default value for a control parameter that is a list of strings.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ExpressionDescription **   <a name="securityhub-Type-StringListConfigurationOptions-ExpressionDescription"></a>
 The description of the RE2 regular expression.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MaxItems **   <a name="securityhub-Type-StringListConfigurationOptions-MaxItems"></a>
 The maximum number of list items that a string list control parameter can accept.
Type: Integer
Required: No

 ** Re2Expression **   <a name="securityhub-Type-StringListConfigurationOptions-Re2Expression"></a>
 An RE2 regular expression that Security Hub CSPM uses to validate a user-provided list of strings for a control parameter.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StringListConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StringListConfigurationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StringListConfigurationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StringListConfigurationOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

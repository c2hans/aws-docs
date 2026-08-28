---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StringConfigurationOptions.html
---

# StringConfigurationOptions
<a name="API_StringConfigurationOptions"></a>

 The options for customizing a security control parameter that is a string.

## Contents
<a name="API_StringConfigurationOptions_Contents"></a>

 ** DefaultValue **   <a name="securityhub-Type-StringConfigurationOptions-DefaultValue"></a>
 The Security Hub CSPM default value for a control parameter that is a string.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExpressionDescription **   <a name="securityhub-Type-StringConfigurationOptions-ExpressionDescription"></a>
 The description of the RE2 regular expression.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Re2Expression **   <a name="securityhub-Type-StringConfigurationOptions-Re2Expression"></a>
 An RE2 regular expression that Security Hub CSPM uses to validate a user-provided control parameter string.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StringConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StringConfigurationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StringConfigurationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StringConfigurationOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

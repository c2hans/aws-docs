---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BlockedPhrasesConfigurationUpdate.html
---

# BlockedPhrasesConfigurationUpdate
<a name="API_BlockedPhrasesConfigurationUpdate"></a>

Updates a blocked phrases configuration in your Amazon Q Business application.

## Contents
<a name="API_BlockedPhrasesConfigurationUpdate_Contents"></a>

 ** blockedPhrasesToCreateOrUpdate **   <a name="qbusiness-Type-BlockedPhrasesConfigurationUpdate-blockedPhrasesToCreateOrUpdate"></a>
Creates or updates a blocked phrases configuration in your Amazon Q Business application.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 36.
Pattern: `\P{C}*`
Required: No

 ** blockedPhrasesToDelete **   <a name="qbusiness-Type-BlockedPhrasesConfigurationUpdate-blockedPhrasesToDelete"></a>
Deletes a blocked phrases configuration in your Amazon Q Business application.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 36.
Pattern: `\P{C}*`
Required: No

 ** systemMessageOverride **   <a name="qbusiness-Type-BlockedPhrasesConfigurationUpdate-systemMessageOverride"></a>
The configured custom message displayed to your end user when they use blocked phrase during chat.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_BlockedPhrasesConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/BlockedPhrasesConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/BlockedPhrasesConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/BlockedPhrasesConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

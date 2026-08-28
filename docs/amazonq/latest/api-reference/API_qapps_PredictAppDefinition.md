---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictAppDefinition.html
---

# PredictAppDefinition
<a name="API_qapps_PredictAppDefinition"></a>

The definition of an Amazon Q App generated based on input such as a conversation or problem statement.

## Contents
<a name="API_qapps_PredictAppDefinition_Contents"></a>

 ** appDefinition **   <a name="qbusiness-Type-qapps_PredictAppDefinition-appDefinition"></a>
The definition specifying the cards and flow of the generated Q App.
Type: [AppDefinitionInput](API_qapps_AppDefinitionInput.md) object
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_PredictAppDefinition-title"></a>
The title of the generated Q App definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** description **   <a name="qbusiness-Type-qapps_PredictAppDefinition-description"></a>
The description of the generated Q App definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_qapps_PredictAppDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/PredictAppDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/PredictAppDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/PredictAppDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

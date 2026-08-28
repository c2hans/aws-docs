---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictQAppInputOptions.html
---

# PredictQAppInputOptions
<a name="API_qapps_PredictQAppInputOptions"></a>

The input options for generating an Q App definition.

## Contents
<a name="API_qapps_PredictQAppInputOptions_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conversation **   <a name="qbusiness-Type-qapps_PredictQAppInputOptions-conversation"></a>
A conversation to use as input for generating the Q App definition.
Type: Array of [ConversationMessage](API_qapps_ConversationMessage.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** problemStatement **   <a name="qbusiness-Type-qapps_PredictQAppInputOptions-problemStatement"></a>
A problem statement to use as input for generating the Q App definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: No

## See Also
<a name="API_qapps_PredictQAppInputOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/PredictQAppInputOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/PredictQAppInputOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/PredictQAppInputOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UserTurnOutputSpecification.html
---

# UserTurnOutputSpecification
<a name="API_UserTurnOutputSpecification"></a>

Contains results that are output for the user turn by the test execution.

## Contents
<a name="API_UserTurnOutputSpecification_Contents"></a>

 ** intent **   <a name="lexv2-Type-UserTurnOutputSpecification-intent"></a>
Contains information about the intent.
Type: [UserTurnIntentOutput](API_UserTurnIntentOutput.md) object
Required: Yes

 ** activeContexts **   <a name="lexv2-Type-UserTurnOutputSpecification-activeContexts"></a>
The contexts that are active in the turn.
Type: Array of [ActiveContext](API_ActiveContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** transcript **   <a name="lexv2-Type-UserTurnOutputSpecification-transcript"></a>
The transcript that is output for the user turn by the test execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_UserTurnOutputSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UserTurnOutputSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UserTurnOutputSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UserTurnOutputSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

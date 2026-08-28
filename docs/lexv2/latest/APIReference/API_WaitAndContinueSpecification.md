---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_WaitAndContinueSpecification.html
---

# WaitAndContinueSpecification
<a name="API_WaitAndContinueSpecification"></a>

Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

## Contents
<a name="API_WaitAndContinueSpecification_Contents"></a>

 ** continueResponse **   <a name="lexv2-Type-WaitAndContinueSpecification-continueResponse"></a>
The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: Yes

 ** waitingResponse **   <a name="lexv2-Type-WaitAndContinueSpecification-waitingResponse"></a>
The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: Yes

 ** active **   <a name="lexv2-Type-WaitAndContinueSpecification-active"></a>
Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot aren't used. If the `active` field isn't specified, the default is true.
Type: Boolean
Required: No

 ** stillWaitingResponse **   <a name="lexv2-Type-WaitAndContinueSpecification-stillWaitingResponse"></a>
A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.
Type: [StillWaitingResponseSpecification](API_StillWaitingResponseSpecification.md) object
Required: No

## See Also
<a name="API_WaitAndContinueSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/WaitAndContinueSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/WaitAndContinueSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/WaitAndContinueSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

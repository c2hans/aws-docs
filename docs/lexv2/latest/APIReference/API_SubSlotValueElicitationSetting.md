---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SubSlotValueElicitationSetting.html
---

# SubSlotValueElicitationSetting
<a name="API_SubSlotValueElicitationSetting"></a>

Subslot elicitation settings.

 `DefaultValueSpecification` is a list of default values for a constituent sub slot in a composite slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values. This is similar to `DefaultValueSpecification` for slots.

 `PromptSpecification` is the prompt that Amazon Lex uses to elicit the sub slot value from the user. This is similar to `PromptSpecification` for slots.

## Contents
<a name="API_SubSlotValueElicitationSetting_Contents"></a>

 ** promptSpecification **   <a name="lexv2-Type-SubSlotValueElicitationSetting-promptSpecification"></a>
Specifies a list of message groups that Amazon Lex sends to a user to elicit a response.
Type: [PromptSpecification](API_PromptSpecification.md) object
Required: Yes

 ** defaultValueSpecification **   <a name="lexv2-Type-SubSlotValueElicitationSetting-defaultValueSpecification"></a>
Defines a list of values that Amazon Lex should use as the default value for a slot.
Type: [SlotDefaultValueSpecification](API_SlotDefaultValueSpecification.md) object
Required: No

 ** sampleUtterances **   <a name="lexv2-Type-SubSlotValueElicitationSetting-sampleUtterances"></a>
If you know a specific pattern that users might respond to an Amazon Lex request for a sub slot value, you can provide those utterances to improve accuracy. This is optional. In most cases Amazon Lex is capable of understanding user utterances. This is similar to `SampleUtterances` for slots.
Type: Array of [SampleUtterance](API_SampleUtterance.md) objects
Required: No

 ** waitAndContinueSpecification **   <a name="lexv2-Type-SubSlotValueElicitationSetting-waitAndContinueSpecification"></a>
Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.
Type: [WaitAndContinueSpecification](API_WaitAndContinueSpecification.md) object
Required: No

## See Also
<a name="API_SubSlotValueElicitationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SubSlotValueElicitationSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SubSlotValueElicitationSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SubSlotValueElicitationSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

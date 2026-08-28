---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DialogAction.html
---

# DialogAction
<a name="API_runtime_DialogAction"></a>

The next action that Amazon Lex should take.

## Contents
<a name="API_runtime_DialogAction_Contents"></a>

 ** type **   <a name="lexv2-Type-runtime_DialogAction-type"></a>
The next action that the bot should take in its interaction with the user. The following values are possible:
+  `Close` – Indicates that there will not be a response from the user. For example, the statement "Your order has been placed" does not require a response.
+  `ConfirmIntent` – The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as "Place the order?"
+  `Delegate` – The next action is determined by Amazon Lex.
+  `ElicitIntent` – The next action is to elicit an intent from the user.
+  `ElicitSlot` – The next action is to elicit a slot value from the user.
Type: String
Valid Values: `Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot | None`
Required: Yes

 ** slotElicitationStyle **   <a name="lexv2-Type-runtime_DialogAction-slotElicitationStyle"></a>
Configures the slot to use spell-by-letter or spell-by-word style. When you use a style on a slot, users can spell out their input to make it clear to your bot.
+ Spell by letter - "b" "o" "b"
+ Spell by word - "b as in boy" "o as in oscar" "b as in boy"
For more information, see [ Using spelling to enter slot values ](https://docs.aws.amazon.com/lexv2/latest/dg/spelling-styles.html).
Type: String
Valid Values: `Default | SpellByLetter | SpellByWord`
Required: No

 ** slotToElicit **   <a name="lexv2-Type-runtime_DialogAction-slotToElicit"></a>
The name of the slot that should be elicited from the user.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** subSlotToElicit **   <a name="lexv2-Type-runtime_DialogAction-subSlotToElicit"></a>
The name of the constituent sub slot of the composite slot specified in slotToElicit that should be elicited from the user.
Type: [ElicitSubSlot](API_runtime_ElicitSubSlot.md) object
Required: No

## See Also
<a name="API_runtime_DialogAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/DialogAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/DialogAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/DialogAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

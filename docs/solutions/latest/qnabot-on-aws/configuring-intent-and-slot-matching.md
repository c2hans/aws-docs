---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/configuring-intent-and-slot-matching.html
---

# Configuring intent and slot matching
<a name="configuring-intent-and-slot-matching"></a>

The guidance supports different types of question and answer workflows. For example:
+ You can create a question and answer experience to help answer frequently asked questions. In this model, the user asks a question and QnABot on AWS responds with the most relevant answer to the question (from the list of created Item IDs). For more information, see [Step 3. Populate the chatbot with your questions and answers](step-3-populate-the-chatbot-with-your-questions-and-answers.md).
+ Build a diagnostic or questionnaire-based workflow, where a question from a user can result with QnABot on AWS asking follow-up questions. If you are creating a survey or building a diagnostic workflow where you may require inputs to different questions, you can use the `ResponseBots` and `Document Chaining` capabilities of QnABot on AWS. For more information, see [Configuring the chatbot to ask the questions and use response bots](configuring-the-chatbot-to-ask-the-questions-and-use-response-bots.md).

Both of these options provide flexibility in creating an interactive chat experience. For example:
+ Accepting dynamic user input in a question.
+ Automatically asking a question for a given input without needing to setup document chaining.
+ Validating user input against an available list of options.

With this early implementation of the intent and slot matching capability in QnABot on AWS, you can now build a richer conversational experiences. For example, you might create an intent that makes a car reservation, or assists an agent during a live chat or call (via Amazon Connect). You can use intent and slot matching also for cases where you might want better intent matching via Amazon Lex NLU engine, as an alternative to QnABot on AWS default OpenSearch Service queries.

**Note**
The intent and slot matching capability in QnABot on AWS was initially implemented in version 5.2.0. The content and step-by-step procedures in this section apply to QnABot on AWS versions 5.2.0 and later.

## Item ID setup
<a name="item-id-setup"></a>

The **Item ID** setup is made of the following attributes:
+  **Intent** Represents an action that the user wants to perform. For each intent, provide the following required information:
  +  **Intent name** Descriptive name for the intent by providing an Item ID, for example, `IntentSlotMatching.Example.Q1`.
  +  **Sample utterances** The intent a user might convey. For example, a user might say, *"book a car"* or *"make a car reservation"*.
+  **Slot** An intent can require zero or more slots, or parameters. You add slots as part of the Item ID configuration. At runtime, Amazon Lex V2 prompts the user for specific slot values. The user must provide values for all required slots before Amazon Lex V2 can fulfill the intent.
+  **Slot type** Define the values that users can supply for your intent slots. Each slot has a type. You can create your own slot type, or you can use [built-in slot types](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slots.html).

## Creating custom intent with slots and slot types
<a name="creating-custom-intent-with-slots-and-slot-types"></a>

To create a custom intend with slots and slot types:

1. Create a QnABot question as you would normally do by providing an Item ID and questions/utterances.

1. Expand the **Advanced** option.

1. Select the option for **Create a dedicated bot intent for this item** during LEX REBUILD.

Slots can be configured to be either required or optional. If a conversation flow requires user input, choose the **Slot required** option.

For each slot, provide the slot type and one or more prompts that Amazon Lex V2 sends to the client to elicit values from the user. A user can reply with a slot value when input might be needed. You can create your own custom slot type, or you can use [built-in slot types](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slots.html).

 **Intent and slot configuration**

![image19](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image19.png)

Additional **Slots** attributes:
+  **Cache slot value for re-use during a session**? The slot value can be stored in session variables and accessed via **qnabotcontext.slots.slotName**. When a slot value is stored in a session attribute, it is used automatically as the value for other slots with the same name without reprompting the user. This can be beneficial when you are capturing a user’s profile information to support different conversational workflows, and don’t want to ask the same profile information again from the user.
+  **Slot sample utterances** A slot can also include optional sample utterances. These are phrases that a user might use to provide the slot value. A comprehensive set of pre-defined utterances is included (via built-in slot type or a custom slot type). You can add more if required. In most cases, Amazon Lex can understand user utterances. If you know a specific pattern that users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. In most cases, you won’t need to provide any utterances.

## Creating custom slot types
<a name="creating-custom-slot-types"></a>

In addition to using built-in slot types, you can also create custom slot types. If an intent requires a custom slot type, you can create a custom slot type by creating a new item and choosing the type **slottype**. Similar to built-in slot types, a custom slot type can be used across more than one intent.
+  **Slot type values** - The values for the slot. If you chose `Restrict to` slot values, you can add synonyms for the value. For example, for the value `football` you can add the synonym `soccer`. If the user enters `soccer` in a conversation with your bot, the actual value of the slot is `football`.
+  **Slot value resolution** - Determines how slot values are resolved. If you don’t choose `Restrict to` slot values, Amazon Lex V2 uses the values as representative values for training. If you choose `Restrict to` slot values, the allowed values for the slot are restricted to the ones that you provide.

   **Creating a custom slot type**
![image20](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image20.png)

## Accessing slot values
<a name="accessing-slot-values"></a>

To support a conversational experience, you might want to:
+ Display what the user provided as slot values, such as workflows that require confirming user input.
+ Use the slot values to support conditional branching via document chaining.
+ Display a summary such as an order summary.

There are several ways to access slot values within an Item ID and/or Lambda hook. Using Handlebars you can access slot values using:
+  **getSlot** - A new helper function that returns named slot value if it is defined, or default value. For example: `{{getSlot 'slotName' 'default'}}`.
+  **Session attribute {{qnabotcontext.slots.*slotName*}}** - A value in a session attribute, where `_slotName_` is the name of the slot defined in an Item ID. If the slot value is cached for re-use, the value is available in a session attribute, and can be used across Item IDs.
+  **{{Slots.*slotName*}}** - A slot name, where `_slotName_` is the name of the slot defined in an Item ID.

## Import sample intent and slot types
<a name="import-sample-intent-and-slot-types"></a>

In the QnABot content designer, select the **Tools** menu link on the top left and select **Import**. From the **Examples/Extensions** section, select **Load** for **IntentSlotMatching** to load sample intent and slot types. This example imports:
+  **IntentSlotMatching.Example.Q1** - An Item ID of type **qna** with custom intent and slot.
+  **IntentSlotMatching\_Example\_slottype\_CarType** and **IntentSlotMatching\_Example\_slottype\_Confirmation** Item ID of type `slottype` with sample slot values.

## Lex rebuild
<a name="lex-rebuild"></a>

Once you have loaded the questions, choose **Edit** from the Tools menu and choose **LEX REBUILD** from the top right edit card menu (⋮). This re-trains Amazon Lex using the newly added questions as training data.

## Testing the experience
<a name="testing-the-experience"></a>

On the **Tools** menu and choose **QnABot Client** from the options. Try the following conversation flow:

```
User: Book a car
 Bot: In what city do you need to rent a car?

 User: Seattle
 Bot: What day do you want to start your rental?

 User: Today
 Bot: What day do you want to return this car?

 User: Next Sunday
 Bot: What type of car would you like to rent? Our most popular options are economy, midsize, and luxury.

 User: Economy
 Bot: Okay, should I go ahead and book the reservation?

 User: Yes
 Bot: Okay, I have confirmed your reservation. The reservation details are below:
      Car Type: economy
      Pick up City: Seattle
      Pick up Date: 2022-05-30
      Return Date: 2022-06-12
```

## Notes and considerations
<a name="notes-and-considerations"></a>
+ Utterances must be unique across intents. Duplicate utterances across intents will cause the Amazon Lex build to fail. Suppose you have two intents `OrderPizza` and `OrderDrink` in your bot and both are configured with an `I want to order` utterance. This utterance does not map to a specific intent that Amazon Lex V2 can learn from while building the language model for the bot at build time. As a result, when a user inputs this utterance at runtime, Amazon Lex V2 can’t pick an intent with a high degree of confidence.
+  `Topics` and `ClientFilters` are not supported when an Item ID is activated with custom intent.
+ Bot locale must be set to user’s locale for QnABot on AWS multi-language text interactions.
+ Always initiate a LEX REBUILD when activating Item IDs with custom intent and slots. This creates the custom intents, slots, and slot types in Amazon Lex V2, and also trains Amazon Lex using the added/updated Item IDs as training data.
+ To take advantage of the additional features supported by Amazon Lex, such as confirmation prompts and regular expression to validate the value of a slot, you can also create the Amazon Lex intents and slot types in the QnABot Lex bot using the Amazon Lex console. For more information, see [Adding intents](https://docs.aws.amazon.com/lexv2/latest/dg/build-intents.html) in the *Amazon Lex V2 Developer Guide*.
+ Even if the Amazon Lex intents and slot types are created in the Amazon Lex console (created outside of the **QnABot** content designer), you can reference any `SlotType` defined in the bot in a QnABot Item ID, and also map a QID to a manually created Amazon Lex intent in QnABot on AWS.
+ The **Test All** or **Test** options don’t work correctly for Item IDs with custom intent.
+ While you are building your knowledge bank of questions, you might have a combination of FAQ-based questions and intent-based questions. There may be instances where a wrong intent gets matched or a FAQ question is matched instead. To troubleshoot this issue, try the following:

Enable the `ENABLE_DEBUG_RESPONSES` setting in QnABot on AWS. This setting provides debug information to help understand what is processing the request, such as, `Intent`, `OpenSearch`, or `Amazon Kendra`.

---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/configuring-the-chatbot-to-ask-the-questions-and-use-response-bots.html
---

# Configuring the chatbot to ask the questions and use response bots
<a name="configuring-the-chatbot-to-ask-the-questions-and-use-response-bots"></a>

You can configure your chatbot to ask questions and process your end user’s answers. Use this feature for data collection and validation; to implement surveys, quizzes, personalized recommendations; or triage chatbot applications.

Use the following procedure to configure the chatbot to ask questions.

1. Sign in to the content designer and choose **Add.**

1. Enter ID: `ElicitResponse.001`

1. Enter question: `Ask my name`

1. Enter answer: `Hello. Can you give me your First Name and Last Name please?`

1. Choose **Advanced**.

1. Under **Elicit Response**, enter the following:

   1.  **Elicit Response: ResponseBot Hook**: `QNAName`

      Alternatively for Lex V2 bots, you can use the syntax `lexv2::BotId/BotAliasId/LocaleId`. This allows you when you are combining elicit responses with multi-language to use a specific language for the elicit response bot.

   1.  **Elicit Response: Response Session Attribute Namespace**: `name_of_user`

1. Choose **CREATE** to save the new item.

1. Use the web UI to say: ` "Ask my name" `

1. Respond by entering your name. Try responding naturally and see if chatbot confirms your name correctly. If not, you can choose **NO** and try again.

   The **ResponseBot Hook** field specifies the name of an Amazon Lex chatbot. In this case, specify the name of a chatbot, **QNAName**, that the guidance creates automatically during installation. QNAName is a built-in response chatbot designed to process names (first and last name). It handles a variety of ways the user might state their name and prompts the user to confirm or try again. If the user confirms by choosing YES, the response chatbot returns the `FirstName` and `LastName` values to the guidance as slot values in a fulfilled response.

   The guidance stores the returned `FirstName` and `LastName` values in a session attribute. The name of the session attribute is determined by the value you provided for **Response Session Attribute Namespace** (in this case `name_of_user`) and the slot name(s) returned by the response chatbot (in this case `FirstName` and `LastName`).

   The session attribute set by Elicit Response can be used in other items to provide conditional or personalized responses.

1. Sign in to the content designer, and choose **Add.**

   1. Enter ID: `ElicitResponse.002`

   1. Enter question: `Ask my age`

   1. Enter answer: `Hello {{SessionAttributes.name_of_user.FirstName}} What is your age in years?`

1. Choose **Advanced**.

   1. Enter **Elicit Response: ResponseBot Hook**: `QNAAge`

   1. Enter **Elicit Response: Response Session Attribute Namespace**: `age_of_user`

1. Choose **CREATE** to save the new item.

1. Use the web UI to say: ` "Ask my age." `

## Response bots
<a name="response-bots"></a>

The guidance provides a set of built-in response bots that you can use out of the box:
+  **QNAYesNo -** Returns slot `Yes_No` with value either `Yes` or `No`
+  **QNAYesNoExit -** Returns slot `Yes_No_Exit` with value either `Yes`, `No`, or `Exit`
+  **QNADate -** Returns slot `Date` with value of date (`YYYY-MM-DD`)
+  **QNADayOfWeek -** Returns slot `DayOfWeek`
+  **QNAMonth -** Returns slot `Month`
+  **QNANumber -** Returns slot `Number`
+  **QNAAge -** Returns slot `Age`
+  **QNAPhoneNumber -** Returns slot `PhoneNumber`
+  **QNATime -** Returns slot `Time` with value of time (`hh:mm`)
+  **QNAEmailAddress -** Returns slot `EmailAddress`
+  **QNAName -** Returns slots `FirstName` and `LastName`
+  **QNAFreeText -** Returns slots `FreeText` and `Sentiment`

You can also add your own Amazon Lex bots and use them as response bots. Response chatbot names must start with the letters `QNA`. The guidance calls your chatbot with the user’s response, and captures all the slot names and values returned when your chatbot sends back a fulfilled message.

## Advancing and branching through a series of questions
<a name="advancing-and-branching-through-a-series-of-questions"></a>

The following example configures the guidance to automatically ask your age after you provide your name.

1. Sign in to the content designer and edit item `ElicitResponse.00.1`

1. Choose **Advanced**.

1. Enter **Document Chaining: Chaining Rule**: `ask my age`

1. Choose **UPDATE** to save the modified item.

1. Use the web UI to say: ` "Ask my name" `
   + Enter and confirm your name.
   + Enter and confirm your age.

The guidance automatically asks you for your age after you confirm your name. Because you specified the next question, `ask my age`, as the chaining rule, the guidance automatically found and advanced to the matching item.

Next, create a *conditional* chaining rule that will branch to different items depending on previous answers.

1. Sign in to the content designer and add two new items:
   + ID: `ElicitResponse.003`, question: `"Under 18"`, answer: `"Under 18 answer"`.
   + ID: `ElicitResponse.004`, question: `"Over 18"`, answer: `"Over 18 answer"`.

1. Edit item `ElicitResponse.002`

   1. Add Chaining Rule: `(SessionAttributes.age_of_user.Age< 18) ? "Under 18" : "Over 18"`

   1. Choose **UPDATE** to save the modified item.

1. Use the web UI to ask: ` "Ask my name" `.
   + Enter and confirm your name.
   + Enter and confirm your age.

When you confirm your age, the guidance automatically branches to one of the two new items you added, depending on your age. The chaining rule is a JavaScript programming expression used to test the value of the session attribute set by elicit response; if it is less than 18 then advance to the item matching the question `"Under 18"`, otherwise advance to the item matching the question `"Over 18"`.

Combine expressions with logical operators to test multiple session attributes in a single rule, and use nested expressions to implement more than two branches in a chaining rule. Use the alternate syntax `SessionAttributes('age_of_user.Age')` to avoid a processing error if the referenced session attribute does not exist.

You can also apply chaining rule expressions to all the context variables supported by the Handlebars feature including `UserInfo` fields, `Settings` fields, and more. For a list of available variables, see the [Handlebars](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/handlebars/README.md) section in GitHub repository.

Identify the next document using its QID value instead of a question using a string that starts with `QID::` followed by the QID value of the document, for example, a rule that evaluates to `QID::Admin001` will chain to item `Admin.001`.

You can optionally specify an AWS Lambda function instead of a JavaScript expression when you need to evaluate complex chaining rule logic. Your Lambda function is invoked with the full user request context and should evaluate and return the next question as a simple string. Alternatively, the Lambda function may return an event object where the `event.req.question` key was updated to specify the next question - by returning an event object, your `chaining rule` Lambda function can modify session attributes, similar to Lambda hooks. Use Lambda functions to implement chaining rules that require complex logic and data lookup. A `chaining rule` Lambda function name must start with the letters "QNA", and is specified in the **Document Chaining:Chaining Rule** field as `Lambda::FunctionNameOrARN`.

**Note**
If the chaining rule has an error, the guidance returns the message, ` "Unfortunately I encountered an error when searching for your answer. Please ask me again later." `

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

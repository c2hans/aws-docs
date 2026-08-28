---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/bot-routing.html
---

# Bot routing
<a name="bot-routing"></a>

Bots come in many shapes and sizes, and exist to perform a variety of automation tasks. Usually, they take input from a human and respond by performing a task. Bots might ask for additional input, verify the input, and respond with completion. You can implement bots by using Amazon Lex or other toolsets. An example is the [nutritionix bot](https://www.nutritionix.com/natural-demo?q=for%20breakfast%20i%20ate%203%20eggs,%20bacon%20and%20cheese) where you can tell the bot what you’ve had for breakfast and it responds with nutrition information.

QnABot on AWS coordinates (routes) bot requests through a supervisory bot, to the appropriate bot based on questions or tasks.

Content designers associate questions or tasks (QIDs) that identify a BotRouter to target for the question. This is performed using the **QnABot** content designer UI. Once configured, if a user asks a question or directs the bot with some instruction, QnABot on AWS responds with an answer and sets up a channel to communicate with the specialty bot. From that point, messages or responses from the user are delivered to the specialty bot. Specialty bots respond to actions and QnABot on AWS delivers the answers.

This flow continues until one of these events occurs:

1. The user cancels the conversation with the specialty bot by uttering *"exit"*, *"quit"*, *"bye"*, or a configurable phrase defined in the settings configuration of QnABot on AWS.

1. The specialty `BotRouter` (custom code) responds with a message indicating the conversation should be discontinued (`QNABOT_END_ROUTING`).

1. The specialty bot is a LexBot (non QnABot on AWS) that indicates fulfillment is complete.

1. If the target bot is another QnABot on AWS, session attributes can be set by the specialty QnABot on AWS set indicating the conversation should be discontinued (`QNABOT_END_ROUTING`).

Specialty bots can be developed for specific parts of an organization like IT, or Finance, or Project Management, or Documentation. A supervisory bot at an enterprise level can direct users to answers from any of their bots.

## Configuration of bot routing
<a name="configuration"></a>

Configuration of bot routing is simple. Each question in QnAbot on AWS contains an optional section which allows configuration of a `BotRouter`.

**Note**
This is optional. Leave empty and QnABot on AWS will not act as a `BotRouter` for the question being edited.

 **Bot routing**

![botrouting](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/botrouting.png)

The example image shows an integration we’ve developed which communicates with the Nutritionix bot.
+ Bot name or Lambda function - You can configure and existing Lex bot or configure a specialty `BotRouter` implemented via a Lambda function.
+ Simple name - A short string that we expect web user interfaces to use as a breadcrumb to identify where in an enterprise the user is interacting.

**Note**
When integrating with other Amazon Lex bots or Lambda functions, the permission to communicate with the target Amazon Lex bot or with a new `BotRouter` Lambda function need to be added to the guidance’s `Fulfillment` Lambda role.

## Message protocol for a new bot router implemented in Lambda
<a name="message-protocol-for-a-new-bot-router-implemented-in-lambda"></a>

The input JSON payload to the target Lambda function is as follows:

```
req: {
        request: "message",
        inputText: <String>,
        sessionAttributes: <Object>),
        userId: <String>
    }
```

The expected response payload from the target Lambda function is the following:

```
{
    response: "message",
    status: "success", "failed"
    message: <String>,
    messageFormat:  "PlainText", "CustomPayload", "SSML", "Composite"
    sessionAttributes: Object,
    sessionAttributes.appContext.altMessages.ssml: <String>,
    sessionAttributes.appContext.altMessages.markdown: <String>,
    sessionAttributes.QNABOT_END_ROUTING: <AnyValue>
    responseCard: <standard Lex Response Card Object>
}
```

## Sample bot router
<a name="sample-bot-router"></a>

The Nutrionix node.js based sample `BotRouter` is provided as a zip file in the [GitHub repository](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/nutritionix_botrouter.zip). To use this sample you’ll need to provision an [API account with Nutritionix](https://www.nutritionix.com/business/api) and configure the source to use your own `x-app-id` and `x-app-key` from Nutritionix.

```
'x-app-id': process.env.xAppId,
    'x-app-key': process.env.xAppKey
```

Next, you must build and deploy the code into Lambda using your favorite techniques and grant permission within the QnABot `Fulfillment` Lambda role using IAM to invoke this Lambda.

**Tip**
If you name the Lambda function starting with `qna`, QnABot on AWS is already configured with permissions to invoke this Lambda.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

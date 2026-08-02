---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/step-4-interact-with-the-chatbot.html
---

# Step 4: Interact with the chatbot
<a name="step-4-interact-with-the-chatbot"></a>

## Getting answers using an Amazon Lex web client user interface
<a name="getting-answers-using-an-amazon-lex-web-client-user-interface"></a>

You can launch QnABot on AWS from a Chrome, Firefox, or Microsoft Edge browser on your PC, Mac OS, Chromebook, or Android tablet.

1. From the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks?filter=active), select the main QnABot on AWS stack, choose **Output**, and then select the link to the **ClientURL**. Alternatively, launch the client by choosing **QnABot on AWS Client** from the content designer tools menu ( **☰** ).

1. When your browser requests access to the microphone on behalf of the web application, allow it. The QnABot on AWS chat window opens.

    **QnABot on AWS web user interface chat window**
![image9](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image9.png)

1. Interact with the chatbot through the chat window. You can communicate through voice or text.

Select the microphone icon (bottom right) and say, ` "What is Q and A Bot?" `

The chatbot responds with the answer you programmed in Step 3: Create chatbot content and load sample Q and A data.

## Getting answers using Amazon Alexa
<a name="getting-answers-using-amazon-alexa"></a>

The QnABot on AWS solution also works with Amazon Alexa, allowing your end users to get answers from your programmed content via any Amazon Alexa device, including Amazon FireTV, and any of the Amazon Echo family of devices.

**Note**
To integrate with Amazon Alexa, you must first use the Amazon Developer Console to create an Alexa skill for QnABot on AWS. This solution doesn’t automatically create Alexa skills. You can use the content designer to launch a walkthrough for creating an Alexa skill.
Starting in v7.4.0, Alexa integration requires you to register your Alexa Skill IDs using the `AlexaSkillIds` AWS CloudFormation stack parameter. New deployments have Alexa integration turned off by default. To turn it on, provide your Alexa Skill IDs when launching or updating the stack. **If you currently use Alexa, you must provide your Alexa Skill IDs during stack update to maintain Alexa functionality.**
To find your Alexa Skill ID, sign in to the Amazon Developer Console, open your skill, and copy the Skill ID (format: `amzn1.ask.skill.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`). You can register up to 30 skill IDs as a comma-separated list with no spaces (for example, `amzn1.ask.skill.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx,amzn1.ask.skill.yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy`).

Use the following procedure to create an Alexa skill.

1. Sign in to the QnABot on AWS content designer, open the tools menu ( **☰** ), and choose **Alexa**.

1. Follow the instructions in the console.

1. (Optional) Test your new skill in the Amazon Developer Console, even if you don’t have an Alexa device nearby.

When testing the skill, invoke the skill with the invocation name before asking questions and answers. For example, if your invocation name is *my qnabot*, in the Alexa skill test console, first say, ` "Open my Q and A Bot." ` Alexa will reply with ` "Hello, please ask a question," ` then you can ask your QnABot a question.

**Note**
If you want to publish your new QnABot on AWS skill to the Alexa skills store so that other users can access it, see [Submitting an Alexa Skill for Certification](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/publishing-an-alexa-skill). Unpublished skills are accessible only to Alexa devices registered to your Amazon account; published skills are available to anyone.

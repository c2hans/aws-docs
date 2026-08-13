---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/tuning-testing-and-troubleshooting-unexpected-answers.html
---

# Tuning, testing, and troubleshooting unexpected answers
<a name="tuning-testing-and-troubleshooting-unexpected-answers"></a>

You can use the content designer to tune, test, and troubleshoot answers to fix problems.

## Tuning answers using the content designer
<a name="tuning-answers-using-the-content-designer"></a>

By default, QnABot on AWS attempts to match an end user’s question to the list of questions and answers stored in Amazon OpenSearch Service. QnABot on AWS uses full text search to find the item that is the best match for the question asked. Words that are used infrequently score higher than words that are used often, so sentence constructs such as prepositions have lower weighting than unique keywords. The closer the alignment between a question associated with an item and a question asked by the user, the greater the probability that QnABot on AWS will choose that item as the most relevant answer.

The guidance tries to find the best answer to questions by applying the keyword filters, and by matching the words used in the end user’s question to the words used in the question fields of the stored answers—​giving preference when the same words are used in the same order.

You might find that end users ask questions in ways that you haven’t anticipated, resulting in unexpected answers being returned by QnABot on AWS. When this happens, you can use the content designer to troubleshoot and fix the problem.

For more information, see the [Tuning Recognition Accuracy](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/tuning_accuracy_guide) section in the GitHub repository.

## Testing all your questions
<a name="testing-all-your-questions"></a>

Use the following procedure to test your questions.

1. Sign in to the content designer, and choose **TEST ALL.**

1. Use the default filename, or enter your own.

1. Optionally, if you want to test only a subset of questions, you can filter by the `qid` prefix. Leave this field blank to test all the questions.

1. Select **TEST ALL**, and wait for the tests to complete.

1. Select the **view results** icon on the bottom right to view the test results. Any incorrect matches are highlighted in red. Test results can be viewed in the browser, or downloaded to your computer as a CSV file.

## Tuning the chatbot’s ASR
<a name="tuning-the-chatbots-asr"></a>

When you ask QnABot on AWS a question, it is processed and transcribed by either Amazon Lex or Alexa using an ASR engine. QnABot on AWS initially trains the ASR to match a wide variety of possible questions and statements, so that the Amazon Lex chatbot and Alexa skill will accept almost any question a user asks.

This guidance supports `AMAZON.FallbackIntent` in both Amazon Lex and Alexa, which allows it to process anything end users say without needing to retrain and rebuild the Amazon Lex chatbot or Alexa skill.

Occasionally, the transcription shown in the web client or the Alexa app isn’t accurate. This can happen with unusual words that are confused for other more common words or phrases. Use one of the following approaches to troubleshoot this error:
+ Use the content designer to add additional question variants that match the actual transcription shown in the web client or in the Alexa app; this allows QnABot on AWS to anticipate the transcription accuracy problem, and respond anyway.
+ Retrain the Amazon Lex and Alexa ASR with examples to influence the transcription to more closely match what you want - see **Retrain Amazon Lex** for more information.

### Retrain Amazon Lex
<a name="retrain-amazon-lex"></a>

QnABot on AWS can automatically generate additional ASR training data for Amazon Lex using questions from the data you have added.

1. Sign in to the content designer and choose **LEX REBUILD** from the top right edit menu ( ⋮ ) **0**

1. Wait for the rebuild to complete.

### Retrain Alexa
<a name="retrain-alexa"></a>

QnABot on AWS can generate additional ASR training data for Alexa using questions from the data you have added.

1. Sign in to the content designer and choose **ALEXA UPDATE** from the top right edit menu ( ⋮ ).

1. Select **COPY SCHEMA** to copy the updated Alexa skill schema.

1. Sign in to the Alexa Developer Console, open your QnABot on AWS skill, and then use the JSON editor to paste the new schema, replacing the existing one.

1. Save and then build the updated model.

## Monitoring QnABot on AWS usage and user feedback
<a name="monitoring-qnabot-on-aws-usage-and-user-feedback"></a>

The guidance logs everything that end users say to the chatbot. Amazon Data Firehose stores logged utterances to a new index in Amazon OpenSearch Service.

You can also allow your end users to provide feedback about the chatbot’s answers. Use the following procedure to set up the feedback mechanism.

1. From the content designer’s top left tools menu (☰), select **Import**.

1. Open **Examples**/**Extensions**, and select the **LOAD** for the **QnAUtility** demo.

1. From the top left tools menu (☰), select **EDIT** and examine the newly imported items, `Feedback.001` and `Feedback.002`; observe the list of default expressions that the end user can input to invoke feedback. (The example **QnAUtility** demo package also loads `Help`, `CustomNoMatches`, `CustomNoVerifiedIdentity` items.)

1. Test the feedback mechanism.

Use the web UI to ask a question, such as: *"What happens if I ask an unanticipated question?"*. Because we have not entered a suitable answer for this question, QnABot on AWS responds with the newly imported `CustomNoMatches` response—​indicating that it doesn’t know the answer.

From the web UI, say or type *"Thumbs down"*, or select the *Thumbs down* icon beside the answer.

The guidance publishes *Thumbs down* feedback messages to the Amazon Simple Notification Service (SNS) topic identified by the **FeedbackSNSTopic** on the **Outputs** tab of the CloudFormation stack. To learn how to subscribe to the SNS topic, and receive a message from the each time a user provides feedback, see [Subscribing to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the *Amazon Simple Service Notification Developer Guide.*

If you have selected a non-English language for your QnABot on AWS deployment and have multi-language enabled then you should do the following steps:

1. Use the AWS Translate API to translate *Thumbs up* and *Thumbs down* to your deployment language, if it is not English.

1. Add the translation of the Thumbs up and down as a question in your QnABot on AWS deployment.

1. Go to the content, select the top left tools menu (☰), and choose **Settings**.

1. Find the `PROTECTED_UTTERANCES` variable and insert that phrase in by adding a comma, then enter the translation.

Use the following process to visualize the usage logs and feedback using [OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html). Note that it can take up to 5 minutes for new utterances and end user feedback to become visible in the dashboard.

1. From the content designer, select the top left tools menu ( ☰ ), and choose **OpenSearch**\***Dashboards** and it opens in a new browser tab.

1. Choose the **QnABot on AWS** dashboard to visualize usage history and sentiment, all logged utterances, no hits utterances, positive user feedback, and negative user feedback.

    **Sample OpenSearch Dashboard**
![image23](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image23.png)

1. Edit [OpenSearch Dashboards](https://opensearch.org/docs/latest/dashboards/) to change the time span, customize and build your own visualizations, or to run your own queries.

## Using Amazon CloudWatch to monitor and troubleshoot
<a name="using-amazon-cloudwatch-to-monitor-and-troubleshoot"></a>

The guidance’s metrics and logs are available in an Amazon CloudWatch dashboard. Use the following procedure to launch the dashboard and visualize the guidance’s AWS resources.

1. From the CloudFormation stack’s **Outputs** tab, select the **CloudWatchDashboardURL** link.

1. When troubleshooting the chatbots responses to your questions, trace the request and response using the logs created by the `Fulfillment` Lambda function.

   1. Choose the **menu** tool in the upper right of the `Fulfillment` Lambda widget, select **View logs**, then and choose the **AWS Lambda** function **0**

       **FulfillmentLambda function**
![image24](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image24.jpeg)

   1. Inspect the log messages. Each interaction with the guidance is delimited by **START** and **END** messages. Between these messages are insights into how the guidance processes the question.

### Use Log Insights to query logs from CloudWatch groups
<a name="use-log-insights-to-query-logs-from-cloudwatch-groups"></a>

1. Go to **Log Insights** in Amazon CloudWatch and select the log group you would like to query.

1. Create your query in **Log Insights**.

   Example query for Fulfillment Lambda logs to query for any errors:

   ```
   filter @message like /(?i)(Exception|error|KeyError)/
   | fields @timestamp, @message
   | sort @timestamp desc
   | limit 200
   ```

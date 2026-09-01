---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/lex-bot-analytics.html
---

# Evaluate the performance of your conversational AI bot in Connect Customer
<a name="lex-bot-analytics"></a>

You can use the comprehensive analytics tools in Connect Customer to help you evaluate and optimize your conversational AI bot performance. With these insights, you can identify successful interactions, pinpoint failure points, and visualize conversation patterns to continuously improve customer experience.

The analytics dashboard includes key metrics such as Utterance recognition rate and Conversation performance. These metrics help you understand both the success and failure rates of your bot's interactions with customers.

**Note**
The Bot Analytics page shows data for conversations triggered only from flows. You can trigger bots externally using Lex APIs or custom integrations, but data for those conversations are not reflects on this page.

**To view analytics for your bot**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an Admin account or an account that has the following permissions in its security profile:
   + **Channels and Flows** - **Bots** - **View**
   + **Channels and Flows** - **Bots** - **Edit**
   + **Analytics and Optimization** - **Historical metrics** - **Access**

1. In the left navigation menu, choose **Routing**, **Flows**.

1. On the **Flows** page, choose **Bots**, choose the bot whose performance you want to evaluate, and then choose **Analytics**.
![The Flows page, the Analytics tab.](http://docs.aws.amazon.com/connect/latest/adminguide/images/bot-analytics1.png)

 The following image shows sample analytics data.

![The Analytics tab with sample analytics data for a bot.](http://docs.aws.amazon.com/connect/latest/adminguide/images/bot-analytics.png)

Use these analytics to identify improvement opportunities, refine your bot's responses, and enhance the overall customer experience.

For additional metrics and advanced analysis techniques specific to Amazon Lex, see [Monitoring bot performance in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-bot-performance.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

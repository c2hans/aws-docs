---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/connecting-qnabot-on-aws-to-an-amazon-connect-call-center.html
---

# Connecting QnABot on AWS to an Amazon Connect call center
<a name="connecting-qnabot-on-aws-to-an-amazon-connect-call-center"></a>

The guidance can automate data collection and answer frequently asked questions using QnABot on AWS within an Amazon Connect contact flow. Optionally, you can also configure the guidance to use Amazon Connect to make outbound calls; your users can use the web UI or the Alexa skill to ask QnABot on AWS to call their phone so they can speak to a human.

Using the Amazon Connect integration wizard, follow these steps to connect QnABot on AWS to a call center.

1. Sign in to the content designer, select the tools menu (☰), and then choose **Connect**.

1. Follow the step-by-step directions in the wizard to create a contact center using the guidance to answer caller’s questions.

    **Amazon Connect integration wizard**
![image22](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image22.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

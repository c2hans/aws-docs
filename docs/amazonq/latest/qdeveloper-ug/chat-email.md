---
source_url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-email.html
---

# Chatting about email sending
<a name="chat-email"></a>

Amazon Q can help you set up email sending in Amazon Simple Email Service (Amazon SES), helping you to optimize your sending delivery and engagement rates, and troubleshoot sending problems. When you ask Amazon Q about Amazon SES, it’s responses include information about the sending identities, configuration sets, and other Amazon SES resources in your account. It is also able to answer questions about your email sending patterns, as well as patterns of responses from mailbox providers such as Gmail and Yahoo.

## Prerequisites
<a name="chat-email-prereqs"></a>

You can chat about your Amazon SES in the AWS Management Console and in [configured chat applications](q-in-chat-applications.md).

For Amazon Q to answer questions about your email sending, the following prerequisites must be met.

### Add permissions
<a name="add-permissions-chat-email"></a>

To chat about your email sending, your IAM identity must have permissions to chat with Amazon Q. For an IAM policy that grants the required permissions, see [Allow users to chat with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat). You must also have permissions to access the Amazon SES resources you ask about.

## Example questions
<a name="example-questions-email"></a>

Following are example questions about email sending that you can ask Amazon Q:
+ Do I need to do anything to finish setting up SES for email sending?
+ Tell me which sending identities have the best deliverability performance.
+ How is my deliverability for emails sent to Yahoo?
+ Do you have any recommendations to improve my sending?
+ Tell me if there have been any recent events where my deliverability performance suddenly improved or worsened.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/ses/latest/dg/send-email.html
---

# Set up email sending with Amazon SES
<a name="send-email"></a>

You can send an email with Amazon Simple Email Service (Amazon SES) using the Amazon SES console, the Amazon SES Simple Mail Transfer Protocol (SMTP) interface, or the Amazon SES API. You typically use the console to send test emails and manage your sending activity. To send bulk emails, you use either the SMTP interface or the API. For information about Amazon SES email pricing, see [Amazon SES Pricing](https://aws.amazon.com/ses/pricing).
+ If you want to use an SMTP-enabled software package, application, or programming language to send email through Amazon SES, or integrate Amazon SES with your existing mail server, use the Amazon SES SMTP interface. For more information, see [Sending emails programmatically through the Amazon SES SMTP interface](send-using-smtp-programmatically.md).
+ If you want to call Amazon SES by using raw HTTP requests, use the Amazon SES API. For more information, see [Using the Amazon SES API to send email](send-email-api.md).

**Important**
When you send an email to multiple recipients (recipients are "To", "CC", and "BCC" addresses) and the call to Amazon SES fails, the entire email is rejected and none of the recipients will receive the intended email. Therefore, we recommend that you send an email to one recipient at a time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

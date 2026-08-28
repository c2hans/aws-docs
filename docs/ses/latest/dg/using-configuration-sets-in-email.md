---
source_url: https://docs.aws.amazon.com/ses/latest/dg/using-configuration-sets-in-email.html
---

# Specifying a configuration set when you send email
<a name="using-configuration-sets-in-email"></a>

To use a configuration set when sending an email, you must pass the name of the configuration set in the headers of the email. All of the Amazon SES email sending methods—including the [AWS CLI](https://aws.amazon.com/cli), the [AWS SDKs](https://aws.amazon.com/tools/#sdk), and the [Amazon SES SMTP interface](send-email-smtp.md)—allow you to pass a configuration set in the headers of the email you send.

If you are using the [SMTP interface](send-email-smtp.md) or the [`SendRawEmail` API operation](/ses/latest/APIReference/API_SendRawEmail.html), you can specify a configuration set by including the following header in your email (replacing `{{ConfigSet}}` with the name of the configuration set you want to use):

```
X-SES-CONFIGURATION-SET: {{ConfigSet}}
```

This guide includes code examples for sending email using the AWS SDKs and the Amazon SES SMTP interface. Each of these examples includes a method of specifying a configuration set. To see step-by-step procedures for sending emails that include references to configuration sets, see the following:
+ [Sending email through Amazon SES using an AWS SDK](send-an-email-using-sdk-programmatically.md)
+ [Using the Amazon SES SMTP interface to send email](send-email-smtp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

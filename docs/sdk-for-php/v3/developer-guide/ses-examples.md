---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-examples.html
---

# Amazon SES examples using the AWS SDK for PHP Version 3
<a name="ses-examples"></a>

Amazon Simple Email Service (Amazon SES) is an email platform that provides an easy, money-saving way for you to send and receive email using your own email addresses and domains. For more information about Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/).

AWS offers two versions of Amazon SES service and, correspondingly, the SDK for PHP offers two versions of the client: [SesClient](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Ses.SesClient.html) and [SesV2Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.SesV2.SesV2Client.html). The functionality of the clients overlap in many cases although the way the methods are called or the results may differ. The two APIs also offer exclusive features, so you can use both clients to access all the functionality.

The examples in this section all use the original, `SesClient`.

All the example code for the AWS SDK for PHP Version 3 is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

**Topics**
+ [Verifying email addresses](ses-verify.md)
+ [Working with email templates](ses-template.md)
+ [Managing email filters](ses-filters.md)
+ [Using email rules](ses-rules.md)
+ [Monitor your sending activity](ses-send-email.md)
+ [Authorizing senders](ses-sender-policy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

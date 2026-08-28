---
source_url: https://docs.aws.amazon.com/translate/latest/dg/protect-terminology.html
---

# Encrypting your terminology
<a name="protect-terminology"></a>

Amazon Translate endeavors to protect all your data and your custom terminologies are no different. When created, each custom terminology is encrypted so it accessible only by you.

Three encryption options are available:
+ Using AWS encryption. AWS encryption is the default option to safeguard your information.
+ Using an encryption key associated with your account. A menu in the console provides you with a choice of associated encryption keys to use.
+ Using an encryption key not associated with your account. The console displays an input field for you to enter the Amazon Resource Name (ARN) of the encryption key.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-email.html
---

# AMAZON.EmailAddress
<a name="built-in-slot-email"></a>

Recognizes words that represent an email address provided as username@domain. Addresses can include the following special characters in a user name: underscore (\_), hyphen (-), period (.), and the plus sign (\+).

The `AMAZON.EmailAddress` slot type supports inputs using spelling styles. You can use the spell-by-letter and spell-by-word styles to help your customers enter email addresses. For more information, see [Capturing slot values with spelling styles during the conversation](spelling-styles.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

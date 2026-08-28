---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guides-pii-redaction.html
---

# Prevent PII from appearing in a contact record transcript using Connect Customer conversational analytics
<a name="step-by-step-guides-pii-redaction"></a>

By default, any information passed through a guide is included in the contact record transcript. To prevent PII from appearing in your contact record transcript, use the [Set recording and analytics behavior block](set-recording-behavior.md) in your step-by-step guide flow, [enable conversational analytics](sensitive-data-redaction.md), and enable the redaction of sensitive date.

For full details on how to enable PII redaction, see [Enable redaction of sensitive data](enable-analytics.md#enable-redaction).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-add-header.html
---

# Add header action
<a name="receiving-email-action-add-header"></a>

The **Add Header** action adds a custom header to the received email. You typically use this action only in combination with another action. This action has the following options.
+ **Header name—**The name of the header to add. It must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
+ **Header value—**The value of the header to add. It must be less than 2048 characters, and must not contain newline characters ("\\r" or "\\n").

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

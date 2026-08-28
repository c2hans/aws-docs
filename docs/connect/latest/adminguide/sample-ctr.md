---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/sample-ctr.html
---

# View a contact record in the Connect Customer admin website
<a name="sample-ctr"></a>

1. Do a [contact search](contact-search.md). A list of contact IDs will be returned.

1. Choose an ID to view the contact record for the contact.

The following image shows part of a contact record in the UI, for a chat conversation. Note the following:
+ For chats, the initiation method is always **API**.
+ The chat transcript is visible in the UI.

![The Contact Record page, a chat transcript.](http://docs.aws.amazon.com/connect/latest/adminguide/images/sample-ctr.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

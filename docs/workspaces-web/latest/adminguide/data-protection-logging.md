---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/data-protection-logging.html
---

# User access logging in Amazon WorkSpaces Secure Browser
<a name="data-protection-logging"></a>

Administrators are able to record WorkSpaces Secure Browser session events, including start, stop, and URL visits. These logs are encrypted and securely delivered to customers through an Amazon Kinesis Data Stream. Browsing information from user access logging is not stored by AWS, or available from sessions without logging configured. URL visits in incognito mode, or deleted URLs from browser history, are not recorded in user access logging.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

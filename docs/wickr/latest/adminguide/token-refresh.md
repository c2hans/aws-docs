---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/token-refresh.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Grace period for token refresh
<a name="token-refresh"></a>

Occasionally, there may be instances where identity providers encounter temporary or extended outages, which may lead to your users being logged out unexpectedly due to a failed refresh token for their client session. To prevent this problem, you can establish a grace period that allows your users to remain signed in even if their client refresh token fails during such outages.

Here are the available options for the grace period:
+ No grace period (default): Users will be signed out immediately after a refresh token failure.
+ 30 minute grace period: Users can stay signed in for up to 30 minutes after a refresh token failure.
+ 60 minute grace period: Users can stay signed in for up to 60 minutes after a refresh token failure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

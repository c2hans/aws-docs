---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/batchupdatecommand-interfaces.html
---

# Batch command in different interfaces
<a name="batchupdatecommand-interfaces"></a>

The batch update schedule command is represented differently in different interfaces:
+ In the AWS CLI, the command is `batch-update-schedule`.
+ In the API, the command is represented by an `HTTP PUT` on `channels/channelId/schedule`.
+ In the AWS SDKs, the command is represented by constructs that are suitable to that SDK language.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

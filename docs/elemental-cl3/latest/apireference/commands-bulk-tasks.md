---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-bulk-tasks.html
---

# Bulk Tasks
<a name="commands-bulk-tasks"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Start Channel | POST | /channels/start | Start one or more channels. |
| POST Stop Channel | POST | /channels/stop | Stop one or more channels. |
| GET Task Report List | GET | /task\_reports/<ID of report> | Get the list of task reports. |
| GET Task Report | GET | /task\_reports/<ID of report> | Get the specified task report. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

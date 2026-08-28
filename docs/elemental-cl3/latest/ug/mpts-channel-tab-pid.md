---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-channel-tab-pid.html
---

# PID Controls tab
<a name="mpts-channel-tab-pid"></a>

On this tab, you can assign the output PIDs for the streams that are in the source program. You can leave one, several or all the fields empty, and Elemental Statmux will assign a unique ID.

If you do enter a PID, you must make sure that each PID is unique in the entire MPTS. You should also assign PIDs only to streams that you know are in the stream, otherwise you are wasting a number.

If you leave the fields empty, Elemental Statmux assigns PIDs after you save. It makes sure that each stream has a PID that is unique in the entire MPTS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

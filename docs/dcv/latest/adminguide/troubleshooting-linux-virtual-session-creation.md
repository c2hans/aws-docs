---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/troubleshooting-linux-virtual-session-creation.html
---

# Troubleshooting Virtual Session Creation on Linux
<a name="troubleshooting-linux-virtual-session-creation"></a>

If connecting to a virtual session results in a `No session available` or `The sessionId {{session}} is not available` error, this is probably due to the fact that the virtual session creation failed and was terminated.

You can check if the session is present with the `dcv list-sessions` command. See [Viewing Amazon DCV sessions](managing-sessions-lifecycle-view.md) for more information about inspecting running sessions. If the session is not present in the list, then it might have failed.

**Topics**
+ [Investigating Virtual Session Creation Failure on Linux](investigating-linux-virtual-session-creation-failure.md)
+ [Creating a Failsafe Virtual Session on Linux](creating-linux-failsafe-virtual-session-creation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

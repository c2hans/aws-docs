---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/actions-process-flow.html
---

# Process flow
<a name="actions-process-flow"></a>
+ **Process step** - Groups logically related actions. Used for organizing your process.
+ **If decision** - Checks a true/false condition. The process is split into two branches based on the result.
+ **Loop through items** - Repeats actions for each item. Used for processing multiple items like emails, files, or data rows one at a time.
+ **Loop while true** - Repeats while a condition is met. The condition is checked before each loop and must be True for the loop to continue.
+ **End process** - Ends the current run successfully. Optionally, provide a custom message or value as the final outcome of the process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

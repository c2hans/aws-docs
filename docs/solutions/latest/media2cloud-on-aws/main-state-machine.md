---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/main-state-machine.html
---

# Main state machine
<a name="main-state-machine"></a>

 The main state machine is the entry point to the backend ingestion and analysis workflows. The main state machine chains the backend ingestion and analysis workflows as sub-state machines:
+  **Start ingestion state machine (nested)** – Runs the ingestion process using the ingestion state machine when a customer uploads a media file to Media2Cloud on AWS.
+  **Start analysis state machine (nested)** - Runs the analysis process using the analysis state machine after the ingestion state machine completes the ingestion process.

![Main state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-main-state-machine.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

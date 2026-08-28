---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/detection.html
---

# Detection
<a name="detection"></a>

 An alert is the main component of the detection phase. It generates a notification to initiate the incident response process based on AWS account activity of interest.

 Alerting accuracy is challenging; it’s not always possible to determine with complete certainty if an incident has occurred, is in progress, or if it will happen in the future. Here are a few reasons:
+  Detection mechanisms are based on baseline deviation, known patterns, and notification from internal or external entities.
+  Because of the unpredictable nature of technology and people, respectively *the means* and *the actors* of security incidents, baselines change over time. Rogue patterns emerge through novel or modified threat actor *tactics*, *techniques*, and *procedures* (TTPs).
+  Changes to people, technology, and processes are not immediately incorporated into the incident response process. Some are discovered during the progress of an investigation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

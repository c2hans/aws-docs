---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/citizen-engagement-reference-architecture.html
---

# Citizen engagement reference architecture
<a name="citizen-engagement-reference-architecture"></a>

 Governments are increasingly investing in citizen facing channels: mobile applications, web portals, call center agents, and chatbots to enhance the overall citizen experience. In a regulated industry space, user engagement architectures challenge the segregation often recommended for classified workloads and in some cases with citizen engagement it’s based on verifiable identity along with:
+  High volumes of real-time ingestion from public and private sources.
+  The requirement for different data protection based on data classification.
+  Use of event-driven architectures to leverage on-demand scalability and pay-per-use model.
+  Inclusion of real-time and archival flows.

![A reference architecture diagram showing a citizen engagement solution to perform sentiment analysis on content posted to Twitter.](http://docs.aws.amazon.com/wellarchitected/latest/government-lens/images/citizen-engagement.jpg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

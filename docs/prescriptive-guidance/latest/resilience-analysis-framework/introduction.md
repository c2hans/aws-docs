---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/introduction.html
---

# Resilience analysis framework
<a name="introduction"></a>

*John Formento, Jason Barto, Bruno Emer, Mike Haken, and Steven Hooper, Amazon Web Services*

Consistent, repeatable standards and processes are an important part of continuous improvement. This is true for the resilience of distributed systems as well. The purpose of this guidance is to introduce a resilience analysis framework that provides a consistent way to analyze failure modes and how they could impact your workloads. Using this framework throughout the lifecycle of your workload, from design to operation, helps you continuously improve the resilience of your workloads to a broader range of potential failure modes in a consistent and repeatable way. This helps ensure that you meet your resilience objectives and maintain the desired resilience properties of your workloads.

This framework was developed through the experience of the AWS solutions architecture field teams in their work with customers across industries. It targets builders who can have many job titles, including product managers, software developers, systems engineers, operations teams, and architects. These are the people who know the most about the system, service, or product that is being analyzed. Using the framework in continuous exercises can help you make incremental progress and meet your long-term resilience objectives.

The focus of the framework is to identify potential failure modes and the preventative and corrective controls you can use to mitigate their impact. Even if the failures occur in components that are not directly under your control, such as increased error rates in a dependency, you need to consider how those failures might impact your workload and how to design that workload to respond to these failures. Ultimately, you should focus on *failures that you can respond to* by using a mitigation that is under your control.

This guide outlines the framework, and then discusses how to identify and document a workload, how to apply the framework to that workload, and how to evaluate mitigation strategies for any potential failures you find.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

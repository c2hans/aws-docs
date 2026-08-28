---
source_url: https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-information-collected.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Information collected
<a name="microservice-extractor-information-collected"></a>

You can choose to share data when you first set up the Microservice Extractor application. You have the option to turn off usage data sharing by clearing the check box for usage data sharing on the AWS Microservice Extractor for .NET **Settings** page .

Usage data sharing is enabled by default. You can disable usage data sharing by clearing the check box for usage data sharing on the AWS Microservice Extractor for .NET **Settings** page .

When usage data sharing is enabled, Microservice Extractor collects the following information when you onboard your source code:
+ Success and failure operations performed during onboarding, static code analysis, application build, graph creation, and AI recommendations.
+ Resources consumed during operations, such as CPU and memory usage.
+ Number of nodes and dependencies.
+ Number of detected islands.
+ Types of nodes.
+ Number of canvases.

Microservice Extractor doesn’t collect proprietary information, such as source code. In case of failure, the tool may collect stack traces to improve product experience.

Microservice Extractor uses the information collected to continuously improve its API replacement suggestions. Microservice Extractor periodically analyzes the collected information and updates its replacement engine so that the Microservice Extractor experience is continuously improved.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Microservice Extractor for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query microservice-extractor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

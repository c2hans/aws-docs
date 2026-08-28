---
source_url: https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-failure-modes.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Failure modes
<a name="microservice-extractor-use-failure-modes"></a>

What used to be called a function call is now a network call. A network call can fail for various reasons; for example, network connectivity, service outages, authentication errors, or unknown server errors. While Microservice Extractor provides some handling for these new types of errors, you may want to update them to accommodate your error-handling scheme.

We recommend copying artifacts or package dependencies that lie outside the scope of the directory of your solution (with the exception of standard “reference assemblies” installed in known locations) into your solution directory, and adjusting project files to point to the updated location before starting automatic refactoring.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Microservice Extractor for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query microservice-extractor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

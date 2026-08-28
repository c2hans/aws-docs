---
source_url: https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-application-analysis.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Application analysis and extraction
<a name="microservice-extractor-application-analysis"></a>

AWS Microservice Extractor for .NET analyzes the source code of a monolithic application and creates a visualization of the application, which includes nodes, dependencies, call flows, and relevant metrics. You can use the visualization of the application to make informed decisions about the structure of the application, and to identify parts of the application to group together and extract as independent services.

After Microservice Extractor extracts a specified functionality group within the application, you can manually package and deploy the functionalities as independent services in containers. You can then integrate the smaller services with your custom workflows.

Extracting monolithic applications into smaller, independent services is an iterative process. Based on your requirements, you can repeat the process by onboarding the newly extracted monolithic application into Microservice Extractor. This further assists with identifying and extracting components as independent services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Microservice Extractor for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query microservice-extractor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

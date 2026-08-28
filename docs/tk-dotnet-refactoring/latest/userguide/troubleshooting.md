---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/troubleshooting.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Troubleshooting
<a name="troubleshooting"></a>

This section contains troubleshooting information for Toolkit for .NET Refactoring.

## Sidecar logs
<a name="sidecar-troubleshooting"></a>

If you are using Microsoft Active Directory (AD) with Toolkit for .NET Refactoring, the sidecar container performs authentication with Active Directory using the credentials from the specified secret. If the authentication fails, the deployment job will fail.

The logs of the sidecar are returned in the details of the deployment. Check the logs for text that says something similar to `invalid password`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

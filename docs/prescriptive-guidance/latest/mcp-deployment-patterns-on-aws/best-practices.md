---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/best-practices.html
---

# MCP server deployment models
<a name="best-practices"></a>

Understanding where and how to deploy MCP servers is fundamental to building scalable AI-powered applications. MCP servers can run:

1. Locally on developer workstations for personal productivity and development scenarios or

1. Deployed remotely on cloud infrastructure for team-wide access and production workloads.

The choice between local and remote deployment significantly impacts the development of workflows, security models, scalability, and operational complexity.

The following section explores both deployment models, their characteristics, and appropriate use cases. While local MCP servers excel for individual development and testing, remote deployments on AWS infrastructure enable enterprise-scale AI applications with centralized management, security controls, and reliable access for multiple users and applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

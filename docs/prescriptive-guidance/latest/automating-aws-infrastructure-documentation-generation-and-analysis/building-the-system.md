---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/building-the-system.html
---

# Core components of the Infrastructure Documentation Generator
<a name="building-the-system"></a>

The Infrastructure Documentation Generator is built in [Python](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/) for deployment and a [React](https://react.dev/)-based user interface for visualization. Its architecture is composed of modular components, each responsible for a specific part of the infrastructure discovery and documentation process.

This section explains the following key components in detail:
+ Resource scanning
+ Documentation generation
+ Dependency mapping
+ Caching mechanism

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

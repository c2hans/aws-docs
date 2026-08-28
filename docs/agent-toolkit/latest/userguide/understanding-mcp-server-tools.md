---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/understanding-mcp-server-tools.html
---

# Understanding the MCP Server tools
<a name="understanding-mcp-server-tools"></a>

AWS MCP Server provides the following tools to help you complete AWS tasks through natural language interactions.

**Deprecation**
We deprecated `aws___call_aws` as of July 15, 2026 and will remove it on August 31, 2026. We recommend `aws___run_script` for running AWS operations; it provides the same access to AWS APIs, so no functionality is lost. As a general best practice, avoid referring to specific tool names in prompts, agent skills, or configurations. Let your agent select the appropriate tool.

## AWS Knowledge Tools
<a name="aws-knowledge-tools"></a>
+ `aws___retrieve_skill` - Retrieve domain-specific expertise for a particular AWS domain. Skills provide workflows, context, best practices, decision frameworks, and step-by-step procedures. When called with a skill name, returns the full skill content including reference materials. Use `aws___search_documentation` to discover available skills.
+ `aws___search_documentation` - Search across all AWS documentation, including API references, best practices, service guides, and skills (formerly Agent SOPs). Use the topic filter to search skills exclusively, or see skills alongside general knowledge search results. Find relevant information from multiple AWS knowledge sources.
+ `aws___read_documentation` - Retrieve and convert AWS documentation pages to markdown format for easy consumption by AI assistants.
+ `aws___list_regions` - Retrieve a list of all AWS regions, including their identifiers and names.
+ `aws___get_regional_availability` - Check AWS regional availability information for services, features, SDK APIs, and CloudFormation resources.

## AWS API Tools
<a name="aws-api-tools"></a>
+ *(deprecated)* `aws___call_aws` - Execute authenticated AWS API calls with proper syntax validation and error handling. Supports most of the 15,000\+ AWS APIs with automatic credential management.
+ `aws___run_script` - Execute Python code in a sandboxed environment with AWS API access. Use for tasks that involve listing resources and checking their properties, parallel API calls, multi-step workflows, cross-service checks, and retry logic.
+ `aws___get_presigned_url` - Generate pre-signed Amazon S3 URLs for uploading or downloading files. Use this tool for direct Amazon S3 uploads and downloads, or when an AWS CLI command requires a local file path.
+ `aws___get_tasks` - Poll the status of long-running tasks started by `aws___call_aws` or `aws___run_script`. Use when a previous tool call returns a task ID with a working status.

These tools work together to provide comprehensive AWS task completion: skills guide the workflow, knowledge tools provide current information and best practices, and API tools execute the actual AWS operations with proper authentication and authorization.

When multiple profiles are configured (via `--profile` or `AWS_MCP_PROXY_PROFILES`), the MCP Proxy for AWS injects an optional `aws_profile` parameter into the schema of `aws___call_aws`, `aws___run_script`, `aws___get_presigned_url`, and `aws___get_tasks`. This parameter lets the agent route individual requests through different AWS credential profiles. The parameter is stripped by the proxy before forwarding to the server. See [Multi-profile support](multi-account-access.md) for configuration details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

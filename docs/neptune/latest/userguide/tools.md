---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/tools.html
---

# Neptune tools and utilities
<a name="tools"></a>

Amazon Neptune provides a number of tools and utilities that can simplify and automate your work with a graph. Among these are the following:

**Amazon Neptune tools**
+ **[Amazon Neptune utility for GraphQL](tools-graphql.md)**   –   The Amazon Neptune utility for GraphQL is an open-source Node.js command-line tool that can help you create and maintain a [GraphQL](https://graphql.org/) API for a Neptune property-graph database. It is a no-code way to create a GraphQL resolver for GraphQL queries that have a variable number of input parameters and return a variable number of nested fields.
+  **[Nodestream](tools-Nodestream.md)**   –   Nodestream is a framework for dealing with semantically modeling data as a graph. It is designed to be flexible and extensible, allowing you to define how data is collected and modeled as a graph. It uses a pipeline-based approach to define how data is collected and processed, and it provides a way to define how the graph should be updated when the schema changes.
+  **[Amazon Neptune MCP Query Servers](https://github.com/aws-samples/amazon-neptune-generative-ai-samples/blob/main/neptune-mcp-servers/neptune-query/README.md)**   –   Model Context Protocol (MCP) server for Amazon Neptune that supports both Neptune Database and Neptune Analytics by providing the ability to run graph queries (openCypher and Gremlin) as well as fetch the graph schema.
+  **[Amazon Neptune MCP Memory Servers](https://github.com/aws-samples/amazon-neptune-generative-ai-samples/blob/main/neptune-mcp-servers/neptune-memory/README.md)**   –   Model Context Protocol (MCP) server for Amazon Neptune that provides memory to agents, stored in a knowledge graph against Amazon Neptune.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/working-with-network-access-scopes.html
---

# Network Access Scopes in Network Access Analyzer
<a name="working-with-network-access-scopes"></a>

With Network Access Analyzer, you can specify your network access requirements by using Network Access Scopes. A Network Access Scope defines outbound and inbound traffic patterns, including sources, destinations, paths, and traffic types. Each Network Access Scope consists of one or more match conditions, and zero or more exclusion conditions.

When you start an analysis on a Network Access Scope, Network Access Analyzer produces findings. It identifies network paths in the Network Access Scope that match at least one of the match conditions, and none of the exclude conditions. By combining match and exclude conditions, you can refine the findings produced by Network Access Analyzer to identify unexpected connectivity in your network.

Match and exclude conditions have similar structures. They consist of resource statements and packet header statements that specify the network traffic to match or exclude.

**Topics**
+ [Resource statements](resource-statement.md)
+ [Packet header statements](packet-header-statement.md)
+ [Match conditions](match-paths.md)
+ [Exclusion conditions](exclude-paths.md)
+ [Example Network Access Scopes](example-scopes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

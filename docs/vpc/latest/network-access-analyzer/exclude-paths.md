---
source_url: https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/exclude-paths.html
---

# Exclusion conditions in Network Access Analyzer
<a name="exclude-paths"></a>

A Network Access Scope produces findings only for paths that match at least one match condition, but do not match any exclusion conditions.

An exclusion condition can contain source, destination, and through fields. Each field is optional, but you must specify at least one field. Each source and destination can include a resource statement, a packet header statement, or both.

A through entry contains exactly one element that contains a resource statement. It excludes paths that contain the specified network component anywhere along the path, not just at the beginning or end. You can use a through entry in combination with a source, a destination, or both a source and a destination.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

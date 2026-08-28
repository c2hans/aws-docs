---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/entity-profiles.html
---

# Analyzing entities in Amazon Detective
<a name="entity-profiles"></a>

An entity is a single object extracted from the source data. Examples include a specific IP address, Amazon EC2 instance, or AWS account. For a list of entity types, see [Types of entities in the behavior graph data structure](graph-data-structure-overview.md#entity-types).

An Amazon Detective entity profile is a single page that provides detailed information about the entity and its activity. You might use an entity profile to get supporting details for an investigation into a finding or as part of a general hunt for suspicious activity.

**Topics**
+ [Using entity profiles](using-entity-profiles.md)
+ [Viewing and interacting with Detective profile panels](profile-panels.md)
+ [Navigating directly to an entity profile or finding overview](navigate-to-profile.md)
+ [Pivoting from a profile panel to another console](profile-panel-console-links.md)
+ [Exploring activity details on a profile panel](profile-panel-drilldown.md)
+ [Managing the scope time](scope-time-managing.md)
+ [Viewing details for associated findings in Detective](entity-finding-list.md)
+ [Viewing details for high-volume entities in Detective](high-volume-entities.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

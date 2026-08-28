---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.2.html
---

# Amazon Neptune Engine Version 1.0.1.2 (2020-06-10)
<a name="engine-releases-1.0.1.2"></a>

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED
<a name="engine-releases-1.0.1.2-deprecation"></a>

Starting from 2021-04-27, no new instances using this engine version will be created.

## Improvements in This Engine Release
<a name="engine-releases-1.0.1.2-improvements"></a>
+ Neptune now raises an `IllegalArgumentException` if you try to access a non-existent property, vertex, or edge. Previously, Neptune raised an `UnsupportedOperationException` in that situation.

  For example, if you try to add an edge referencing a nonexistent vertex, you will now raise an `IllegalArgumentException`.

## Defects Fixed in This Engine Release
<a name="engine-releases-1.0.1.2-defects"></a>
+ Fixed a bug where dictionary and user transaction commits were out of order when two `value->id` mappings were being inserted concurrently.
+ Fixed a bug in load-status serialization.
+ Fixed a stochastic failure in server startup which delayed instance creation.
+ Fixed a cursor leak.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.0.1.2-query-versions"></a>

Before upgrading a DB cluster to version 1.0.1.2, make sure that your project is compatible with these query-language versions:
+ *Gremlin version:* `3.4.1`
+ *SPARQL version:* `1.1`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

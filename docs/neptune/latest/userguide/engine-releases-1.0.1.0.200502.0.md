---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200502.0.html
---

# Amazon Neptune Engine Updates 2019-10-31
<a name="engine-releases-1.0.1.0.200502.0"></a>

**Version:** 1.0.1.0.200502.0

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED
<a name="engine-releases-1.0.1.0.200502.0-deprecation"></a>

No new instances using this engine version will be created, beginning 2021-04-27.

## Defects Fixed in This Engine Release
<a name="engine-releases-200502-defects"></a>
+ Fixed a Gremlin bug in the serialization of the `tree()` step's response when clients connect to Neptune using `traversal().withRemote(...)` (in other words, using GLV bytecode).

  This release addresses an issue in which clients who connected to Neptune using `traversal().withRemote(...)` received an invalid response to Gremlin queries that contained a `tree()` step.
+ Fixed a SPARQL bug in `DELETE WHERE LIMIT` queries, in which the query termination process would hang because of a race condition, causing the query to time out.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

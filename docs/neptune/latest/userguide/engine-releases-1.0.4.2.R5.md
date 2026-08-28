---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.R5.html
---

# Amazon Neptune Engine Version 1.0.4.2.R5 (2021-08-16)
<a name="engine-releases-1.0.4.2.R5"></a>

As of 2021-08-16, engine version 1.0.4.2.R5 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## Defects Fixed in This Engine Release
<a name="engine-releases-1.0.4.2.R5-defects"></a>
+ Disabled an optimization made in [engine release `1.0.4.2.R4`](engine-releases-1.0.4.2.R4.md) that made the [Neptune lookup cache](feature-overview-lookup-cache.md) survive engine restarts on replicas. Replica restarts now clear the lookup cache.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.0.4.2.R5-query-versions"></a>

Before upgrading a DB cluster to version 1.0.4.2.R5, make sure that your project is compatible with these query-language versions:
+ *Gremlin version:* `3.4.10`
+ *SPARQL version:* `1.1`

## Upgrade Paths to Engine Release 1.0.4.2.R5
<a name="engine-releases-1.0.4.2.R5-upgrade-paths"></a>

Your cluster will be upgraded to this patch release automatically during your next maintenance window if you are running engine version `1.0.4.2`.

You can manually upgrade any previous Neptune engine release to this release.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

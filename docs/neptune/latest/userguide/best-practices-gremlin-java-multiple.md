---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-multiple.html
---

# Add multiple read replica endpoints to a Gremlin Java connection pool
<a name="best-practices-gremlin-java-multiple"></a>

When creating a Gremlin Java `Cluster` object, you can use the `.addContactPoint()` method to add multiple read replica instances to the connection pool's contact points.

```
Cluster.Builder readerBuilder = Cluster.build()
          .port(8182)
          .minConnectionPoolSize(…)
          .maxConnectionPoolSize(…)
          ………
          .addContactPoint("{{reader-endpoint-1}}")
          .addContactPoint("{{reader-endpoint-2}}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

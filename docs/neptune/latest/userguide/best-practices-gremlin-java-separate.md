---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-separate.html
---

# Create separate Gremlin Java client objects for read and write endpoints
<a name="best-practices-gremlin-java-separate"></a>

You can increase performance by only performing writes on the writer endpoint and reading from one or more read-only endpoints.

```
Client readerClient = Cluster.build("https://{{reader-endpoint}}")
          ...
          .connect()

Client writerClient = Cluster.build("https://{{writer-endpoint}}")
          ...
          .connect()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

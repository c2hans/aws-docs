---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-disable-dns-caching.html
---

# Disable DNS caching in the Java Virtual Machine
<a name="best-practices-gremlin-java-disable-dns-caching"></a>

In an environment where you want to load-balance requests across multiple read replicas, you need to disable DNS caching in the Java Virtual Machine (JVM) and provide Neptune's reader endpoint while creating the [Cluster object](https://tinkerpop.apache.org/javadocs/current/core/org/apache/tinkerpop/gremlin/driver/Cluster.html). Disabling the JVM DNS cache ensures that DNS is resolved again for every new connection so that the requests are distributed across all of the read replicas. You can do this in your application's initialization code with the following line:

```
java.security.Security.setProperty("networkaddress.cache.ttl", "0");
```

However, a more complete and robust solution for load-balancing is provided by the [Amazon Gremlin Java client code](https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-gremlin-client) on GitHub. The Amazon Java Gremlin client is aware of your cluster topology and fairly distributes connections and requests across a set of instances in your Neptune cluster. See [this blog post](https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/) for a sample Java Lambda function that uses that client.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

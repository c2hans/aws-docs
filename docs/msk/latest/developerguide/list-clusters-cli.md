---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/list-clusters-cli.html
---

# List clusters using the AWS CLI
<a name="list-clusters-cli"></a>

To get a bootstrap broker for an Amazon MSK cluster, you need the cluster Amazon Resource Name (ARN). If you don't have the ARN for your cluster, you can find it by listing all clusters. See [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).

```
aws kafka list-clusters
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

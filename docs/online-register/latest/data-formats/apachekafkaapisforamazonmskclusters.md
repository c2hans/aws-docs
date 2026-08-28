---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/apachekafkaapisforamazonmskclusters.html
---

# Data retrieval APIs for Apache Kafka APIs for Amazon MSK clusters
<a name="apachekafkaapisforamazonmskclusters"></a>

Apache Kafka APIs for Amazon MSK clusters provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="kafka-cluster-DescribeCluster"></a>[DescribeCluster](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Describe various aspects of the cluster, equivalent to Apache Kafka's DESCRIBE CLUSTER ACL | List |
| <a name="kafka-cluster-DescribeClusterDynamicConfiguration"></a>[DescribeClusterDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Describe the dynamic configuration of a cluster, equivalent to Apache Kafka's DESCRIBE\_CONFIGS CLUSTER ACL | List |
| <a name="kafka-cluster-DescribeGroup"></a>[DescribeGroup](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Describe groups on a cluster, equivalent to Apache Kafka's DESCRIBE GROUP ACL | List |
| <a name="kafka-cluster-DescribeTopic"></a>[DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Describe topics on a cluster, equivalent to Apache Kafka's DESCRIBE TOPIC ACL | List |
| <a name="kafka-cluster-DescribeTopicDynamicConfiguration"></a>[DescribeTopicDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Describe the dynamic configuration of topics on a cluster, equivalent to Apache Kafka's DESCRIBE\_CONFIGS TOPIC ACL | List |
| <a name="kafka-cluster-DescribeTransactionalId"></a>[DescribeTransactionalId](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Describe transactional IDs on a cluster, equivalent to Apache Kafka's DESCRIBE TRANSACTIONAL\_ID ACL | List |
| <a name="kafka-cluster-ReadData"></a>[ReadData](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions) | Read data from topics on a cluster, equivalent to Apache Kafka's READ TOPIC ACL | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

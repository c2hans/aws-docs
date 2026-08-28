---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption-cluster-create.html
---

# Specify encryption settings when creating a Amazon MSK cluster
<a name="msk-working-with-encryption-cluster-create"></a>

This process describes how to specify encryption settings when creating a Amazon MSK cluster.

**Specify encryption settings when creating a cluster**

1. Save the contents of the previous example in a file and give the file any name that you want. For example, call it `encryption-settings.json`.

1. Run the `create-cluster` command and use the `encryption-info` option to point to the file where you saved your configuration JSON. The following is an example. Replace {{{YOUR MSK VERSION}}} with a version that matches the Apache Kafka client version. For information on how to find your MSK cluster version, see [Determining your MSK cluster version](create-topic.md#find-msk-cluster-version). Be aware that using an Apache Kafka client version that is not the same as your MSK cluster version may lead to Apache Kafka data corruption, loss and down time.

   ```
   aws kafka create-cluster --cluster-name "ExampleClusterName" --broker-node-group-info file://brokernodegroupinfo.json --encryption-info file://encryptioninfo.json --kafka-version "{{{YOUR MSK VERSION}}}" --number-of-broker-nodes 3
   ```

   The following is an example of a successful response after running this command.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/SecondTLSTest/abcdabcd-1234-abcd-1234-abcd123e8e8e",
       "ClusterName": "ExampleClusterName",
       "State": "CREATING"
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

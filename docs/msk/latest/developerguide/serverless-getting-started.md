---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/serverless-getting-started.html
---

# Use MSK Serverless clusters
<a name="serverless-getting-started"></a>

This tutorial shows you an example of how you can create an MSK Serverless cluster, create a client machine that can access it, and use the client to create topics on the cluster and to write data to those topics. This exercise doesn't represent all the options that you can choose when you create a serverless cluster. In different parts of this exercise, we choose default options for simplicity. This doesn't mean that they're the only options that work for setting up a serverless cluster. You can also use the AWS CLI or the Amazon MSK API. For more information, see the [Amazon MSK API Reference 2.0](https://docs.aws.amazon.com/MSK/2.0/APIReference/what-is-msk.html).

**Topics**
+ [Create an MSK Serverless cluster](create-serverless-cluster.md)
+ [Create an IAM role for topics on MSK Serverless cluster](create-iam-role.md)
+ [Create a client machine to access MSK Serverless cluster](create-serverless-cluster-client.md)
+ [Create an Apache Kafka topic](msk-serverless-create-topic.md)
+ [Produce and consume data in MSK Serverless](msk-serverless-produce-consume.md)
+ [Delete resources that you created for MSK Serverless](delete-resources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

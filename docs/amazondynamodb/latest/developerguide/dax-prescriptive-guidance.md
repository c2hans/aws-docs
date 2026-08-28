---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-prescriptive-guidance.html
---

# Prescriptive guidance to integrate DAX with DynamoDB applications
<a name="dax-prescriptive-guidance"></a>

[DynamoDB Accelerator](DAX.md) (DAX), is a DynamoDB-compatible caching service that provides fast in-memory performance for demanding applications, such as read-heavy applications. Using DAX, you can achieve response times in microseconds for accessing frequently requested data. This DynamoDB Accelerator prescriptive guide provides comprehensive insights and best practices for integrating DAX with your DynamoDB applications.

This guide provides foundational knowledge for those who are new to DAX or want to optimize their existing configurations. This guide covers various topics, for example, when to use DAX and creating a [DAX cluster](DAX.concepts.cluster.md#DAX.concepts.clusters). It also includes practical examples and detailed explanations to help you effectively implement DAX in your projects. Finally, this guide offers advanced strategies that you need to implement to maximize DAX caching capabilities for ensuring fast and scalable applications.

**Topics**
+ [Evaluating the suitability of DAX for your use cases](evaluate-dax-suitability.md)
+ [Configuring your DAX client](dax-config-dax-client.md)
+ [Configuring your DAX cluster](dax-config-considerations.md)
+ [Sizing your DAX cluster](dax-cluster-sizing.md)
+ [Deploying a cluster](dax-deploy-cluster.md)
+ [Managing cluster operations](dax-cluster-operations.md)
+ [Monitoring DAX](pres-guide-monitor-dax.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

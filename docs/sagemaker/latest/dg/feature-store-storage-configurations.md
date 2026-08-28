---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations.html
---

# Feature Store storage configurations
<a name="feature-store-storage-configurations"></a>

Amazon SageMaker Feature Store consists of an online store and an offline store. The online store enables real-time lookup of features for inference, while the offline store contains historical data for model training and batch inference. When creating a feature group, you have the option of enabling either the online store, offline store, or both. When you enable both, they sync to avoid discrepancies between training and serving data. For more information about the online and offline stores and other Feature Store concepts, see [Feature Store concepts](feature-store-concepts.md).

The following topics discuss online store storage types and offline store table formats.

**Topics**
+ [Online store](feature-store-storage-configurations-online-store.md)
+ [Offline store](feature-store-storage-configurations-offline-store.md)
+ [Throughput modes](feature-store-throughput-mode.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

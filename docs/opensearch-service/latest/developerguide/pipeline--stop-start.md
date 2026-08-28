---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop-start.html
---

# Managing Amazon OpenSearch Ingestion pipeline costs
<a name="pipeline--stop-start"></a>

You can start and stop ingestion pipelines in Amazon OpenSearch Ingestion to control data flow based on your needs. Stopping a pipeline halts data processing while preserving configurations, so you can restart it without reconfiguring it. This can help optimize costs, manage resource usage, or troubleshoot issues. When you stop a pipeline, OpenSearch Ingestion doesn't process incoming data, but previously ingested data remains available in OpenSearch.

Starting and stopping simplifies the setup and teardown processes for pipelines that you use for development, testing, or similar activities that don't require continuous availability. While your pipeline is stopped, you aren't charged for any Ingestion OCU hours. You can still update stopped pipelines, and they receive automatic minor version updates and security patches.

Stopping and starting a pipeline will result in reprocessing all the data from the beginning for pull based pipelines (DDB, S3, DocDB, etc). When you stop a pipeline, any service-managed VPC endpoints created by the pipeline are removed. For pipelines with self-managed VPC endpoints, you must recreate the VPC endpoint in your account when you restart the pipeline. For more information, see [Self-managed VPC endpoints](pipeline-security.md#pipeline-vpc-self-managed).

**Note**
If your pipeline has excess capacity but needs to remain operational, consider adjusting its maximum capacity limits rather than stopping and restarting it. This can help manage costs while ensuring that the pipeline continues processing data efficiently. For more details, see [Scaling pipelines in Amazon OpenSearch Ingestion](ingestion-scaling.md).

The following topics explain how to start and stop pipelines using the AWS Management Console, AWS CLI, and OpenSearch Ingestion API.

**Topics**
+ [Stopping an Amazon OpenSearch Ingestion pipeline](pipeline--stop.md)
+ [Starting an Amazon OpenSearch Ingestion pipeline](pipeline--start.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

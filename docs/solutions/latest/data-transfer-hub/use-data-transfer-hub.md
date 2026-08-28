---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/use-data-transfer-hub.html
---

# Use Data Transfer Hub
<a name="use-data-transfer-hub"></a>

 This guide provides detailed instructions to perform these tasks:
+ [Create an Amazon S3 transfer task ]()
+  [Create an Amazon ECR transfer task]()
+  [Transfer Amazon S3 object from Alibaba Cloud OSS]()
+  [Transfer Amazon S3 object via Direct Connect]()

## Transferring data cross China Partition
<a name="transferring-data-cross-china-partition"></a>

 Any data moving out and into the Chinese Partition for AWS has to go through the Chinese Great Firewall. This Great Firewall monitors the content and the size of the data being transferred. If you have too few instances, and are transferring terabytes of data, then that Firewall will block those IP's tied to those few instances. For large use cases of this solution where you might be transferring terabytes of data across Partition, we recommend you spin up multiple instances 200\+ and in order to avoid CPU/Memory issues, we recommend using a larger instance type for the AutoScale Group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

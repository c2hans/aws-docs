---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/writing-with-msk.html
---

# Configure source settings for Amazon MSK
<a name="writing-with-msk"></a>

When you choose Amazon MSK to send information to a Firehose stream, you can choose between MSK provisioned and MSK-Serverless clusters. You can then use Firehose to read data easily from a specific Amazon MSK cluster and topic and load it into the specified S3 destination.

In the **Source settings** section of the page, provide values for the following fields.

****Amazon MSK cluster connectivity****
Choose either the **Private bootstrap brokers** (recommended) or **Public bootstrap brokers** option based on your cluster configuration. Bootstrap brokers is what Apache Kafka client uses as a starting point to connect to the cluster. Public bootstrap brokers are intended for public access from outside of AWS, while private bootstrap brokers are intended for access from within AWS. For more information about Amazon MSK, see [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html).
To connect to a provisioned or serverless Amazon MSK cluster through private bootstrap brokers, the cluster must meet all of the following requirements.
+ The cluster must be active.
+ The cluster must have IAM as one of its access control methods.
+ Multi-VPC private connectivity must be enabled for the IAM access control method.
+ You must add to this cluster a resource-based policy which grants Firehose service principal the permission to invoke the Amazon MSK `CreateVpcConnection` API operation.
To connect to a provisioned Amazon MSK cluster through public bootstrap brokers, the cluster must meet all of the following requirements.
+ The cluster must be active.
+ The cluster must have IAM as one of its access control methods.
+ The cluster must be public-accessible.

****MSK cluster account****
You can choose the account where the Amazon MSK cluster resides. This can be one of the following.
+ **Current account** – Allows you to ingest data from an MSK cluster in the current AWS account. For this, you must specify the ARN of the Amazon MSK cluster from where your Firehose stream will read data.
+ **Cross-account** – Allows you to ingest data from an MSK cluster in another AWS account. For more information, see [Cross-account delivery from Amazon MSK](controlling-access.md#cross-account-delivery-msk).

****Topic****
Specify the Apache Kafka topic from which you want your Firehose stream to ingest data. You cannot update this topic after Firehose stream creation completes.
Firehose automatically decompresses Apache Kafka messages.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

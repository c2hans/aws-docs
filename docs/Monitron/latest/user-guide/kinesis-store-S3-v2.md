---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/kinesis-store-S3-v2.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Storing exported data in Amazon S3
<a name="kinesis-store-S3-v2"></a>

If you want to store your exported data in Amazon S3, use the following procedure.

**Topics**
+ [Configuring Kinesis manually in the console](#kinesis-configure-console-v2)

## Configuring Kinesis manually in the console
<a name="kinesis-configure-console-v2"></a>

1. Sign in to the AWS Management Console and open the Kinesis console at https://console.aws.amazon.com/kinesis.

1. Choose **Delivery streams** in the navigation pane.

1. Choose **Create delivery stream**.

1. For Source, select **Amazon Kinesis Data Streams**.

1. For Destination, select **Amazon S3**.

1. Under **Source settings, Kinesis data stream**, enter the ARN of your Kinesis data stream.

1. Under **delivery stream name**, enter the name of your Kinesis data stream.

1. Under **Desination settings**, choose an Amazon S3 bucket or enter a bucket URI.

1. (optional) Enable dynamic partitioning using inline parsing for JSON. This option is appropriate if you want to partition streaming measurement data based on source information and timestamp. For example:
   + Choose **Enabled** for **Dynamic partitioning**.
   + Choose **Enabled** for **New line delimiter**.
   + Choose **Enabled** for **Inline parsing for JSON**.
   + Under **Dynamic partitioning keys**, add:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Monitron/latest/user-guide/kinesis-store-S3-v2.html)

1. Choose **Apply dynamic partitioning keys** and confirm the generated Amazon S3 bucket prefix is `!{partitionKeyFromQuery:project}/!{partitionKeyFromQuery:site}/!{partitionKeyFromQuery:time}/`.

1. In Amazon S3, objects will use the following key format: `/project={projectName}/site={siteName}/time={yyyy-mm-dd 00:00:00}/{filename}`.

1. Choose **Create delivery stream**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

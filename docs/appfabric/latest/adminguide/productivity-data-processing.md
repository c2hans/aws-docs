---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/productivity-data-processing.html
---

# Data processing in AppFabric
<a name="productivity-data-processing"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

AppFabric takes steps to store user content individually, in an Amazon S3 bucket managed by AppFabric, and separately; which helps ensure that we generate user-specific insights. We use reasonable safeguards to protect your content, which can include encryption at-rest and in-transit. We've configured our systems to delete customer content automatically within 30 days from ingestion. AppFabric does not generate insights using data artifacts to which a user no longer has access. For example, when a user disconnects a data source (an app), AppFabric stops collecting data from that app and does not use any lingering artifacts from the disconnected apps to generate insights. AppFabric’s systems are configured to delete such data within 30 days.

AppFabric does not use user content to train or improve the underlying large language models used to generate insights. For more information about AppFabric's generative AI feature, see [Amazon Bedrock FAQs](https://aws.amazon.com/bedrock/faqs/).

## Encryption at rest
<a name="ahead-encryption-at-rest"></a>

AWS AppFabric supports encryption at rest, a server-side encryption feature in which AppFabric transparently encrypts all data related to users when it is persisted to disk, and decrypts them when you access the data.

## Encryption in transit
<a name="ahead-encryption-in-transit"></a>

AppFabric secures all content in transit using TLS 1.2 and signs API requests for AWS services with AWS Signature Version 4.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/select-and-implement-querying-mechanisms.html
---

# Select and implement querying mechanisms for logs
<a name="select-and-implement-querying-mechanisms"></a>

 In AWS, the main services you can use to query logs are [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) for data stored in CloudWatch log groups, and [Amazon Athena](https://aws.amazon.com/athena/) and [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) for data stored in Amazon S3. You can also use third-party querying tools such as a security information and event management (SIEM).

 The process for selecting a log querying tool should consider the people, process, and technology aspects of your security operations. Select a tool that fulfills operational, business, and security requirements, and is both accessible and maintainable in the long term. Keep in mind that log querying tools work optimally when the number of logs to be scanned is kept within the tool’s limits. It is not uncommon for customers to have multiple querying tools because of cost or technical constraints. For example, customers might use a third-party SIEM to perform queries for the last 90 days of data, and use Athena to perform queries beyond 90 days because of the log ingestion cost of a SIEM. No matter the implementation, verify that your approach minimizes the number of tools required to maximize operational efficiency, especially during a security event investigation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

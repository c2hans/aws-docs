---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aosops03-bp03.html
---

# AOSOPS03-BP03 Enable search and indexing slow log functionality
<a name="aosops03-bp03"></a>

 Turn on slow log functionality to gain insights into query latency and optimize search and indexing operations.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome**: You use slow logs for search and indexing operations, providing a detailed view of query latency and enabling optimization efforts.

 **Benefits of establishing this best practice:**
+  **Optimize queries:** Slow logs provide detailed information about slow or long-running queries, which helps you identify areas for optimization and make changes to improve performance.
+  **Troubleshoot issues:** By capturing logs of slow searches, indexing operations, and other queries, slow logs help you troubleshoot issues more effectively, reducing downtime and improving overall efficiency in your OpenSearch Service domains.

## Implementation guidance
<a name="implementation-guidance-7"></a>

 Search slow logs, indexing slow logs, and error logs are valuable for diagnosing performance and stability issues. Audit logs record user activity for compliance purposes.

 For a detailed guide on enabling logging slow index and search operations, see [AOSPERF04-BP01](aosperf04-bp01.md).

## Resources
<a name="resources-7"></a>
+  [Monitoring OpenSearch logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

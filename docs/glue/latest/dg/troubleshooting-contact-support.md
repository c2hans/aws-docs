---
source_url: https://docs.aws.amazon.com/glue/latest/dg/troubleshooting-contact-support.html
---

# Gathering AWS Glue troubleshooting information
<a name="troubleshooting-contact-support"></a>

If you encounter errors or unexpected behavior in AWS Glue and need to contact AWS Support, you should first gather information about names, IDs, and logs that are associated with the failed action. Having this information available enables Support to help you resolve the problems you're experiencing.

Along with your *account ID*, gather the following information for each of these types of failures:

**When a crawler fails, gather the following information:**
+ Crawler name

  Logs from crawler runs are located in CloudWatch Logs under `/aws-glue/crawlers`.

**When a test connection fails, gather the following information:**
+ Connection name
+ Connection ID
+ JDBC connection string in the form `jdbc:protocol://host:port/database-name`.

  Logs from test connections are located in CloudWatch Logs under ` /aws-glue/testconnection`.

**When a job fails, gather the following information:**
+ Job name
+ Job run ID in the form `jr_xxxxx`.

  Logs from job runs are located in CloudWatch Logs under ` /aws-glue/jobs`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena.html
---

# Connectivity issues when using Amazon Athena with Amazon Quick Sight
<a name="troubleshoot-athena"></a>

Following, you can find information about troubleshooting issues that you might encounter when using Amazon Athena with Amazon Quick Sight.

Before you try troubleshooting anything else for Athena, make sure that you can connect to Athena. For information about troubleshooting Athena connection issues, see [I can't connect to Amazon Athena](troubleshoot-connect-athena.md).

If you can connect but have other issues, it can be useful to run your query in the Athena console ([https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home)) before adding your query to Amazon Quick Sight. For additional troubleshooting information, see [Troubleshooting](https://docs.aws.amazon.com/athena/latest/ug/troubleshooting.html) in the *Athena User Guide*.

**Topics**
+ [Column not found when using Athena with Amazon Quick Sight](troubleshoot-athena-column-not-found.md)
+ [Invalid data when using Athena with Amazon Quick Sight](troubleshoot-athena-invalid-data.md)
+ [Query timeout when using Athena with Amazon Quick Sight](troubleshoot-athena-query-timeout.md)
+ [Staging bucket no longer exists when using Athena with Amazon Quick Sight](troubleshoot-athena-missing-bucket.md)
+ [Table incompatible when using AWS Glue with Athena in Amazon Quick Sight](troubleshoot-athena-glue-table-not-upgraded.md)
+ [Table not found when using Athena with Amazon Quick Sight](troubleshoot-athena-table-not-found.md)
+ [Workgroup and output errors when using Athena with Quick Sight](troubleshoot-athena-workgroup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

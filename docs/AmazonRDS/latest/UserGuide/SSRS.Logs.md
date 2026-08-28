---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Logs.html
---

# SSRS and PBIRS log files
<a name="SSRS.Logs"></a>

You can list, view, and download SSRS and PBIRS log files. Log files follow a naming convention of ReportServerService\_{{timestamp}}.log and are located in the `D:\rdsdbdata\Log\SSRS` directory. (The `D:\rdsdbdata\Log` directory is also the parent directory for error logs and SQL Server Agent logs.)

For existing SSRS or PBIRS instances, you might need to restart the service to access report server logs. You can restart the SSRS service by updating the `SSRS` option, or the PBIRS service by updating the `PBIRS` option.

For more information, see [Working with Amazon RDS for Microsoft SQL Server logs](Appendix.SQLServer.CommonDBATasks.Logs.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

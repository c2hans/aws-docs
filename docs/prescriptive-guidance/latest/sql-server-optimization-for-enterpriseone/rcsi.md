---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/rcsi.html
---

# Configure RCSI
<a name="rcsi"></a>

We recommend that you enable read-committed snapshot isolation (RCSI) for each EnterpriseOne database. Otherwise, you might encounter locking scenarios that affect system performance. In some cases, EnterpriseOne might revert to `*NOLOCK`, which can result in dirty read operations, if RCSI isn't in effect.

To enable RCSI, run the following command for each database, and revise the database name accordingly.

```
USE master
ALTER DATABASE JDE_Prist920 SET READ_COMMITTED_SNAPSHOT ON
GO
```

After you enable RCSI, adjust the EnterpriseOne configuration as described in My Oracle Support (MOS) note 2565588 (requires registration). The adjustments disable the SQL query timeout and disable retries with `*NOLOCK`. These settings are required when RCSI isn't enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

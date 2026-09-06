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

---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-attaching-to-remote.html
---

# Attaching to the remote RDS for Db2 DB instance
<a name="db2-attaching-to-remote"></a>

Use the following steps to attach to your remote RDS for Db2 DB instance and run `get snapshot` operations.

**To attach to the remote RDS for Db2 DB instance**

1. Run a client-side IBM Db2 CLP session. For information about cataloging your RDS for Db2 DB instance and database, see [Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 CLP](db2-connecting-with-clp-client.md). Make a note of the master username and master password for your RDS for Db2 DB instance.

1. Attach to the RDS for Db2 DB instance. In the following example, replace {{node\_name}}, {{master\_username}}, and {{master\_password}} with the TCPIP node name that you catalogued and the master username and master password for your RDS for Db2 DB instance.

   ```
   db2 attach to {{node_name}} user {{master_username}} using {{master_password}}
   ```

After attaching to the remote RDS for Db2 DB instance, you can run the following commands and other `get snapshot` commands. For more information, see [GET SNAPSHOT command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-get-snapshot) in the IBM Db2 documentation.

```
db2 list applications
db2 get snapshot for all databases
db2 get snapshot for database manager
db2 get snapshot for all applications
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

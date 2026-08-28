---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.PermissionsNonMasters.html
---

# Granting privileges to non-master users
<a name="Appendix.Oracle.CommonDBATasks.PermissionsNonMasters"></a>

You can grant select privileges for many objects in the `SYS` schema by using the `SELECT_CATALOG_ROLE` role. The `SELECT_CATALOG_ROLE` role gives users `SELECT` privileges on data dictionary views. The following example grants the role `SELECT_CATALOG_ROLE` to a user named `user1`.

```
GRANT SELECT_CATALOG_ROLE TO {{user1}};
```

You can grant `EXECUTE` privileges for many objects in the `SYS` schema by using the `EXECUTE_CATALOG_ROLE` role. The `EXECUTE_CATALOG_ROLE` role gives users `EXECUTE` privileges for packages and procedures in the data dictionary. The following example grants the role `EXECUTE_CATALOG_ROLE` to a user named *user1*.

```
GRANT EXECUTE_CATALOG_ROLE TO {{user1}};
```

The following example gets the permissions that the roles `SELECT_CATALOG_ROLE` and `EXECUTE_CATALOG_ROLE` allow.

```
  SELECT *
    FROM ROLE_TAB_PRIVS
   WHERE ROLE IN ('SELECT_CATALOG_ROLE','EXECUTE_CATALOG_ROLE')
ORDER BY ROLE, TABLE_NAME ASC;
```

The following example creates a non-master user named `user1`, grants the `CREATE SESSION` privilege, and grants the `SELECT` privilege on a table named *sh.sales*.

```
CREATE USER {{user1}} IDENTIFIED BY PASSWORD;
GRANT CREATE SESSION TO {{user1}};
GRANT SELECT ON {{sh.sales}} TO {{user1}};
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

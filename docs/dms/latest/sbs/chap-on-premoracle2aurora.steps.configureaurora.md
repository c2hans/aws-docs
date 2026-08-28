---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.configureaurora.html
---

# Step 2: Configure Your Aurora Target Database
<a name="chap-on-premoracle2aurora.steps.configureaurora"></a>

As with your source database, it’s a good idea to restrict access of the user you’re connecting with. You can also create a temporary user that you can remove after the migration.

```
CREATE USER 'dms_user'@'%' IDENTIFIED BY 'dms_user';
GRANT ALTER, CREATE, DROP, INDEX, INSERT, UPDATE, DELETE,
SELECT ON <target database(s)>.* TO 'dms_user'@'%';
```

 AWS DMS uses some control tables on the target in the database awsdms\_control. The following command ensures that your dms\_user has the necessary access to the `awsdms_control` database:

```
GRANT ALL PRIVILEGES ON awsdms_control.* TO 'dms_user'@'%';
flush privileges;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/chap-oracle-aurora-pg.special.inlineviews.html
---

# Inline views
<a name="chap-oracle-aurora-pg.special.inlineviews"></a>

With AWS DMS, you can create and use inline views to streamline data transformations during migration tasks. An inline view is a subquery that acts as a virtual table, allowing you to combine and manipulate data from multiple sources without creating a persistent database object.

| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences |
| --- | --- | --- | --- |
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-5.png)  | N/A | N/A |

## Oracle usage
<a name="chap-oracle-aurora-pg.special.inlineviews.ora"></a>

Inline views refer to a `SELECT` statement located in the `FROM` clause of secondary `SELECT` statement. Inline views can help make complex queries simpler by removing compound calculations or eliminating join operations while condensing several separate queries into a single simplified query.

 **Examples**

The SQL statement marked in red represents the inline view code. The query returns each employee matched to their salary and department id. In addition, the query returns the average salary for each department using the inline view column `SAL_AVG`.

```
SELECT A.LAST_NAME, A.SALARY, A.DEPARTMENT_ID, B.SAL_AVG
FROM EMPLOYEES A,
(SELECT DEPARTMENT_ID, ROUND(AVG(SALARY))
AS SAL_AVG FROM EMPLOYEES GROUP BY DEPARTMENT_ID)
WHERE A.DEPARTMENT_ID = B.DEPARTMENT_ID;
```

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.special.inlineviews.pg"></a>

PostgreSQL semantics may refer to inline views as Subselect or as Subquery. In either case, the functionality is the same. Running the Oracle inline view example above, as is, will result in an error: **ERROR: subquery in FROM must have an alias**. This is because Oracle supports omitting aliases for the inner statement while in PostgreSQL the use of aliases is mandatory. The following example uses `B` as an alias.

Mandatory aliases are the only major difference when migrating Oracle inline views to PostgreSQL.

 **Examples**

The following example uses `B` as an alias.

```
SELECT A.LAST_NAME, A.SALARY, A.DEPARTMENT_ID, B.SAL_AVG
FROM EMPLOYEES A,
(SELECT DEPARTMENT_ID, ROUND(AVG(SALARY)) AS SAL_AVG
FROM EMPLOYEES GROUP BY DEPARTMENT_ID) B
WHERE A.DEPARTMENT_ID = B.DEPARTMENT_ID;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

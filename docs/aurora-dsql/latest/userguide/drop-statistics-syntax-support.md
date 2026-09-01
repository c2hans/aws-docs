---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/userguide/drop-statistics-syntax-support.html
---

# `DROP STATISTICS`
<a name="drop-statistics-syntax-support"></a>

## Supported syntax
<a name="drop-statistics-supported-syntax"></a>

```
DROP STATISTICS [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description
<a name="drop-statistics-description"></a>

`DROP STATISTICS` removes statistics object(s) from the database. Only the statistics object's owner, the schema owner, or a superuser can drop a statistics object.

## Parameters
<a name="drop-statistics-parameters"></a>

**`IF EXISTS`**
Do not throw an error if the statistics object does not exist. A notice is issued in this case.

**{{name}}**
The name (optionally schema-qualified) of the statistics object to drop.

**`CASCADE``RESTRICT`**
These key words do not have any effect, since there are no dependencies on statistics.

## Examples
<a name="drop-statistics-examples"></a>

To destroy two statistics objects in different schemas, without failing if they don't exist:

```
DROP STATISTICS IF EXISTS
    accounting.users_uid_creation,
    public.grants_user_role;
```

## Compatibility
<a name="drop-statistics-compatibility"></a>

There is no `DROP STATISTICS` command in the SQL standard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

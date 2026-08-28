---
source_url: https://docs.aws.amazon.com/athena/latest/ug/show-databases.html
---

# SHOW DATABASES
<a name="show-databases"></a>

Lists all databases defined in the metastore. You can use `DATABASES` or `SCHEMAS`. They mean the same thing.

The programmatic equivalent of `SHOW DATABASES` is the [ListDatabases](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListDatabases.html) Athena API action. The equivalent method in AWS SDK for Python (Boto3) is [list\_databases](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/client/list_databases.html).

## Synopsis
<a name="synopsis"></a>

```
SHOW {DATABASES | SCHEMAS} [LIKE '{{regular_expression}}']
```

## Parameters
<a name="parameters"></a>

**[LIKE '{{regular\_expression}}']**
Filters the list of databases to those that match the `{{regular_expression}}` that you specify. For wildcard character matching, you can use the combination `.*`, which matches any character zero to unlimited times.

## Examples
<a name="examples"></a>

```
SHOW SCHEMAS;
```

```
SHOW DATABASES LIKE '.*analytics';
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

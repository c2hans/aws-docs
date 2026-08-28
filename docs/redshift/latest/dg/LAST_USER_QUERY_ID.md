---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/LAST_USER_QUERY_ID.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# LAST\_USER\_QUERY\_ID
<a name="LAST_USER_QUERY_ID"></a>

Returns the query ID of the most recently completed user query in the current session. If no queries have been run in the current session, last\_user\_query\_id returns -1. The function does not return the query ID for queries that run exclusively on the leader node. For more information, see [Leader node–only functions](c_SQL_functions_leader_node_only.md).

## Syntax
<a name="LAST_USER_QUERY_ID-synopsis"></a>

```
last_user_query_id()
```

## Return type
<a name="LAST_USER_QUERY_ID-return-type"></a>

Returns an integer.

## Example
<a name="LAST_USER_QUERY_ID-example"></a>

The following query returns the ID of the latest query run by a user completed in the current session.

```
select last_user_query_id();
```

Results are the following.

```
last_user_query_id
-----------------------
    5437
(1 row)
```

The following query returns the query ID and text of the most recently completed query run by a user in the current session.

```
select query_id, query_text from sys_query_history where query_id = last_user_query_id();
```

Results are the following.

```
 query_id, query_text
---------+-------------------------------------------------------------------------------------------------------------
 5556975 | select last_user_query_id() limit 100 --RequestID=<unique request ID>; TraceID=<unique trace ID>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

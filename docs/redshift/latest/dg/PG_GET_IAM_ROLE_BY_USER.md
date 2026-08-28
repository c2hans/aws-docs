---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/PG_GET_IAM_ROLE_BY_USER.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# PG\_GET\_IAM\_ROLE\_BY\_USER
<a name="PG_GET_IAM_ROLE_BY_USER"></a>

Returns all IAM roles and command privileges granted to a user.

## Syntax
<a name="PG_GET_IAM_ROLE_BY_USER-synopsis"></a>

```
pg_get_iam_role_by_user('name')
```

## Arguments
<a name="PG_GET_IAM_ROLE_BY_USER-arguments"></a>

 *name*
The name of the user for which to return IAM roles.

## Return type
<a name="PG_GET_IAM_ROLE_BY_USER-return-type"></a>

VARCHAR

## Usage notes
<a name="PG_GET_IAM_ROLE_BY_USER-usage-notes"></a>

The PG\_GET\_IAM\_ROLE\_BY\_USER function returns one row for each set of roles and command privileges. The row contains a comma-separated list with the user name, IAM role, and command.

A value of `default` in the result indicates that the user can specify any available role to perform the displayed command.

You must be a superuser to use this function.

## Example
<a name="PG_GET_IAM_ROLE_BY_USER-example"></a>

The following example indicates that user `reg_user1` can specify any available IAM role to perform COPY operations. The user can also specify the `Redshift-S3-Write` role for UNLOAD operations.

```
select pg_get_iam_role_by_user('reg_user1');
```

```
                             pg_get_iam_role_by_user
---------------------------------------------------------------------------------
 (reg_user1,default,COPY)
 (reg_user1,arn:aws:iam::123456789012:role/Redshift-S3-Write,COPY|UNLOAD)
```

The following example of the PG\_GET\_IAM\_ROLE\_BY\_USER function formats the result as a table.

```
select username, iam_role, cmd FROM pg_get_iam_role_by_user('reg_user1') res_iam_role(username text, iam_role text, cmd text);
```

```
 username  |                    iam_role                     | cmd
-----------+-------------------------------------------------+------
 reg_user1 | default                                         | None
 reg_user1 | arn:aws:iam::123456789012:role/Redshift-S3-Read | COPY
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

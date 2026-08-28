---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_RLS_POLICY.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# DROP RLS POLICY
<a name="r_DROP_RLS_POLICY"></a>

Drops a row-level security policy for all tables in all databases.

Superusers and users or roles that have the sys:secadmin role can drop a policy.

## Syntax
<a name="r_DROP_RLS_POLICY-synopsis"></a>

```
DROP RLS POLICY [ IF EXISTS ]
{ policy_name | database_name.policy_name }
[ CASCADE | RESTRICT ]
```

## Parameters
<a name="r_DROP_RLS_POLICY-parameters"></a>

 *IF EXISTS*
A clause that indicates if the specified policy already exists.

 *policy\_name*
The name of the policy.

database\_name
The name of the database from where the policy to be dropped. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

 *CASCADE*
A clause that indicates to automatically detach the policy from all attached tables before dropping the policy.

 *RESTRICT*
A clause that indicates not to drop the policy when it is attached to some tables. This is the default.

For the usage of DROP RLS POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).

## Examples
<a name="r_DROP_RLS_POLICY-examples"></a>

The following example drops the row-level security policy.

```
DROP RLS POLICY policy_concerts;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/udf-security-and-privileges.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# UDF security and permissions
<a name="udf-security-and-privileges"></a>

To create a UDF, you must have permission for usage on language for SQL or plpythonu (Python). By default, USAGE ON LANGUAGE SQL is granted to PUBLIC, but you must explicitly grant USAGE ON LANGUAGE PLPYTHONU to specific users or groups.

To revoke usage for SQL, first revoke usage from PUBLIC. Then grant usage on SQL only to the specific users or groups permitted to create SQL UDFs. The following example revokes usage on SQL from PUBLIC. Then it grants usage to the user group `udf_devs`.

```
revoke usage on language sql from PUBLIC;
grant usage on language sql to group udf_devs;
```

To run a UDF, you must have permission to do so for each function. By default, permission to run new UDFs is granted to PUBLIC. To restrict usage, revoke this permission from PUBLIC for the function. Then grant the privilege to specific individuals or groups.

The following example revokes execution on function `f_py_greater` from PUBLIC. Then it grants usage to the user group `udf_devs`.

```
revoke execute on function f_py_greater(a float, b float) from PUBLIC;
grant execute on function f_py_greater(a float, b float) to group udf_devs;
```

Superusers have all privileges by default.

For more information, see [GRANT](r_GRANT.md) and [REVOKE](r_REVOKE.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

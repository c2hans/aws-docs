---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_DEFAULT_IAM_ROLE.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# DEFAULT\_IAM\_ROLE
<a name="r_DEFAULT_IAM_ROLE"></a>

Returns the default IAM role currently associated with the Amazon Redshift cluster. The function returns none if there isn't any default IAM role associated.

## Syntax
<a name="r_DEFAULT_IAM_ROLE-synopsis"></a>

```
select default_iam_role();
```

## Return type
<a name="r_DEFAULT_IAM_ROLE-return-type"></a>

Returns a VARCHAR string.

## Example
<a name="r_DEFAULT_IAM_ROLE-example"></a>

The following example returns the default IAM role currently associated with the specified Amazon Redshift cluster,

```
select default_iam_role();
              default_iam_role
-----------------------------------------------
 arn:aws:iam::123456789012:role/myRedshiftRole
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

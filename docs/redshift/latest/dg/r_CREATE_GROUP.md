---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_GROUP.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# CREATE GROUP
<a name="r_CREATE_GROUP"></a>

Defines a new user group. Only a superuser can create a group.

## Syntax
<a name="r_CREATE_GROUP-synopsis"></a>

```
CREATE GROUP group_name
[ [ WITH ] [ USER username ] [, ...] ]
```

## Parameters
<a name="r_CREATE_GROUP-parameters"></a>

 *group\_name*
Name of the new user group. Group names beginning with two underscores are reserved for Amazon Redshift internal use. For more information about valid names, see [Names and identifiers](r_names.md).

WITH
Optional syntax to indicate additional parameters for CREATE GROUP.

USER
Add one or more users to the group.

 *username*
Name of the user to add to the group.

## Examples
<a name="r_CREATE_GROUP-examples"></a>

The following example creates a user group named ADMIN\_GROUP with a two users, ADMIN1 and ADMIN2.

```
create group admin_group with user admin1, admin2;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

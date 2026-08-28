---
source_url: https://docs.aws.amazon.com/athena/latest/ug/show-tblproperties.html
---

# SHOW TBLPROPERTIES
<a name="show-tblproperties"></a>

Lists table properties for the named table.

## Synopsis
<a name="synopsis"></a>

```
SHOW TBLPROPERTIES table_name [('property_name')]
```

## Parameters
<a name="parameters"></a>

**[('property\_name')]**
If included, only the value of the property named `property_name` is listed.

## Examples
<a name="examples"></a>

```
SHOW TBLPROPERTIES orders;
```

```
SHOW TBLPROPERTIES orders('comment');
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

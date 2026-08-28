---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-conversion.html
---

# Conversion functions
<a name="s3-select-sql-reference-conversion"></a>

**Important**
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Amazon S3 Select supports the following conversion function.

**Topics**
+ [CAST](#s3-select-sql-reference-cast)

## CAST
<a name="s3-select-sql-reference-cast"></a>

The `CAST` function converts an entity, such as an expression that evaluates to a single value, from one type to another.

### Syntax
<a name="s3-select-sql-reference-cast-syntax"></a>

```
CAST ( {{expression}} AS {{data_type}} )
```

### Parameters
<a name="s3-select-sql-reference-cast-parameters"></a>

 *`{{expression}}`*
A combination of one or more values, operators, and SQL functions that evaluate to a value.

 *`{{data_type}}`*
The target data type, such as `INT`, to cast the expression to. For a list of supported data types, see [Data types](s3-select-sql-reference-data-types.md).

### Examples
<a name="s3-select-sql-reference-cast-examples"></a>

```
CAST('2007-04-05T14:30Z' AS TIMESTAMP)
CAST(0.456 AS FLOAT)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

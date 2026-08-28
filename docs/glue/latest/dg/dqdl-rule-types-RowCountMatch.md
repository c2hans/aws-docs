---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-RowCountMatch.html
---

# RowCountMatch
<a name="dqdl-rule-types-RowCountMatch"></a>

Checks the ratio of the row count of the primary dataset and the row count of a reference dataset against the given expression.

**Syntax**

```
RowCountMatch {{<REFERENCE_DATASET_ALIAS>}} {{<EXPRESSION>}}
```
+ **REFERENCE\_DATASET\_ALIAS** – The alias of the reference dataset against which to compare row counts.

  **Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Row count check against a reference dataset**

The following example rule checks whether the row count of the primary dataset is at least 90% of the row count of the reference dataset.

```
RowCountMatch "reference" >= 0.9
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

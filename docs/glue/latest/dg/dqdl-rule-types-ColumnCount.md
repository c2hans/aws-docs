---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnCount.html
---

# ColumnCount
<a name="dqdl-rule-types-ColumnCount"></a>

Checks the column count of the primary dataset against a given expression. In the expression, you can specify the number of columns or a range of columns using operators like `>` and `<`.

**Syntax**

```
ColumnCount {{<EXPRESSION>}}
```
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Column count numeric check**

The following example rule checks whether the column count is within a given range.

```
ColumnCount between 10 and 20
```

**Sample dynamic rules**
+ `ColumnCount >= avg(last(10))`
+ `ColumnCount between min(last(10))-1 and max(last(10))+1`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

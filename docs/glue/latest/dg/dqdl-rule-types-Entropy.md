---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Entropy.html
---

# Entropy
<a name="dqdl-rule-types-Entropy"></a>

Checks whether the *entropy* value of a column matches a given expression. Entropy measures the level of information that's contained in a message. Given the probability distribution over values in a column, entropy describes how many bits are required to identify a value.

**Syntax**

```
Entropy {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Column entropy**

The following example rule checks that the column named `Feedback` has an entropy value greater than one.

```
Entropy "Star_Rating" > 1
Entropy "First_Name" > 1  where "Customer_ID < 10"
```

 **Sample dynamic rules**
+ `Entropy "colA" < max(last(10))`
+ `Entropy "colA" between min(last(10)) and max(last(10))`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

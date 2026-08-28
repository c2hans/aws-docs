---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_conditions.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Conditions
<a name="r_conditions"></a>

**Topics**
+ [Syntax](#r_conditions-synopsis)
+ [Comparison condition](r_comparison_condition.md)
+ [Logical conditions](r_logical_condition.md)
+ [Pattern-matching conditions](pattern-matching-conditions.md)
+ [BETWEEN range condition](r_range_condition.md)
+ [Null condition](r_null_condition.md)
+ [EXISTS condition](r_exists_condition.md)
+ [IN condition](r_in_condition.md)

 A condition is a statement of one or more expressions and logical operators that evaluates to true, false, or unknown. Conditions are also sometimes referred to as predicates.

**Note**
All string comparisons and LIKE pattern matches are case-sensitive. For example, 'A' and 'a' do not match. However, you can do a case-insensitive pattern match by using the ILIKE predicate.

## Syntax
<a name="r_conditions-synopsis"></a>

```
comparison_condition
| logical_condition
| range_condition
| pattern_matching_condition
| null_condition
| EXISTS_condition
| IN_condition
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

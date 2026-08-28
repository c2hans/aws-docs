---
source_url: https://docs.aws.amazon.com/athena/latest/ug/sorting-arrays.html
---

# Sort arrays
<a name="sorting-arrays"></a>

To create a sorted array of unique values from a set of rows, you can use the [array\_sort](https://prestodb.io/docs/current/functions/array.html#array_sort) function, as in the following example.

```
WITH
dataset AS (
  SELECT ARRAY[3,1,2,5,2,3,6,3,4,5] AS items
)
SELECT array_sort(array_agg(distinct i)) AS array_items
FROM dataset
CROSS JOIN UNNEST(items) AS t(i)
```

This query returns:

```
+--------------------+
| array_items        |
+--------------------+
| [1, 2, 3, 4, 5, 6] |
+--------------------+
```

For information about expanding an array into multiple rows, see [Flatten nested arrays](flattening-arrays.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

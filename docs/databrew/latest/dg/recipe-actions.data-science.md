---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.data-science.html
---

# Data science recipe steps
<a name="recipe-actions.data-science"></a>

Use these recipe steps to tabulate and summarize data from different perspectives, or to perform advanced transformations.

**Topics**
+ [BINARIZATION](recipe-actions.BINARIZATION.md)
+ [BUCKETIZATION](recipe-actions.BUCKETIZATION.md)
+ [CATEGORICAL\_MAPPING](recipe-actions.CATEGORICAL_MAPPING.md)
+ [ONE\_HOT\_ENCODING](recipe-actions.ONE_HOT_ENCODING.md)
+ [SCALE](#recipe-actions.SCALE)
+ [SKEWNESS](recipe-actions.SKEWNESS.md)
+ [TOKENIZATION](recipe-actions.TOKENIZATION.md)

## SCALE
<a name="recipe-actions.SCALE"></a>

Scales or normalizes the range of data in a numeric column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `strategy` – The operation to be applied to the column values:
  + `MIN_MAX` – Rescales the values into a range of [0,1]
  + `SCALE_BETWEEN` – Rescales the values into a range of 2 specified values.
  +  `MEAN_NORMALIZATION` – Rescales the data to have a mean (μ) of 0 and standard deviation (σ) of 1 within a range of [-1, 1]
  +  `Z_SCORE` – Linearly scale data values to have a mean (μ) of 0 and standard deviation (σ) of 1. Best for handling outliers.
+ `targetColumn` – The name of a column to contain the results.

**Example**

```
{
    "Action": {
        "Operation": "NORMALIZATION",
        "Parameters": {
            "sourceColumn": "all_votes",
            "strategy": "MIN_MAX",
            "targetColumn": "all_votes_normalized"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

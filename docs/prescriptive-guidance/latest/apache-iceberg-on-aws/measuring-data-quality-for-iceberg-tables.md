---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/measuring-data-quality-for-iceberg-tables.html
---

# Measuring data quality for Iceberg tables

Maintaining high data quality in Iceberg tables is essential for reliable analytics and decision‑making. Without regular measurement, data issues propagate through the pipeline and turn into wrong reports and lost trust. AWS Glue Data Quality lets you define rules — using the **Data Quality Definition Language (DQDL)** — and apply them to Iceberg tables in two complementary ways.

## At-rest data quality
<a name="at-rest-data-quality"></a>

At-rest checks run **periodic evaluations of a ruleset against an existing table**. You attach the ruleset to an Iceberg table registered in the AWS Glue Data Catalog and schedule how often it runs. Findings are surfaced as evaluation results in the Data Catalog and — via CloudWatch — in metrics and dashboards you can alarm on.

Use at-rest checks to detect drift that arises after data has already landed: missing values, out-of-range aggregates, distributional shifts, referential integrity gaps, and so on. This applies equally to self-managed Iceberg on Amazon S3 and to Amazon S3 Tables — the AWS Glue Data Catalog is the anchor in both cases.

## In-transit data quality
<a name="in-transit-data-quality"></a>

In-transit checks run **as part of an AWS Glue ETL job**, before the data is written to the target Iceberg table. You have two integration paths:
+ **Programmatic** — use the `EvaluateDataQuality` transform in the Glue Spark job code. The transform reads the DQDL ruleset, evaluates it against the current DataFrame, and returns pass/fail plus per-rule results.
+ **Glue Visual ETL** — drop an "Evaluate Data Quality" node into the visual job graph and configure the ruleset in the console.

`EvaluateDataQuality` identifies failing records but does not route them anywhere on its own. With row-level results enabled, it appends outcome columns to each row — `DataQualityEvaluationResult` (`Passed`/`Failed`) plus `DataQualityRulesPass`/`DataQualityRulesFail`/`DataQualityRulesSkip`. To quarantine bad data you add your own ETL step after the transform: filter on `DataQualityEvaluationResult`, then write the passing rows to the target Iceberg table and the failing rows to a quarantine location (an Iceberg branch, an Amazon S3 error prefix, or a dead-letter queue).

## Write-Audit-Publish pattern with Iceberg branching
<a name="write-audit-publish-pattern-with-iceberg-branching"></a>

Combine in-transit Data Quality checks with **Iceberg branching** to implement Write-Audit-Publish (WAP):

1. **Write** — the Glue ETL job writes new data to an isolated Iceberg branch (for example, `audit`) instead of `main`.

1. **Audit** — AWS Glue Data Quality evaluates the ruleset against the branch. If it fails, the branch is discarded (or kept for triage) and downstream consumers never see the bad data.

1. **Publish** — on pass, the job fast-forwards `main` to the audit branch, atomically making the vetted data visible to readers.

This pattern is well suited to gold-layer publishes and CDC pipelines where correctness matters more than latency. See the AWS blog post [Build Write-Audit-Publish pattern with Apache Iceberg branching and AWS Glue Data Quality](https://aws.amazon.com/blogs/big-data/build-write-audit-publish-pattern-with-apache-iceberg-branching-and-aws-glue-data-quality/) for an end-to-end walkthrough on Iceberg on Amazon S3 and on Amazon S3 Tables.

## Example DQDL ruleset
<a name="example-dqdl-ruleset"></a>

The following ruleset combines completeness checks, a primary-key constraint, categorical value validation, and regex validation for date strings on a hypothetical `orders` table.

```
Rules = [
    # Completeness — required columns
    IsComplete "order_id",
    IsComplete "region",
    IsComplete "country",
    IsComplete "item_type",

    # Uniqueness — primary key
    IsPrimaryKey "order_id",

    # Business logic — non-negative units
    ColumnValues "units_sold" >= 0,

    # Enumerations — allowed values
    ColumnValues "sales_channel" in ["Online", "Offline"],
    ColumnValues "order_priority" in ["L", "M", "H", "C"],

    # Format — ISO date pattern
    ColumnValues "order_date" matches "^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$",
    ColumnValues "ship_date"  matches "^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$"
]
```

For the full DQDL reference — including rule types (`Completeness`, `Uniqueness`, `DataFreshness`, `RowCount`, `ColumnCount`, statistical rules, referential integrity, and so on), thresholds, and how results are reported — see the [AWS Glue Data Quality documentation](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html).

## References
<a name="references"></a>
+ AWS blog: [Accelerate your data quality journey for lakehouse architecture with Amazon SageMaker, Apache Iceberg on AWS, Amazon S3 Tables, and AWS Glue Data Quality](https://aws.amazon.com/blogs/big-data/accelerate-your-data-quality-journey-for-lakehouse-architecture-with-amazon-sagemaker-apache-iceberg-on-aws-amazon-s3-tables-and-aws-glue-data-quality/)
+ [AWS Glue Data Quality documentation](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
+ [DQDL (Data Quality Definition Language) reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html)

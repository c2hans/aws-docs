---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/continuous-queries-concepts.html
---

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# Continuous Queries
<a name="continuous-queries-concepts"></a>

A query over a stream executes continuously over streaming data. This continuous execution enables scenarios, such as the ability for applications to continuously query a stream and generate alerts.

In the Getting Started exercise, you have an in-application stream named `SOURCE_SQL_STREAM_001`. It continuously receives stock prices from a demo stream (a Kinesis data stream). The schema is as follows:

```
(TICKER_SYMBOL VARCHAR(4),
 SECTOR varchar(16),
 CHANGE REAL,
 PRICE REAL)
```

Suppose that you are interested in stock price changes greater than 15 percent. You can use the following query in your application code. This query runs continuously and emits records when a stock price change greater than 15 percent is detected.

```
SELECT STREAM TICKER_SYMBOL, PRICE
      FROM   "SOURCE_SQL_STREAM_001"
      WHERE  (ABS((CHANGE / (PRICE-CHANGE)) * 100)) > 15
```

Use the following procedure to set up an Amazon Kinesis Data Analytics application and test this query.

**To test the query**

1. Create an application by following the [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html).

1. Replace the `SELECT` statement in the application code with the preceding `SELECT` query. The resulting application code is shown following:

   ```
   CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (ticker_symbol VARCHAR(4),
                                                      price DOUBLE);
   -- CREATE OR REPLACE PUMP to insert into output
   CREATE OR REPLACE PUMP "STREAM_PUMP" AS
     INSERT INTO "DESTINATION_SQL_STREAM"
         SELECT STREAM TICKER_SYMBOL,
                       PRICE
         FROM   "SOURCE_SQL_STREAM_001"
         WHERE  (ABS((CHANGE / (PRICE-CHANGE)) * 100)) > 15;
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

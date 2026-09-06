---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-write.html
---

# Optimizing write performance
<a name="best-practices-write"></a>

This section discusses table properties that you can tune to optimize write performance on Iceberg tables, independent of the engine.

## Set the table distribution mode
<a name="write-distribution-mode"></a>

Iceberg offers multiple write distribution modes that define how write data is distributed across Spark tasks. For an overview of the available modes, see [Writing Distribution Modes](https://iceberg.apache.org/docs/latest/spark-writes/#writing-distribution-modes) in the Iceberg documentation.

For use cases that prioritize write speed, especially in streaming workloads, set `write.distribution-mode` to `none`. This ensures that Iceberg doesn't request additional Spark shuffling and that data is written as it becomes available in Spark tasks. This mode is particularly suitable for Spark Structured Streaming applications.

**Note**
Setting the write distribution mode to `none` tends to produce numerous small files, which degrades read performance. We recommend regular compaction to consolidate these small files into properly sized files for query performance.

## Choose the right update strategy
<a name="write-update-strategy"></a>

Use a merge-on-read** **strategy to optimize write performance, when slower read operations on the latest data are acceptable for your use case.

When you use merge-on-read, Iceberg writes updates and deletes to storage as separate small files. When the table is read, the reader has to merge these changes with the base files to return the latest view of the data. This results in a performance penalty for read operations, but speeds up the writing of updates and deletes. Typically, merge-on-read is ideal for streaming workloads with updates or jobs with few updates that are spread across many table partitions.

You can set merge-on-read configurations (`write.update.mode`, `write.delete.mode`, and `write.merge.mode`) at the table level or independently on the application side.

Using merge-on-read requires running regular compaction to prevent read performance from degrading over time. Compaction reconciles updates and deletes with existing data files to create a new set of data files, thereby eliminating the performance penalty incurred on the read side. By default, Iceberg's compaction doesn't merge delete files unless you change the default of the `delete-file-threshold` property to a smaller value (see the [Iceberg documentation](https://iceberg.apache.org/docs/latest/spark-procedures/#rewrite_data_files)). To learn more about compaction, see the section [Iceberg compaction](best-practices-compaction.md) later in this guide.

## Choose the right file format
<a name="write-file-format"></a>

Iceberg supports writing data in Parquet, ORC, and Avro formats. Parquet is the default format. Parquet and ORC are columnar formats that offer superior read performance but are generally slower to write. This represents the typical trade-off between read and write performance.

If write speed is important for your use case, such as in streaming workloads, consider writing in Avro format by setting `write-format` to `Avro` in the writer's options. Because Avro is a row-based format, it provides faster write times at the cost of slower read performance.

To improve read performance, run regular compaction to merge and transform small Avro files into larger Parquet files. The outcome of the compaction process is governed by the `write.format.default` table setting. The default format for Iceberg is Parquet, so if you write in Avro and then run compaction, Iceberg will transform the Avro files into Parquet files. Here's an example:

```
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS glue_catalog.{DB_NAME}.{TABLE_NAME} (
        Col_1 float,
        <<<…other columns…>>
        ts timestamp)
    USING iceberg
    PARTITIONED BY (days(ts))
    OPTIONS (
      'format-version'='2',
      write.format.default'=parquet)
""")

query = df \
    .writeStream \
    .format("iceberg") \
    .option("write-format", "avro") \
    .outputMode("append") \
    .trigger(processingTime='60 seconds') \
    .option("path", f"glue_catalog.{DB_NAME}.{TABLE_NAME}") \
    .option("checkpointLocation", f"s3://{BUCKET_NAME}/checkpoints/iceberg/")

    .start()
```

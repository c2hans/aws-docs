---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/performance-efficiency.html
---

# Performance efficiency pillar
<a name="performance-efficiency"></a>

The [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html) of the AWS Well-Architected Framework focuses on how to optimize performance while ingesting or querying data. Performance optimization is an incremental and continual process of the following:
+ Confirming business requirements
+ Measuring the workload performance
+ Identifying underperforming components
+ Tuning the components to meet your business needs

The performance efficiency pillar provides guidelines that can help you choose a high-performing data model. The performance efficiency pillar includes query and write optimization best practices.

The performance efficiency pillar focuses on the following key areas:
+ Influx data modeling and query optimization
+ Write optimization

## Influx data modeling and query optimization
<a name="data-modeling"></a>

Designing an effective schema is crucial for optimizing the performance and querying capabilities of time-series data in InfluxDB. Start by choosing the right tags and fields. InfluxDB indexes tags, so the query engine doesn't need to scan every record in a measurement to locate a tag value. This means that querying tags is more efficient than querying fields. To compact and store data, the storage engine groups field values by series key, and then it orders those field values by time. A series key is defined by measurement, tag key and value, and field key. For more information about data design, see the [InfluxDB documentation](https://docs.influxdata.com/influxdb/v2/reference/key-concepts/data-elements/).

The storage engine uses a Time-Structured Merge Tree (TSM) data format. For more information about the TSM data format, see the [InfluxDB documentation](https://docs.influxdata.com/influxdb/v2/reference/internals/storage-engine/#time-structured-merge-tree-tsm)..

Imagine that you're collecting data (`timestamp`, `host_id`, `region`, `cpu`, `memory`, `network_in_bytes`, `network_out_bytes`, `disk_io`) as part of a DevOps use case. Tags, including the record timestamp, provide context to help identify the who, what, when, and where of a record. Tags are used to organize and categorize data, and to filter data as part of a query.

The `host_id` and `region` tags are ideal tags for organizing and categorizing the DevOps use case. These columns help to filter the data for particular host or to run analysis based on the region column.

Measures provide the basis for performing mathematical calculations (such as computing totals, averages, and differences in rate of change) and quantitative analysis on your data. Therefore, `cpu`, `memory`, `network_in_bytes`, `network_out_bytes`, and `disk_io` capture important metrics related to the DevOps that are changing over time. You can use these metrics to perform various analyses, such as calculating the CPU and memory across different hosts. You can use these metric values to make data-driven decisions that help with avoiding  production outages and performing infrastructure planning.

Cardinality is the combination of unique tag values. Aim to keep the cardinality as low as possible, If your application requires a unique identifier for each data point, use field values instead of tag values. This will result in significantly better query latency. Good schema design can prevent high series cardinality, resulting in better performing queries. If you notice data reads and writes slowing down or you want to learn how cardinality affects performance, see the [Timestream for InfluxDB documentation](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html#timestream-for-influx-getting-started-security-best-practices).

If your application emits JSON objects, convert them to individual columns (tags or fields), and load the columns into InfluxDB. InfluxDB is designed for time-series data, so organizing your data with individual columns is a best practice for taking full advantage of the service's capabilities.

A single InfluxDB v2.7 OSS instance supports approximately 20 InfluxDB buckets actively being written to or queried across all organizations. More than 20 buckets can adversely affect performance. There are limits on some InfluxDB configuration options, and there are some options that you can configure based on your use case. Validate the configuration based on the application workload during the testing phase. Data retentions are configured at the bucket level, so data with different data-retention requirements should be stored in different buckets. For more information about configuration options, see the [Timestream for InfluxDB documentation](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-db-connecting.html#timestream-for-influx-parameter-groups).

Store data in tag values or field values, not in tag keys, field keys, or measurements. If you design your schema to store data in tag and field values, your queries will be easier to write and more efficient. For more best practices on data modeling, see [Design for performance](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html#timestream-for-influx-getting-started-security-best-practices-design-for-performance).

Use [InfluxDB tasks](https://docs.influxdata.com/influxdb/cloud/process-data/get-started/) to pre-aggregate data, load the data into different measurements or buckets, and generate data for dashboards and visualizations from them.

InfluxDB OSS exposes a `/metrics` [endpoint](https://docs.influxdata.com/influxdb/v2/reference/internals/metrics/) that returns performance, resource, and usage metrics formatted in the** **Prometheus plain-text exposition format. Use InfluxDB templates to set up [monitoring and alerting](https://docs.influxdata.com/influxdb/v2/monitor-alert/templates/) to proactively detect issues, such as high query latency, write throughput degradation, or resource usage spikes.

Timestream for InfluxDB provides Influx IO Included storage. Selecting the appropriate IOPS  size can significantly speed up query execution. This is especially helpful for queries that need to scan large amounts of data or handle a high range of requests. In some situations, a combination of scaling up the instance and enhancing the IOPS might be necessary to achieve the performance improvements that you want.

We recommend matching the dev and prod environments (instance class, storage type, configurations). Test changes in the lower environment for every release before moving to production. On Influx IO Included storage volumes, Timestream for InfluxDB provides three storage tiers that are preconfigured with optimal IOPS (3,000, 12,000, 16,000) and throughput required for different types of workloads. Most use cases require less than 3,000 IOPS. Choose 12,000 or 16,000 only if performance testing indicates a need for high IOPS. For more information, see the [Setting up section](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html#timestream-for-influx-dbi-setting-up) in the Timestream for InfluxDB documentation.

## Optimize writes
<a name="optimize-writes"></a>

To optimize writes to InfluxDB, we recommend writing data in batches of 5,000 lines of line protocol per request to minimize network overhead. For better performance, sort tags by key in lexicographic order before writing data points. Using the coarsest time precision possible for timestamps, instead of nanoseconds, can also improve performance. Enabling gzip compression is another way to speed up writes and reduce network bandwidth. In the `influxdb_v2` output plugin configuration in your `telegraf.conf` file, set the `content_encoding` option to `gzip`. Implementing these optimizations can significantly improve the performance and efficiency of writing data to InfluxDB. For more InfluxDB write best practices, see [Optimize writes to InfluxDB](https://docs.influxdata.com/influxdb/v2/write-data/best-practices/optimize-writes/).

InfluxDB' s write performance is often closely tied to the available IOPS. When writing data, InfluxDB needs to perform a significant number of I/O operations to store the data. When you  increase the IOPS, InfluxDB can process more writes per second.

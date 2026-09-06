---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_InfluxDBv3CoreParameters.html
---

# InfluxDBv3CoreParameters
<a name="API_InfluxDBv3CoreParameters"></a>

All the customer-modifiable InfluxDB v3 Core parameters in Timestream for InfluxDB.

## Contents
<a name="API_InfluxDBv3CoreParameters_Contents"></a>

 ** dataFusionConfig **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionConfig"></a>
Provides custom configuration to DataFusion as a comma-separated list of key:value pairs.
Type: String
Pattern: `[a-zA-Z0-9_]+=[^,\s]+(?:,[a-zA-Z0-9_]+=[^,\s]+)*`
Required: No

 ** dataFusionMaxParquetFanout **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionMaxParquetFanout"></a>
When multiple parquet files are required in a sorted way (deduplication for example), specifies the maximum fanout.
Default: 1000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: No

 ** dataFusionNumThreads **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionNumThreads"></a>
Sets the maximum number of DataFusion runtime threads to use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2048.
Required: No

 ** dataFusionRuntimeDisableLifoSlot **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeDisableLifoSlot"></a>
Disables the LIFO slot of the DataFusion runtime.
Type: Boolean
Required: No

 ** dataFusionRuntimeEventInterval **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeEventInterval"></a>
Sets the number of scheduler ticks after which the scheduler of the DataFusion tokio runtime polls for external events–for example: timers, I/O.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

 ** dataFusionRuntimeGlobalQueueInterval **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeGlobalQueueInterval"></a>
Sets the number of scheduler ticks after which the scheduler of the DataFusion runtime polls the global task queue.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

 ** dataFusionRuntimeMaxBlockingThreads **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeMaxBlockingThreads"></a>
Specifies the limit for additional threads spawned by the DataFusion runtime.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** dataFusionRuntimeMaxIoEventsPerTick **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeMaxIoEventsPerTick"></a>
Configures the maximum number of events processed per tick by the tokio DataFusion runtime.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4096.
Required: No

 ** dataFusionRuntimeThreadKeepAlive **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeThreadKeepAlive"></a>
Sets a custom timeout for a thread in the blocking pool of the tokio DataFusion runtime.
Type: [Duration](API_Duration.md) object
Required: No

 ** dataFusionRuntimeThreadPriority **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeThreadPriority"></a>
Sets the thread priority for tokio DataFusion runtime workers.
Default: 10
Type: Integer
Valid Range: Minimum value of -20. Maximum value of 19.
Required: No

 ** dataFusionRuntimeType **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionRuntimeType"></a>
Specifies the DataFusion tokio runtime type.
Default: multi-thread
Type: String
Valid Values: `multi-thread | multi-thread-alt`
Required: No

 ** dataFusionUseCachedParquetLoader **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-dataFusionUseCachedParquetLoader"></a>
Uses a cached parquet loader when reading parquet files from the object store.
Type: Boolean
Required: No

 ** deleteGracePeriod **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-deleteGracePeriod"></a>
Specifies the grace period before permanently deleting data.
Default: 24h
Type: [Duration](API_Duration.md) object
Required: No

 ** disableParquetMemCache **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-disableParquetMemCache"></a>
Disables the in-memory Parquet cache. By default, the cache is enabled.
Type: Boolean
Required: No

 ** distinctCacheEvictionInterval **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-distinctCacheEvictionInterval"></a>
Specifies the interval to evict expired entries from the distinct value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.
Default: 10s
Type: [Duration](API_Duration.md) object
Required: No

 ** execMemPoolBytes **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-execMemPoolBytes"></a>
Specifies the size of memory pool used during query execution. Can be given as absolute value in bytes or as a percentage of the total available memory–for example: 8000000000 or 10%.
Default: 20%
Type: [PercentOrAbsoluteLong](API_PercentOrAbsoluteLong.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** forceSnapshotMemThreshold **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-forceSnapshotMemThreshold"></a>
Specifies the threshold for the internal memory buffer. Supports either a percentage (portion of available memory) or absolute value in MB–for example: 70% or 100
Default: 70%
Type: [PercentOrAbsoluteLong](API_PercentOrAbsoluteLong.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** gen1Duration **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-gen1Duration"></a>
Specifies the duration that Parquet files are arranged into. Data timestamps land each row into a file of this duration. Supported durations are 1m, 5m, and 10m. These files are known as “generation 1” files that the compactor in InfluxDB 3 Enterprise can merge into larger generations.
Default: 10m
Type: [Duration](API_Duration.md) object
Required: No

 ** gen1LookbackDuration **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-gen1LookbackDuration"></a>
Specifies how far back to look when creating generation 1 Parquet files.
Default: 24h
Type: [Duration](API_Duration.md) object
Required: No

 ** hardDeleteDefaultDuration **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-hardDeleteDefaultDuration"></a>
Sets the default duration for hard deletion of data.
Default: 90d
Type: [Duration](API_Duration.md) object
Required: No

 ** lastCacheEvictionInterval **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-lastCacheEvictionInterval"></a>
Specifies the interval to evict expired entries from the Last-N-Value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.
Default: 10s
Type: [Duration](API_Duration.md) object
Required: No

 ** logFilter **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-logFilter"></a>
Sets the filter directive for logs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** logFormat **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-logFormat"></a>
Defines the message format for logs.
Default: full
Type: String
Valid Values: `full`
Required: No

 ** maxHttpRequestSize **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-maxHttpRequestSize"></a>
Specifies the maximum size of HTTP requests.
Default: 10485760
Type: Long
Valid Range: Minimum value of 1024. Maximum value of 16777216.
Required: No

 ** parquetMemCachePruneInterval **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-parquetMemCachePruneInterval"></a>
Sets the interval to check if the in-memory Parquet cache needs to be pruned.
Default: 1s
Type: [Duration](API_Duration.md) object
Required: No

 ** parquetMemCachePrunePercentage **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-parquetMemCachePrunePercentage"></a>
Specifies the percentage of entries to prune during a prune operation on the in-memory Parquet cache.
Default: 0.1
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** parquetMemCacheQueryPathDuration **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-parquetMemCacheQueryPathDuration"></a>
Specifies the time window for caching recent Parquet files in memory.
Default: 5h
Type: [Duration](API_Duration.md) object
Required: No

 ** parquetMemCacheSize **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-parquetMemCacheSize"></a>
Specifies the size of the in-memory Parquet cache in megabytes or percentage of total available memory.
Default: 20%
Type: [PercentOrAbsoluteLong](API_PercentOrAbsoluteLong.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** preemptiveCacheAge **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-preemptiveCacheAge"></a>
Specifies the interval to prefetch into the Parquet cache during compaction.
Default: 3d
Type: [Duration](API_Duration.md) object
Required: No

 ** queryFileLimit **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-queryFileLimit"></a>
Limits the number of Parquet files a query can access. If a query attempts to read more than this limit, InfluxDB 3 returns an error.
Default: 432
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** queryLogSize **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-queryLogSize"></a>
Defines the size of the query log. Up to this many queries remain in the log before older queries are evicted to make room for new ones.
Default: 1000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** retentionCheckInterval **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-retentionCheckInterval"></a>
The interval at which retention policies are checked and enforced. Enter as a human-readable time–for example: 30m or 1h.
Default: 30m
Type: [Duration](API_Duration.md) object
Required: No

 ** snapshottedWalFilesToKeep **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-snapshottedWalFilesToKeep"></a>
Specifies the number of snapshotted WAL files to retain in the object store. Flushing the WAL files does not clear the WAL files immediately; they are deleted when the number of snapshotted WAL files exceeds this number.
Default: 300
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** tableIndexCacheConcurrencyLimit **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-tableIndexCacheConcurrencyLimit"></a>
Limits the concurrency level for table index cache operations.
Default: 8
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** tableIndexCacheMaxEntries **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-tableIndexCacheMaxEntries"></a>
Specifies the maximum number of entries in the table index cache.
Default: 1000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** walMaxWriteBufferSize **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-walMaxWriteBufferSize"></a>
Specifies the maximum number of write requests that can be buffered before a flush must be executed and succeed.
Default: 100000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: No

 ** walReplayConcurrencyLimit **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-walReplayConcurrencyLimit"></a>
Concurrency limit during WAL replay. Setting this number too high can lead to OOM. The default is dynamically determined.
Default: max(num\_cpus, 10)
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** walReplayFailOnError **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-walReplayFailOnError"></a>
Determines whether WAL replay should fail when encountering errors.
Default: false
Type: Boolean
Required: No

 ** walSnapshotSize **   <a name="tsinfluxdb-Type-InfluxDBv3CoreParameters-walSnapshotSize"></a>
Defines the number of WAL files to attempt to remove in a snapshot. This, multiplied by the interval, determines how often snapshots are taken.
Default: 600
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## See Also
<a name="API_InfluxDBv3CoreParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/InfluxDBv3CoreParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/InfluxDBv3CoreParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/InfluxDBv3CoreParameters)

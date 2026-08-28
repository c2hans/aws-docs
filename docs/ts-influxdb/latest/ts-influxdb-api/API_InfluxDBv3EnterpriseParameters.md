---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_InfluxDBv3EnterpriseParameters.html
---

# InfluxDBv3EnterpriseParameters
<a name="API_InfluxDBv3EnterpriseParameters"></a>

All the customer-modifiable InfluxDB v3 Enterprise parameters in Timestream for InfluxDB.

## Contents
<a name="API_InfluxDBv3EnterpriseParameters_Contents"></a>

 ** dedicatedCompactor **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dedicatedCompactor"></a>
Specifies if the compactor instance should be a standalone instance or not.
Type: Boolean
Required: Yes

 ** ingestQueryInstances **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-ingestQueryInstances"></a>
Specifies number of instances in the DbCluster which can both ingest and query.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4.
Required: Yes

 ** queryOnlyInstances **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-queryOnlyInstances"></a>
Specifies number of instances in the DbCluster which can only query.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: Yes

 ** catalogSyncInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-catalogSyncInterval"></a>
Defines how often the catalog synchronizes across cluster nodes.
Default: 10s
Type: [Duration](API_Duration.md) object
Required: No

 ** compactionCheckInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-compactionCheckInterval"></a>
Specifies how often the compactor checks for new compaction work to perform.
Default: 10s
Type: [Duration](API_Duration.md) object
Required: No

 ** compactionCleanupWait **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-compactionCleanupWait"></a>
Specifies the amount of time that the compactor waits after finishing a compaction run to delete files marked as needing deletion during that compaction run.
Default: 10m
Type: [Duration](API_Duration.md) object
Required: No

 ** compactionGen2Duration **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-compactionGen2Duration"></a>
Specifies the duration of the first level of compaction (gen2). Later levels of compaction are multiples of this duration. This value should be equal to or greater than the gen1 duration.
Default: 20m
Type: [Duration](API_Duration.md) object
Required: No

 ** compactionMaxNumFilesPerPlan **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-compactionMaxNumFilesPerPlan"></a>
Sets the maximum number of files included in any compaction plan.
Default: 500
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** compactionMultipliers **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-compactionMultipliers"></a>
Specifies a comma-separated list of multiples defining the duration of each level of compaction. The number of elements in the list determines the number of compaction levels. The first element specifies the duration of the first level (gen3); subsequent levels are multiples of the previous level.
Default: 3,4,6,5
Type: String
Length Constraints: Minimum length of 7. Maximum length of 16.
Pattern: `\d+,\d+,\d+,\d+`
Required: No

 ** compactionRowLimit **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-compactionRowLimit"></a>
Specifies the soft limit for the number of rows per file that the compactor writes. The compactor may write more rows than this limit.
Default: 1000000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000000.
Required: No

 ** dataFusionConfig **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionConfig"></a>
Provides custom configuration to DataFusion as a comma-separated list of key:value pairs.
Type: String
Pattern: `[a-zA-Z0-9_]+=[^,\s]+(?:,[a-zA-Z0-9_]+=[^,\s]+)*`
Required: No

 ** dataFusionMaxParquetFanout **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionMaxParquetFanout"></a>
When multiple parquet files are required in a sorted way (deduplication for example), specifies the maximum fanout.
Default: 1000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: No

 ** dataFusionNumThreads **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionNumThreads"></a>
Sets the maximum number of DataFusion runtime threads to use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2048.
Required: No

 ** dataFusionRuntimeDisableLifoSlot **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeDisableLifoSlot"></a>
Disables the LIFO slot of the DataFusion runtime.
Type: Boolean
Required: No

 ** dataFusionRuntimeEventInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeEventInterval"></a>
Sets the number of scheduler ticks after which the scheduler of the DataFusion tokio runtime polls for external events–for example: timers, I/O.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

 ** dataFusionRuntimeGlobalQueueInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeGlobalQueueInterval"></a>
Sets the number of scheduler ticks after which the scheduler of the DataFusion runtime polls the global task queue.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

 ** dataFusionRuntimeMaxBlockingThreads **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeMaxBlockingThreads"></a>
Specifies the limit for additional threads spawned by the DataFusion runtime.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** dataFusionRuntimeMaxIoEventsPerTick **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeMaxIoEventsPerTick"></a>
Configures the maximum number of events processed per tick by the tokio DataFusion runtime.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4096.
Required: No

 ** dataFusionRuntimeThreadKeepAlive **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeThreadKeepAlive"></a>
Sets a custom timeout for a thread in the blocking pool of the tokio DataFusion runtime.
Type: [Duration](API_Duration.md) object
Required: No

 ** dataFusionRuntimeThreadPriority **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeThreadPriority"></a>
Sets the thread priority for tokio DataFusion runtime workers.
Default: 10
Type: Integer
Valid Range: Minimum value of -20. Maximum value of 19.
Required: No

 ** dataFusionRuntimeType **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionRuntimeType"></a>
Specifies the DataFusion tokio runtime type.
Default: multi-thread
Type: String
Valid Values: `multi-thread | multi-thread-alt`
Required: No

 ** dataFusionUseCachedParquetLoader **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-dataFusionUseCachedParquetLoader"></a>
Uses a cached parquet loader when reading parquet files from the object store.
Type: Boolean
Required: No

 ** deleteGracePeriod **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-deleteGracePeriod"></a>
Specifies the grace period before permanently deleting data.
Default: 24h
Type: [Duration](API_Duration.md) object
Required: No

 ** disableParquetMemCache **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-disableParquetMemCache"></a>
Disables the in-memory Parquet cache. By default, the cache is enabled.
Type: Boolean
Required: No

 ** distinctCacheEvictionInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-distinctCacheEvictionInterval"></a>
Specifies the interval to evict expired entries from the distinct value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.
Default: 10s
Type: [Duration](API_Duration.md) object
Required: No

 ** distinctValueCacheDisableFromHistory **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-distinctValueCacheDisableFromHistory"></a>
Disables populating the distinct value cache from historical data. If disabled, the cache is still populated with data from the write-ahead log (WAL).
Type: Boolean
Required: No

 ** execMemPoolBytes **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-execMemPoolBytes"></a>
Specifies the size of memory pool used during query execution. Can be given as absolute value in bytes or as a percentage of the total available memory–for example: 8000000000 or 10%.
Default: 20%
Type: [PercentOrAbsoluteLong](API_PercentOrAbsoluteLong.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** forceSnapshotMemThreshold **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-forceSnapshotMemThreshold"></a>
Specifies the threshold for the internal memory buffer. Supports either a percentage (portion of available memory) or absolute value in MB–for example: 70% or 100
Default: 70%
Type: [PercentOrAbsoluteLong](API_PercentOrAbsoluteLong.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** gen1Duration **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-gen1Duration"></a>
Specifies the duration that Parquet files are arranged into. Data timestamps land each row into a file of this duration. Supported durations are 1m, 5m, and 10m. These files are known as “generation 1” files, which the compactor can merge into larger generations.
Default: 10m
Type: [Duration](API_Duration.md) object
Required: No

 ** gen1LookbackDuration **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-gen1LookbackDuration"></a>
Specifies how far back to look when creating generation 1 Parquet files.
Default: 24h
Type: [Duration](API_Duration.md) object
Required: No

 ** hardDeleteDefaultDuration **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-hardDeleteDefaultDuration"></a>
Sets the default duration for hard deletion of data.
Default: 90d
Type: [Duration](API_Duration.md) object
Required: No

 ** lastCacheEvictionInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-lastCacheEvictionInterval"></a>
Specifies the interval to evict expired entries from the Last-N-Value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.
Default: 10s
Type: [Duration](API_Duration.md) object
Required: No

 ** lastValueCacheDisableFromHistory **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-lastValueCacheDisableFromHistory"></a>
Disables populating the last-N-value cache from historical data. If disabled, the cache is still populated with data from the write-ahead log (WAL).
Type: Boolean
Required: No

 ** logFilter **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-logFilter"></a>
Sets the filter directive for logs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** logFormat **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-logFormat"></a>
Defines the message format for logs.
Default: full
Type: String
Valid Values: `full`
Required: No

 ** maxHttpRequestSize **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-maxHttpRequestSize"></a>
Specifies the maximum size of HTTP requests.
Default: 10485760
Type: Long
Valid Range: Minimum value of 1024. Maximum value of 16777216.
Required: No

 ** parquetMemCachePruneInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-parquetMemCachePruneInterval"></a>
Sets the interval to check if the in-memory Parquet cache needs to be pruned.
Default: 1s
Type: [Duration](API_Duration.md) object
Required: No

 ** parquetMemCachePrunePercentage **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-parquetMemCachePrunePercentage"></a>
Specifies the percentage of entries to prune during a prune operation on the in-memory Parquet cache.
Default: 0.1
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** parquetMemCacheQueryPathDuration **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-parquetMemCacheQueryPathDuration"></a>
Specifies the time window for caching recent Parquet files in memory.
Default: 5h
Type: [Duration](API_Duration.md) object
Required: No

 ** parquetMemCacheSize **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-parquetMemCacheSize"></a>
Specifies the size of the in-memory Parquet cache in megabytes or percentage of total available memory.
Default: 20%
Type: [PercentOrAbsoluteLong](API_PercentOrAbsoluteLong.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** preemptiveCacheAge **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-preemptiveCacheAge"></a>
Specifies the interval to prefetch into the Parquet cache during compaction.
Default: 3d
Type: [Duration](API_Duration.md) object
Required: No

 ** queryFileLimit **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-queryFileLimit"></a>
Limits the number of Parquet files a query can access. If a query attempts to read more than this limit, InfluxDB 3 returns an error.
Default: 432
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** queryLogSize **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-queryLogSize"></a>
Defines the size of the query log. Up to this many queries remain in the log before older queries are evicted to make room for new ones.
Default: 1000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** replicationInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-replicationInterval"></a>
Specifies the interval at which data replication occurs between cluster nodes.
Default: 250ms
Type: [Duration](API_Duration.md) object
Required: No

 ** retentionCheckInterval **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-retentionCheckInterval"></a>
The interval at which retention policies are checked and enforced. Enter as a human-readable time–for example: 30m or 1h.
Default: 30m
Type: [Duration](API_Duration.md) object
Required: No

 ** snapshottedWalFilesToKeep **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-snapshottedWalFilesToKeep"></a>
Specifies the number of snapshotted WAL files to retain in the object store. Flushing the WAL files does not clear the WAL files immediately; they are deleted when the number of snapshotted WAL files exceeds this number.
Default: 300
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** tableIndexCacheConcurrencyLimit **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-tableIndexCacheConcurrencyLimit"></a>
Limits the concurrency level for table index cache operations.
Default: 8
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** tableIndexCacheMaxEntries **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-tableIndexCacheMaxEntries"></a>
Specifies the maximum number of entries in the table index cache.
Default: 1000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** walMaxWriteBufferSize **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-walMaxWriteBufferSize"></a>
Specifies the maximum number of write requests that can be buffered before a flush must be executed and succeed.
Default: 100000
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: No

 ** walReplayConcurrencyLimit **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-walReplayConcurrencyLimit"></a>
Concurrency limit during WAL replay. Setting this number too high can lead to OOM. The default is dynamically determined.
Default: max(num\_cpus, 10)
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** walReplayFailOnError **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-walReplayFailOnError"></a>
Determines whether WAL replay should fail when encountering errors.
Default: false
Type: Boolean
Required: No

 ** walSnapshotSize **   <a name="tsinfluxdb-Type-InfluxDBv3EnterpriseParameters-walSnapshotSize"></a>
Defines the number of WAL files to attempt to remove in a snapshot. This, multiplied by the interval, determines how often snapshots are taken.
Default: 600
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## See Also
<a name="API_InfluxDBv3EnterpriseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/InfluxDBv3EnterpriseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/InfluxDBv3EnterpriseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/InfluxDBv3EnterpriseParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Timestream for InfluxDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ts-influxdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

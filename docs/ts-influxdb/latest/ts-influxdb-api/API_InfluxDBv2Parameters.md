---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_InfluxDBv2Parameters.html
---

# InfluxDBv2Parameters
<a name="API_InfluxDBv2Parameters"></a>

All the customer-modifiable InfluxDB v2 parameters in Timestream for InfluxDB.

## Contents
<a name="API_InfluxDBv2Parameters_Contents"></a>

 ** fluxLogEnabled **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-fluxLogEnabled"></a>
Include option to show detailed logs for Flux queries.
Default: false
Type: Boolean
Required: No

 ** httpIdleTimeout **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-httpIdleTimeout"></a>
Maximum duration the server should keep established connections alive while waiting for new requests. Set to 0 for no timeout.
Default: 3 minutes
Type: [Duration](API_Duration.md) object
Required: No

 ** httpReadHeaderTimeout **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-httpReadHeaderTimeout"></a>
Maximum duration the server should try to read HTTP headers for new requests. Set to 0 for no timeout.
Default: 10 seconds
Type: [Duration](API_Duration.md) object
Required: No

 ** httpReadTimeout **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-httpReadTimeout"></a>
Maximum duration the server should try to read the entirety of new requests. Set to 0 for no timeout.
Default: 0
Type: [Duration](API_Duration.md) object
Required: No

 ** httpWriteTimeout **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-httpWriteTimeout"></a>
Maximum duration the server should spend processing and responding to write requests. Set to 0 for no timeout.
Default: 0
Type: [Duration](API_Duration.md) object
Required: No

 ** influxqlMaxSelectBuckets **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-influxqlMaxSelectBuckets"></a>
Maximum number of group by time buckets a SELECT statement can create. 0 allows an unlimited number of buckets.
Default: 0
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** influxqlMaxSelectPoint **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-influxqlMaxSelectPoint"></a>
Maximum number of points a SELECT statement can process. 0 allows an unlimited number of points. InfluxDB checks the point count every second (so queries exceeding the maximum aren’t immediately aborted).
Default: 0
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** influxqlMaxSelectSeries **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-influxqlMaxSelectSeries"></a>
Maximum number of series a SELECT statement can return. 0 allows an unlimited number of series.
Default: 0
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** logLevel **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-logLevel"></a>
Log output level. InfluxDB outputs log entries with severity levels greater than or equal to the level specified.
Default: info
Type: String
Valid Values: `debug | info | error`
Required: No

 ** metricsDisabled **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-metricsDisabled"></a>
Disable the HTTP /metrics endpoint which exposes [internal InfluxDB metrics](https://docs.influxdata.com/influxdb/v2/reference/internals/metrics/).
Default: false
Type: Boolean
Required: No

 ** noTasks **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-noTasks"></a>
Disable the task scheduler. If problematic tasks prevent InfluxDB from starting, use this option to start InfluxDB without scheduling or executing tasks.
Default: false
Type: Boolean
Required: No

 ** pprofDisabled **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-pprofDisabled"></a>
Disable the /debug/pprof HTTP endpoint. This endpoint provides runtime profiling data and can be helpful when debugging.
Default: true
Type: Boolean
Required: No

 ** queryConcurrency **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-queryConcurrency"></a>
Number of queries allowed to execute concurrently. Setting to 0 allows an unlimited number of concurrent queries.
Default: 0
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 256.
Required: No

 ** queryInitialMemoryBytes **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-queryInitialMemoryBytes"></a>
Initial bytes of memory allocated for a query.
Default: 0
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** queryMaxMemoryBytes **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-queryMaxMemoryBytes"></a>
Maximum number of queries allowed in execution queue. When queue limit is reached, new queries are rejected. Setting to 0 allows an unlimited number of queries in the queue.
Default: 0
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** queryMemoryBytes **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-queryMemoryBytes"></a>
Maximum bytes of memory allowed for a single query. Must be greater or equal to queryInitialMemoryBytes.
Default: 0
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** queryQueueSize **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-queryQueueSize"></a>
Maximum number of queries allowed in execution queue. When queue limit is reached, new queries are rejected. Setting to 0 allows an unlimited number of queries in the queue.
Default: 0
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 256.
Required: No

 ** sessionLength **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-sessionLength"></a>
Specifies the Time to Live (TTL) in minutes for newly created user sessions.
Default: 60
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2880.
Required: No

 ** sessionRenewDisabled **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-sessionRenewDisabled"></a>
Disables automatically extending a user’s session TTL on each request. By default, every request sets the session’s expiration time to five minutes from now. When disabled, sessions expire after the specified [session length](https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length) and the user is redirected to the login page, even if recently active.
Default: false
Type: Boolean
Required: No

 ** storageCacheMaxMemorySize **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageCacheMaxMemorySize"></a>
Maximum size (in bytes) a shard’s cache can reach before it starts rejecting writes. Must be greater than storageCacheSnapShotMemorySize and lower than instance’s total memory capacity. We recommend setting it to below 15% of the total memory capacity.
Default: 1073741824
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** storageCacheSnapshotMemorySize **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageCacheSnapshotMemorySize"></a>
Size (in bytes) at which the storage engine will snapshot the cache and write it to a TSM file to make more memory available. Must not be greater than storageCacheMaxMemorySize.
Default: 26214400
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** storageCacheSnapshotWriteColdDuration **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageCacheSnapshotWriteColdDuration"></a>
Duration at which the storage engine will snapshot the cache and write it to a new TSM file if the shard hasn’t received writes or deletes.
Default: 10 minutes
Type: [Duration](API_Duration.md) object
Required: No

 ** storageCompactFullWriteColdDuration **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageCompactFullWriteColdDuration"></a>
Duration at which the storage engine will compact all TSM files in a shard if it hasn't received writes or deletes.
Default: 4 hours
Type: [Duration](API_Duration.md) object
Required: No

 ** storageCompactThroughputBurst **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageCompactThroughputBurst"></a>
Rate limit (in bytes per second) that TSM compactions can write to disk.
Default: 50331648
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** storageMaxConcurrentCompactions **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageMaxConcurrentCompactions"></a>
Maximum number of full and level compactions that can run concurrently. A value of 0 results in 50% of runtime.GOMAXPROCS(0) used at runtime. Any number greater than zero limits compactions to that value. This setting does not apply to cache snapshotting.
Default: 0
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 64.
Required: No

 ** storageMaxIndexLogFileSize **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageMaxIndexLogFileSize"></a>
Size (in bytes) at which an index write-ahead log (WAL) file will compact into an index file. Lower sizes will cause log files to be compacted more quickly and result in lower heap usage at the expense of write throughput.
Default: 1048576
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** storageNoValidateFieldSize **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageNoValidateFieldSize"></a>
Skip field size validation on incoming write requests.
Default: false
Type: Boolean
Required: No

 ** storageRetentionCheckInterval **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageRetentionCheckInterval"></a>
Interval of retention policy enforcement checks. Must be greater than 0.
Default: 30 minutes
Type: [Duration](API_Duration.md) object
Required: No

 ** storageSeriesFileMaxConcurrentSnapshotCompactions **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageSeriesFileMaxConcurrentSnapshotCompactions"></a>
Maximum number of snapshot compactions that can run concurrently across all series partitions in a database.
Default: 0
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 64.
Required: No

 ** storageSeriesIdSetCacheSize **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageSeriesIdSetCacheSize"></a>
Size of the internal cache used in the TSI index to store previously calculated series results. Cached results are returned quickly rather than needing to be recalculated when a subsequent query with the same tag key/value predicate is executed. Setting this value to 0 will disable the cache and may decrease query performance.
Default: 100
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000000.
Required: No

 ** storageWalMaxConcurrentWrites **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageWalMaxConcurrentWrites"></a>
Maximum number writes to the WAL directory to attempt at the same time. Setting this value to 0 results in number of processing units available x2.
Default: 0
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 256.
Required: No

 ** storageWalMaxWriteDelay **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-storageWalMaxWriteDelay"></a>
Maximum amount of time a write request to the WAL directory will wait when the [maximum number of concurrent active writes to the WAL directory has been met](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-concurrent-writes). Set to 0 to disable the timeout.
Default: 10 minutes
Type: [Duration](API_Duration.md) object
Required: No

 ** tracingType **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-tracingType"></a>
Enable tracing in InfluxDB and specifies the tracing type. Tracing is disabled by default.
Type: String
Valid Values: `log | jaeger | disabled`
Required: No

 ** uiDisabled **   <a name="tsinfluxdb-Type-InfluxDBv2Parameters-uiDisabled"></a>
Disable the InfluxDB user interface (UI). The UI is enabled by default.
Default: false
Type: Boolean
Required: No

## See Also
<a name="API_InfluxDBv2Parameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/InfluxDBv2Parameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/InfluxDBv2Parameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/InfluxDBv2Parameters)

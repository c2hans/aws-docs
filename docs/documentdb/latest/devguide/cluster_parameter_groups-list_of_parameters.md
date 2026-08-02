---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html
---

# Amazon DocumentDB cluster parameters reference
<a name="cluster_parameter_groups-list_of_parameters"></a>

When you change a dynamic parameter and save the cluster parameter group, the change is applied immediately regardless of the *Apply immediately* setting. When you change a static parameter and save the cluster parameter group, the parameter change takes effect after you manually reboot the instance. You can reboot an instance using the Amazon DocumentDB console or by explicitly calling `reboot-db-instance`.

The following table shows the parameters that apply to all instances in an Amazon DocumentDB cluster.

**Amazon DocumentDB cluster-level parameters**

| Parameter | Default Value | Valid Values | Modifiable | Apply Type | Data Type | Description |
| --- | --- | --- | --- | --- | --- | --- |
| audit\_logs | disabled | enabled, disabled, ddl, dml\_read, dml\_write, all, none | Yes | Dynamic | String | Defines whether Amazon CloudWatch audit logs are enabled. [See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |
| change\_stream\_log\_retention\_duration | 10800 | 3600-604800 | Yes | Dynamic | Integer | Defines the duration of time (in seconds) that the change stream log is retained and can be consumed.  |
| default\_collection\_compression | disabled | enabled, disabled (Amazon DocumentDB 5.0) / zstd, lz4, none (Amazon DocumentDB8.0) | Yes | Dynamic | String | Defines the default compression setting for new collections in a cluster [See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |
| profiler | disabled | enabled, disabled | Yes | Dynamic | String | Enables profiling for slow operations. [See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |
| profiler\_sampling\_rate | 1.0 | 0.0-1.0 | Yes | Dynamic | Float | Defines the sampling rate for logged operations. |
| profiler\_threshold\_ms | 100 | 50-2147483646 | Yes | Dynamic | Integer | Defines the threshold for profiler. [See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |
| planner\_version | 3.0 | 1.0, 2.0, 3.0 | Yes | Dynamic | Float | Defines the query planner version to use for queries.[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |
| tls | enabled | enabled, disabled, fips-140-3, tls1.2\+, tls1.3\+ | Yes | Static | String | Defines whether Transport Layer Security (TLS) connections are required. [See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |
| ttl\_monitor | enabled | enabled, disabled | Yes | Dynamic | String | Defines whether Time to Live (TTL) monitoring is enabled for the cluster. [See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_groups-list_of_parameters.html) |

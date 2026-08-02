---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/manage-connections.html
---

# Managing connections
<a name="manage-connections"></a>

As the demand for your application grows, the front-end traffic increases. In a typical scenario, you set up automatic scaling at the application tier to handle such a burst of incoming traffic. As a result, the application tier starts to auto scale, and more application servers (instances) are added to meet the increase in traffic. Because all application servers have preconfigured database connection pool settings, the number of incoming connections to the database grows in proportion to the newly deployed instances.

For example, 20 application servers configured with 200 database connections each would open a total of 4,000 database connections. If the application pool scales up to 200 instances (for example, during peak hours), the total connection count will reach 40,000. Under a typical workload, most of these connections are likely idle. But the spike in the connections might limit your Amazon Aurora MySQL-Compatible Edition database's ability to scale. This is because even idle connections consume memory and other server resources, such as file descriptors. Aurora MySQL-Compatible typically uses less memory than MySQL Community Edition to maintain same number of connections. However, memory usage for idle connections is still not zero.

## Configuration variables
<a name="config-variables"></a>

You can control the number of incoming connections allowed to your database with two major server configuration variables: `max_connections` and `max_connect_errors`.

### Configuration variable max\_connections
<a name="configuration-variable-max-connections.5a6664ca-7ca7-5203-b660-2bd9f70dbfd6"></a>

The configuration variable `max_connections` limits the number of database connections for each MySQL instance. The best practice is to set it slightly higher than the maximum number of connections you expect to open on each database instance.

If you also enabled `performance_schema`, be extra careful with the `max_connections` setting. The Performance Schema memory structures are sized automatically based on server configuration variables, including `max_connections`. The higher you set the variable, the more memory Performance Schema uses. In extreme cases, this can lead to out-of-memory issues on smaller instance types. Note that enabling Performance Insights will automatically enable Performance Schema.

### Configuration variable max\_connect\_errors
<a name="configuration-variable-max-connect-errors.4cd1f22e-9ef5-509d-a8df-2682b6436fe5"></a>

The configuration variable `max_connect_errors` determines how many successive interrupted connection requests are permitted from a given client host. If the client host exceeds the specified number of successive failed connection attempts, the server blocks it. Further connection attempts from that client yield an error.

`Host 'host_name' is blocked because of many connection errors. Unblock with 'mysqladmin flush-hosts'`

If you experience "host is blocked" errors, avoid increasing the value of the `max_connect_errors` variable. Instead, investigate the server's diagnostic counters in the `aborted_connects` status variable and the `host_cach`e table. Use the collected information to identify and fix clients that run into connection issues. Also, note that this parameter has no effect if `skip_name_resolve` is set to `1` (default).

See the MySQL Reference Manual for details on the following:
+ [Max\_connect\_errors variable](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_connect_errors)
+ ["Host is blocked" error](https://dev.mysql.com/doc/refman/8.0/en/host-cache.html#blocked-host)
+ [Aborted\_connects status variable](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html#statvar_Aborted_connects)
+ [Host\_cache table](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-host-cache-table.html)

## Implement connection pooling
<a name="connection-pooling"></a>

A scaling event might add more application servers, which in-turn might cause the DB server to exceed the fully loaded active connections number. The addition of a connection pool or proxy layer between the application servers and the database acts like a funnel, reducing the total number of connections on the database. A proxy's main purpose is reuse of database connections by means of multiplexing.

On one side, the proxy connects to the database with a controlled number of connections. On the other side, the proxy accepts application connections. It also provides additional features, such as query caching, connection buffering, query rewriting and routing, and load balancing. The connection pool layer needs to be configured to keep the maximum number of connections to the database below the fully loaded number. [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) is a fully managed proxy that you can implement for this purpose. Amazon RDS Proxy requires no code changes for most applications, and you don't need to manage any extra infrastructure to implement the solution.

You can also explore the following third-party proxies that can be used with Aurora MySQL Compatible:
+ [ProxySQL](https://proxysql.com/)
+ [MariaDB MaxScale](https://mariadb.com/kb/en/maxscale/)
+ [ScaleARC](https://www.scalearc.com/)
+ [Heimdall Data](https://aws.amazon.com/blogs/apn/using-the-heimdall-proxy-to-split-reads-and-writes-for-amazon-aurora-and-amazon-rds/)

### Avoid connection storms
<a name="avoid-connection-storms.afacb958-a9bf-5015-9305-53bc3cd26744"></a>

Consider how your connection pool behaves in the event of an overloaded database or a replica falling too far behind the primary node. When configuring your proxy server or connection pools, ensure that you do not reset the entire connection pool based on slow database responses (caused by underlying hardware or storage issues or DB resource constraints).

Suddenly starting hundreds of connections generates a *connection storm* because a large number of requests for new connections to the database are all initiated at the same time. The storm is resource intensive. Creating a new database connection in MySQL is an expensive operation because the backend exchanges several network packets for the initial handshake, spawns a new process, allocates memory, handles authentication, and so on. If a large number of requests are received in a short period of time, the database can appear to be unresponsive.

MySQL has a mechanism to protect against such a spike in connection requests. The `back_log` variable can be set to the number of requests that can be stacked during a short time before MySQL momentarily stops answering new requests. The value is enforced by a connection handling thread, which itself might get overwhelmed by a connection storm. For more information, see the [MySQL Reference Manual](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_back_log).

If your connection is configured to reset when the database is slow, you will be initiating the cycle again and again. Similarly, if you anticipate a sudden increase in database traffic at certain times during the day (for example, when the stock market opens), prewarm your connection pool so that you are not trying to open many connections at the same time that a high traffic load is starting.

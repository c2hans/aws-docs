---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/migration-options.html
---

# Migration options
<a name="migration-options"></a>

The following decision tree diagram presents the options as different migration paths based on the platform family, outage requirements, and configuration. These paths can help you understand different options:
+ Little endian compared with big endian
+ A short outage window (less than 15 minutes, with time unrelated to database size) compared with a long outage window (more than 15 minutes, with time related to the database size)
+ [Data Partitioning Feature (DPF)](https://www.ibm.com/docs/en/db2/11.5?topic=environment-setting-up-partitioned-database) has been used or not

![Options shown in the diagram are described in the following tables.](http://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/images/guide-img/4110482b-c82b-44be-8423-7af4c399c9a0/images/9e25b02a-2526-431d-be44-bece1e4adcfd.png)

|
|
| Note:Options 4, 7, and 8 require additional licenses.For options 1, 8, 9, and 10, the exact outage window is based on the database size. |
| --- |

The following tables show high-level comparisons of the migration options based on the source platform.

## Little-endian platform
<a name="little-endian-platform"></a>

|  |
| --- |
|  | Backup and restore | HADR failover | Backup and restore with log shipping |
| --- |--- |--- |--- |
| Outage | Long (related to DB size) | Short | Short |
| Complexity | Low | Medium | Medium |
| Extra license | No | No | No |
| DB size limit | Small to medium size | Any size | Any size |
| Schema migration required | No | No | No |
| Supports non-logged transaction | Yes | No | No |
| DPF support | Yes | No | Yes |
| Fallback capability | Manual setup | Automatic | Manual setup |

## Logical replication
<a name="logical-replication"></a>

|  |
| --- |
|  | Q Replication | SQL Replication | AWS DMS |
| --- |--- |--- |--- |
| Outage | Short | Short | Short |
| Complexity | High | High | Medium |
| Extra license | Yes | No | No |
| DB size limit | Any size | Any size | Any size |
| Schema migration required | Yes | Yes | Yes |
| Performance impact on source database | Low | High | Low |
| Replication performance for heavy write traffic | Good | Bad | Good |
| Supports non-logged transaction | No | No | No |
| DPF support | Yes | Yes | Yes |
| Fallback capability | Reverse replication | Reverse replication | Reverse replication |

## Big-endian platform
<a name="big-endian-platform"></a>

In the following table, logical replication includes Q Replication, SQL Replication, InfoSphere CDC, and third-party replication tools.

|  |
| --- |
|   | Logical replication | Unload and load |
| --- |--- |--- |
| **Optim High Performance Unload** | **LOAD FROM CURSOR** | **db2move** |
| Outage | Short | Medium | Varies | Varies |
| Complexity | High | Medium | Medium | Low |
| Extra license | Depends (See the Logical replication table.) | Yes | No | No |
| DB size limit | Any size | Medium | Small | Small |
| Schema migration required | Yes | Yes | Yes | Yes |
| Supports non-logged transaction | No | Yes | Yes | Yes |
| DPF support | Yes | Yes | Yes | Yes |
| Fallback capability | Reverse replication | Extract and load new data | Extract and load new data | Extract and load new data |

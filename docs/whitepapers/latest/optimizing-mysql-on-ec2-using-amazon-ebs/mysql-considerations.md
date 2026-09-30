---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/mysql-considerations.html
---

# MySQL considerations
<a name="mysql-considerations"></a>

 MySQL offers a lot of parameters that you can tune to obtain efficient performance for every type of workload. This section focuses on the MySQL InnoDB storage engine. It also looks at the MySQL parameters that you can optimize to improve performance related to the I/O of Amazon EBS volumes.

## Caching
<a name="caching"></a>

 Caching is an important feature in MySQL. Knowing when MySQL will perform a disk I/O instead of accessing the cache will help you tune for performance. When you are reading or writing data, an InnoDB buffer pool caches your table and index data. This in-memory area resides between your read/write operations and the Amazon EBS volumes. Disk I/O will occur if the data you are reading isn't in the cache or when the data from dirty (that is, modified only in memory) InnoDB pages needs to be flushed to disk.

 The buffer pool uses the Least Recently Used (LRU) algorithm for cached pages. When you size the buffer pool too small, the buffer pages might have to be constantly flushed to and from the disk, which affects performance and lowers the query concurrency. The default size of the buffer pool is 128 MB. You can [set this value](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html) to 80 percent of your server's memory; however, be aware that there might be paging issues if other processes are consuming memory. Increasing the size of the buffer pool works well when your dataset and queries can take advantage of it. For example, if you have one GiB of data and the buffer pool is configured at 5 GiB, then increasing the buffer pool size to 10 GiB will not make your database faster. A good rule of thumb is that the buffer pool should be large enough to hold your "hot" dataset, which is composed of the rows and indexes that are used by your queries. Starting in MySQL 5.7 version, the `innodb_buffer_pool_size` can be set dynamically, which allows you to resize the buffer pool without restarting the server.

## Database writes
<a name="database-writes"></a>

 InnoDB does not write directly to disk. Instead, it first writes the data into a double write buffer. Dirty pages are the modified portion of these in-memory areas. The dirty pages are flushed if there isn't enough free space. The default setting (`innodb_flush_neighbors = 1`) results in a sequential I/O by flushing the contiguous dirty pages in the same extent from the buffer pool. This option should be turned off (by setting `innodb_flush_neighbors = 0`) so you can maximize the performance by spreading the write operations over your Amazon EBS SSD volumes.

 Another parameter that can be modified for write-intensive workloads is `innodb_log_file_size`. When the size of your log file is large there are fewer data flushes, which reduces disk I/O. However, if your log file is too big, you will generally have a longer recovery time after a crash. MySQL recommends that the size of your log files should be large enough where your MySQL server will spread out the checkpoint flush activity over a longer period. The recommendation from MySQL is to size the log file to where it can accommodate an hour of write activity.

## MySQL read replica configuration
<a name="mysql-read-replica-configuration"></a>

 MySQL allows you to replicate your data so you can scale out your read-heavy workloads with primary / secondary (read replica) configuration. You can create multiple copies of your MySQL database into one or more secondary databases so that you can increase the read throughput of your application. The availability of your MySQL database can be increased with the secondary. When a primary instance fails, one of the secondary servers can be promoted, reducing the recovery time.

 MySQL supports different replication methods. There is the traditional binary log file position-based replication where the primary's binary log is synchronized with the secondary's relay log. The following diagram shows the binary log file position-based replication process.

![Diagram showing the Binary log file position-based replication process](https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/images/binary-log-replication-process.jpg)

 Replication between primary and secondary using global transaction identifiers (GTIDs) was introduced in MySQL 5.6. A GTID is a unique identifier created and associated with each transaction committed on the server of origin (primary). This identifier is unique not only to the server on which it originated, but is unique across all servers in a given replication setup. With GTID-based replication, it is no longer necessary to keep track of the binary log file or position on the primary to replay those events on the secondary. The benefits of this solution include a more malleable replication topology, simplified failover, and improved management of multi-tiered replication.

## MySQL replication considerations
<a name="mysql-replication-considerations"></a>

 Prior to MySQL 5.6, replication was single threaded, with only one event occurring at a time. Achieving throughput in this case was usually done by pushing a lot of commands at low latency. To obtain larger I/O throughput, your storage volume requires a larger queue depth. An Amazon EBS io1 SSD volume can have up to 64,000 IOPS, which, in turn, means it has a larger queue depth. AWS recommends using this volume type on workloads that require heavy replication.

 As mentioned in the [*Provisioned IOPS SSD volumes*](ebs-volume-types.md#provisioned-iops-ssd-io1-volumes) section of this document, RAID 0 increases the performance and throughput of Amazon EBS volumes for your MySQL database. You can join several volumes together in a RAID 0 configuration to use the available bandwidth of the Amazon EBS–optimized instances to deliver the additional network throughput dedicated to Amazon EBS. For MySQL 5.6 and above, replication is multi-threaded. This performs well on Amazon EBS volumes because it relies on parallel requests to achieve maximum I/O throughput. During replication there are sequential and random traffic patterns.

 There are the sequential writes for the binary log (binlog) shipment from the primary server and sequential reads of the binlog and relay log. Additionally, there is the traffic of regular random updates to your data files. Using RAID 0 in this case improves the parallel workloads since it spreads the data across the disks and their queues. However, you must be aware of the penalty from the sequential and single-threaded workloads because extra synchronization is needed to wait for the acknowledgments from all members in the stripe. Only use RAID 0 if you need more throughput than that which the single Amazon EBS volume can provide.

## Switching from a physical environment to AWS
<a name="switching-from-a-physical-environment-to-aws"></a>

 Customers migrating from their physical MySQL Server environment into AWS usually have a battery-backed caching RAID controller, which allows data in the cache to survive a power failure. Synchronous operations are set up so that all I/O is committed to the RAID controller cache instead of the OS main memory. Therefore, it is the controller instead of the OS that completes the write process. Due to this environment, the following MySQL parameters are used to ensure that there is no data loss:

 **On the Primary Side**

```
sync_binlog = 1
innodb_flush_log_at_trx_commit=1
```

 **On the Secondary Side**

```
sync_master_info = 1
sync_relay_log = 1
sync_relay_log_info = 1
innodb_flush_log_at_trx_commit=1
```

 These parameters will cause MySQL to call `fsync()` to write the data from the buffer cache to the disk after any operation with the binlog and relay log. This is an expensive operation that increases the amount of disk I/O.

 The immediate synchronize log to disk MySQL parameter does not provide any benefit for Amazon EBS volumes. In fact, it causes degraded performance. Amazon EBS volumes are automatically replicated within an Availability Zone, which protects them from component failures. Turning off the `sync_binlog` parameter allows the OS to determine when to flush the bin and relay log buffers to the disk, reducing I/O.

 The `innodb_flush_log_at_trx_commit=1` is required for full ACID compliance. If you need to synchronize the log to disk for every transaction, then you might want to consider increasing the IOPS and throughput of the Amazon EBS volume. In this situation, you might want to separate the binlog and relay log from your data files as separate Amazon EBS volumes. You can use Provisioned IOPS SSD volumes for the binlog and relay log to have more predictable performance. You might also use the local SSD of the MySQL secondary instance if you need more throughput and IOPS.

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/postgresql-considerations.html
---

# PostgreSQL considerations
<a name="postgresql-considerations"></a>

 PostgreSQL offers many settings that can be tuned to obtain efficient performance for every type of workload. This section focuses on the PostgreSQL database engine settings. It also looks at the PostgreSQL parameters that can be optimized to improve performance related to Amazon EBS volumes I/Os.

## Caching
<a name="caching"></a>

 PostgreSQL tracks the access patterns of data and keeps frequently accessed data in cache. While PostgreSQL does have a few parameter settings that directly affect memory allocation for the purposes of caching, most of the cache that PostgreSQL uses is provided by the underlying operating system. PostgreSQL also uses caching of its data in a space called `shared_buffers`. Knowing when PostgreSQL will perform a disk I/O instead of accessing the cache helps performance tuning. While reading data, `shared_buffers` caches recent accessed data. While writing, `shared_buffers` hosts dirty pages. This in-memory area resides between read/write operations and the Amazon EBS volumes. Disk I/O occurs if the data is not in the cache for read requests, or when the data from dirty pages are flushed to disk.

 The `shared_buffers` uses the Least Recently Used (LRU) algorithm for cached pages. When the size of `shared_buffers` is too small, it could result in frequent read I/O operations to get data from storage and the buffer pages might have to be constantly flushed to and from the disk. This affects performance and lowers the query concurrency. The default size of the shared buffers is 128 MB. Increasing the size of the `shared_buffers` works well when the dataset and queries take advantage of it. For example, if you have 1 GiB of data and the `shared_buffers` is configured at 5 GiB, then increasing the `shared_buffers` size to 10 GiB doesn't make the database faster. A good rule of thumb is that the `shared_buffers` should be large enough to hold the working dataset, which is composed of the rows and indexes that are used by the queries. For most PostgreSQL workloads, 20%-25% of total RAM as `shared_buffers` is a good practice. While modifying `shared_buffers` parameter, you should consider that enough memory is left for other database operations such as sorting, hashing, auto-vacuum, temp\_buffers, and wal\_buffers.

## Database writes
<a name="database-writes"></a>

 PostgreSQL does not write directly to disk. Instead, PostgreSQL writes all modifications into a persistent storage to prepare for failures. In PostgreSQL, Write Ahead Logging (WAL) is the standard method for ensuring data integrity. It makes sure that changes to data files must be written only after those changes have been logged, that is, after log records describing the changes have been flushed to permanent storage. WAL data records are written into the in-memory WAL buffer by change operations such as insertion, deletion, or commit actions. Then, they are written into WAL segment files on the storage when a transaction commits or aborts. Now, background writer process keeps flushing modified data pages to Amazon EBS volumes permanent storage. Checkpoints make sure that all modified data pages have been flushed to storage after a point in time.

 Frequent checkpoints can cause high IOs, high commit latency and low throughput. In practice, checkpoints should happen infrequently not to affect the users, but frequently enough to reasonably limit time for recovery and disk space requirements. A checkpoint begins after every checkpoint\_timeout seconds, or if max\_wal\_size is about to be exceeded, whichever comes first. The default settings are 5 minutes and 1 GB respectively. Reducing these parameters allows faster after-crash recovery, since less work will need to be redone. However, this could increase the cost of flushing modified data pages more often. Checkpoint\_completion\_target parameter specifies the target of checkpoint completion, as a fraction of total time between checkpoints.  Reducing this parameter is not recommended because it causes the checkpoint to complete faster. This results in a higher rate of I/O during the checkpoint followed by a period of less I/O between the checkpoint completion and the next scheduled checkpoint.

## PostgreSQL read replica configuration
<a name="postgresql-read-replica-configuration"></a>

 PostgreSQL allows you to replicate data so you can scale out read-heavy workloads with source/replica configuration. You can create multiple copies of PostgreSQL databases into one or more replica instances to increase the read throughput for application. The availability of PostgreSQL database can be increased with the replicated instances. When a source instance fails, one of the replica instance servers can be promoted, reducing the recovery time.

 In PostgreSQL, there are two types of replication methods: Physical replication that collectively replicates a database cluster, and logical replication that replicates given database objects such as tables, schemas and databases. PostgreSQL built-in streaming replication (physical replication) continuously sends data changes from primary instance to secondary instance. In cascaded replication, secondary instances can also be senders as well as receivers. `max_wal_senders`, `max_replication_slots`, `wal_keep_size`, `max_slot_wal_keep_size`, `wal_sender_timeout` are some of the parameters that can be set at primary server to send replication data to one or more secondary instances. The `max_wal_senders` parameter specifies the maximum number of concurrent connections from secondary instances. The default is 10. The value 0 means replication is disabled. The `wal_keep_size` parameter specifies the minimum size of WAL segments kept in the `pg_wal` directory, in case a standby server needs to fetch them for streaming replication. If a secondary instance connected to the sending server falls behind by more than `wal_keep_size` megabytes, the sending server might remove a WAL segment still needed by the standby, in which case the replication connection will be terminated. However, the standby server can recover by fetching the segment from archive, if WAL archiving is in use. `wal_keep_size` should be set high enough that spiky write workloads don't terminate replication. The following diagram illustrates how PostgreSQL performs streaming replication:

![Diagram that illustrates how PostgreSQL performs streaming replication.](https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image1.png)

 In PostgreSQL, logical replication is a method of replicating data objects and their changes, based upon their replication identity, usually a primary key. Unlike physical replication which uses exact block addresses and byte-by-byte replication, logical replication uses a *publish* and *subscribe* model with one or more *subscribers* subscribing to one or more *publications* on a *publisher* node. Subscribers pull data from the publications they subscribe to and might subsequently re-publish data to allow cascading replication or more complex configurations. Logical replication of a table typically starts with taking a snapshot of the data on the publisher database and copying that to the subscriber. Once that is done, the changes on the publisher are sent to the subscriber as they occur in real-time. The subscriber applies the data in the same order as the publisher so that transactional consistency is guaranteed for publications within a single subscription. This method of data replication is sometimes referred to as transactional replication. The following diagram represents the data flow for initial data copy and synchronization.

![Diagram that represents the data flow for initial data copy and synchronization.](https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image2.png)

 *PostgreSQL logical replication*

## PostgreSQL replication considerations
<a name="postgresql-replication-considerations"></a>

 PostgreSQL has single process for replaying Write Ahead Logs (WAL) file. Running out of IOs can cause replication lag. To obtain larger I/O throughput, storage volume requires a larger queue depth. An Amazon EBS io1 or io2  can provide up to 64,000 IOPS/volume, which, in turn, means it has a larger queue depth. An Amazon EBS io2 Block Express SSD volumes can provide up to 256,000 IOPS/volume.  AWS recommends using this volume type on workloads that require heavy replication.

 As mentioned in the [Provisioned IOPS SSD volumes](ebs-volume-types.md#provisioned-iops-ssd-volumes) section of this document, RAID 0 increases the performance and throughput of Amazon EBS volumes for your PostgreSQL database. You can join several volumes together in a RAID 0 configuration to use the available bandwidth of the Amazon EBS–optimized instances to deliver the additional network throughput dedicated to Amazon EBS.

 There are the sequential writes for the WAL shipment from the primary server and sequential reads of the WAL. Additionally, there is the traffic of regular random updates to your data files. Using RAID 0 in this case improves the parallel workloads since it spreads the data across the disks and their queues. However, you must be aware of the penalty from the sequential and single-threaded workloads because extra synchronization is needed to wait for the acknowledgments from all members in the stripe. Only use RAID 0 if you need more throughput than that which the single Amazon EBS volume can provide. As RAID 0 has no data redundancy, for high read and write throughput, RAID10 (mirrored striped sets) should be considered.

## Migrating PostgreSQL from on-premises to Amazon EC2
<a name="migrating-postgresql-from-on-premises-to-amazon-ec2"></a>

 Migrating databases requires strategy, resources, and downtime maintenance. If you have already running PostgreSQL databases out of AWS, you have several options to migrate to Amazon EC2 hosted PostgreSQL. If downtime is affordable, you can use `pg_dump/ pg_restore` to migrate PostgreSQL databases from on-premises to Amazon EC2.

 Single database backup:

```
pg_dump --host <hostname> --format=directory --create --jobs 5 --dbname <database name> --username <username> --file /home/db11.dump
pg_restore --host <hostname> --format=directory --create --jobs 5 --dbname <database name> --username <username> --file /home/ec2-user/db11.dump
```

 `pg_dumpall` can be used for migrating all databases along with globals.

 Backup all databases:

 `pg_dumpall > alldb.dump`

 Restore all databases:

 `psql -f alldb.dump postgres`

 If downtime is not permissible, you can set up physical replication between on-premises PostgreSQL and Amazon EC2 hosted PostgreSQL. Once data is in sync with no replica lag, you can promote Amazon EC2 PostgreSQL and set it up as new primary. For setting up physical replication, customers need to do these changes:

 On the on-premises PostgreSQL side:

```
echo "listen_addresses = '*'" >> $PGDATA/postgresql.conf
echo "wal_level = replica" >> $PGDATA/postgresql.conf
systemctl restart postgresql
postgres=# CREATE USER migration_replication WITH REPLICATION ENCRYPTED PASSWORD 'secret';
echo "host replication migration_replication 192.0.2.11/32 md5" >> $PGDATA/pg_hba.conf
psql -c "select pg_reload_conf()"
```

 On the EC2 PostgreSQL side:

```
pg_ctl -D $PGDATA start
pg_basebackup -h <primary IP> -U migration_replication -p 5432 -D $PGDATA  -Fp -Xs -R
```

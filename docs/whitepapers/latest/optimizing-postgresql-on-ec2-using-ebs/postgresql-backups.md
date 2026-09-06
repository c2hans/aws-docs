---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/postgresql-backups.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# PostgreSQL backups
<a name="postgresql-backups"></a>

## Backup methodologies
<a name="backup-methodologies"></a>

 There are several approaches to protect PostgreSQL data depending on recovery time objective (RTO) and recovery point objective (RPO) requirements. PostgreSQL production databases should be backed up regularly. There are three fundamentally different approaches to back up PostgreSQL data:
+ **SQL dump**

  This is the method to generate a file with SQL commands that, when fed back to the server, will recreate the database in the same state as it was at the time of the backup. PostgreSQL provides the utility program `pg_dump` for this purpose. The basic usage of this command is:

  ```
  pg_dump dbname > dumpfile
  ```

   `pg_dump` is a PostgreSQL client application that perform backup procedure from any remote host that has access to the database. The user running `pg_dump` command should have read access to the objects being backed up. `pg_dump` can be used to back up given tables, schemas or databases. The `pg_dump` file can be restored by using psql client or `pg_restore` utility. `pg_dumpall` backs up all databases in the given cluster, and also preserves cluster-wide data such as roles and tablespace definitions. The basic usage of this command is:

  ```
          pg_dumpall > dumpfile
  ```

  The resulting dump can be restored with `psql`:

  ```
  psql -f dumpfile postgres
  ```
+ **File system level backup:**

  An alternative backup strategy is to directly copy the files that PostgreSQL uses to store the data in the database. You can use your preferred method for file system backups. For example:

  ```
  tar -cf backup.tar /usr/local/pgsql/data
  ```

  There are two restrictions, however, which make this method impractical, or at least inferior to the `pg_dump` method.
  + The database server must be shut down in order to get a usable backup. Half-way measures such as disallowing all connections will not work.
  + File system backups only work for complete backup and restoration of an entire database cluster.

  Unlike `pg_dump`, it can't be used to back up given tables, schemas or databases.  Alternatively, you can use `pg_basebackup`, a PostgreSQL native utility to take a base backup of a PostgreSQL cluster. The following is the basic command to use `pg_basebackup`:

  ```
  pg_basebackup -h <host> -D <PostgreSQL data directory>
  ```
+ **Continuous archiving**

  The WAL log records every change made to the database's data files. This log exists primarily for crash-safety purposes. If the system crashes, the database can be restored to consistency by "replaying" the log entries made since the last checkpoint. However, the existence of the log makes it possible to use a third strategy for backing up databases. We can combine a file-system-level backup with backup of the WAL files. If recovery is needed, we restore the file system backup and then replay from the backed-up WAL files to bring the system to a current state. This PostgreSQL [document](https://www.postgresql.org/docs/current/continuous-archiving.html) discusses about setting up continuous archiving.

 If the primary database server exhibits performance issues during a backup, a replicated secondary database server can be used for the backups to alleviate the backup load from the primary database server. One approach can be to back up from a secondary server's SSD data volume to a backup server's Throughput Optimized HDD (st1) volume. The high throughput of 500 MiB/s per volume and large 1 MiB I/O block size make it an ideal volume type for sequential backups meaning it can use the larger I/O blocks. The following diagram shows a backup server using the PostgreSQL secondary server to read the backup data.

![Diagram that shows a backup server using the PostgreSQL secondary server to read the backup data.](http://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image3.png)

 Regarding file system level backup, `pg_basebackup` is a widely used PostgreSQL backup tool that allows us to take an online and consistent file system level backup. These backups can be used for point-in-time-recovery or to set up a secondary PostgreSQL server. The following image shows PostgreSQL files system backup using `pg_basebackup` and streaming the write-ahead logs from a running PostgreSQL cluster:

![Diagram that shows PostgreSQL files system backup using pg_basebackup and streaming the write-ahead logs from a running PostgreSQL cluster.](http://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image4.png)

 Another option is to have the PostgreSQL secondary server back up the database files directly to Amazon Elastic File System (Amazon EFS) or Amazon S3. Amazon EFS stores its data redundantly across multiple Availability Zones. Both the primary and the secondary instances can attach to Amazon EFS. The secondary instance can initiate a backup to Amazon EFS from where the primary instance can do a restore. Amazon S3 can also be used as a backup target. Amazon S3 can be used in a manner similar to Amazon EFS except that Amazon S3 is object-based storage rather than a file system. The following diagram depicts the option of using Amazon EFS or Amazon S3 as a backup target.

![Diagram that depicts the option of using Amazon EFS or Amazon S3 as a backup target.](http://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image5.png)

 Second approach of backing up PostgreSQL database is to use volume-level EBS snapshots. Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved. This minimizes the time required to create the snapshot and saves on storage costs. When you delete a snapshot, only the data unique to that snapshot is removed. Active snapshots contain all the information needed to restore your data to a new Amazon EBS volume.

 One consideration when utilizing Amazon EBS snapshots for backups is to make sure the PostgreSQL data remains consistent. During an Amazon EBS snapshot, any data not flushed from cache to disk will not be captured. There is a PostgreSQL command CHECKPOINT that flushes all the modified data pages from buffers to the disk. The snapshot takes a point-in-time capture of all the content within that volume. The database lock needs to be active until the snapshot process starts, but it doesn't have to wait for the snapshot to complete before releasing the lock. You can use [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) to automate the creation, retention, and deletion of Amazon EBS snapshots and Amazon EBS-backed AMIs.

 You can also combine these approaches for an effective backup strategy. You can use database-level backups for more granular objects, such as databases or tables. You can leverage Amazon EBS snapshots for large scale operations such as recreating the database server, restoring the entire volume or migrating a database server to another Availability Zone or another Region for disaster recovery (DR).

## Multi-Volume Crash-Consistent Snapshots
<a name="multi-volume-crash-consistent-snapshots"></a>

 Amazon Elastic Block Store ([Amazon EBS](https://aws.amazon.com/ebs/)) enables to back up volumes at any time using Amazon EBS snapshots. Snapshots retain the data from all completed I/O operations, allowing you to restore the volume to its exact state at the moment before backup (referred to as crash-consistency). There is a one-click solution to take backups across multiple Amazon EBS volumes while ensuring that the data on each volume is in sync. Refer to this [user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html#ebs-create-snapshots) for details.

 Additionally, you can use AWS Backup, which creates crash-consistent backups of Amazon EBS volumes that are attached to an Amazon EC2 instance. Crash consistency means that the snapshots for every Amazon EBS volume attached to the same Amazon EC2 instance are taken at the exact same moment. You no longer have to stop your instances or coordinate between multiple Amazon EBS volumes to ensure crash-consistency of your application state.

 Refer to the [*AWS Backup Developer Guide*](https://docs.aws.amazon.com/aws-backup/latest/devguide/multi-volume-crash-consistent.html) for details.

 You can evaluate PostgreSQL performance related to storage by looking at latency when you run into performance issues of transactional operations. Further, if the performance is degraded due to PostgreSQL loading or replicating data, then throughput is evaluated. These issues are diagnosed by looking at the Amazon EBS volume metrics collected by [CloudWatch](https://aws.amazon.com/cloudwatch/).

## Throughput
<a name="throughput"></a>

 Throughput is the measure of the amount of data transferred from/to a storage. It affects PostgreSQL database workload, replication, backup, and import/export activities. When considering which AWS storage option to use to achieve high throughput, you must also consider that PostgreSQL has random I/O caused by small transactions that are committed to the database. To accommodate these two different types of traffic patterns, our recommendation is to use io1, io2/io2bx  volumes on an Amazon EBS-optimized instance.

 Amazon EBS calculates throughput using the equation:

```
Throughput = Number of IOPS * size per I/O operation
```

Insufficient throughput to underlying Amazon EBS volumes can cause PostgreSQL secondary servers to lag, and can also cause PostgreSQL backups to take longer to complete. To diagnose throughput issues, CloudWatch provides the metrics Volume Read/Write Bytes (the amount of data being transferred) and Volume Read/ Write Ops (the number of I/O operations).

 You can use the CloudWatch metric to monitor the Amazon EBS volume level throughput:

```
 Read Bandwidth (KiB/s) = Sum(VolumeReadBytes) / Period / 1024
 Write Bandwidth (KiB/s) = Sum(VolumeWriteBytes) / Period / 1024
```

## Latency
<a name="latency"></a>

 Latency is the round-trip time elapsed between sending a PostgreSQL I/O request to an Amazon EBS volume and receiving an acknowledgement from the volume that the I/O read or write is complete. Latency is experienced by slow queries, which can be diagnosed in PostgreSQL by enabling the parameter [log\_min\_duration\_statement](https://www.postgresql.org/docs/current/runtime-config-logging.html) to log slow queries.

 Latency can also occur at the disk I/O-level, which can be viewed in the "Average Read Latency (ms/op)" and "Average Write Latency (ms/op)" in the monitoring tab of the Amazon EC2 console.

 Average Read Latency (ms/op) is defined as blow:

```
 Avg(VolumeTotalReadTime) × 1000
```

 For Nitro-based instances, the following formula derives Average Read Latency using [CloudWatch Metric Math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html):

```
 (Sum(VolumeTotalReadTime) / Sum(VolumeReadOps)) × 1000
```

 The `VolumeTotalReadTime` and `VolumeReadOps` metrics are available in the Amazon EBS CloudWatch console.

 Average Write Latency (ms/op) is defined as follows:

```
 Avg(VolumeTotalWriteTime) × 1000
```

 For Nitro-based instances, the following formula derives Average Write Latency using [CloudWatch Metric Math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html):

```
 (Sum(VolumeTotalWriteTime) / Sum(VolumeWriteOps)) * 1000
```

 The `VolumeTotalWriteTime` and `VolumeWriteOps` metrics are available in the Amazon EBS CloudWatch console.

 This section covers the factors contributing to high latency for `gp2`, `gp3`, `io1`, and `io2` Amazon EBS volumes. High latency can result from exhausting the baseline IOPS in Amazon EBS volumes. However, gp2 volumes comes with burstable performance. If the workload is driving I/O traffic beyond its baseline performance, then burst credit gets depleted. If burst credit reaches zero, then these volume types get throttled at their baseline IOPS or throughput. The CloudWatch metric `BurstBalance` indicates if you have depleted the available burstable credit for IOPS for `gp2` volumes.

 **Burst duration** can be calculated as follows:

```
                        (I/O credit balance)
Burst duration = ------------------------------
                   (Burst IOPS) - (Baseline IOPS)
```

 For example, for 100 GB `gp2` volume, the baseline IOPS is 100\*3=300 IOPS. However, any `gp2` volume upto 1000 GB comes with burstable capability upto 3,000 IOPS.  Hence, this particular volume will be able to sustain a workload upto 3,000 IOPS for the burst duration of 2000 secs as calculated from the above formula. After the burst credit are depleted, the volume performance will be back to baseline of 300 IOPS.

 Disk queue length can also contribute to high latency. Disk queue length refers to the outstanding read/write requests that are waiting for instance and volume resources to be available. The CloudWatch metric `VolumeQueueLength` shows the number of pending read/write operation requests for the volume.

```
 Avg Queue Length (Operations) = Avg(VolumeQueueLength)
```

 This metric is an important measurement to monitor if you have reached the full utilization of the allocated IOPS on your Amazon EBS volumes. A value of average queue length greater than one for every 1000 IOPS can cause latency.

 It is recommended to monitor the CloudWatch metrics for IOPS and throughput so it that does not go beyond the provisioned limits. If it goes beyond that limit, it causes the I/O to be queued up a disk level which in turn increase the Round-trip time for the I/O.  This increases the latency, and thus impacts the PostgreSQL database performance.

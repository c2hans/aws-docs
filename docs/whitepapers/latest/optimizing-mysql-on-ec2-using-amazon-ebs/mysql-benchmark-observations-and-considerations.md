---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/mysql-benchmark-observations-and-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MySQL benchmark observations and considerations
<a name="mysql-benchmark-observations-and-considerations"></a>

 Testing your MySQL database will help you determine what type of volume you need and ensure that you are choosing the most cost-effective and performant solution.

 There are a couple of ways to determine the number of IOPS that you need. For an existing workload, you can monitor the current consumption of EBS volume IOPS through the CloudWatch metrics detailed in the [*Monitoring MySQL and EBS volumes*](mysql-backups.md#monitoring-mysql-and-ebs-volumes) section of this document.

 If this is a new workload, you can do a synthetic test, which will provide you with the maximum number of IOPS that your new AWS infrastructure can achieve. If you are moving your workload to the AWS Cloud, you can run a tool such as `iostat` to profile the IOPS required by your workload. While you can use a synthetic test to estimate your storage performance needs, the best way to quantify your storage performance needs is through profiling an existing production database if that is an option.

 Performing a synthetic test on the EBS volume allows you to specify the amount of concurrency and throughput that you want to simulate. Testing will allow you to determine the maximum number of IOPS and throughput needed for your MySQL workload.

 There are a couple of tools that you can use:
+  [Mysqlslap](http://dev.mysql.com/doc/refman/5.7/en/mysqlslap.html) is an application that emulates client load for MySQL Server.
+  [Sysbench](https://dev.mysql.com/downloads/benchmarks.html) is a popular open-source benchmark used to test open-source database management systems (DBMS).

## The test environment
<a name="the-test-environment"></a>

 To simulate the MySQL client for the Sysbench tests, this example uses an r5.8xlarge instance type with a 10-gigabit network interface.

 *Table 1: Sysbench machine specifications *

|  Sysbench server  |   |
| --- | --- |
|  Instance type  | r5.8xlarge |
|  Memory  |  256 GB  |
|  CPU  |  32 vCPUs  |

 All of the MySQL servers tested on used the `r5.8xlarge` instance type.

* Table 2: MySQL server machine specifications *

|  MySQL server  |   |
| --- | --- |
|  Instance type  | r5.8xlarge  |
|  Memory  |  256 GB  |
|  CPU  |  32 vCPUs  |
|  Storage  |  500 GB gp2 EBS Volume  |
|  Root volume  |  256 GB gp2  |
|  MySQL data volume  |  500 GB (gp2, gp3, io1 or io2)  |

 To increase performance on the Sysbench Linux client, enable Receive Packet Steering (RPS) and Receive Flow Steering (RFS). RPS generates a hash to determine which CPU will process the packet. RFS handles the distribution of packets to the available CPUs.

 Enable RPS with the following shell command:

```
sudo sh -c 'for x in /sys/class/net/eth0/queues/rx-*; do echo ffffffff > $x/rps_cpus; done'
sudo sh -c "echo 4096 > /sys/class/net/eth0/queues/rx-0/rps_flow_cnt"

sudo sh -c "echo 4096 > /sys/class/net/eth0/queues/rx-1/rps_flow_cnt
```

 Enable RFS with the following shell command:

```
sudo sh -c "echo 32768 > /proc/sys/net/core/rps_sock_flow_entries"
```

## Tuned compared to default configuration parameter testing
<a name="tuned-compared-to-default-configuration-parameter-testing"></a>

 Perform a Sysbench test to compare the difference between tuned MySQL and default parameter configurations (refer to Table 3). Use a MySQL dataset of 100 tables with 10 million records per table for the test.

* Table 3: MySQL parameters *

|  Parameters  |  Default  |  Tuned  |
| --- | --- | --- |
|  innodb\_buffer\_pool\_size  |  134MB  |  193G  |
|  innodb\_flush\_method  |  fsync (Linux)  |  O\_DIRECT  |
|  innodb\_flush\_neighbors  |  1  |  0  |
|  innodb\_log\_file\_size  |  50MB  |  256MB  |

 Run the following Sysbench read/write command:

```
$ sysbench ./oltp_read_write.lua <connection info>  --table_size=10000000 --max-requests=0
--simple-ranges=0 --distinct-ranges=0 --sum-ranges=0 --order-ranges=0 --point-selects=0
--time=3600 --threads=1024 --rand-type=uniform run
```

 Results of the Sysbench test are presented in Table 4. Under optimized conditions, the MySQL server processed approximately 12 times the number of transactions per section compared to the default configuration.

* Table 4: Sysbench results *

|  Sysbench metrics  |  Default  |  Tuned  |
| --- | --- | --- |
|  Queries:  |   |   |
|  Read  |  17511928  |  223566532  |
|  Write  |  5003408  |  63876152  |
|  Other  |  2501704  |  31938076  |
|  Total  |  25017040  |  319380760  |
|  Transactions  |  1250852 (347.37 per sec.)  |  15969038 (4434.57 per sec.)  |
|  Queries  |  25017040 (6947.43 per sec.)  |  319380760 (88691.33 per sec.)  |
|  ignored errors:  |  0 (0.00 per sec.)  |  0 (0.00 per sec.)  |
|  reconnects:  |  0 (0.00 per sec.)  |  0 (0.00 per sec.)  |
|  General statistics:  |   |   |
|  Total time  |  3600.9046s  |  3601.0355s  |
|  Total number of events  |  1250852  |  15969038  |
|  Latency (ms):  |   |   |
|  min  |  7.72  |  4.843  |
|  avg  |  2947.65  |  230.90  |
|  max  |  95885.04  |  6158.04  |
|  95th percentile  |  9284.15  |  1258.08  |
|  sum  |  3687074024.45  |  3687189581.27  |
|  Thread fairness:  |   |   |
|  events (avg/stddev):  |  1221.5352/48.86  |  15594.7637/45.63  |
|  runtime (avg/stddev):  |  3600.6582/0.11  |  3600.7711/0.04  |

 Other InnoDB configuration options to consider for better performance of heavy I/O MySQL workloads are detailed in the [MySQL Optimizing InnoDB Disk I/O documentation](https://dev.mysql.com/doc/refman/5.7/en/optimizing-innodb-diskio.html). When considering these configurations, AWS suggests performing a test after deployment to ensure that it will be safe for your application.

## Comparative analysis of different storage types
<a name="comparative-analysis-of-different-storage-types"></a>

 Conduct the test across four different MySQL server configurations with the following configurations:
+  MySQL Server - EBS General Purpose SSD (gp2)
  +  500 GB SQL data drive
  +  1,500 baseline IOPS / 3,000 burstable IOPS
+  MySQL Server - EBS Provisioned IOPS SSD (gp3)
  +  500 GB SQL data drive
  +  3,000 Provisioned IOPS
+  MySQL Server - EBS Provisioned IOPS SSD (io1)
  +  500 GB SQL data drive
  +  3,000 Provisioned IOPS
+  MySQL Server - EBS Provisioned IOPS SSD (io2)
  +  500 GB SQL data drive
  +  3,000 Provisioned IOPS

**Note**
Unless specified, all EBS volumes are unencrypted.

### Sysbench client and MySQL server setup
<a name="sysbench-client-and-mysql-server-setup"></a>

* Table 5: Server setup for MySQL database and Sysbench client *

|  Use case  |  Instance type  |  vCPUs  |  Memory  |  Instance storage  |  EBS-optimized  |  Network  |
| --- | --- | --- | --- | --- | --- | --- |
|  MySQL database  |  r5.8xlarge  |  32  |  256  |  EBS only  |  Yes  |  10 Gigabit  |
|  Sysbench client (AWS Cloud9)  |  r5.8xlarge  |  32  |  256  |  EBS only  |  Yes  |  10 Gigabit  |

 Tests were performed using Sysbench read/write OLTP test by running the following Sysbench command below over a one-hour period.

```
$ sysbench ./oltp_read_write.lua <connection info>  --table_size=10000000
--max-requests=0 --simple-ranges=0 --distinct-ranges=0 --sum-ranges=0
--order-ranges=0 --point-selects=0 --time=3600 --threads=1024
--rand-type=uniform run
```

### Results
<a name="results"></a>

 The various tests of the four different volume configurations yielded similar results, with each server processing approximately 3,600 Sysbench transactions per second. There was no discernible workload difference is noticed while running performance consistency test in all four volumes. Upon closer examination, you observe that the minimum latency is offered by the IO2 volume and less than one millisecond latency is observed for the same workload.

* Table 6: Performance analysis of same MySQL workload on different EBS volume types *

|  Sysbench metrics  |  gp2  |  gp3  |  io1  |  io2  |
| --- | --- | --- | --- | --- |
|  SQL statistics  |   |   |   |   |
|  read queries  |  17511928  |  181507690  |  188343428  |  186051460  |
|  write queries  |  5003408  |  51859340  |  53812408  |  53157560  |
|  other queries  |  2501704  |  25929670  |  26906204  |  26578780  |
|  total queries  |  25017040  |  259296700  |  269062040  |  265787800  |
|  transactions  |  12508520 <br /> (3470.37 per sec.)  |  12964835 (3600.93 per sec.)  |  13453102 (3733.12 per sec.)  |  13289390 (3690.20 per sec.)  |
|  queries  |  250170400 <br /> (69470.43 per sec.)  |  259296700 (72018.53 per sec.)  |  269062040 (74662.42 per sec.)  |  265787800 (73803.92 per sec.)  |
|  Latency (ms)  |   |   |   |   |
|  min  |  7.72  |  6.82  |  6.1  |  6.02  |
|  avg  |  294.65  |  284.35  |  274.24  |  277.45  |
|  max  |  95885.04  |  43718.24  |  33179.31  |  34803.75  |
|  95th percentile  |  928.15  |  816.63  |  943.16  |  861.95  |
|  sum  |  3687074024.45  |  3686559158.83  |  3689386834.2  |  3687138536.08  |
|  EBS statistics  |   |   |   |   |
|  Write latency (ms)  |  1.1  |  1.01  |  0.994  |  0.824  |
|  Volume queue length (count)  |  3.49  |  3.01  |  3.227  |  2.71  |

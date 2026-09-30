---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/postgresql-benchmark-observations-and-considerations.html
---

# PostgreSQL benchmark observations and considerations
<a name="postgresql-benchmark-observations-and-considerations"></a>

 Testing PostgreSQL database helps determine what type of volume is needed and ensures the most cost-effective and performant solution. For a new workload, you can do a synthetic test, which provides the maximum number of IOPS that the new AWS infrastructure can achieve. If you are moving your workloads to the AWS Cloud, you can run a tool such as `iostat` to profile the IOPS required by your workloads. While you can use a synthetic test to estimate your storage performance needs, the best way to quantify storage performance needs is through profiling an existing production database if that is an option.

 Performing a synthetic test on the Amazon EBS volume allows you to specify the amount of concurrency and throughput that you want to simulate. It also helps determine the maximum number of IOPS and throughput needed for PostgreSQL workloads. [`pgbench`](https://www.postgresql.org/docs/current/pgbench.html) is an open-source benchmark utility to run benchmark tests on PostgreSQL.

## The test environment
<a name="the-test-environment"></a>

 To simulate the PostgreSQL client, we are using `pgbench` as the benchmarking tool. In this example, we are using an `r5.4xlarge` instance type.

 *Table 1: Amazon EC2 machine specifications*

|  Configuration  |  Value  |
| --- | --- |
|  Instance type  |  r5.4xlarge  |
|  Operating system  |  Amazon Linux 6.1.41-63.114.amzn2023.x86\_64  |
|  Memory  |  128 GB  |
|  CPU  |  16 vCPUs  |
|  Root volume  |  100 GB gp2  |
|  PostgreSQL data volume  |  500 GB (gp2, gp3, io1, or io2)  |

As part of the testing, four Amazon EC2 instances are provisioned for each of the volume type (`gp2`, `gp3`, `io1`, `io2`) with `r5.4xlarge` each having 100 GB `gp2` as root volume and 500 GB data volume.

The following `pgbench` settings are used for the performance benchmarking test for each of the Amazon EBS volumes.

Install `pgbench` in each of the PostgreSQL database server:

```
 sudo yum install postgresql15-contrib
```

 Load test data in the each of the PostgreSQL databases:

```
pgbench -i --fillfactor=90 --scale=10000 postgres

bash-5.2$ pgbench -i --fillfactor=90 --scale=10000 postgres
dropping old tables...
NOTICE: table "pgbench_accounts" does not exist, skipping
NOTICE: table "pgbench_branches" does not exist, skipping
NOTICE: table "pgbench_history" does not exist, skipping
NOTICE: table "pgbench_tellers" does not exist, skipping
creating tables...
generating data (client-side)...
1000000000 of 1000000000 tuples (100%) done (elapsed 2441.43 s, remaining 0.00 s))
vacuuming...
creating primary keys...
done in 3096.86 s (drop tables 0.01 s, create tables 0.03 s, client-side generate 2445.44 s, vacuum 0.86 s, primary keys 650.52 s).
```

 Set the max\_connection parameter to 1,000 in the PostgreSQL configuration for each of the servers:

```
echo "max_connections=1000">>/data/pgsql15/data/postgresql.conf
pg_ctl -D /data/pgsql15/data/ restart
```

Run the following command to conduct the performance testing in each of the PostgreSQL servers. `pgbench` uses the `-S` and `-N` options to execute a workload comprising an equal distribution of read and write operations, with 50% of the test involving `UPDATE` queries, and the remaining 50% consisting of `SELECT` queries. The variables that can be adjusted to align with the available system resources are the number of clients and threads. In this benchmarking, we used 5,000 number of worker threads, and 950 clients.

```
 pgbench -U postgres -P 60 -c 950 -j 5000 -T 1800 -S -N postgres
```

## Results
<a name="results"></a>

 The various tests of the four different volume configurations yielded different results. The result set we focused on includes latency average and transaction per second (TPS). The workload was run for 1,800 seconds and below are the trends in our result set. After closer observation, we observe that the minimum latency is offered by `io2` volume, that is 136 ms. See the following performance analysis of same PostgreSQL workload on different Amazon EBS volume types:

|  **`pgbench` metrics**  |  **`gp2`**  |  **`gp3`**  |  **`io1`**  |  **`io2`**  |
| --- | --- | --- | --- | --- |
|  Initial connection time(ms)  |  444  |  420  |  384  |  381  |
|  Number of transactions actually processed  |  10238208  |  11931975  |  10926661  |  11267355  |
|  Transaction Per Sec (TPS)  |  5686  |  6628  |  6748  |  6956  |

The following diagram shows the gradual increase in TPS.

![Graph that shows the gradual increase in TPS.](https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image6.png)

The following graph shows the gradual decrease in latency.

![Graph that shows the gradual decrease in latency.](https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image7.png)

 *Latency comparison for various Amazon EBS storage types*

 The following graph shows the gradual decrease in initial connection time.

![Graph that shows the gradual decrease in initial connection time.](https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/images/image8.png)

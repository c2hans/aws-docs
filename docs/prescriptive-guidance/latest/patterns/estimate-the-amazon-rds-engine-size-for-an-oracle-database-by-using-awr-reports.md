---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports.html
---

# Estimate the Amazon RDS engine size for an Oracle database by using AWR reports
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports"></a>

*Abhishek Verma and Eduardo Valentim, Amazon Web Services*

## Summary
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-summary"></a>

When you migrate an Oracle database to Amazon Relational Database Service (Amazon RDS) or Amazon Aurora, computing the CPU, memory, and disk I/O for the target database is a key requirement. You can estimate the required capacity of the target database by analyzing the Oracle Automatic Workload Repository (AWR) reports. This pattern explains how to use AWR reports to estimate these values.

The source Oracle database could be on premises or hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance, or it could be an Amazon RDS for Oracle DB instance. The target database could be any Amazon RDS or Aurora database.

**Note**
Capacity estimates will be more precise if your target database engine is Oracle. For other Amazon RDS databases, the engine size can vary due to differences in database architecture.

We recommend that you run the performance test before you migrate your Oracle database.

## Prerequisites and limitations
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-prereqs"></a>

**Prerequisites**
+ An Oracle Database Enterprise Edition license and Oracle Diagnostics Pack license in order to download AWR reports.

**Product versions**
+ All Oracle Database editions for versions 11g (versions 11.2.0.3.v1 and later) and up to 12.2, and 18c,19c.
+ This pattern doesn’t cover Oracle Engineered Systems or Oracle Cloud Infrastructure (OCI).

## Architecture
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-architecture"></a>

**Source technology stack  **

One of the following:
+ An on-premises Oracle database
+ An Oracle database on an EC2 instance
+ An Amazon RDS for Oracle DB instance

**Target technology stack**
+ Any Amazon RDS or Amazon Aurora database

**Target architecture**

For information about the full migration process, see the pattern [Migrate an Oracle database to Aurora PostgreSQL using AWS DMS and AWS SCT](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-aurora-postgresql-using-aws-dms-and-aws-sct.html).

**Automation and scale**

If you have multiple Oracle databases to migrate and you want to use additional performance metrics, you can automate the process by following the steps described in the blog post [Right-size Amazon RDS instances at scale based on Oracle performance metrics](https://aws.amazon.com/blogs/database/right-sizing-amazon-rds-instances-at-scale-based-on-oracle-performance-metrics/).

## Tools
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-tools"></a>
+ [Oracle Automatic Workload Repository (AWR)](https://docs.oracle.com/en-us/iaas/performance-hub/doc/awr-report-ui.html) is a repository that’s built into Oracle databases. It periodically gathers and stores system activity and workload data, which is then analyzed by Automatic Database Diagnostic Monitor (ADDM). AWR takes snapshots of system performance data periodically (by default, every 60 minutes) and stores the information (by default, up to 8 days).  You can use AWR views and reports to analyze this data.

## Best practices
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-best-practices"></a>
+ To calculate resource requirements for your target database, you can use a single AWR report, multiple AWR reports, or dynamic AWR views. We recommend that you use multiple AWR reports during the peak load period to estimate the resources required to handle those peak loads. In addition, dynamic views provide more data points that help you calculate resource requirements more precisely.
+ You should estimate IOPS only for the database that you plan to migrate, not for other databases and processes that use the disk.
+ To calculate how much I/O is being used by the  database, don’t use the information in the Load Profile section of the AWR report. Use the I/O Profile section instead, if it’s available, or skip to the Instance Activity Stats section and look at the total values for physical read and write operations.
+ When you estimate CPU utilization, we recommend that you use the database metrics method instead of operating system (OS) statistics, because it’s based on the CPU used only by databases. (OS statistics also include CPU usage by other processes.) You should also check CPU-related recommendations in the ADDM report to improve performance after migration.
+ Consider I/O throughput limits―Amazon Elastic Block Store (Amazon EBS) throughput and network throughput―for the specific instance size when you’re determining the right instance type.
+ Run the performance test before migration to validate the engine size.

## Epics
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-epics"></a>

### Create an AWR report
<a name="create-an-awr-report"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable the AWR report. | To enable the report, follow the instructions in the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/18/tgdba/gathering-database-statistics.html#GUID-26D359FA-F809-4444-907C-B5AFECD9AE29). | DBA |
| Check the retention period. | To check the retention period of the AWR report, use the following query.<pre>SQL> SELECT snap_interval,retention FROM dba_hist_wr_control;</pre> | DBA |
| Generate the snapshot. | If the AWR  snapshot interval isn’t granular enough to capture the spike of the peak workload, you can generate the AWR report manually. To generate the manual AWR snapshot, use the following query.<pre>SQL> EXEC dbms_workload_repository.create_snapshot;</pre> | DBA |
| Check recent snapshots. | To check recent AWR snapshots, use the following query.<pre>SQL> SELECT snap_id, to_char(begin_interval_time,'dd/MON/yy hh24:mi') Begin_Interval,<br /> to_char(end_interval_time,'dd/MON/yy hh24:mi') End_Interval<br /> FROM dba_hist_snapshot<br /> ORDER BY 1;</pre> | DBA |

### Estimate disk I/O requirements
<a name="estimate-disk-i-o-requirements"></a>

<table>
<thead>
  <tr><th>Task</th><th>Description</th><th>Skills required</th></tr>
</thead>
<tbody>
  <tr><td>Choose a method.</td><td>IOPS is the standard measure of input and output operations per second on a storage device, and includes both read and write operations. <br />If you are migrating an on-premises database to AWS, you need to determine the peak disk I/O used by the database. You can use the following methods to estimate disk I/O for your target database:<ul><li>Load Profile section of the AWR report</li><li>Instance Activity Stats section of the AWR report (use this section for Oracle Database 12c or later)</li><li>I/O Profile section of the AWR report (use this section for Oracle Database versions before 12c)</li><li>AWR views</li></ul><br />The following steps describe these four methods.</td><td>DBA</td></tr>
  <tr><td>Option 1: Use the load profile.</td><td>The following table shows an example of the Load Profile section of the AWR report.For more accurate information, we recommend that you use option 2 (I/O profiles) or option 3 (instance activity statistics) instead of the load profile.
<table>
<tbody>
</tbody>
</table>
<br />Based on this information, you can calculate IOPs and throughput as follows:<br /><i>   IOPS = Read I/O requests: + Write I/O requests = 3,586.8 + 574.7 = 4134.5 </i><br /><i>   Throughput = Physical read (blocks) + Physical write (blocks) = 13,575.1 + 3,467.3 = 17,042.4</i><br />Because the block size in Oracle is 8 KB, you can calculate total throughput as follows:<br /><i>   Total throughput in MB is 17042.4 * 8 * 1024 / 1024 / 1024 = 133.2 MB</i>Don’t use the load profile to estimate the instance size. It isn’t as precise as instance activity statistics or I/O profiles.</td><td>DBA</td></tr>
  <tr><td>Option 2: Use instance activity statistics.</td><td>If you’re using an Oracle Database version before 12c, you can use the Instance Activity Stats section of the AWR report to estimate IOPS and throughput. The following table shows an example of this section.
<table>
<tbody>
</tbody>
</table>
<br />Based on this information, you can calculate total IOPS and throughput as follows:<br /><i>   Total IOPS = 3,610.28 + 757.11 = 4367 </i><br /><i>   Total Mbps = 114,482,426.26 + 36,165,631.84 = 150648058.1 / 1024 / 1024 = 143 Mbps</i></td><td>DBA</td></tr>
  <tr><td>Option 3: Use I/O profiles.</td><td>In  Oracle Database 12c, the AWR report includes an I/O Profiles section that presents all the information in a single table and provides more accurate data about database performance. The following table shows an example of this section.
<table>
<tbody>
</tbody>
</table>
<br />This table provides the following values for throughput and total IOPS:<br /><i>   Throughput = 143 MBPS (from the fifth row, labeled Total, second column)</i><br /><i>   IOPS = 4,367.4 (from the first row, labeled Total Requests, second column)</i></td><td>DBA</td></tr>
  <tr><td>Option 4: Use AWR views.</td><td>You can see the same IOPS and throughput information by using AWR views. To get this information, use the following query: <pre>break on report<br /> compute sum of Value on report<br /> select METRIC_NAME,avg(AVERAGE) as "Value"<br /> from dba_hist_sysmetric_summary<br /> where METRIC_NAME in ('Physical Read Total IO Requests Per Sec','Physical Write Total IO Requests Per Sec')<br /> group by metric_name;</pre></td><td>DBA</td></tr>
</tbody>
</table>

### Estimate CPU requirements
<a name="estimate-cpu-requirements"></a>

<table>
<thead>
  <tr><th>Task</th><th>Description</th><th>Skills required</th></tr>
</thead>
<tbody>
  <tr><td>Choose a method.</td><td>You can estimate the CPU required for the target database in three ways:<ul><li>By using the actual available cores of the processor</li><li>By using the utilized cores based on OS statistics</li><li>By using the utilized cores based on database statistics</li></ul><br />If you’re looking at utilized cores, we recommend that you use the database metrics method instead of OS statistics, because it’s based on the CPU used only by the databases that you’re planning to migrate. (OS statistics also include CPU usage by other processes.) You should also check CPU-related recommendations in the ADDM report to improve performance after migration.<br />You can also estimate requirements based on CPU generation. If you are using different CPU generations, you can estimate the required CPU of the target database by following the instructions in the whitepaper <a href="https://d1.awsstatic.com/whitepapers/Demystifying_vCPUs.df200b766578b75009ad8d15c72e493d6408c68a.pdf">Demystifying the Number of vCPUs for Optimal Workload Performance</a>.</td><td>DBA</td></tr>
  <tr><td>Option 1: Estimate requirements based on available cores.</td><td>In AWR reports:<ul><li>CPUs refer to logical and virtual CPUs. </li><li>Cores are the number of processors  in a physical CPU chipset. </li><li>A socket is a physical device that connects a chip to a board. Multi-core processors have sockets with several CPU cores.</li></ul><br />You can estimate available cores in two ways:<ul><li>By using OS commands</li><li>By using  the AWR report</li></ul><br /><b>To estimate available cores by using OS commands</b><br />Use the following command to count the cores in the processor.<pre>$ cat /proc/cpuinfo |grep "cpu cores"|uniq<br />cpu cores    : 4<br />cat /proc/cpuinfo | egrep "core id|physical id" | tr -d "\n" | sed s/physical/\\nphysical/g | grep -v ^$ | sort | uniq | wc -l </pre><br />Use the following command to count the sockets in the processor.<pre>grep "physical id" /proc/cpuinfo | sort -u<br />  physical id     : 0<br />  physical id     : 1</pre>  We don’t recommend using OS commands such as <b>nmon</b> and <b>sar</b> to extract CPU utilization. This is because those calculations include CPU utilization by other processes and might not reflect the actual CPU that is used by the database.<br /><b>To estimate available cores by using the AWR report</b><br />You can also derive CPU utilization from the first section of the AWR report. Here’s an excerpt from the report.
<table>
<tbody>
</tbody>
</table>
<br />In this example, the CPUs count is 80, which indicates that these are logical (virtual) CPUs. You can also see that this configuration has two sockets, one physical processor on each socket (for a total of two physical processors), and 40 cores for each physical processor or socket. </td><td>DBA</td></tr>
  <tr><td>Option 2: Estimate CPU utilization by using OS statistics.</td><td>You can check the OS CPU usage statistics either directly in the OS (using <b>sar</b> or another host OS utility) or by reviewing the IDLE/(IDLE+BUSY) values from the Operating System Statistics section of the AWR report. You can see the seconds of CPU consumed directly from <b>v$osstat</b>. The AWR and Statspack reports also show this data in the Operating System Statistics section.<br />If there are multiple databases on the same box, they all have the same <b>v$osstat</b> values for BUSY_TIME.
<table>
<tbody>
</tbody>
</table>
<br />If there are no other major CPU consumers in the system, use the following formula to calculate the percentage of CPU utilization:<br /><i>   Utilization = Busy time / Total time</i><br /><i>   Busy time = requirements = v$osstat.BUSY_TIME</i><br /><i>   C = Total time (Busy + Idle)</i><br /><i>   C = capacity = v$ostat.BUSY_TIME + v$ostat.IDLE_TIME</i><br /><i>   Utilization = BUSY_TIME / (BUSY_TIME + IDLE_TIME)</i><br /><i>      = -1,305,569,937 / (1,305,569,937 + 4,312,718,839 )</i><br /><i>      = 23% utilized</i></td><td>DBA</td></tr>
  <tr><td>Option 3: Estimate CPU utilization by using database metrics.</td><td>If multiple databases are running in the system, you can use the database metrics that appears at the beginning of the report.
<table>
<tbody>
</tbody>
</table>
<br />To get CPU utilization metrics, use this formula:<br /><i>   Database CPU usage (% of CPU power available) = CPU time / NUM_CPUS / elapsed time</i><br />where CPU usage is described by <i>CPU time</i> and represents the time spent on CPU, not the time waiting for CPU. This calculation results in:<br /><i>   = 312,625.40 / 11,759.64/80 = 33% of CPU is being used</i><br /><i>   Number of cores (33%) * 80 = 26.4 cores</i><br /><i>   Total cores = 26.4 * (120%) = 31.68 cores</i><br />You can use the greater of these two values to calculate the CPU utilization of the Amazon RDS or Aurora DB instance.On IBM AIX, the calculated utilization doesn’t match the values from the operating system or the database. These values do match on other operating systems.</td><td>DBA</td></tr>
</tbody>
</table>

### Estimate memory requirements
<a name="estimate-memory-requirements"></a>

<table>
<thead>
  <tr><th>Task</th><th>Description</th><th>Skills required</th></tr>
</thead>
<tbody>
  <tr><td>Estimate memory requirements by using memory statistics.</td><td>You can use the AWR report to calculate the memory of the source database and match it in the target database. You should also check the performance of the existing database and reduce your memory requirements to save costs, or increase your requirements to improve performance. That requires a detailed analysis of the AWR response time and the service-level agreement (SLA) of the application. Use the sum of Oracle system global area (SGA) and program global area (PGA) usage as the estimated memory utilization for Oracle. Add an extra 20 percent for the OS to determine a target memory size requirement. For Oracle RAC, use the sum of the estimated memory utilization on all RAC nodes and reduce the total memory, because it’s stored on common blocks.<ol><li>Check for the metrics in the Instance Efficiency Percentage table. The table uses the following terms:<ul><li><i>Buffer Hit %</i> is the percentage of times a particular block was found in the buffer cache instead of performing a physical I/O. For better performance,  target 100 percent . </li><li><i>Buffer Nowait %</i> should be close to 100 percent.</li><li><i>Latch Hit %</i> should be close to 100 percent. </li><li><i>% Non-Parse CPU</i> is the percentage of CPU time spent in non-parsing activities. This value should be close to 100 percent..</li></ul><br /><b>Instance Efficiency Percentages (target 100%)</b>
<table>
<tbody>
</tbody>
</table>
<br />In this example, all the metrics look fine, so you can use the SGA and PGA for the existing database as the capacity planning requirement.</li><li>Check the memory statistics section and calculate the SGA/PGA.
<table>
<tbody>
</tbody>
</table>
</li></ol><br /><i>   Total instance memory in use = SGA + PGA = 220 GB + 45 GB  = 265 GB</i><br />Add 20 percent of buffer:<br /><i>   Total instance memory = 1.2 * 265 GB = 318 GB </i><br />Because SGA and PGA account for 70 percent of host memory, the total memory requirement is: <br /><i>   Total host memory = 318/0.7 = 464 GB</i>When you migrate to Amazon RDS for Oracle, the PGA and SGA are pre-calculated based on a predefined formula. Make sure that the pre-calculated values are close to your estimates.</td><td>DBA</td></tr>
</tbody>
</table>

### Determine the DB instance type of the target database
<a name="determine-the-db-instance-type-of-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the DB instance type based on disk I/O, CPU, and memory estimates. | Based on the estimates  in the previous steps, the capacity of the target Amazon RDS or Aurora database should be:+ 68 cores of CPU<br />+ 143 MBPS of throughput  <br />+ 4367 IOPS for disk I/O<br />+ 464 GB of memory<br />In the target Amazon RDS or Aurora database, you can map these values to the db.r5.16xlarge instance type, which has a capacity of 32 cores, 512 GB of RAM, and 13,600 Mbps of throughput. For more information, see the AWS blog post [Right-size Amazon RDS instances at scale based on Oracle performance metrics](https://aws.amazon.com/blogs/database/right-sizing-amazon-rds-instances-at-scale-based-on-oracle-performance-metrics/). | DBA |

## Related resources
<a name="estimate-the-amazon-rds-engine-size-for-an-oracle-database-by-using-awr-reports-resources"></a>
+ [Aurora DB instance class](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) (Amazon Aurora documentation)
+ [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) (Amazon RDS documentation)
+ [AWS Miner tool](https://github.com/tmuth/AWR-Miner/blob/master/release/5.0.8/AWR-Miner-capture-5.0.8/awr_miner.sql) (GitHub repository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

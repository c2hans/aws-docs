---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/delayed-durability.html
---

# Enable delayed durability
<a name="delayed-durability"></a>

Certain processes such as EnterpriseOne's Material Requirements Planning (MRP) encounter a bottleneck caused by the disk latency of committing transactions to the transaction log. Moving the transaction log (LDF) to `io2 `or `io2 `Block Express storage often improves the performance sufficiently to meet business requirements. If this is insufficient, you can configure delayed durability in the database.

**Important**
You should enable delayed durability only if performance isn't acceptable and you fully understand how your transactions will behave across databases during system failure scenarios.

When you enable delayed durability, transaction commits are cached by using a write-back (instead of a write-through) operation. In the event of a system failure, the consistency of the database is still guaranteed. However, any transactions that haven't been committed to disk are lost. Also, additional functionality related to replication, including the functionality used by AWS Database Migration Service (AWS DMS), becomes unavailable when delayed durability is in effect.

During MRP testing in a specific configuration, we observed the following:
+ Moving the LDF file to `io2 `Block Express dropped the runtime by 52 percent compared to a baseline with the LDF file on `gp3`.
+ Enabling delayed durability dropped the runtime by 79 percent compared to a baseline with the LDF file on `gp3`.

To enable delayed durability, run the following command on the database.

```
USE master
ALTER DATABASE JDE_Prist920 SET DELAYED_DURABILITY = FORCE
```

Delayed durability typically flushes the log several times per second, but there can be an increased lag if there is a disk I/O bottleneck. To ensure a low recovery point objective (RPO), you can place the `sys.sp_flush_log` command on a scheduler to run at a high frequency. This procedure forces a flush of the log to disk.

The following script creates a job on the SQL job scheduler to run every minute. Adjust the job name and database name in the script to reflect your requirements.

```
USE msdb;
GO

DECLARE  @myjob nvarchar(128);
DECLARE @mydb nvarchar(128);
DECLARE @mycommand nvarchar(max);
DECLARE @myschedule nvarchar(128);
DECLARE @jobId binary(16);
DECLARE @scheduleId binary(16);

SET @myjob = 'JDE_Prist920 Flush Log Cache';
SET @mydb = 'JDE_Prist920';
SET @mycommand  = 'sys.sp_flush_log';
SET @myschedule = 'EveryMinute';

SELECT @scheduleId = schedule_id FROM msdb.dbo.sysschedules WHERE (name = @myschedule)
IF (@scheduleId IS NULL)
BEGIN
	EXEC sp_add_schedule
	    @schedule_name = @myschedule,
	    @freq_type = 4,
	    @freq_interval = 1,
	    @freq_subday_type = 0x2,
	    @freq_subday_interval= 60
END

SELECT @jobId = job_id FROM msdb.dbo.sysjobs WHERE (name = @myjob)
IF (@jobId IS NULL)
BEGIN
    EXEC sp_add_job @job_name = @myjob

	EXEC sp_add_jobstep
	    @job_name = @myjob,
	    @step_name = N'process step',
	    @subsystem = N'TSQL',
		@command = @mycommand,
		@database_name = @mydb

	EXEC sp_attach_schedule
		@job_name = @myjob,
		@schedule_name = @myschedule;

	EXEC dbo.sp_add_jobserver
		@job_name = @myjob

END
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

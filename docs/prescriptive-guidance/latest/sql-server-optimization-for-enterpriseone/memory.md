---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/memory.html
---

# Adjust memory settings
<a name="memory"></a>

We recommend that you configure the default memory values for a SQL Server database that is running JD Edwards workloads. These include:
+ Configuring maximum and minimum memory settings
+ Locking pages in memory

## Configure maximum and minimum memory
<a name="max-min-memory"></a>

Setting the maximum memory of the SQL Server database ensures that the operating systems and other processes have enough memory to perform their actions without paging to disk. Setting maximum and minimum memory can prevent multiple SQL Server instances that are installed on the same EC2 instance from starving one another for memory.

You can use the following script to automatically configure maximum and minimum settings with conservative values. This script reserves 1 GB for the operating system, and 25 percent of the memory under 16 GB and 12.5 percent of the remaining memory as overhead. SQL Server minimum memory is set to half of maximum memory. The script assumes that you have a single SQL Server database installed on the EC2 instance.

```
DECLARE @OSMemoryTotalKB bigint;
DECLARE @OSMemoryUnder16GB bigint;
DECLARE @OSMemoryOver16GB bigint;
DECLARE @OSOverhead bigint;
DECLARE @MemoryOverheadLower bigint;
DECLARE @MemoryOverheadUpper bigint;
DECLARE @MemoryOverheadTotal bigint;
DECLARE @SQLMaxMemory int;
DECLARE @SQLMinMemory int;

-- Find how much memory is available on the OS
SELECT @OSMemoryTotalKB = total_physical_memory_kb from sys.dm_os_sys_memory;
SET @OSMemoryUnder16GB = IIF(@OSMemoryTotalKB>16777216, 16777216, @OSMemoryTotalKB);
SET @OSMemoryOver16GB = IIF(@OSMemoryTotalKB>16777216, @OSMemoryTotalKB-16777216, 0);

-- Calculate overhead for the OS
SET @OSOverhead= 1048576; -- static 1GB reservation

-- Calculate overhead for managing memory
SET @MemoryOverheadLower = @OSMemoryUnder16GB/4; --reserve 25% of memory under 16GB for overhead
SET @MemoryOverheadUpper = @OSMemoryOver16GB/8; -- reserve 12.5% of memory over 16GB for overhead
SET @MemoryOverheadTotal = @OSOverhead + @MemoryOverheadLower + @MemoryOverheadUpper;

-- Calculate remaining memory available for SQL
SET @SQLMaxMemory = (@OSMemoryTotalKB-@MemoryOverheadTotal)/1024;
SET @SQLMinMemory = @SQLMaxMemory/2; -- set minimum to half of maximum

Print N'Total Server memory (KB): ' + CAST(@OSMemoryTotalKB as NVARCHAR);
Print N'Memory Overhead for OS Overhead (KB): ' + CAST(@OSOverhead as NVARCHAR);
Print N'Memory Overhead for management of lower 16GB (KB): ' + CAST(@MemoryOverheadLower as NVARCHAR);
Print N'Memory Overhead for management of over 16GB (KB): ' + CAST(@MemoryOverheadUpper as NVARCHAR);
Print N'Memory Overhead Total: ' + CAST(@MemoryOverheadTotal as NVARCHAR);
Print N'SQL Minimum Memory (MB): ' + CAST(@SQLMinMemory as NVARCHAR);
Print N'SQL Maximum Memory (MB): ' + CAST(@SQLMaxMemory as NVARCHAR);

EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'min server memory', @SQLMinMemory
RECONFIGURE;
EXEC sp_configure 'max server memory', @SQLMaxMemory;
RECONFIGURE;
```

## Lock pages in memory
<a name="lock-pages"></a>

To ensure stability of the memory used for an EnterpriseOne SQL Server database, we recommend that you lock pages in memory. Follow the steps in the [Best practices for deploying SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/lock-pages.html) guide to complete this configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

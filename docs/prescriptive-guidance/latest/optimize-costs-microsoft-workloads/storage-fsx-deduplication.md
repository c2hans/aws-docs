---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-deduplication.html
---

# Enable data deduplication in Amazon FSx
<a name="storage-fsx-deduplication"></a>

## Overview
<a name="storage-fsx-deduplication-overview"></a>

Data deduplication is a feature that enables you to store your data more efficiently and with lower capacity requirements. It involves finding and removing duplication within data without compromising its fidelity or integrity. Data deduplication uses subfile variable-size chunking and compression, which deliver optimization ratios of 2:1 for general file servers and up to 20:1 for virtualization data. Data deduplication can be more effective than New Technology File System (NTFS) compression. The deduplication architecture provides resiliency during hardware failures through full checksum validation on data and metadata, including redundancy for metadata and the most frequently accessed data chunks.

Amazon FSx for Windows File Server supports data deduplication. Using it can lead to average savings of 50–60% for general-purpose file shares. Within shares, savings range from 30–50% for user documents and up to 70–80% for software development datasets. The storage savings that you can achieve with data deduplication depend on the nature of your dataset, including how much duplication exists across files. Deduplication is less effective if your data changes frequently.

## Cost impact
<a name="storage-fsx-deduplication-cost"></a>

To cope with data storage growth in the enterprise, administrators consolidate servers and make capacity scaling and data optimization key goals. Data deduplication's default settings can provide savings immediately, or administrators can fine-tune the settings to see additional gains. For example, you can configure deduplication to run only on certain file types, or you can create a custom job schedule.

At a high level, deduplication has three types of jobs: optimization, garbage collection, and scrubbing. Deduplication doesn't free space until you run a garbage collection job after optimization. You can schedule the job or run it manually. All settings available when you schedule a data deduplication job are also available when you start a job manually, except for those that are scheduling-specific.

Even with only a 25 percent effective savings from deduplication, you can achieve significant cost savings for Amazon FSx for Windows File Server. These projected savings are based on an [estimate](https://calculator.aws/#/estimate?id=b25b166595553e055c594e89e3c13610df570bc9) in the AWS Pricing Calculator.

## Cost optimization recommendations
<a name="storage-fsx-deduplication-rec"></a>

Deduplication on FSx for Windows File Server file systems is not enabled by default. To enable deduplication by using [remote management on PowerShell](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/administering-file-systems.html#remote-pwrshell), you must run the `Enable-FSxDedup` command and then use the `Set-FSxDedupConfiguration` command to set the configuration. For more information, see [Administering file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/administering-file-systems.html) in the FSx for Windows File Server documentation.

To enable deduplication, run the following command:

```
PS C:\Users\Admin> Invoke-Command -ComputerName amznfsxzzzzzzzz.corp.example.com -ConfigurationName FSxRemoteAdmin -ScriptBlock {Enable-FsxDedup }
```

To set a custom deduplication optimization schedule, run the following command:

```
Invoke-Command -ComputerName amznfsxzzzzzzzz.corp.example.com -ConfigurationName FSxRemoteAdmin -ScriptBlock {
Set-FSxDedupSchedule -Name "CustomOptimization" -Type Optimization -Days Mon,Tues,Wed,Sat -Start 09:00 -DurationHours 7
}
```

By running the PowerShell `Measure-DedupFileMetadata` cmdlet, you can determine how much potential disk space can be reclaimed on a volume if you delete a group of folders, a single folder, or a single file, and then run a garbage collection job. Specifically, the `DedupDistinctSize` value tells you how much space you get back if you delete those files. Files often have chunks that are shared across other folders, so the deduplication engine calculates which chunks are unique and would be deleted after the garbage collection job.

The default [data deduplication job schedules](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) are designed to work well for recommended workloads and to minimize intrusion (excluding the priority optimization job that's enabled for the backup usage type). If your workloads have large resource requirements, we recommend that you schedule jobs to run only during idle hours, or that you reduce or increase the amount of system resources that a data deduplication job can consume.

By default, data deduplication uses 25 percent of the available memory. You can increase this value by using the `-memory` switch. For optimization jobs, we recommend that you set the memory to a value from 15 to 50 percent. For jobs that you schedule to run during off hours, such as garbage collection and scrubbing jobs, you can set higher memory consumption (such as 50 percent).

For more information about data deduplication settings, see [Reducing storage costs with Data Deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) in the FSx for Windows File Server documentation.

## Additional resources
<a name="storage-fsx-deduplication-resources"></a>
+ [Understanding Data Deduplication](https://learn.microsoft.com/en-gb/windows-server/storage/data-deduplication/understand) (Microsoft documentation)
+ [Reducing storage costs with Data Deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) (FSx for Windows File Server documentation)

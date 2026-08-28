---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-deduplication.html
---

# Enable data deduplication in Amazon FSx
<a name="storage-fsx-deduplication"></a>

## Overview
<a name="storage-fsx-deduplication-overview"></a>

Data deduplication is a feature that enables you store your data more efficiently and with less capacity requirements. It involves finding and removing duplication within data without compromising its fidelity or integrity. Data deduplication uses subfile variable-size chunking and compression, which deliver optimization ratios of 2:1 for general file servers and up to 20:1 for virtualization data. Data deduplication is much more effective than NTFS compression. Inherent in the deduplication architecture is resiliency during hardware failures—with full checksum validation on data and metadata, including redundancy for metadata and the most accessed data chunks.

FSx for Windows File Server fully supports data deduplication. Using it can lead to an average savings of 50–60% for general-purpose file shares. Within shares, savings range from 30–50% for user documents and up to 70–80% for software development datasets. It's important to understand that the storage savings that you can achieve with data deduplication depend on the nature of your dataset, including how much duplication exists across files. Deduplication is not a good option if the data stored is dynamic in nature.

## Cost impact
<a name="storage-fsx-deduplication-cost"></a>

To cope with data storage growth in the enterprise, administrators consolidate servers and make capacity scaling and data optimization key goals. Data deduplication's default settings can provide savings immediately, or administrators can fine-tune the settings to see additional gains. For example, you can configure deduplication to run only on certain file types, or you can create a custom job schedule.

At a high level, deduplication has three types of jobs: optimization, garbage collection, and scrubbing. Be aware that space won't be freed until you run a garbage collection job after optimization. You can schedule the job or you can manually run it. All settings available when you schedule a data deduplication job are also available when you start a job manually (except for those which are scheduling-specific).

Even with only a 25-percent effective savings from deduplication, there's a significant cost savings for FSx for Windows File Server. These projected savings are based on an [estimate](https://calculator.aws/#/estimate?id=b25b166595553e055c594e89e3c13610df570bc9) in the AWS Pricing Calculator.

## Cost optimization recommendations
<a name="storage-fsx-deduplication-rec"></a>

Deduplication on FSx for Windows File Server file systems is not enabled by default. To enable deduplication by using [remote management on PowerShell](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/administering-file-systems.html#remote-pwrshell), you must run the `Enable-FSxDedup` command and then use the `Set-FSxDedupConfiguration` command to set the configuration. For more information, see [Administering file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/administering-file-systems.html) in the FSx for Windows File Server documentation.

To enable deduplication, run the following command:

```
PS C:\Users\Admin> Invoke-Command -ComputerName amznfsxzzzzzzzz.corp.example.com -ConfigurationName FSxRemoteAdmin -ScriptBlock {Enable-FsxDedup }
```

To verify your deduplication configuration, run the following command:

```
Invoke-Command -ComputerName amznfsxzzzzzzzz.corp.example.com -ConfigurationName FSxRemoteAdmin -ScriptBlock {
Set-FSxDedupSchedule -Name "CustomOptimization" -Type Optimization -Days Mon,Tues,Wed,Sat -Start 09:00 -DurationHours 7
}
```

By running the PowerShell `Measure-DedupFileMetadata` cmdlet, you can determine how much potential disk space can be reclaimed on a volume if you delete a group of folders, a single folder, or a single file, and then run a garbage collection job. Specifically, the `DedupDistinctSize` value tells you how much space you get back if you delete those files. Files often have chunks that are shared across other folders, so the deduplication engine calculates which chunks are unique and would be deleted after the garbage collection job.

The default [data deduplication job schedules](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) are designed to work well for recommended workloads and be as non-intrusive as possible (excluding the priority optimization job that's enabled for the backup usage type). If workloads have large resource requirements, we recommend that you schedule jobs run only during idle hours, or to reduce or increase the amount of system resources that a data deduplication job is allowed to consume.

By default, data deduplication uses 25 percent of the memory available. However, this can be increased by using `-memory switch`. For optimization jobs, we recommend that you set a range from 15 to 50. For scheduled jobs, you can use higher memory consumption. For example, with garbage collection and scrubbing jobs (which you typically schedule to run in off hours), you can set higher memory consumption (such as 50).

For additional information regarding data deduplication settings, see [Reducing storage costs with Data Deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) in the FSx for Windows File Server documentation.

## Additional resources
<a name="storage-fsx-deduplication-resources"></a>
+ [Understanding Data Deduplication](https://learn.microsoft.com/en-gb/windows-server/storage/data-deduplication/understand) (Microsoft documentation)
+ [Reducing storage costs with Data Deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) (FSx for Windows File Server documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

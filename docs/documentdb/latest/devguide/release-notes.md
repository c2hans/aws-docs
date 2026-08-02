---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html
---

# Release notes
<a name="release-notes"></a>

These release notes describe the Amazon DocumentDB features, improvements, and bug fixes organized by major engine version. Within each version section, entries are listed by date in a table format.

For details about how engine versions and patch versions are numbered (including the mapping between engine patch version prefixes and Amazon DocumentDB engine versions), see [Engine version numbering](db-instance-maintain.md#engine-version-numbering).

You can determine the current Amazon DocumentDB engine patch version by running the following command:

```
db.runCommand({getEngineVersion: 1})
```

If your cluster is not on the latest version of the engine, it is likely that you have pending maintenance available that will upgrade your engine. For more information, see [Maintaining Amazon DocumentDB](db-instance-maintain.md) in the Developer Guide.

**Topics**
+ [Amazon DocumentDB engine version release notes](#release-notes-engine-versions)
+ [General Amazon DocumentDB release notes](#release-notes-general)
+ [Amazon DocumentDB elastic clusters release notes](#release-notes-elastic)

## Amazon DocumentDB engine version release notes
<a name="release-notes-engine-versions"></a>

Release notes for Amazon DocumentDB engine versions organized by major version.

------
#### [ Amazon DocumentDB 8.0 ]

Release notes for Amazon DocumentDB engine version 8.0 (MongoDB 8.0 compatibility).

| Date | Release notes |
| --- | --- |
| July 22, 2026 | **New feature**<br />Amazon DocumentDB clusters running Engine Version 8.0 and later now support a maximum storage limit of 256 TiB, doubling the previous limit of 128 TiB. For more information, see [Amazon DocumentDB quotas](limits.md). |
| July 13, 2026 | **Amazon DocumentDB 8.0.1 (Engine Version: 4.0.8864)**<br />**New features and improvements**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| May 13, 2026 | **New feature**<br />Amazon DocumentDB serverless is now available for Amazon DocumentDB 8.0. For more information, see [Using Amazon DocumentDB serverless](docdb-serverless.md). |
| May 6, 2026 | **Bug fixes and other changes**<br />**Amazon DocumentDB 8.0 (Engine Version: 4.0.6940)**<br />This update provides an optional engine patch with the following improvements:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| April 20, 2026 | **New feature**<br />In-place major version upgrade (MVU) from Amazon DocumentDB 5.0 to Amazon DocumentDB 8.0 is now available. For more information, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md). |
| April 20, 2026 | **New features and improvements**<br />**Amazon DocumentDB 8.0 (Engine Versions: 4.0.5995, 4.0.6473)**<br />This is a required engine patch that includes the following new features, improvements, and fixes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />All Amazon DocumentDB 8.0 clusters will be automatically upgraded to this patch version during their next maintenance window. |
| March 26, 2026 | **New features**<br />Amazon DocumentDB now supports the latest generation of memory-optimized instances, db.r8g, powered by Arm-based AWS Graviton4 processors, providing up to 30% better performance over R6G instances. For more information, see [Managing instance classes](db-instance-classes.md) in this guide  |
| November 11, 2025 | **New features**<br />Amazon DocumentDB now offers full wire protocol compatibility with MongoDB 8.0. Amazon DocumentDB 8.0 improves query performance enabling you to build high-performance applications at a lower cost. <br />**Amazon DocumentDB 8.0 (Engine Patch Version 4.0.4448)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |

------
#### [ Amazon DocumentDB 5.0 ]

Release notes for Amazon DocumentDB engine version 5.0 (MongoDB 5.0 compatibility).

| Date | Minor version | Release notes |
| --- | --- | --- |
| Instance type | Original limit | New limit |
| --- | --- | --- |
| June 8, 2026 | 5.0.1 | **New minor version**<br />**Amazon DocumentDB 5.0.1 (Engine Version 3.0.21138)**<br />Amazon DocumentDB 5.0.1 is the first minor version release for the Amazon DocumentDB 5.0 major version. Minor versions include improvements such as new features, security fixes, and bug fixes. You can upgrade to 5.0.1 from 5.0.0 using a minor version upgrade. For more information, see [Amazon DocumentDB minor version upgrade](docdb-minor-version-upgrade.md).<br />This minor version includes the following new features and improvements:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| May 6, 2026 | 5.0.0 | **Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Version: 3.0.20421)**<br />This release is for a required security patch. |
| April 20, 2026 | 5.0.0 | **New feature**<br />In-place major version upgrade (MVU) from Amazon DocumentDB 5.0 to Amazon DocumentDB 8.0 is now available. For more information, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md). |
| April 13, 2026 | 5.0.0 | **Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Versions: 3.0.19917)**<br />This is a required engine patch that includes the following new features, improvements, and fixes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />All Amazon DocumentDB 5.0 clusters will be automatically upgraded to this patch version during their next maintenance window. |
| October 22, 2025 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.17983)**<br />Amazon DocumentDB now supports the latest generation of memory-optimized instances, db.r8g, powered by Arm-based AWS Graviton4 processors, providing up to 30% better performance over R6G instances. For more information, see [Managing instance classes](db-instance-classes.md) in this guide and this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-graviton4-based-r8g-database-instances/).<br />**New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| October 16, 2025 | 5.0.0 | **New feature**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**<br />Amazon DocumentDB now supports dual-stack mode (IPv4/IPv6) when your cluster is in a virtual private cloud (VPC).<br />For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-ipv6-support) and [Amazon VPC and Amazon DocumentDB](vpc-docdb.md) in the *Amazon DocumentDB Developer Guide*. |
| September 15, 2025 | 5.0.0 | **Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.17983)**<br />Fixed engine crash when queries contain subsequent `$replaceRoot` and `$lookup` stage. |
| July 29, 2025 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**<br />Fixed an issue during index creation that affected large collections. |
| July 28, 2025 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.14228)**<br />Amazon DocumentDB instance-based clusters now support Amazon DocumentDB Serverless, an on-demand, auto-scaling configuration.<br />For more information, see [Using Amazon DocumentDB serverless](docdb-serverless.md) and this [what's new blog post](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-documentdb-serverless/). |
| March 24, 2025 | 5.0.0 | **New feature**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11800)**<br />Added support for `postBatchResumeToken` in change streams.<br />For more information, see [Resuming a change stream with `postBatchResumeToken`](change_streams.md#change_streams-postBatchResumeToken). |
| January 15, 2025 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11800)**<br />Amazon DocumentDB now maintains read availability through writer instance restarts. Reader instances will now continue to serve read requests during writer instance restarts.<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11800)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| December 18, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.5721)**<br />Amazon DocumentDB instance-based clusters now support NVMe-backed R6GD instances.<br />For more information, see [NVMe-backed instances](db-instance-nvme.md) and this [what's new blog post](https://aws.amazon.com/about-aws/whats-new/2024/12/nvme-backed-r6gd-instances-amazon-documentdb-mongodb-compatibility/). |
| November 6, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11051)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| September 17, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.10696)**<br />Amazon DocumentDB now supports rebuilding indexes with `reIndex` in the `runCommand`. For more information, see [Index maintenance using `reIndex`](managing-indexes.md#reIndex). `reIndex` is only supported on Amazon DocumentDB 5.0 (Engine Patch Version 3.0.10696 and higher). <br />**Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.10696)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| August 22, 2024 | 5.0.0 | **New feature**<br />**Amazon DocumentDB 5.0 (All engine patch versions)**<br />Amazon DocumentDB global clusters now support cluster switchovers and managed cluster failovers. For more information, see [Performing a switchover for an Amazon DocumentDB global cluster](global-clusters-disaster-recovery.md#global-cluster-switchover) and [Performing a managed failover for an Amazon DocumentDB global cluster](global-clusters-disaster-recovery.md#managed-failover). Global cluster switchovers and failovers are supported on Amazon DocumentDB 4.0 and 5.0 only.  |
| July 23, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.8126)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.8126)**<br />Enhanced the logic to synchronize `CurrentTime` and `ResumeToken` for the change stream on readers. |
| July 22, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.6742)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| July 9, 2024 | 5.0.0 | **New feature**<br />For Amazon DocumentDB 5.0 (minimum engine patch version 3.0.4780), TLS CA certificate updates no longer require a system reboot. For more information, see [Updating your Amazon DocumentDB TLS certificates](ca_cert_rotation.md). |
| May 29, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.6742)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| April 3, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.5721)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 10, 2024 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Versions 3.0.4574, 3.0.4780, 3.0.4960)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| November 29, 2023 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3727)**<br />Added support for vector search. For more information, see this [blog post](https://aws.amazon.com/blogs/aws/vector-search-for-amazon-documentdb-with-mongodb-compatibility-is-now-generally-available/) and visit [Vector search for Amazon DocumentDB](vector-search.md) in the *Amazon DocumentDB Developer Guide*. |
| November 21, 2023 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3727)**<br />Added support for I/O-optimized storage. For more information, see [Amazon DocumentDB cluster storage configurations](db-cluster-storage-configs.md) in the *Amazon DocumentDB Developer Guide*.<br />Added integration for no-code machine learning with SageMaker Canvas. For more information, see [No-code machine learning with Amazon SageMaker AI Canvas](no-code-machine-learning.md) in the *Amazon DocumentDB Developer Guide*. |
| November 6, 2023 | 5.0.0 | **Amazon DocumentDB 5.0 (Engine Patch Versions 3.0.3727)**<br />**New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />Fixed issue where a change stream update from `-NaN` to `NaN` was not being displayed. |
| September 15, 2023 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3140)**<br />Added support for $jsonSchema schema validator in instance-based clusters only. For more information see [Using JSON schema validation](json-schema-validation.md). |
| July 13, 2023 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.1948)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.1948)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| June 7, 2023 | 5.0.0 | **Bug fixes and other changes**<br />**Amazon DocumentDB 5.0**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| May 10, 2023 | 5.0.0 | **Bug fixes and other changes**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.1361)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| March 1, 2023 | 5.0.0 | **New features**<br />**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.775)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| t3.medium | 500 | 1000 |
| t4g.medium | 500 | 1000 |
| r5.large | 1700 | 3400 |
| r5.xlarge | 3500 | 7000 |
| r5.2xlarge | 7100 | 14200 |
| r5.4xlarge | 14200 | 28400 |
| r5.8xlarge | 28400 | 60000 |
| r5.12xlarge | 30000 | 60000 |
| r5.16xlarge | 30000 | 60000 |
| r5.24xlarge | 30000 | 60000 |
| r6g.large | 1700 | 3400 |
| r6g.xlarge | 3500 | 7000 |
| r6g.2xlarge | 7100 | 14200 |
| r6g.4xlarge | 14200 | 28400 |
| r6g.8xlarge | 28400 | 60000 |
| r6g.12xlarge | 30000 | 60000 |
| r6g.16xlarge | 30000 | 60000 |

------
#### [ Amazon DocumentDB 4.0 ]

Release notes for Amazon DocumentDB engine version 4.0 (MongoDB 4.0 compatibility).

| Date | Release notes |
| --- | --- |
| Instance type | Original limit | New limit |
| --- | --- | --- |
| April 27, 2026 | **Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Version: 2.0.14278)**<br />This is a required engine patch that addresses the following issues:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />All Amazon DocumentDB 4.0 clusters will be automatically upgraded to this patch version during their next maintenance window. |
| March 9, 2026 | **Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Version: 2.0.14165)**<br />This update provides an optional engine patch with the following improvements:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| October 22, 2025 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**<br />Added new fields in `collstats` for "MVCCIDStats" and "gcRuntimeStats" that provide information into the overall health of the collection with respect to garbage collection and aging collections. |
| October 16, 2025 | **New feature**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**<br />Amazon DocumentDB now supports dual-stack mode (IPv4/IPv6) when your cluster is in a virtual private cloud (VPC).<br />For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-ipv6-support) and [Amazon VPC and Amazon DocumentDB](vpc-docdb.md) in the *Amazon DocumentDB Developer Guide*. |
| July 29, 2025 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**<br />Fixed an issue during index creation that affected large collections. |
| January 15, 2025 | **Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11096)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| November 6, 2024 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10980)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| September 17, 2024 | **Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10898)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| August 22, 2024 | **New feature**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.5704)**<br />Amazon DocumentDB global clusters now support cluster switchovers and managed cluster failovers. For more information, see [Performing a switchover for an Amazon DocumentDB global cluster](global-clusters-disaster-recovery.md#global-cluster-switchover) and [Performing a managed failover for an Amazon DocumentDB global cluster](global-clusters-disaster-recovery.md#managed-failover). Global cluster switchovers and failovers are supported on Amazon DocumentDB 4.0 and 5.0 only.  |
| July 23, 2024 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10709)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| July 22, 2024 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10593)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| July 9, 2024 | **New feature**<br />For Amazon DocumentDB 4.0 (minimum engine patch version 2.0.10179), TLS CA certificate updates no longer require a system reboot. For more information, see [Updating your Amazon DocumentDB TLS certificates](ca_cert_rotation.md). |
| May 29, 2024 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10593)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| April 3, 2024 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10392)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 10, 2024 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Versions 2.0.10124, 2.0.10179, 2.0.10221)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| December 20, 2023 | **Other changes**<br />Enabled support for in-place major version upgrade in Amazon DocumentDB 4.0. For more information, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md). |
| November 6, 2023 | **Amazon DocumentDB 4.0 (Engine Patch Versions 2.0.9876)**<br />**New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />Fixed issue where a change stream update from `-NaN` to `NaN` was not being displayed. |
| September 20, 2023 | **New features**<br />Added support for in-place major version upgrades in Amazon DocumentDB 4.0. For more information see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md). |
| September 15, 2023 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.9686)**<br />Added support for $jsonSchema schema validator in instance-based clusters only. For more information see [Using JSON schema validation](json-schema-validation.md). |
| July 13, 2023 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.9259)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.9259)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| April 4, 2023 | **Bug fixes and other changes**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.8934)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| February 27, 2023 | **Bug fixes and other changes**<br />**Amazon DocumentDB 4.0**<br />Added support for AWS Lambda. For more information, see [Using AWS Lambda with Change Streams](https://docs.aws.amazon.com/documentdb/latest/devguide/using-lambda.html). |
| August 9, 2022 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| July 25, 2022 | **New features**<br />**Amazon DocumentDB 4.0**<br />You can now create clusters faster with the ability to create clones that use the same DocumentDB cluster volume and have the same data as the original cluster. For details, see [Managing Amazon DocumentDB Clusters](https://docs.aws.amazon.com/documentdb/latest/devguide/db-clusters.html). |
| June 27, 2022 | **New features**<br />**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.7509)**<br />Amazon DocumentDB dynamically resizes your database based on usage patterns. Adding more data increases the space up to 64 Tebibytes (TiB) and deleting data decreases allotted space. |
| April 7, 2022 | **New features**<br />**4.0 (Engine Patch Versions 2.0.6142 and 2.0.6948)**<br />Amazon DocumentDB Performance Insights is now in preview. You can now store seven days of performance history in a rolling window at no additional cost. For more information, see [Monitoring with Performance Insights](https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html). |
| January 24, 2022 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 21, 2022 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| October 25, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| June 24, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| May 4, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 15, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| November 9, 2020 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| t3.medium | 500 | 1000 |
| t4g.medium | 500 | 1000 |
| r5.large | 1700 | 3400 |
| r5.xlarge | 3500 | 7000 |
| r5.2xlarge | 7100 | 14200 |
| r5.4xlarge | 14200 | 28400 |
| r5.8xlarge | 28400 | 60000 |
| r5.12xlarge | 30000 | 60000 |
| r5.16xlarge | 30000 | 60000 |
| r5.24xlarge | 30000 | 60000 |
| r6g.large | 1700 | 3400 |
| r6g.xlarge | 3500 | 7000 |
| r6g.2xlarge | 7100 | 14200 |
| r6g.4xlarge | 14200 | 28400 |
| r6g.8xlarge | 28400 | 60000 |
| r6g.12xlarge | 30000 | 60000 |
| r6g.16xlarge | 30000 | 60000 |

------
#### [ Amazon DocumentDB 3.6 ]

Release notes for Amazon DocumentDB engine version 3.6 (MongoDB 3.6 compatibility).

| Date | Release notes |
| --- | --- |
| April 27, 2026 | **New features**<br />**Amazon DocumentDB 3.6 (Engine Version: 1.0.208692) [in progress]**<br />This update provides an optional engine patch with the following improvements:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| February 12, 2026 | **Bug fixes and other changes**<br />**Amazon DocumentDB 3.6 (Engine Version: 1.0.208675)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| August 20, 2024 | **New feature**<br />For Amazon DocumentDB 3.6 (minimum engine patch version 1.0.208662), TLS CA certificate updates no longer require a system reboot. For more information, see [Updating your Amazon DocumentDB TLS certificates](ca_cert_rotation.md). |
| July 22, 2024 | **New features**<br />**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208662)**<br />Removed index limitations on db.r5.\* and db.r6.\* instances in Amazon DocumentDB MVU. For more information, see [Prerequisites](docdb-mvu.md#mvu-prerequisites).<br />**Bug fixes and other changes**<br />**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208662)**<br />Amazon DocumentDB now recognizes -NaN as a valid JSON token. |
| December 20, 2023 | **Other changes**<br />Enabled support for in-place major version upgrade in Amazon DocumentDB 3.6. For more information, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md). |
| November 17, 2023 | **Bug fixes and other changes**<br />**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208570)**<br />User defined local variable names now support “\_” (underscore) for projection operators such as `$let` and `$filter`. |
| September 20, 2023 | **New features**<br />Added support for in-place major version upgrades in Amazon DocumentDB 3.6. For more information see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md). |
| February 2, 2023 | **Bug fixes and other changes**<br />**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208432)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| August 9, 2022 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| April 7, 2022 | **New features**<br />**Amazon DocumentDB 3.6 (Engine Patch Versions 1.0.207836 and 1.0.208015)**<br />Amazon DocumentDB Performance Insights is now in preview. You can now store seven days of performance history in a rolling window at no additional cost. For more information, see [Monitoring with Performance Insights](https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html). |
| January 24, 2022 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 21, 2022 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| October 25, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| June 24, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| May 4, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 15, 2021 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| November 9, 2020 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| October 30, 2020 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| September 22, 2020 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| July 10, 2020 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| June 30, 2020 | **New features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |

------

## General Amazon DocumentDB release notes
<a name="release-notes-general"></a>

General service updates including Region availability, tooling integrations, and cross-version features.

| Date | Release notes |
| --- | --- |
| April 29, 2026 | **New feature**<br />Amazon DocumentDB is now available in the Canada West (Calgary) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-documentdb-available-in-canada-west-region/). |
| April 17, 2026 | **New feature**<br />Faster scaling on DocumentDB serverless is now available. |
| February 11, 2026 | **New feature**<br />Amazon DocumentDB is now available in the Asia Pacific (Melbourne) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-documentdb-mongodb-compatibility-asia-pacific-melbourne-region).<br />Amazon DocumentDB is now available in the Europe (Zurich) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-documentdb-mongodb-compatibility-europe-zurich-region). |
| January 08, 2026 | **New feature**<br />Amazon DocumentDB is now available in the Asia Pacific (Jakarta) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-documentdb-mongodb-compatibility-asia-pacific-jakarta-region). |
| October 13, 2025 | **New feature**<br />Amazon DocumentDB now supports R6G and T4G instances in the Asia Pacific (Hyderabad) Region.<br />For more information, see [Supported instance classes by Region](db-instance-classes.md#db-instance-classes-by-region). |
| October 7, 2025 | **New feature**<br />Amazon DocumentDB is now available in the following Regions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-mongodb-compatibility-new-regions-asia-pacific-mexico/). |
| September 26, 2025 | **New features**<br />Amazon DocumentDB now supports cross-Region and cross-account snapshot copy and snapshot sharing.<br />For more information, see [Copying snapshots across AWS Regions](backup_restore-copy_cluster_snapshot.md#backup_restore-copy_snapshot_across_regions) and [Sharing Amazon DocumentDB cluster snapshots](backup_restore-share_cluster_snapshots.md). |
| June 18, 2025 | **New feature**<br />Amazon DocumentDB is now available in the Israel (Tel Aviv) Region. |
| May 8, 2025 | **New feature**<br />Amazon DocumentDB is now available in the Europe (Stockholm) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-document-db-mongofb-compatibility-aws-europe-stockholm-region/). |
| April 2, 2025 | **Bug fixes and other changes**<br />Fixed a bug in vector index creation with background indexes. |
| February 6, 2025 | **New feature**<br />Amazon DocumentDB is now integrated with AWS Toolkit for Visual Studio Code. For more information, see this [What's New blog post](https://aws.amazon.com/about-aws/whats-new/2025/02/aws-toolkit-visual-studio-code-documentdb-mongodb/), and see [Working with Amazon DocumentDB in the Toolkit](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/docdb.html) in the *AWS Toolkit for Visual Studio Code User Guide*. |
| October 22, 2024 | **New feature**<br />Amazon DocumentDB now supports storage network throughput metrics `StorageNetworkReceiveThroughput`, `StorageNetworkTransmitThroughput`, and `StorageNetworkThroughput`. For more information, see [Evaluating Amazon DocumentDB instance usage with CloudWatch metrics](best_practices.md#best-practice-evaluating-instance-usage). |
| September 18, 2024 | **New feature**<br />Amazon DocumentDB is now available in the Africa (Cape Town) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-documentdb-mongodb-compatibility-cape-town-region/).<br />Amazon DocumentDB is now available in the Europe (Spain) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-documentdb-mongodb-compatibility-spain-region/). |
| June 25, 2024 | **New feature**<br />Authentication with AWS IAM ARNs is available in Amazon DocumentDB instance-based 5.0 clusters across all supported Regions. For more information, see [Authentication using IAM identity](iam-identity-auth.md). |
| April 3, 2024 | **New feature**<br />Amazon DocumentDB is now available in the Middle East (UAE) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-documentdb-middle-east-uae-region/).<br />**Bug fixes and other changes**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 30, 2024 | **New features**<br />**Amazon DocumentDB global clusters**<br />Global clusters are now available in both AWS GovCloud (US) regions: AWS GovCloud (US-East) and AWS GovCloud (US-West). |
| December 13, 2023 | **New features**<br />Added support for 1-click EC2 connectivity. For more information, see [Connect using Amazon EC2](connect-ec2.md). |
| November 17, 2023 | **New features**<br />Amazon DocumentDB is now available in the AWS GovCloud (US-East) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-documentdb-mongodb-compatibility-aws-govcloud-us-east-region/). |
| September 25, 2023 | **New features**<br />Amazon DocumentDB is now available in the Asia Pacific (Hong Kong) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-mongodb-hong-kong/). |
| September 11, 2023 | **New features**<br />Amazon DocumentDB is now available in the Asia Pacific (Hyderabad) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-asia-pacific-hyderabad-region/). |
| April 29, 2022 | **New features**<br />Amazon DocumentDB is now available in the China (Beijing) Region. For more information, see this [blog post](https://www.amazonaws.cn/en/new/2022/amazon-documentdb-mongodb-beijing/). |
| March 16, 2022 | **New features**<br />Amazon DocumentDB is now available in the Europe (Milan) Region. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2022/03/amazon-documentdb-mongodb-milan/). |
| February 8, 2022 | **New features**<br />Amazon DocumentDB R6G and T4G instances are now available in Asia Pacific, South America, and Europe. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2022/02/amazon-documentdb-mongodb-r6g-t4g-additional-regions/). |
| May 4, 2021 | **New features**<br />See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-documentdb-improves-mongodb-compatibility-and-indexing-improvements/). |
| November 9, 2020 | **New features**<br />See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/11/amazon-documentdb-with-mongodb-compatibility-adds-support-for-mongodb-4-and-transactions/). |
| October 30, 2020 | **New features**<br />See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-documentdb-mongodb-compatibility-support-increased-change-stream-retention/). |
| September 22, 2020 | **New features**<br />See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-documentdb-with-mongodb-compatibility-adds-aggregration-stage-increases-number-of-connections-and-cursors/). |
| July 10, 2020 | **New features**<br />See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-documentdb-support-cross-region-snapshot-copy/). |
| June 30, 2020 | **New features**<br />See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-documentdb-support-cross-region-snapshot-copy/). |

## Amazon DocumentDB elastic clusters release notes
<a name="release-notes-elastic"></a>

Release notes for Amazon DocumentDB elastic clusters.

| Date | Release notes |
| --- | --- |
| January 28, 2025 | **New feature**<br />For one-click connectivity, Amazon DocumentDB is now integrated with AWS CloudShell for instance-based and elastic clusters.<br />For more information see any or all of the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| November 12, 2024 | **New features**<br />Amazon DocumentDB elastic clusters now support Background Indexes. |
| November 1, 2024 | **New feature**<br />Amazon DocumentDB now supports elastic cluster maintenance actions. For more information, see [Maintaining Amazon DocumentDB elastic clusters](elastic-cluster-maintenance.md). |
| August 8, 2024 | **New feature**<br />Amazon DocumentDB elastic clusters are now available in the Asia Pacific (Hong Kong), Canada (Central), and Europe (Paris) Regions. For more information, see [Region availability for elastic clusters](docdb-using-elastic-clusters.md#elastic-region-availability). |
| July 8, 2024 | **New feature**<br />Amazon DocumentDB elastic clusters are now available in the Europe (Milan) Region. For more information, see [Region availability for elastic clusters](docdb-using-elastic-clusters.md#elastic-region-availability). |
| February 22, 2024 | **New features**<br />**Amazon DocumentDB elastic clusters**<br />Amazon DocumentDB elastic clusters now support the following features:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| January 30, 2024 | **New features**<br />**Amazon DocumentDB elastic clusters**<br />Amazon DocumentDB elastic clusters are now available in the following Regions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html)<br />For more information, see [Elastic cluster Region and version availability](docdb-using-elastic-clusters.md#elastic-region-version). |
| August 3, 2023 | **New features**<br />**Amazon DocumentDB Elastic clusters**[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/release-notes.html) |
| March 22, 2023 | **New features**<br />Amazon DocumentDB elastic clusters are now available in the Asia Pacific (Singapore), Asia Pacific (Sydney), and Asia Pacific (Tokyo) Regions. For more information, see [Elastic cluster Region and version availability](docdb-using-elastic-clusters.md#elastic-region-version). |
| November 30, 2022 | **New features**<br />**Amazon DocumentDB Elastic clusters**<br />Amazon DocumentDB elastic clusters is a new type of Amazon DocumentDB cluster that enables users to leverage the MongoDB sharding APIs to scale out their cluster. Elastic clusters handle virtually any number of reads and writes with petabytes of storage capacity by distributing the data and compute across multiple underlying compute instances and volumes. To learn more, see [Using Amazon DocumentDB elastic clusters](https://docs.aws.amazon.com/documentdb/latest/devguide/docdb-using-elastic-clusters). |

---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/drs-cedr-release-notes.html
---

# CEDR Upgrade Tool Version History
<a name="drs-cedr-release-notes"></a>

 The following table describes the released versions of the [CloudEndure to DRS Upgrade Tool](FAQ.md#cedr-to-drs). The latest version of the CloudEndure to DRS Upgrade Tool can be downloaded by following [ the Upgrade Tool Guide](https://docs.cloudendure.com/Content/Configuring_and_Running_Disaster_Recovery/Upgrade_CEDR_to_DRS/Upgrade_CEDR_to_DRS.htm#Quick_start_guide).

[What's in a Release?](drs-client-release-notes.md#client-release-notes-definition)

| Client Version | Details | Release date |
| --- | --- | --- |
| 5.28.0 |  +  Fixed an issue preventing upgrades when source machines had very large PIT EBS Snapshots.   | 27 February 2024 |
| 5.20.0 |  +  Fixed an issue preventing upgrades from non-Nitro instances running Windows Server 2022.   | 8 January 2024 |
| 5.14.0 |  +  Fixed issue preventing upgrades when unencrypted EBS volumes were used for replication. <br />+  Fixed issue preventing upgrades when specifying devices using the `--drives` flag. <br />+  Fixed issue preventing upgrades in GovCloud when KMS keys were specified.   | 18 November 2023 |
| 5.12.0 |  +  Fixed issue preventing DRS service tags from being applied when `--import-blueprint` was used.   | 12 November 2023 |
| 5.3.1 |  +  Fixed issue preventing certain operating systems from installing the DRS agent after upgrade.   | 13 August 2023 |
| 5.2.0 |  +  Added support for legacy operating systems.   | 2 August 2023 |
| 3.7.0 |  +  Fixed issue preventing upgrade on CloudEndure servers with large disks.   | 28 December 2022 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

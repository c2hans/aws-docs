---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrating-fsx-ontap.html
---

# Migrating to Amazon FSx for NetApp ONTAP
<a name="migrating-fsx-ontap"></a>

The following sections provide information on how to migrate your existing NetApp ONTAP file systems to Amazon FSx for NetApp ONTAP.

**Note**
If you plan to use the `All` tiering policy to migrate your data to the capacity pool tier, keep in mind that file metadata is always stored on the SSD tier, and that all new user data is first written to the SSD tier. When data is written to the SSD tier, the background tiering process will begin tiering your data to capacity pool storage, but the tiering process is not immediate and consumes network resources. You need to size your SSD tier to account for file metadata (3-7% of the size of user data), as a buffer for user data before it is tiered to capacity pool storage. We recommend that you do not exceed 80% utilization of your SSD tier.
While migrating data, be sure to monitor your SSD tier using [CloudWatch File system metrics](file-system-metrics.md) to ensure that it is not filling faster than the tiering process can move data to the capacity pool storage.

**Topics**
+ [Migrating to FSx for ONTAP using NetApp SnapMirror](migrating-fsx-ontap-snapmirror.md)
+ [Migrating to FSx for ONTAP using AWS DataSync](migrate-files-to-fsx-datasync.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

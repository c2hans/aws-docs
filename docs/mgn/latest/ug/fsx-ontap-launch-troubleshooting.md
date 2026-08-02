---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/fsx-ontap-launch-troubleshooting.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Troubleshooting FSx for ONTAP launch errors
<a name="fsx-ontap-launch-troubleshooting"></a>

Use the information in this section to troubleshoot launch errors specific to FSx for ONTAP migrations.

## Insufficient file system capacity
<a name="fsx-ontap-insufficient-capacity"></a>

Before launching a test or cutover, MGN validates that the FSx for ONTAP file system has sufficient capacity. The launch fails if predicted usage would exceed 90% of the aggregate capacity, with an error similar to:

```
Launch check failed: insufficient capacity on file system fs-0123456789abcdef0
(85% used). This job needs ~50 GB of free space. Expand storage and retry.
```

**Cause**
The FSx for ONTAP file system does not have enough free SSD storage capacity to create FlexClone volumes for all source servers in the launch job.

**Resolution**
Increase the SSD storage capacity of your FSx for ONTAP file system.

1. Open the FSx for ONTAP console at [https://console.aws.amazon.com/fsx/](https://docs.aws.amazon.com/fsx/), and choose **File systems**.

1. Select the file system shown in the error message.

1. On the **Summary** panel, choose **Update** next to **SSD storage capacity**.

1. Enter the new desired capacity. The minimum increase is 10% of the current capacity or 1 TiB, whichever is greater.

1. Choose **Update**.

1. Wait for the storage update to complete, then retry the launch from the MGN console.

**Note**
Storage capacity increases are non-disruptive. The file system remains available during the scaling operation.

**Tip**
During migration, the file system holds both the replica volumes (used for ongoing replication) and the cloned volumes (created at launch). Both coexist until you finalize the cutover and delete the replica volumes. Plan your SSD capacity to accommodate both sets simultaneously, or reduce the number of source servers in a single launch job.

For more information, see [Managing SSD storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html).

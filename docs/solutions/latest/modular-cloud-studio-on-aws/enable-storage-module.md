---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-storage-module.html
---

# Step 5: Enable Storage modules (Optional)
<a name="enable-storage-module"></a>

The solution supports two Amazon FSx storage options. Choose the storage module that best fits your workload requirements.

## Amazon FSx for Windows File Server module
<a name="amazon-fsx-for-windows-file-server-module"></a>

Follow these steps to enable the Amazon FSx for Windows File Server module.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Storage** from the left navigation pane.

1. Choose **Deploy New Module**.

1. For **Select Region**, select the Region where you want the FSx for Windows File Server module. There should be only one hub Region option if you have not deployed any spoke Regions.

1. For **Select Storage module**, select **Amazon FSx for Windows File Server** and choose **Next**.

1. For **Configure storage settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.

<table>
<thead>
  <tr><th> <b>Parameter</b> </th><th> <b>Default</b> </th><th> <b>Description</b> </th></tr>
</thead>
<tbody>
  <tr><td>Automatic Backup Retention Period</td><td>30</td><td>Choose the number of days that Amazon FSx should retain automatic backups for this file system.</td></tr>
  <tr><td>Throughput Capacity</td><td>64</td><td>The sustained speed for your file system. The system can <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html#impact-throughput-cap-performance">burst to higher speeds</a>. Values range from 32 MB/s to 12288 MB/s.</td></tr>
  <tr><td>SSD Storage Capacity</td><td>256</td><td>Specify the size (in GiB) of the Amazon FSx storage that you would like to create. The allowed value is minimum 32 GiB and maximum 65536 GiB.</td></tr>
</tbody>
</table>

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided and choose **Deploy Module** if you confirm that they are correct. The status of the storage shows as **Enabling in progress**. The deployment of this module takes approximately 30 minutes. After the deployment is complete, the status of the Storage module shows as **Enabled**.

1. Follow the [manual configuration steps](manual-configurations.md) in the guide or you can follow the instructions by clicking the **View** button on the MCS Web UI to complete the manual configuration.

## Amazon FSx for Lustre module
<a name="amazon-fsx-for-lustre-module"></a>

Follow these steps to enable the Amazon FSx for Lustre module.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Storage** from the left navigation pane.

1. Choose **Deploy New Module**

1. For **Select Region**, select the Region where you want the FSx for Lustre module. There should be only one hub Region option if you have not deployed any spoke Regions.

1. For **Select Storage module**, select **Amazon FSx for Lustre** and choose **Next**.

1. For **Configure storage settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.

<table>
<thead>
  <tr><th> <b>Parameter</b> </th><th> <b>Default</b> </th><th> <b>Description</b> </th></tr>
</thead>
<tbody>
  <tr><td>Storage Capacity</td><td>1200</td><td>Storage capacity in GiB. Minimum is 1,200 GiB; maximum is 24,000 GiB</td></tr>
  <tr><td>Compression Type</td><td>NONE</td><td>Data compression reduces the physical disk space needed to store file data. Select LZ4 to enable data compression</td></tr>
  <tr><td>S3 Path for Data Repository Association (optional)</td><td> <i>Optional input</i> </td><td>Specify an S3 Path to create a Data Repository Association within the Lustre Filesystem. If you leave this field blank, no Data Repository Association will be created.</td></tr>
  <tr><td>Lustre Mount Path for Data Repository Association (optional)</td><td>/</td><td>Specify a path within the Lustre Filesystem to mount an S3 Data Repository Association. This parameter is required if you specified an S3 Path for Data Repository Association.</td></tr>
</tbody>
</table>

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided and choose **Deploy Module** if you confirm that they are correct. The status of the storage shows as **Enabling in progress**. The deployment of this module takes approximately 10 minutes with no Data Repository Association, and approximately 20 minutes if you specify an S3 Path for Data Repository Association. After the deployment is complete, the status of the Storage module shows as **Enabled**.

1. Follow the [manual configuration steps](manual-configurations.md) in the guide or you can follow the instructions by clicking the **View** button on the MCS Web UI to complete the manual configuration.

**Note**
MCS deploys a SCRATCH filesystem and does not automatically create a backup when the module is disabled. However, if a Data Repository Association is deployed, data is bidirectionally synchronized between S3 and Lustre, and the data remains in S3 after module disablement.

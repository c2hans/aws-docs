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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-storage-module.html)

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-storage-module.html)

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided and choose **Deploy Module** if you confirm that they are correct. The status of the storage shows as **Enabling in progress**. The deployment of this module takes approximately 10 minutes with no Data Repository Association, and approximately 20 minutes if you specify an S3 Path for Data Repository Association. After the deployment is complete, the status of the Storage module shows as **Enabled**.

1. Follow the [manual configuration steps](manual-configurations.md) in the guide or you can follow the instructions by clicking the **View** button on the MCS Web UI to complete the manual configuration.

**Note**
MCS deploys a SCRATCH filesystem and does not automatically create a backup when the module is disabled. However, if a Data Repository Association is deployed, data is bidirectionally synchronized between S3 and Lustre, and the data remains in S3 after module disablement.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

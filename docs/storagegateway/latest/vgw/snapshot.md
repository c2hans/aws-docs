---
source_url: https://docs.aws.amazon.com/storagegateway/latest/vgw/snapshot.html
---

# Creating a recovery snapshot
<a name="snapshot"></a>

The following procedure shows you how to create a recovery snapshot from a volume recovery point for a gateway, and where to find that snapshot in the Storage Gateway console after you create it. You can take recovery snapshots on a one time, ad hoc basis or you can set up a snapshot schedule to take recurring snapshots of the volume at regular intervals that you specify.

**To create and use a recovery snapshot of a volume from an existing gateway**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. In the navigation pane on the left side of the console page, choose **Gateways**.

1. Choose the gateway for which you want to create a snapshot, and then choose the **Details** tab.

   The **Details** tab displays a recovery snapshot message for the selected gateway.

1. Choose **Create recovery snapshot** to open the **Create recovery snapshot** dialog box.

1. From the list of volumes that appears, choose the volume that you want to recover, and then choose **Create snapshots**.

   Storage Gateway initiates the snapshot process for the specified volume. When the snapshot process is complete, you can find the snapshot listed in the **Snapshots** column when viewing the volume on the **Volumes** page of the Storage Gateway console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

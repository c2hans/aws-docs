---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/server-post-migration.html
---

# Manage source servers after migration
<a name="server-post-migration"></a>

After you launch cutover instances, use the following actions to complete the migration and clean up your source servers in AWS Transform MGN. We recommend that you perform them in this order:

1. [Finalize cutover](#server-post-migration-finalize-cutover)

1. [Disconnect from AWS Transform MGN](#server-post-migration-disconnect)

1. [Archive the source server](#server-post-migration-archive) or [delete the source server](#server-post-migration-delete)

## Finalize cutover
<a name="server-post-migration-finalize-cutover"></a>

Finalize the cutover after you have launched a cutover instance and confirmed that it works as expected in AWS. Finalizing the cutover changes the server's **Migration lifecycle** status to **Cutover complete**, stops data replication, and discards all replicated data. All AWS resources used for data replication are terminated.

**Note**
We recommend that you turn on termination protection for your cutover instances after you complete your testing and before you finalize the cutover. Learn more about enabling termination protection in [this Amazon EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

To finalize a cutover:

1. Validate that the cutover instance is functioning correctly in AWS, for example by testing connectivity and application behavior.

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers in the **Cutover in progress** state.

1. Choose **Test and cutover**, then choose **Finalize cutover**.

1. In the **Finalize cutover for X servers** dialog, choose **Finalize**.

After the cutover is finalized, the **Migration lifecycle** column shows **Cutover complete**, the **Data replication** column shows **Disconnected**, and the **Next step** column shows **Mark as archived**.

**Note**
After you finalize the cutover, the AWS Replication Agent receives a command to uninstall itself from the source server (within 10 minutes).
If you encounter issues after finalizing, choose **Test and cutover**, then **Revert to "ready for cutover"** to return the server to the **Ready for cutover** state.

## Disconnect from AWS Transform MGN
<a name="server-post-migration-disconnect"></a>

After data replication is complete, you can disconnect the source server from AWS Transform MGN. Disconnecting uninstalls the AWS Replication Agent from the source server and stops data replication for the server. If you already finalized the cutover, the agent received a command to uninstall itself as part of finalizing.

**Warning**
Do not disconnect the source server until you have confirmed that the cutover instance is working correctly in AWS. If you discover issues after cutover, you may need to fall back to the source server.

To disconnect a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Disconnect from service**.

1. In the **Disconnect X server/s from service** dialog, choose **Disconnect**.

**Important**
To restart data replication for a disconnected server, you must reinstall the AWS Replication Agent. Disconnecting does not affect test or cutover instances that were launched for the server, but you can no longer identify which source server each Amazon EC2 instance corresponds to.

[Learn more about uninstalling the AWS Replication Agent](uninstalling-agent.md).

## Archive the source server
<a name="server-post-migration-archive"></a>

After a server is cut over, you can archive it. Archived servers are removed from the main **Source servers** list, which keeps the console organized after large migrations. Only archive servers for which you have already performed a cutover.

To archive a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Mark as archived**.

1. In the **Archive X servers** dialog, choose **Archive**.

To view archived servers, open the **Preferences** menu by choosing the gear button, select **Show only archived servers**, and choose **Confirm**. Clear this option to see your non-archived servers again.

## Delete the source server
<a name="server-post-migration-delete"></a>

You can delete a source server to remove its record from AWS Transform MGN. You can delete one or more servers at a time. Only servers that are not actively replicating can be deleted.

To delete a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers that are not actively replicating.

1. Choose **Actions**, then choose **Delete from service**.

1. Confirm the deletion in the dialog.

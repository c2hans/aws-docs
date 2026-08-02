---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/docdb-overview.html
---

# Working with Amazon DocumentDB in the Toolkit
<a name="docdb-overview"></a>

Amazon DocumentDB (with MongoDB compatibility) is a fast, reliable, and fully-managed database service that simplifies the set up, operation, and scaling of MongoDB-compatible databases in the cloud.

For detailed information about Amazon DocumentDB, getting started information, and tutorials, see the [Amazon DocumentDB](https://docs.aws.amazon.com//documentdb/latest/developerguide/what-is.html) Developer Guide.

The following sections describe how to work with Amazon DocumentDB with the AWS Toolkit for Visual Studio Code.

## Accessing Amazon DocumentDB from the AWS Toolkit
<a name="docdb-overview-access"></a>

To access Amazon DocumentDB with the AWS Toolkit, complete the following procedure.

**Accessing Amazon DocumentDB in the AWS Toolkit**

1. From VS Code, open AWS Toolkit for Visual Studio Code.

1. From the AWS Toolkit, expand the **Explorer**.

1. From the **Explorer**, expand Amazon DocumentDB to display your existing Amazon DocumentDB resources.

## Creating an instance-based cluster.
<a name="docdb-overview-create-cluster"></a>

To get started working with Amazon DocumentDB, create a cluster by completing the following procedure.

**Creating an instance-based cluster**

1. From the AWS Toolkit for Visual Studio Code, open the context menu for (right-click) Amazon DocumentDB, then select **Create Cluster** to open the **Create Amazon DocumentDB Cluster** dialog in VS Code.

1. From the **Cluster type** screen, choose **Instance Based Cluster**.

1. From the **Cluster name** screen, specify a name for your new cluster.

1. From the **Select engine version** screen, choose your preferred Amazon DocumentDB engine version.

1. From the **Admin username and password** screens, specify an admin username and password to protect your cluster.

1. From the **Specify Storage encryption** screen, choose whether or not to encrypt your cluster.

1. From the **Number of instances** screen, configure your preferred number of instances.

1. From the **Select instance class** screen, choose your preferred instance class then proceed to create your new cluster.
**Note**
It could take several minutes to spin-up your cluster.

## Copying a cluster endpoint
<a name="docdb-overview-create-cluster"></a>

To copy your Amazon DocumentDB cluster endpoint, complete the following procedure.

**Copying a cluster endpoint**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster you want to copy the connection details from, then choose **Copy Endpoint** to copy the cluster endpoint information to your clipboard.

1. Your cluster endpoint can now be pasted into your documents.

## Open in browser
<a name="docdb-overview-browser-cluster"></a>

Open your Amazon DocumentDB clusters in the AWS Console for a more cluster management features. To open the AWS Console to your Amazon DocumentDB cluster in your default web browser, complete the following procedure.

**Opening your cluster in the AWS Console**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster you want to view in the AWS Console, then choose **Open in Browser**.

1. The AWS Console opens to the Amazon DocumentDB cluster in your default web browser.

## Expanding an existing cluster
<a name="docdb-overview-expand-cluster"></a>

To scale your Amazon DocumentDB clusters by adding instances, complete the following procedure.

**Adding an instance to expand your cluster**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster you want to expand and choose **Add an Instance** to open the **Add an Instance** dialog in VS Code.

1. When prompted, input a name for your new instance into the text field, then press the **Enter** key to continue.

1. When prompted, select an instance class from the list to continue.

1. The **AWS Explorer** displays the creation status and updates when the new instance is ready.

## Stopping a cluster
<a name="docdb-overview-stopping-cluster"></a>

Stop your Amazon DocumentDB cluster by completing the following procedure.

**Note**
While your cluster is stopped, most cluster management features will be unavailable.

**Stopping your Amazon DocumentDB cluster**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Choose the **Stop Cluster** button located next to the cluster your want to stop or right-click the cluster and choose **Stop Cluster**.

1. When prompted, choose **Yes** to stop your cluster or **Cancel** to cancel the stop process and leave your cluster running.

1. The **AWS Explorer** displays the status of your cluster and updates when the cluster has stopped.

## Rebooting an instance
<a name="docdb-overview-reboot-cluster"></a>

Rebooting an instance is useful for troubleshooting and making minor changes without impacting your entire cluster. To reboot an Amazon DocumentDB instance, complete the following procedure.

**Rebooting a cluster instance**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster instance that you want to reboot, then choose **Reboot Instance**.

1. When prompted, choose **Yes** to reboot your instance or **Cancel** to cancel the reboot process and leave your instance stopped.

1. The **AWS Explorer** displays the status of your cluster and updates when your instance has rebooted.

## Deleting an instance
<a name="docdb-overview-delete-cluster"></a>

To delete an Amazon DocumentDB cluster instance, complete the following procedure.

**Note**
Deleting an instance doesn't impact the data in your cluster. If you delete the primary instance, one of the replica instances takes over as the writable instance.

**Deleting a cluster instance**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster instance you want to delete, then choose **Delete** to open the delete-cluster-instance confirmation dialog in VS Code.

1. Follow the confirmation prompt, then press the **Enter** key to delete your cluster instance.

1. The **AWS Explorer** displays the status of your cluster instance and updates when your instance has been deleted.

## Viewing, adding, and removing tags
<a name="docdb-overview-tags"></a>

Tags are used to organize and track resources within your environment. To view or edit the tags associated with your Amazon DocumentDB cluster, complete one of the following procedures.

**Viewing cluster tags**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster you want to view tags for, then choose **Tags...** to open the **Tags for **your cluster name**** dialog.

1. Your tags are displayed in the dialog window, if no tags are associated with your cluster then the message **[No tags assigned]** is displayed.

**Adding tags to your cluster**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster you want to add tags for, then choose **Tags...** to open the **Tags for **your cluster name**** dialog.

1. Choose the **Add tag...** button to open the **Add Tag** dialog in VS Code.

1. Enter a new tag into the text field, then press the **Enter** key to continue.

1. Enter a value into the text field, then press the **Enter** to add the key/value pair to your cluster.

**Removing tags from your cluster**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster you want to remove tags from, then choose **Tags...** to open the **Tags for **your cluster name**** dialog.

1. Choose the **Remove tag...** button to open the **Remove a tag from **your cluster name**** dialog in VS Code.

1. Choose the tag your want to remove from the provided list to remove the tag from your cluster.

## Modifying an instance class
<a name="docdb-overview-instance-class"></a>

To modify the class of an Amazon DocumentDB cluster instance, complete the following procedure.

**Modifying an instance class**

1. From the AWS Toolkit for Visual Studio Code, expand **Amazon DocumentDB** to display your Amazon DocumentDB clusters.

1. Right-click the cluster instance you want to modify, then choose **Modify Class...** to open the **Select instance class** dialog in VS Code.

1. Choose a new class for your instance from the list to update the class.

1. The **AWS Explorer** displays the status of your cluster instance and updates when the class of your instance has been updated.

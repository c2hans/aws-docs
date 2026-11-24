---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-svm-peers.html
---

# Creating an SVM peer

An SVM peer lets two storage virtual machines (SVMs) on peered clusters work together, for example to replicate data with SnapMirror or cache data with FlexCache. A cluster peer between the two clusters must already exist. For more information, see [Creating a cluster peer](creating-cluster-peers.md).

You create an SVM peer from one side. If the cluster peer allows all SVMs, the SVM peer becomes active immediately with no separate accept step. If the cluster peer allows only specific SVMs, the SVM peer is created in the `INITIATED` state and the other side must accept it. When both SVMs are on FSx for ONTAP file systems in the same AWS account, Amazon FSx also creates the SVM peer resource on the other file system so that you can manage it from either side.

## To create an SVM peer (AWS Management Console)
<a name="create-an-svm-peer-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, under **ONTAP**, choose **SVM peers**. Then choose **Create SVM peer**.

1. In the **SVM peer configuration** section, for **File system ID (local)**, choose the file system that hosts the local SVM. Then for **Storage virtual machine (local)**, choose the SVM that initiates the peer relationship.

1. For **Peer SVM location**, do one of the following:
   + Choose **In this AWS account** if the peer SVM is on an FSx for ONTAP file system in the same AWS account. Then choose the **Peer Region**, **Peer file system ID**, and **Peer SVM** from the dropdown menus. Only file systems that already have a cluster peer with the local file system are shown.
   + Choose **In another AWS account or on premises** if the peer SVM is on an FSx for ONTAP file system in a different AWS account or on an on-premises ONTAP cluster. Then enter the peer SVM name.

1. (Optional) For **Peer SVM alias**, enter an alias for the peer SVM to avoid a name conflict on the local cluster. You can use up to 41 characters.

1. For **Applications**, choose the applications that this SVM peer authorizes: **SnapMirror**, **FlexCache**, **File copy**, or **LUN copy**. Both sides must authorize the same applications.

1. Choose **Create SVM peer**.

## To create an SVM peer (AWS CLI)
<a name="create-an-svm-peer-cli"></a>

1. Create an SVM peer by using the **create-storage-virtual-machine-peer** command.

   ```
   aws fsx create-storage-virtual-machine-peer \
        --storage-virtual-machine-id {{svm-0123456789abcdef0}} \
        --peer-svm-name {{source-svm}} \
        --peer-cluster-name {{FsxId0fedcba9876543210}} \
        --applications SNAPMIRROR
   ```

1. If the SVM peer's state is `INITIATED`, accept it on the other side. If the other SVM is on an FSx for ONTAP file system, use the **update-storage-virtual-machine-peer** command on that side's SVM peer. If the other SVM is on an on-premises ONTAP cluster, run the `vserver peer accept` command on that cluster.

   ```
   aws fsx update-storage-virtual-machine-peer \
        --storage-virtual-machine-peer-id {{svmpeer-0fedcba9876543210}} \
        --state PEERED
   ```

1. Use the **describe-storage-virtual-machine-peers** command to verify that the SVM peer's `State` is `PEERED`.

## To accept the SVM peer on the other cluster
<a name="accept-svm-peer-console"></a>

If the peer SVM is in another AWS account or on premises and the SVM peer is in the **Initiated** state, accept the SVM peer on the other cluster.
+ If the other file system is in another AWS account, use the Amazon FSx console, AWS CLI, or Amazon FSx API in that account. In the console, choose the SVM peer on the **SVM peers** page, choose **Update SVM peer**, and set the state to **Peered**. In the AWS CLI, use the **update-storage-virtual-machine-peer** command, as described on this page.
+ If the other cluster is an on-premises ONTAP cluster, use the ONTAP CLI. Run the following command on that cluster.

  ```
  OnPrem-Cluster::> vserver peer accept -vserver {{OnPremSVM}} -peer-vserver {{FSxSVM}}
  ```

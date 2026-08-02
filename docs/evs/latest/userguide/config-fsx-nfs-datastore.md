---
source_url: https://docs.aws.amazon.com/evs/latest/userguide/config-fsx-nfs-datastore.html
---

# Configure FSx for NetApp ONTAP as an NFS datastore
<a name="config-fsx-nfs-datastore"></a>

The following procedure details the minimum steps required to configure FSx for NetApp ONTAP as an NFS datastore for Amazon EVS using the FSx console and the VMware vSphere client interface that runs on Amazon EVS.

## Prerequisites
<a name="fsx-evs-prereqs-nfs"></a>

Before you use Amazon EVS with Amazon FSx for NetApp ONTAP, make sure that the following prerequisite tasks have been completed.
+ An Amazon EVS environment is deployed in your Virtual Private Cloud (VPC). For more information, see [Getting started with Amazon Elastic VMware Service](getting-started.md).
+ You have access to your vSphere client running on Amazon EVS.
+ You or your storage admin must have necessary permissions to create and manage FSx for ONTAP file systems in your VPC. For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html.).

Your IAM principal has appropriate permissions to create and manage FSx for ONTAP file systems in your VPC. For more information, see [Create and manage an Amazon EVS environment](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env).

## Create an FSx for NetApp ONTAP file system
<a name="create-fsx-file-system-nfs"></a>

1. Go to the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. Choose **Create file system**.

1. Select **Amazon FSx for NetApp ONTAP**.

1. Choose **Next**.

1. Select **Standard create**.

1. For **Deployment type**, select a Single-AZ deployment option.
**Note**
Amazon EVS only supports Single-AZ deployments at this time.

1. For **SSD storage capacity**, specify 1024 GiB.

1. For **Throughput capacity**, choose **Specify throughput capacity**. Choose at least 512 MB/s for Single-AZ 1 or at least 768 MB/s for Single-AZ 2.

1. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets.

1. Select a security group that permits all required FSx for ONTAP NFS traffic to the Amazon EVS host VMkernel management VLAN subnet.

1. Select the Amazon EVS service access subnet that your file system will be deployed in. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

1. For **Junction path**, specify a meaningful name such as `/vol1` to identify this volume in vSphere.

1. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**.

1. Leave the remaining setting at their default values and choose **Next**.

1. Review the file system attributes and choose **Create file system**.

## Retrieve the NFS DNS name for the storage virtual machine
<a name="create-fsx-volume-nfs"></a>

1. Go to the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. On the left menu, select **File systems**.

1. Choose the newly created file system.

1. Select the **Storage virtual machines** tab.

1. Choose the storage virtual machine.

1. Select the **Endpoints** tab.

1. Copy the network file system (NFS) DNS name for later use in VMware Vsphere.

## Create an NFS datastore in vSphere using the FSx for ONTAP volume
<a name="attach-fsx-volume-vsphere-nfs"></a>

Follow the instructions in [Create an NFS Datastore in vSphere Environment](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-B52657D0-248D-4A99-99CC-D35B350461D5-en)to configure Amazon FSx for NetApp ONTAP as external storage for VMware vSphere. For the Server setting in the vSphere client interface, use the storage virtual machine (SVM) NFS DNS name that you copied in the previous step.

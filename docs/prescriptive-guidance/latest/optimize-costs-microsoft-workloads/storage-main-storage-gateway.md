---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-main-storage-gateway.html
---

# AWS Storage Gateway
<a name="storage-main-storage-gateway"></a>

AWS Storage Gateway is a hybrid cloud storage service that connects on-premises environments with AWS cloud storage. It allows you to seamlessly integrate your existing on-premises infrastructure with AWS, enabling you to store and retrieve data from the cloud and run applications in a hybrid environment. For Windows workloads, you can use Storage Gateway to store and access data using native Windows protocols such as SMB and NFS. You can use Storage Gateway to reduce costs associated with running Windows workloads on AWS by using on-premises hardware and software as a bridge to the cloud. This enables you to take advantage of the scalability and cost-efficiency of AWS without having to make significant changes to your existing infrastructure.

Under the umbrella of Storage Gateway, you get Amazon S3 File Gateway, Amazon FSx File Gateway, Tape Gateway, and Volume Gateway. S3 File Gateway and FSx File Gateway are most commonly used with Microsoft workloads.

## Amazon S3 File Gateway
<a name="9999999999999999fgw-s3long-.a33db926-8184-5ad4-ad08-42f7dc48ec4f"></a>

[Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html) enables you to store your files in Amazon S3 while providing access to your users by using traditional SMB shares. This provides a familiar user interface and helps reduce costs by storing your data in Amazon S3 and taking advantage of the various Amazon S3 storage tiers. You can implement Storage Gateway with S3 Intelligent Tiering to help you automatically move lifecycle files to the lowest cost storage tiers to lower your costs even further. We recommend S3 File Gateway for scale-out, read-only access, fast repeated reads (from cache), and database dumps. It's not generally recommended for high performance or high availability writes, editing files, or departmental shares.

## Amazon FSx File Gateway
<a name="9999999999999999fgw-fsxwlong-.a551c59b-d55e-5827-8a1d-1df82540e654"></a>

[Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html) can also offer cost savings when working with Amazon FSx Windows file systems. You can stand up an FSx File Gateway to provide localized access to an Amazon FSx file system in another Region to avoid the costs of having two independent files systems. This can also be helpful if you have multiple on-premises file servers and want to consolidate those to avoid paying for multiple hardware devices.

### Cost impact
<a name="storage-main-storage-gateway-cost"></a>

#### Amazon S3 File Gateway
<a name="9999999999999999fgw-s3long-.d18d0943-617e-5527-9531-57a0b528f90c"></a>

Setting up S3 File Gateway is easy because you can use the launch wizard for Storage Gateway. You can deploy the gateway in a matter of minutes by using an EC2 instance in your AWS environment. After the gateway is set up, you can configure Storage Gateway shares to be accessible through the SMB and NFS protocols. For typical Windows workloads, you can also use this setup to take advantage of an Active Directory environment and set permissions on your file shares. You can effectively integrate a Storage Gateway into your normal usage, as it will work as a typical Windows file share. Files and folders are stored as objects and NTFS access control lists (ACLs) as metadata.

The following table compares the costs of 10 TB of storage with three available storage options:
+ FSx for Windows File Server
+ Amazon S3 File Gateway
+ Amazon Elastic Block Store (Amazon EBS)

The price to store 10 TB of storage in considerably less expensive if you use Amazon S3, because you can partition your data into various usage tiers. In the pricing estimate, S3 Intelligent Tiering is used for its pricing flexibility. This includes 80 percent in S3 Standard, 10 percent in Infrequent Access, and 10 percent in Amazon Glacier. Although you can use Amazon Glacier, it's important to set the proper lifecycle rules to make sure that any files moved to Amazon Glacier won't need to be accessed immediately. Amazon Glacier is purely for archival usage, not regular access usage.

|
|
| Storage systems | Cost for 10 TB of storage | Region |
| --- |--- |--- |
| FSx for Windows File Server (assuming 50% savings for deduplication) | [$683.20 USD SSD](https://calculator.aws/#/estimate?id=0833fc4f9b69ef3902e600afa3bd35e4c43bd034) | US East (N. Virginia) |
| Amazon S3 File Gateway | [$449.51 USD Intelligent Tiering](https://calculator.aws/#/estimate?id=e584593492b7b6e14752516b3022d85c0e701067) | US East (N. Virginia) |
| Amazon EBS | [$1,335.69 USD GP3](https://calculator.aws/#/estimate?id=1645edeaf53d61821ee1fc60d4d8e876630d4331) | US East (N. Virginia) |

Consider the following:
+ In Amazon Glacier, you receive generic I/O errors unless you use the [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) API to restore the object back to Amazon S3. We recommend that you use a notification for this I/O error by using Amazon CloudWatch Events. That way, your operations team can react to a user getting this error on a file they might need to access. For more information about these errors, see [Error: InaccessibleStorageClass](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-file-gateway-issues.html#troubleshoot-logging-errors-inaccessiblestorageclass) in the Amazon S3 File Gateway documentation.
+ In addition to the Amazon Glacier limitation on access, there are [only 10 ACLs allowed per object/folder](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-file-gateway-issues.html#troubleshoot-copying-files-to-s3) on Storage Gateway. Before you decide to use Storage Gateway, make sure that you don't need more than 10 ACL entries.

#### Amazon FSx File Gateway
<a name="9999999999999999fgw-fsxwlong-.6886ef72-4b3a-5258-b6a6-3b3482328e18"></a>

Similar to an Amazon S3 File Gateway, an FSx File Gateway provides access to a file system that retains the data long-term. In the Amazon S3 File Gateway, the data resides in Amazon S3. For FSx File Gateway, your data resides on FSx for Windows File Server. Although Multi-AZ options are available for FSx for Windows File Server, there isn't a multi-Region option. If you have a global company or remote office, you may need to provide a shared storage platform that's geographically closer to the end user to avoid latency. If you were to deploy another Amazon FSx file system, this would add the cost of an entirely new Amazon FSx for Windows File Server file system and the necessary storage. To avoid creating an entirely new file system and duplicating costs, you can deploy FSx File Gateway in the secondary Region. This provides localized access to files for users, while helping to reduce your overall costs.

|
|
| Storage systems | Cost for 10 TB of storage | Region |
| --- |--- |--- |
| Amazon FSx for Windows File Server | $683.20 USD SSD | US East (N. Virginia) |
| Amazon FSx File Gateway | $503.70 / Single Gateway | US East (N. Virginia) |

|
|
| Note: Prices in the preceding table are based on [Storage Gateway pricing](https://aws.amazon.com/storagegateway/pricing/). |
| --- |

Keep in mind the following:
+ FSx File Gateway can help you save approximately $180 per month (or $2100 annually) for multi-Region workloads.
+ Data transfer charges are much lower with FSx File Gateway, because it only needs to cache the files being accessed regularly and not a full secondary copy.
+ Although you can have two deployments of FSx for Windows File Server in different Regions and keep them updated with AWS Backup or AWS DataSync, neither option is near real time.

### Cost optimization recommendations
<a name="storage-main-storage-gateway-rec"></a>

#### Amazon S3 File Gateway
<a name="9999999999999999fgw-s3long-.c58f09a4-7b0a-5456-ab93-2d5ddce39c07"></a>

S3 File Gateway provides a low-cost option for storing files, but there are some issues to consider regarding how it implements and uses the file system. For instance, S3 File Gateway requires the usage of a virtual machine to run Storage Gateway software. In AWS, Storage Gateway is deployed in Amazon EC2 by using an m5.xlarge instance, by default. If you want to reduce your on-premises storage costs, you can deploy Storage Gateway as a virtual appliance on virtualization platforms such as VMware and Hyper-V.

##### High availability considerations
<a name="high-availability-considerations.249eca6f-a62f-5d57-b4f0-024f236c152a"></a>

Running Storage Gateway is a single point of failure for access to the files. To prevent unnecessary downtime, we recommend that you implement strict access control on which users can make changes to or stop and start the Storage Gateway instance. Additionally, for deployments on AWS, it's beneficial to use Amazon Data Lifecycle Manager to create routing snapshots to quickly recover your Storage Gateway implementation. If you're running Storage Gateway on-premises using VMware, you can configure it for [high availability](https://aws.amazon.com/blogs/storage/deploy-a-highly-available-aws-storage-gateway-on-a-vmware-vsphere-cluster/).

##### Running multiple file systems
<a name="running-multiple-file-systems.f2dcd8ca-3785-5aad-9a5a-351570d2ddc3"></a>

Separating your daily-use file workloads from your archive workloads can help you avoid unnecessary storage costs. Storage Gateway has the ability to be deployed alongside an FSx for Windows File Server file system. By using [DFS Namespaces](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html), you can present your primary daily-use storage running on FSx for Windows File Server and your storage running in Amazon S3 (that's accessed through Storage Gateway).

The following diagram shows how a single DFS Namespace can be used as the frontend access point for different backend storage options.

![Using a DFS Namespace as the frontend access point.](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/b3de5cb4-be4e-4daa-97be-09c873943feb.png)

Clients are directed to a folder structure, such as **\\\\example.com\\storage**. This main directory contains the sub-directories. An FSx for Windows File Server file system contains the file shares accessed on a normal basis. You can use a file share created on Storage Gateway for archive data. Users can manually archive items to the archive folder or you can build a process to automate moving some files from your normal file shares to the archive folder.

Consider the following:
+ Review your storage requirements and provide adequate [storage for the cache](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ManagingLocalStorage-common.html).
+ Add your gateway to your Active Directory configuration and use [standard Windows ACLs for access to files](https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html).

#### FSx File Gateway
<a name="9999999999999999fgw-fsxw-.c039d6e5-e0ae-522f-9a34-71a1cb22e873"></a>

The deployment of FSx File Gateway is similar to the deployment of S3 File Gateway, but it's even easier if you use the launch wizard. For detailed instructions, see [Step 3: Create and activate an Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-gateway-file.html) in the Amazon FSx File Gateway documentation. After you deploy FSx File Gateway in your environment, you can associate it to your existing Amazon FSx file systems and gain access to your files.

Storage is the primary consideration when deploying FSx File Gateway. The default storage provides 150 GB, which is a decent amount of space for caching files. Creating monitoring alerts for low free space can help with storage right sizing without overallocation.

### Additional resources
<a name="storage-main-storage-gateway-resources"></a>
+ [AWS Storage Gateway resources](https://aws.amazon.com/storagegateway/resources/) (AWS documentation)

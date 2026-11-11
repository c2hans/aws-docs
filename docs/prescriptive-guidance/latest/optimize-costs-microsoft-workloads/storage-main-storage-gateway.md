---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-main-storage-gateway.html
---

# AWS Storage Gateway
<a name="storage-main-storage-gateway"></a>

[AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3) is a hybrid cloud storage service that connects on-premises environments with AWS cloud storage. It helps you integrate your existing on-premises infrastructure with AWS, so you can store and retrieve data from the cloud and run applications in a hybrid environment. For Windows workloads, you can use Storage Gateway to store and access data by using file protocols such as SMB and NFS. You can use Storage Gateway to help reduce costs associated with running Windows workloads on AWS by using on-premises hardware and software as a bridge to the cloud. This helps you take advantage of the scalability and cost-efficiency of AWS without making significant changes to your existing infrastructure.

Storage Gateway offers four gateway types: Amazon S3 File Gateway, Amazon FSx File Gateway, Tape Gateway, and Volume Gateway. S3 File Gateway and FSx File Gateway are the gateway types that customers most frequently use with Microsoft workloads.

## Amazon S3 File Gateway
<a name="9999999999999999fgw-s3long-.109279d1-1ab1-57b2-8ed2-8ab1611ce78b"></a>

[Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html) enables you to store your files in Amazon S3 while providing your users with access through traditional SMB shares. This provides a familiar user interface and helps reduce costs by storing your data in Amazon S3 and taking advantage of the various Amazon S3 storage tiers. You can use Storage Gateway with Amazon S3 Intelligent-Tiering to automatically move files to lower-cost storage tiers based on access patterns, which can help reduce your costs further. We recommend S3 File Gateway for scale-out, read-only access, fast repeated reads (from cache), and database dumps. We don't generally recommend it for high-performance or high-availability writes, file editing, or departmental shares.

## Amazon FSx File Gateway
<a name="9999999999999999fgw-fsxwlong-.5a86f9ec-1830-5850-865f-8834eea62681"></a>

[Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html) can also help reduce costs when you work with Amazon FSx Windows file systems. You can deploy an FSx File Gateway to provide localized on-premises access to an Amazon FSx file system in the same Region, which avoids the cost of maintaining two independent file systems. It can also help if you have multiple on-premises file servers and want to consolidate them to avoid paying for multiple hardware devices.

### Cost impact
<a name="storage-main-storage-gateway-cost"></a>

#### Amazon S3 File Gateway
<a name="9999999999999999fgw-s3long-.9cb0f191-bd30-5b6e-b9b2-74a5d7d563a5"></a>

You can set up S3 File Gateway by using the launch wizard for Storage Gateway. You can deploy the gateway by using an EC2 instance in your AWS environment. After you set up the gateway, you can configure Storage Gateway shares to be accessible through the Server Message Block (SMB) and Network File System (NFS) protocols. For typical Windows workloads, you can also use this setup to take advantage of an Active Directory environment and set permissions on your file shares. You can integrate a Storage Gateway into your normal usage, because it works as a typical Windows file share. The gateway stores files and folders as objects and New Technology File System (NTFS) access control lists (ACLs) as metadata.

The following table compares the costs of 10 TB of storage with three available storage options:
+ FSx for Windows File Server
+ Amazon S3 File Gateway
+ Amazon Elastic Block Store (Amazon EBS)

The price to store 10 TB of data is considerably less if you use Amazon S3, because you can partition your data into various usage tiers. The pricing estimate uses S3 Intelligent-Tiering for its pricing flexibility. This includes 80 percent in S3 Standard, 10 percent in S3 Standard-Infrequent Access, and 10 percent in Amazon Glacier. Although you can use Amazon Glacier, set lifecycle rules to make sure that you don't need to access files moved to Amazon Glacier immediately. Amazon Glacier is designed for archival usage, not regular access.

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
<a name="9999999999999999fgw-fsxwlong-.cf9249ef-5d7d-58c8-a7dc-807bbda02b9a"></a>

Similar to an Amazon S3 File Gateway, an FSx File Gateway provides access to a file system that retains the data long-term. In the Amazon S3 File Gateway, the data resides in Amazon S3. For FSx File Gateway, your data resides on FSx for Windows File Server. Although Multi-AZ options are available for FSx for Windows File Server, there isn't a multi-Region option. If you have a global company or remote office, you might need to provide a shared storage solution that's geographically closer to the end user to reduce latency. If you were to deploy another Amazon FSx file system, this would add the cost of an entirely new Amazon FSx for Windows File Server file system and the necessary storage. To avoid creating an entirely new file system and duplicating costs, you can deploy FSx File Gateway in the secondary Region. This provides localized access to files for users, while helping to reduce your overall costs.

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
+ FSx File Gateway can help you save approximately $180 per month (or $2,150 annually) for multi-Region workloads.
+ Data transfer charges can be lower with FSx File Gateway, because it only needs to cache the files that you access regularly and not a full secondary copy.
+ Although you can have two deployments of FSx for Windows File Server in different Regions and keep them updated with AWS Backup or AWS DataSync, neither option is near real time.

### Cost optimization recommendations
<a name="storage-main-storage-gateway-rec"></a>

#### Amazon S3 File Gateway
<a name="9999999999999999fgw-s3long-.3aa73619-c0d5-5ddc-a3b9-82c7fa6dbbad"></a>

S3 File Gateway provides a low-cost option for storing files, but consider how it implements and uses the file system. For instance, S3 File Gateway requires a virtual machine to run Storage Gateway software. In AWS, you deploy Storage Gateway in Amazon EC2 on an m5.xlarge instance by default. If you want to reduce your on-premises storage costs, you can deploy Storage Gateway as a virtual appliance in virtualization environments such as VMware and Hyper-V.

##### High availability considerations
<a name="high-availability-considerations.492ab38c-bd41-5408-8a3e-d3f9bc671857"></a>

Running Storage Gateway is a single point of failure for access to the files. To prevent unnecessary downtime, we recommend that you implement strict access control on which users can make changes to or stop and start the Storage Gateway instance. Additionally, for deployments on AWS, use Amazon Data Lifecycle Manager to create routine snapshots to quickly recover your Storage Gateway implementation. If you're running Storage Gateway on-premises using VMware, you can configure it for [high availability](https://aws.amazon.com/blogs/storage/deploy-a-highly-available-aws-storage-gateway-on-a-vmware-vsphere-cluster/).

##### Running multiple file systems
<a name="running-multiple-file-systems.b923117c-aa88-5e9e-867c-fcbd82494d1f"></a>

Separating your daily-use file workloads from your archive workloads can help you avoid unnecessary storage costs. You can deploy Storage Gateway alongside an FSx for Windows File Server file system. By using [Distributed File System (DFS) Namespaces](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html), you can present your primary daily-use storage running on FSx for Windows File Server and your storage running in Amazon S3 (that's accessed through Storage Gateway).

The following diagram shows how you can use a single DFS Namespace as the frontend access point for different backend storage options.

![Using a DFS Namespace as the frontend access point.](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/b3de5cb4-be4e-4daa-97be-09c873943feb.png)

The DFS Namespace directs clients to a folder structure, such as **\\example.com\\storage**. This main directory contains the subdirectories. An FSx for Windows File Server file system contains the file shares that users access regularly. You can use a file share created on Storage Gateway for archive data. Users can manually archive items to the archive folder, or you can build a process to automatically move files from your regularly accessed file shares to the archive folder.

Consider the following:
+ Review your storage requirements and provide adequate [storage for the cache](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ManagingLocalStorage-common.html).
+ Add your gateway to your Active Directory configuration and use [standard Windows ACLs for access to files](https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html).

#### FSx File Gateway
<a name="9999999999999999fgw-fsxw-.1b9bc644-35c7-52bb-ad97-a380fae4cf6b"></a>

The deployment of FSx File Gateway is similar to the deployment of S3 File Gateway, but the launch wizard simplifies the process. For detailed instructions, see [Step 3: Create and activate an Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-gateway-file.html) in the Amazon FSx File Gateway documentation. After you deploy FSx File Gateway in your environment, you can associate it with your existing Amazon FSx file systems and gain access to your files.

Storage is the primary consideration when deploying FSx File Gateway. The default storage provides 150 GiB, which is sufficient for caching files in many workloads. Creating monitoring alerts for low free space can help you right-size storage without overallocation.

### Additional resources
<a name="storage-main-storage-gateway-resources"></a>
+ [AWS Storage Gateway resources](https://aws.amazon.com/storagegateway/resources/) (AWS documentation)

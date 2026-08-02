---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/replatforming-file-shares.html
---

# Replatforming file shares
<a name="replatforming-file-shares"></a>

If your in-house applications use on-premises external file shares, such as Network File Systems (NFS) or Server Message Block (SMB), we recommend changing the application's code to use Amazon Simple Storage Service (Amazon S3) and [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). However, if block-based access is required, you can use [Amazon Elastic File System (Amazon EFS) ](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)or [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html). Amazon EFS and Amazon FSx are AWS options for applications that require shared file storage.

For COTS applications, we recommend migrating data from on-premises file shares to Amazon EFS on Linux or [FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html). You should expose the block-based file shares to the application in the same way that on-premises file shares are exposed. Amazon EFS and Amazon FSx provide NFS and SMB-based file shares with the same functionalities that on-premises file shares provided. To use Amazon EFS or Amazon FSx for file shares, only configuration changes are required for COTS applications.

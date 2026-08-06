---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd.html
---

# Migrate IIS-hosted applications to Amazon EC2 by using appcmd.exe
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd"></a>

*Deepak Kumar, Amazon Web Services*

## Summary
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-summary"></a>

When you migrate Internet Information Services (IIS)-hosted applications to Amazon Elastic Compute Cloud (Amazon EC2) instances, you need to address several authentication challenges. These challenges include re-entering domain credentials for application pool identities and potentially regenerating machine keys for proper website functionality. This pattern describes a clean migration approach that uses the backup and restore functionality of IIS on Amazon EC2 instances. The approach uses appcmd.exe to uninstall and reinstall IIS on the target Amazon EC2 instances, enabling successful migration of IIS-hosted websites, application pool identities, and machine keys.

## Prerequisites and limitations
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-prereqs"></a>

**Prerequisites **
+ An active AWS account for the target server.
+ A functional source IIS server with websites hosted on it.
+ Understanding of IIS working principles, such as administration and configuration.
+ System administrator access on both the source and target servers.
+ Completed migration of the source IIS server to the target AWS account. You can use migration tools such as AWS Transform MGN, an Amazon Machine Image (AMI) snapshot-based approach, or other migration tools.
+ Windows Server 2012 R2 or later on both source and target servers.
+ Microsoft .NET Framework 4.5 or later installed on both servers (required for aspnet\_regiis.exe key container operations)
+ A method to transfer backup files and exported key XML files from the source to target server, such as Amazon Simple Storage Service (Amazon S3), a shared network drive, or secure copy.
+ The source and target IIS instances must run the same IIS version (8.5 or 10.0).

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ IIS 8.5 or IIS 10.0

## Architecture
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-architecture"></a>

**Source technology stack  **
+ Windows Server with IIS 8.5 or IIS 10.0 installed

**Target technology stack  **
+ Windows Server with IIS 8.5 or IIS 10.0 installed
+ AWS Transform MGN

**Target architecture**

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to migrate IIS-hosted applications to Amazon EC2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2f9f7757-b2bc-4077-b51a-700de521424c/images/36aa9b7a-d0aa-4fa4-be47-9fee43b53c22.png)

The solution includes the following steps:

1. [Install](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation.html) and configure the AWS Replication Agent on the source IIS server in your corporate data center. This agent initiates the replication process and manages data transfer to AWS.

1. The AWS Replication Agent establishes a [secure connection ](https://docs.aws.amazon.com/mgn/latest/ug/Agent-Related-FAQ.html#How-Communication-Secured)to MGN and begins replicating the source server data, including IIS configurations, websites, and application files.

1. MGN launches Amazon EC2 instances in the application subnet with the replicated data. The target Amazon EC2 instance runs IIS and contains the migrated applications with their associated Amazon Elastic Block Store (Amazon EBS) volumes. After the initial replication, MGN continues to sync changes until you're [ready to cut over](https://docs.aws.amazon.com/mgn/latest/ug/migration-dashboard.html#ready-for-cutover1) to the new environment.

## Tools
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-tools"></a>

**AWS services**
+ [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) helps you rehost (*lift and shift*) applications to the AWS Cloud without change and with minimal downtime.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) provides block-level storage volumes for use with Amazon EC2 instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.

**Other tools**
+ [Internet Information Services (IIS)](https://www.iis.net/overview) for Windows Server is a web server with a scalable and open architecture for hosting anything on the Web. IIS provides a set of administration tools, including administration and command line tools (for example, appcmd.exe), managed code and scripting APIs, and Windows PowerShell support.

## Best practices
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-best-practices"></a>
+ **Secure exported key files** – The XML files that contain the exported private keys should be transferred securely (encrypted in transit) and deleted from boththe source and target servers after a successful migration.
+ **Test in a non-production environment** – Perform the backup and restore procedure on a test server before running it in production.
+ **Document application pool identities** – Before migration, record all application pool identity credentials because you must re-enter passwords after the restore.
+ **Back up SSL certificates separately** – The appcmd.exe backup does not include SSL or TLS certificates. Export these separately using the Certificates MMC snap-in or PowerShell
+ **Verify web content files** – The IIS configuration backup does not include web application files (wwwroot content). Make sure that these are migrated with the server image through AWS Transform MGN.

## Epics
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-epics"></a>

### Back up IIS at source prior to migration
<a name="back-up-iis-at-source-prior-to-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create backups of IIS-hosted websites, configuration key, and `WAS` key. | To create backups for IIS-hosted websites, the configuration key (`iisConfigurationKey`), and the `WAS` key (`iisWasKey`), use appcmd.exe on the source server. Use the following steps:1. Open a command prompt as administrator.<br />2. Run the following command: `cd c:\windows\system32\inetsrv`<br />3. Run the following command, replacing `<backupname>` with your value: `appcmd.exe add backup "<backupname>`<br />To export the configuration key and the `WAS` key, do the following:1. Create the export directory: `mkdir C:\temp`<br />2. Run the following command: `cd c:\windows\Microsoft.NET\Framework64\v4.0.30319`<br />3. Run the following command: `aspnet_regiis.exe -px "iisConfigurationKey" C:\temp\iisConfKey.xml -pri`<br />4. Run the following command: `aspnet_regiis.exe -px "iisWasKey" C:\temp\iisWasKey.xml -pri` | IIS Administrator |

### Uninstall and reinstall IIS on the target server
<a name="uninstall-and-reinstall-iis-on-the-target-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Uninstall IIS on the target server. | To uninstall IIS on the target server, use the following steps: 1. Sign in to the server with administrator rights.<br />2. Go to **Server manager**.<br />3. Choose **Manage**, **Remove Roles and features**, **Next**, and **Next**.<br />4. Clear the **Web Server (IIS)** checkbox and then choose **Next**, and **Next**.<br />5. Select the **Restart destination server automatically** checkbox. When the uninstall process is completed, the system reboots.<br />6. Validate that IIS uninstalled successfully by going to `C:\Windows\System32\inetsrv` and confirming that this folder is empty. | IIS Administrator |
| Install IIS on the target server. | To install IIS on the target server, use the following steps: 1. Sign in to the server with administrator rights. <br />2. Go to **Server manager**.<br />3. Choose **Add roles and features**, **Next**, **Next**, **Next**, and **Next**.<br />4. Select the **Webserver IIS** checkbox. When prompted, choose **Add features**.<br />5. Choose all the checkboxes that are shown in **App development**, **Add features**, and **Select all features**. You can select features at a granular level just before the confirmation.<br />6. Choose **Install**.  | IIS Administrator |

### Restore IIS websites and configuration from the backups
<a name="restore-iis-websites-and-configuration-from-the-backups"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Restore IIS websites and configuration. | To restore the IIS backups that you created from the source server on the target server, use the following steps:1. Create a folder named `backup` in the `C:\windows\system32\inetsrv` folder, and then place the source backup folder inside it.<br />2. Open a command prompt and run as administrator.<br />3. Run the following command: `cd C:\windows\system32\inetsrv`<br />4. Run the following command: `C:\windows\system32\inetsrv\appcmd.exe list backup`<br />5. Run the following command: `C:\windows\system32\inetsrv\appcmd.exe restore backup <sourcebackup>`<br />6. Run the following command: `cd c:\windows\Microsoft.NET\Framework64\v4.0.30319`<br />7. Run the following command: `aspnet_regiis.exe -pi "iisConfigurationKey" C:\temp\iisConfKey.xml -exp`<br />8. Run the following command: `aspnet_regiis.exe -pi "iisWasKey" C:\temp\iisWasKey.xml -exp`<br />9. Reset IIS, and go to **Application Pool Identity and Website **advanced settings to re-enter the password.<br />10. Open IIS Manager and verify that all websites, application pools, and virtual directories are restored.<br />11. Browse to each website to confirm it is serving content correctly.<br />12. After confirming the restoration is successful, delete the exported key files from `C:\temp`:<br />`del C:\temp\iisConfKey.xml`<br />`del C:\temp\iisWasKey.xml` | IIS Administrator |

## Related resources
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-resources"></a>

**AWS documentation**
+ [Installing the AWS Replication Agent](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation.html) (AWS Transform MGN documentation)

**AWS Prescriptive Guidance**
+ [Migrate an on-premises VM to Amazon EC2 by using AWS Transform MGN](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-vm-to-amazon-ec2-by-using-aws-application-migration-service.html)
+ [Using AMIs or Amazon EBS snapshots for backups](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/ec2-backup.html#amis-snapshots)

**Microsoft resources**
+ [Application pool identities](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/iis/was-service-svchost-process-operation/understanding-identities#application-pool-identities)
+ [IIS documentation](https://learn.microsoft.com/en-us/iis/)
+ [IIS 8 appcmd.exe documentation](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj635852(v=ws.11))
+ [IIS 10 appcmd.exe documentation](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-10/new-features-introduced-in-iis-10)
+ [Powerful Admin Tools](https://learn.microsoft.com/en-us/iis/overview/powerful-admin-tools)

## Additional information
<a name="migrate-iis-hosted-applications-to-amazon-ec2-by-using-appcmd-additional"></a>
+ The appcmd.exe backup includes: application pools, sites, global configuration, and IIS schema. It does not include web content files, SSL certificates, or shared configuration files.
+ For large-scale IIS farm migrations, consider using the PowerShell Web-Administration module for scripted backup and restore operations.

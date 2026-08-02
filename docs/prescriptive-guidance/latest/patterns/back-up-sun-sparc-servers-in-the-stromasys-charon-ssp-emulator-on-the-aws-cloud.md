---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud.html
---

# Back up Sun SPARC servers in the Stromasys Charon-SSP emulator on the AWS Cloud
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud"></a>

*Kevin Yung and Rohit Darji, Amazon Web Services*

*Luis Ramos, Stromasys*

## Summary
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud-summary"></a>

This pattern provides four options for backing up your Sun Microsystems SPARC servers after a migration from an on-premises environment to the Amazon Web Services (AWS) Cloud. These backup options help you to implement a backup plan that meets your organization’s recovery point objective (RPO) and recovery time objective (RTO), uses automated approaches, and lowers your overall operational costs. The pattern provides an overview of the four backup options and steps to implement them.

If you use a Sun SPARC server hosted as a guest on a [Stromasys Charon-SSP emulator](https://www.stromasys.com/solution/charon-on-the-aws-cloud/), you can use one of the following three backup options:
+ **Backup option 1: Stromasys virtual tape **– Use the Charon-SSP virtual tape feature to set up a backup facility in the Sun SPARC server and archive your backup files to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) using [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html).
+ **Backup option 2: Stromasys snapshot **– Use the Charon-SSP snapshot feature to set up a backup facility for the Sun SPARC guest servers in Charon-SSP.
+ **Backup option 3: Amazon Elastic Block Store (Amazon EBS) volume snapshot **–** **If you host the Charon-SSP emulator on Amazon Elastic Compute Cloud (Amazon EC2), you can use an [Amazon EBS volume snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) to create backups for a Sun SPARC file system.** **

If you use a Sun SPARC server hosted as a guest on hardware and Charon-SSP on Amazon EC2, you can use the following backup option:
+ **Backup option 4: AWS Storage Gateway virtual tape library (VTL) **– Use a backup application with a [Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html) VTL Tape Gateway to back up the Sun SPARC servers.

If you use a Sun SPARC server hosted as a branded zone in a Sun SPARC server, you can use backup options 1, 2, and 4.

[Stromasys](https://www.stromasys.com) provides software and services to emulate legacy SPARC, Alpha, VAX, and PA-RISC critical systems. For more information about migrating to the AWS Cloud using Stromasys emulation, see [Rehosting SPARC, Alpha, or other legacy systems to AWS with Stromasys](https://aws.amazon.com/blogs/apn/re-hosting-sparc-alpha-or-other-legacy-systems-to-aws-with-stromasys/) on the AWS Blog.

## Prerequisites and limitations
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Existing Sun SPARC servers.
+ Existing licenses for Charon-SSP. Licenses for Charon-SSP are available from AWS Marketplace and licenses for Stromasys Virtual Environment (VE) are available from Stromasys. For more information, contact [Stromasys sales](https://www.stromasys.com/contact/).
+ Familiarity with Sun SPARC servers and Linux backups.
+ Familiarity with Charon-SSP emulation technology. For more information about this, see [Stromasys legacy server emulation](https://www.stromasys.com/solutions/charon-on-the-aws-cloud/) in the Stromasys documentation.
+ If you want to use the virtual tape facility or backup applications for your Sun SPARC servers file systems, you must create and configure the backup facilities for the Sun SPARC server file system.
+ An understanding of RPO and RTO. For more information about this, see [Disaster recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html) from the [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) whitepaper in the AWS Well-Architected Framework documentation.
+ To use **Backup option 4**, you must have the following:
  + A software-based backup application that supports a Storage Gateway VTL Tape Gateway. For more information about this, see [Working with VTL devices](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html) in the AWS Storage Gateway documentation.
  + Bacula Director or a similar backup application, installed and configured. For more information about this, see the [Bacula Director](https://www.bacula.org/5.2.x-manuals/en/main/main/Configuring_Director.html) documentation.

The following table provides information about the four backup options in this pattern.

|
|
| **Backup options** | **Achieves crash consistency?** | **Achieves application consistency?** | **Virtual backup appliance solution?** | Typical use cases |
| --- |--- |--- |--- |--- |
| **Option 1 – Stromasys virtual tape ** | **Yes**<br />You can automate Sun SPARC file system snapshots to back up data in a virtual tape. For example, you can use UFS or ZFS snapshots. | **Yes**<br />This backup option requires an automated script to flush in-flight transactions, configure a read-only or temporary offline mode during the file system snapshot, or take an application data dump. You might also require application downtime or read-only mode. | **Yes** | Sun SPARC server file systems backup with .tar or .zip files<br />Application data backup |
| **Option 2 – Stromasys snapshot ** | **Yes**<br />You must configure [Charon-SSP Manager](https://stromasys.atlassian.net/wiki/spaces/DocCHSSP40preAWS/pages/522190974/Charon-SSP+Manager+Installation%20/) or use a command-line startup argument to enable this feature.<br />You must also run a Linux command to ask the Charon-SSP emulator to save the Sun SPARC guest server state into a snapshot file.You must shut down the Sun SPARC guest server.  | **Yes**<br />This backup option creates a snapshot of the emulated guest server, including its virtual disks and memory dump. You must shut down the Sun SPARC guest server during the snapshot. | **No** | Sun SPARC server snapshot<br />Application data backup |
| **Option 3 – Amazon EBS volume snapshot ** | **Yes**<br />You can use AWS Backup to automate the Amazon EBS snapshot. | **Yes**<br />This backup option requires an automated script to flush in-flight transactions and configure a read-only or temporary stop of the Amazon EC2 instance during the Amazon EBS volume snapshot.  This backup option might require application downtime or read-only mode to achieve application consistency.<br />  | **No** | Sun SPARC server file systems snapshot<br />Application data backup |
| **Option 4 – AWS Storage Gateway VTL** | **Yes**<br />You can automatically back up Sun SPARC file system backup data to the VTL by using a backup agent. | **Yes**<br />This backup option requires an automated script to flush in-flight transactions and configure a read-only or temporary offline mode during the file system snapshot or application data dump.This backup option might require application downtime or read-only mode. | **Yes** | A large fleet of Sun SPARC server file system backups<br />Application data backup |

**Limitations**
+ You can use this pattern's approaches to back up individual Sun SPARC servers, but you can also use these backup options for shared data if you have applications that run in a cluster.

## Tools
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud-tools"></a>

**Backup option 1: Stromasys virtual tape**
+ [Stromasys Charon-SSP emulator](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/39158045/CHARON-SSP) creates the virtual replica of the original SPARC hardware inside a standard 64-bit x86 compatible computer system. It runs the original SPARC binary code, including operating systems (OSs) such as SunOS or Solaris, their layered products, and applications.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/index.html) is a web service that provides resizable computing capacity that you use to build and host your software systems.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) provides a simple, serverless, set-and-forget elastic file system for use with AWS services and on-premises resources.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is storage for the internet.
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources.

**Backup option 2: Stromasys snapshot**
+ [Stromasys Charon-SSP emulator](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/39158045/CHARON-SSP) creates the virtual replica of the original SPARC hardware inside a standard 64-bit x86 compatible computer system. It runs the original SPARC binary code, including OSs such as SunOS or Solaris, their layered products, and applications.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/index.html) is a web service that provides resizable computing capacity that you use to build and host your software systems.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) provides a simple, serverless, set-and-forget elastic file system for use with AWS services and on-premises resources.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is storage for the internet.
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources.

**Backup option 3: ****Amazon EBS**** volume snapshot**
+ [Stromasys Charon-SSP emulator](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/39158045/CHARON-SSP) emulator creates the virtual replica of the original SPARC hardware inside a standard 64-bit x86 compatible computer system. It runs the original SPARC binary code, including OSs such as SunOS or Solaris, their layered products, and applications.
+ [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a fully-managed data protection service that makes it easy to centralize and automate across AWS services, in the cloud, and on premises.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block level storage volumes for use with Amazon EC2 instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/index.html) is a web service that provides resizable computing capacity that you use to build and host your software systems.

**Backup option 4: ****AWS Storage Gateway**** VTL**
+ [Stromasys Charon-SSP emulator](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/39158045/CHARON-SSP) creates the virtual replica of the original SPARC hardware inside a standard 64-bit x86 compatible computer system. It runs the original SPARC binary code, including OSs such as SunOS or Solaris, their layered products, and applications.
+ [Bacula](https://www.baculasystems.com/try/?gclid=EAIaIQobChMInsywntC98gIVkT2tBh16ug3_EAAYASAAEgL-nPD_BwE) is an open-source, enterprise-level computer backup system. For more information about whether your existing backup application supports Tape Gateway, see [Supported third-party backup applications for a Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html#requirements-backup-sw-for-vtl) in the AWS Storage Gateway documentation.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/index.html) is a web service that provides resizable computing capacity that you use to build and host your software systems.
+ [Amazon Relational Database Service (Amazon RDS) for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html) supports DB instances running several versions of MySQL.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is storage for the internet.
+ [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html) connects an on-premises software appliance with cloud-based storage to provide seamless integration with data security features between your on-premises IT environment and the AWS storage infrastructure.

## Epics
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud-epics"></a>

### Backup option 1 – Create a Stromasys virtual tape backup
<a name="backup-option-1-ndash-create-a-stromasys-virtual-tape-backup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EFS shared file system for virtual tape file storage. | Sign in to the AWS Management Console or use the AWS Command Line Interface (AWS CLI) to create an Amazon EFS file system.<br />For more information about this, see [Create an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/gs-step-two-create-efs-resources.html) in the Amazon EFS documentation. | Cloud architect |
| Configure the Linux host to mount the shared file system. | Install the Amazon EFS driver on the Amazon EC2 Linux instance and configure the Linux OS to mount the Amazon EFS shared file system during startup.<br />For more information about this, see [Mounting file systems using the Amazon EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the Amazon EFS documentation. | DevOps engineer |
| Install the Charon-SSP emulator. | Install the Charon-SSP emulator on the Amazon EC2 Linux instance.<br />For more information about this, see [Setting up an AWS Cloud instance for Charon-SSP](https://stromasys.atlassian.net/wiki/spaces/DocCHSSP405AWS/pages/718241894/Setting+up+a+Charon-SSP+AWS+Cloud+Instance) in the Stromasys documentation. | DevOps engineer |
| Create a virtual tape file container in the shared file system for each Sun SPARC guest server. | Run the `touch <vtape-container-name>` command to create a virtual tape file container in the shared file system for each Sun SPARC guest server deployed in the Charon-SSP emulator. | DevOps engineer |
| Configure Charon-SSP Manager to create virtual tape devices for the Sun SPARC guest servers. | Log in to Charon-SSP Manager, create virtual tape devices, and configure them to use the virtual tape container files for each Sun SPARC guest server.<br />For more information about this, see the [Charon-SSP 5.2 for Linux user guide](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/76429819926/CHARON-SSP+V5.2+for+Linux) in the Stromasys documentation. | DevOps engineer |
| Validate that the virtual tape device is available in the Sun SPARC guest servers. | Log in to each Sun SPARC guest server and run the `mt -f /dev/rmt/1` command to validate that the virtual tape device is configured in the OS. | DevOps engineer |
| Develop the Systems Manager Automation runbook and automation. | Develop the Systems Manager Automation runbook and set up maintenance windows and associations in Systems Manager for scheduling the backup process.<br />For more information about this, see [Automation walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-walk.html) and [Setting up maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the AWS Systems Manager documentation. | Cloud architect |
| Configure Systems Manager Automation to archive rotated virtual tape container files. | Use the code sample from **Back option 1** in the *Additional information* section to develop a Systems Manager Automation runbook to archive rotated virtual tape container files to Amazon S3. | Cloud architect |
| Deploy the Systems Manager Automation runbook for archiving and scheduling. | Deploy the Systems Manager Automation runbook and schedule it to automatically run in Systems Manager.<br />For more information about this, see [Automation walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-walk.html) in the Systems Manager documentation. | Cloud architect |

### Backup option 2 – Create a Stromasys snapshot
<a name="backup-option-2-ndash-create-a-stromasys-snapshot"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EFS shared file system for virtual tape file storage. | Sign in to the AWS Management Console or use the AWS CLI to create an Amazon EFS file system.<br />For more information about this, see [Create your Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/gs-step-two-create-efs-resources.html) in the Amazon EFS documentation. | Cloud architect |
| Configure the Linux host to mount the shared file system. | Install the Amazon EFS driver in the Amazon EC2 Linux instance and configure the Linux OS to mount the Amazon EFS shared file system during startup.<br />For more information about this, see [Mounting file systems using the Amazon EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the Amazon EFS documentation.  | DevOps engineer |
| Install the Charon-SSP emulator. | Install the Charon-SSP emulator on the Amazon EC2 Linux instance.<br />For more information about this, see [Setting up an AWS Cloud instance for Charon-SSP](https://stromasys.atlassian.net/wiki/spaces/DocCHSSP44xAWSGS/pages/7239901201/Setting+up+an+AWS+Cloud+Instance+for+Charon-SSP) in the Stromasys documentation. | DevOps engineer |
| Configure the Sun SPARC guest servers to start up with the snapshot option. | Use Charon-SSP Manager to set up the snapshot option for each Sun SPARC guest servers.<br />For more information about this, see the [Charon-SSP 5.2 for Linux user guide](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/76429819926/CHARON-SSP+V5.2+for+Linux) in the Stromasys documentation.   | DevOps engineer |
| Develop the Systems Manager Automation runbook. | Use the code sample from **Backup option 2** in the *Additional information* section to develop a Systems Manager Automation runbook to remotely run the snapshot command on a Sun SPARC guest server during a maintenance window. | Cloud architect |
| Deploy the Systems Manager Automation runbook and set up the association to the Amazon EC2 Linux hosts. | Deploy the Systems Manager Automation runbook and set up maintenance windows and associations in Systems Manager for scheduling the backup process.<br />For more information about this, see [Automation walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-walk.html) and [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the AWS Systems Manager documentation. | Cloud architect |
| Archive snapshots into long-term storage. | Use the runbook sample code from the *Additional information* section to develop a Systems Manager Automation runbook to archive snapshot files to Amazon S3. | Cloud architect |

### Backup option 3 – Create an Amazon EBS volume snapshot
<a name="backup-option-3-create-an-ebs-volume-snapshot"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the Charon-SSP emulator. | Install the Charon-SSP emulator on the Amazon EC2 Linux instance.<br />For more information about this, see [Setting up an AWS Cloud instance for Charon-SSP](https://stromasys.atlassian.net/wiki/spaces/DocCHSSP44xAWSGS/pages/7239901201/Setting+up+an+AWS+Cloud+Instance+for+Charon-SSP) in the Stromasys documentation.  | DevOps engineer |
| Create Amazon EBS volumes for the Sun SPRAC guest servers. | Sign in to the AWS Management Console, open the Amazon EBS console, and then create Amazon EBS volumes for the Sun SPRAC guest servers.<br />For more information about this, see [Setting up an AWS Cloud instance for Charon-SSP](https://stromasys.atlassian.net/wiki/spaces/DocCHSSP44xAWSGS/pages/7239901201/Setting+up+an+AWS+Cloud+Instance+for+Charon-SSP) in the Stromasys documentation. | Cloud architect |
| Attach the Amazon EBS volumes to the Amazon EC2 Linux instance. | On the Amazon EC2 console, attach the Amazon EBS volumes to the Amazon EC2 Linux instance.<br />For more information about this, see [Attach an Amazon EBS volume to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html) in the Amazon EC2 documentation. | AWS DevOps |
| Map Amazon EBS volumes as SCSI drives in the Charon-SSP emulator. | Configure Charon-SSP Manager to map the Amazon EBS volumes as SCSI drives in the Sun SPARC guest servers.<br />For more information about this, see the *SCSI storage configuration* section of the [Charon-SSP V5.2 for Linux](https://stromasys.atlassian.net/wiki/spaces/KBP/pages/76429819926/CHARON-SSP+V5.2+for+Linux) guide in the Stromasys documentation. | AWS DevOps |
| Configure the AWS Backup schedule for snapshotting the Amazon EBS volumes. | Set up AWS Backup policy and schedules to snapshot the Amazon EBS volumes.<br />For more information about this, see the [Amazon EBS backup and restore using AWS Backup](https://aws.amazon.com/getting-started/hands-on/amazon-ebs-backup-and-restore-using-aws-backup/) tutorial in the AWS Developer Center documentation. | AWS DevOps |

### Backup option 4 – Create an AWS Storage Gateway VTL
<a name="backup-option-4-create-an-awssglong-vtl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Tape Gateway device. | Sign in to the AWS Management Console, open the AWS Storage Gateway console, and then create a Tape Gateway device in a VPC.<br />For more information about this, see [Creating a gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/create-tape-gateway.html) in the AWS Storage Gateway documentation. | Cloud architect |
| Create an Amazon RDS DB instance for the Bacula Catalog. | Open the Amazon RDS console and create an Amazon RDS for MySQL DB instance.<br />For more information about this, see [Creating a MySQL DB instance and connecting to a database on a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html) in the Amazon RDS documentation. | Cloud architect |
| Deploy the backup application controller in the VPC. | Install Bacula on the Amazon EC2 instance, deploy the backup application controller, and then configure the backup storage to connect with the Tape Gateway device. You can use the sample Bacula Director storage daemon configuration in the `Bacula-storage-daemon-config.txt` file (attached).<br />For more information about this, see the [Bacula documentation](https://www.bacula.org/11.0.x-manuals/en/main/main.pdf). | AWS DevOps |
| Set up backup application on the Sun SPARC guest servers. | Set up a second client to install and set up the backup application on the Sun SPARC guest servers by using the sample Bacula configuration in the `SUN-SPARC-Guest-Bacula-Config.txt` file (attached). | DevOps engineer |
| Set up the backup configuration and schedule. | Set up backup configuration and schedules in the backup application controller by using the sample Bacula Director configuration in the `Bacula-Directory-Config.txt` file (attached).<br />For more information about this, see the [Bacula documentation](https://www.bacula.org/11.0.x-manuals/en/main/main.pdf).   | DevOps engineer |
| Validate that the backup configuration and schedules are correct. | Follow the instruction from the [Bacula documentation](https://www.bacula.org/11.0.x-manuals/en/main/main.pdf) to perform the validation and backup testing for your setup in the Sun SPARC guest servers.<br />For example, you can use the following commands to validate the configuration files:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud.html) | DevOps engineer |

## Related resources
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud-resources"></a>
+ [Charon virtual SPARC with VE licensing](https://aws.amazon.com/marketplace/pp/B08TBQS8NZ?qid=1621489108444&sr=0-2&ref_=srh_res_product_title)
+ [Charon virtual SPARC](https://aws.amazon.com/marketplace/pp/B07XF228LH?qid=1621489108444&sr=0-1&ref_=srh_res_product_title)
+ [Using cloud services and object storage with Bacula Enterprise Edition](https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf)
+ [Disaster recovery (DR) objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html)
+ [Charon legacy system emulation solutions](https://www.stromasys.com/solution/charon-ssp/)

## Additional information
<a name="back-up-sun-sparc-servers-in-the-stromasys-charon-ssp-emulator-on-the-aws-cloud-additional"></a>

**Backup option 1 – Create a Stromasys virtual tape **

You can use the following sample Systems Manager Automation runbook code to automatically start the backup and then swap the tapes:

```
...
# example backup script saved in SUN SPARC Server
 #!/usr/bin/bash
 mt -f  rewind
 tar -cvf
 mt -f  offline
...
         mainSteps:
         - action: aws:runShellScript
           name:
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               # Validate tape backup container file exists
               if [ ! -f {{TapeBackupContainerFile}} ]; then
                 logger -s -p local3.warning "Tape backup container file is not exists - {{TapeBackupContainerFile}}, create a new one"
                 touch {{TapeBackupContainerFile}}
               fi
         - action: aws:runShellScript
           name: startBackup
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               user={{BACKUP_USER}}
               keypair={{KEYPAIR_PATH}}
               server={{SUN_SPARC_IP}}
               backup_script={{BACKUP_SCRIPT}}
               ssh -i $keypair $user@$server -c "/usr/bin/bash $backup_script"
         - action: aws:runShellScript
           name: swapVirtualDiskContainer
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               mv {{TapeBackupContainerFile}} {{TapeBackupContainerFile}}.$(date +%s)
               touch {{TapeBackupContainerFile}}
         - action: aws:runShellScript
           name: uploadBackupArchiveToS3
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               aws s3 cp {{TapeBackupContainerFile}} s3://{{BACKUP_BUCKET}}/{{SUN_SPARC_IP}}/$(date '+%Y-%m-%d')/
 ...
```

**Backup option 2 –  Stromasys snapshot **

** **You can use the following sample Systems Manager Automation runbook code to automate the backup process:

```
      ...

         mainSteps:
         - action: aws:runShellScript
           name: startSnapshot
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               # You may consider some graceful stop of the application before taking a snapshot
               # Query SSP PID by configuration file
               # Example: ps ax | grep ssp-4 | grep Solaris10.cfg | awk '{print $1" "$5}' | grep ssp4 | cut -f1 -d" "
               pid=`ps ax | grep ssp-4 | grep {{SSP_GUEST_CONFIG_FILE}} | awk '{print $1" "$5}' | grep ssp4 | cut -f1 -d" "`
               if [ -n "${pid}" ]; then
                 kill -SIGTSTP ${pid}
               else
                 echo "No PID found for SPARC guest with config {{SSP_GUEST_CONFIG_FILE}}"
                 exit 1
               fi
         - action: aws:runShellScript
           name: startBackup
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               # upload snapshot and virtual disk files into S3
               aws s3 sync {{SNAPSHOT_FOLDER}} s3://{{BACKUP_BUCKET}}/$(date '+%Y-%m-%d')/
               aws s3 cp {{VIRTUAL_DISK_FILE}} s3://{{BACKUP_BUCKET}}/$(date '+%Y-%m-%d')/
         - action: aws:runShellScript
           name: restratSPARCGuest
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               /opt/charon-ssp/ssp-4u/ssp4u -f {{SSP_GUEST_CONFIG_FILE}} -d -a {{SPARC_GUEST_NAME}} --snapshot {{SNAPSHOT_FOLDER}}
 ...
```

**Backup option 4 – **AWS Storage Gateway** VTL**

If you use Solaris non-global zones to run virtualized legacy Sun SPARC servers, the backup application approach can be applied to non-global zones running in the Sun SPARC servers (for example, the backup client can run inside the non-global zones). However, the backup client can also run in the Solaris host and take snapshots of the non-global zones. The snapshots can then be backed up on a tape.

The following sample configuration adds the file system that hosts the Solaris non-global zones into the backup configuration for the Solaris host:

```
FileSet {
   Name = "Branded Zones"
   Include {
     Options {
       signature = MD5
     }
     File = /zones
   }
 }
```

## Attachments
<a name="attachments-9688ae50-9d0c-4d61-ab40-93df2bce4b7d"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/9688ae50-9d0c-4d61-ab40-93df2bce4b7d/attachments/attachment.zip)

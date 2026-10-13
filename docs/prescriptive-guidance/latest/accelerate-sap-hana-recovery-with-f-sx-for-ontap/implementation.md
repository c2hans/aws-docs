---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/implementation.html
---

# Implementation
<a name="implementation"></a>

## Prerequisites
<a name="prerequisites.1ce0aeeb-ca94-5ac3-8996-7923b7581a1e"></a>

Before you begin, verify that your environment meets these requirements:

### AWS infrastructure requirements
<a name="aws-infrastructure-requirements.61717a5b-2182-5226-8948-9eecf474c70f"></a>
+ You need two AWS accounts. The Production account hosts the primary HANA workload. The Backup account handles disaster recovery and backup management.
+ Deploy Amazon FSx for NetApp ONTAP file systems in both accounts. For the recommended HANA volume sizes, see the [SAP HANA on AWS Technical Documentation](https://docs.aws.amazon.com/sap/latest/sap-hana/amazon-fsx-sap-hana.html#:~:text=The%20storage%20capacity%20of%20your,your%20single%20Amazon%20EC2%20instance.).
+ Establish network connectivity between accounts via VPC peering or AWS Transit Gateway.
+ Configure [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) keys for encryption in both accounts.
+ Run SAP HANA on Amazon EC2 instances. Supported operating systems include SUSE Linux Enterprise Server 12 SP3 or later, or Red Hat Enterprise Linux 8.0 or later.

### Commvault requirements
<a name="commvault-requirements.20b20574-0450-52be-9491-c7550e218202"></a>
+ Commvault CommServe v11.40 or later
+ Commvault MediaAgent v11.40 or later
+ NetApp IntelliSnap support enabled in your Commvault license

### Permissions and access
<a name="permissions-and-access.0a787514-2f5e-5d32-8702-34bfc3146f7c"></a>
+ IAM permissions to manage Amazon EC2, AWS KMS
+ Amazon FSx for NetApp ONTAP cluster administrator credentials for both production and backup clusters
+ SAP HANA system administrator access (SYSTEM user) for HANA configuration
+ Commvault administrator access to CommServe for policy configuration

**Scope of this guide:** This guide assumes all prerequisites listed above are already in place. Provisioning AWS accounts, deploying Amazon FSx for NetApp ONTAP file systems, establishing network connectivity, configuring KMS encryption, and deploying SAP HANA on EC2 are out of scope. For guidance on these foundational steps, see the following:

[Creating Amazon FSx for NetApp ONTAP file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html) [SAP HANA on AWS — Technical documentation](https://docs.aws.amazon.com/sap/latest/sap-hana/welcome.html) [AWS Transit Gateway documentation](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) [Commvault installation and licensing](https://documentation.commvault.com/)

#### Step-by-step implementation guide
<a name="step-by-step-implementation-guide"></a>

The following steps integrate your existing Amazon FSx for NetApp ONTAP and Commvault infrastructure into an automated snapshot-based backup solution for SAP HANA. You will create dedicated service accounts, install IntelliSnap agents on your EC2 instances running SAP HANA, establish SnapMirror replication between production and backup accounts, and configure Commvault backup policies. The guide concludes with Backint log backup configuration for point-in-time recovery and a full end-to-end validation of the backup and restore workflow.

##### Step 1: Create Amazon FSx for NetApp ONTAP users and permissions
<a name="step-1-create-amazon-fsx-for-netapp-ontap-users-and-permissions"></a>

This step creates new service accounts specifically for Commvault IntelliSnap operations. While the prerequisites assume you deployed Amazon FSx for NetApp ONTAP and you have cluster administrator access, you create the cv-admin service account and the SAP HANA backup/restore users below as new configurations specific to this backup solution.

Create the new service account cv-admin. Configure it with HTTP authentication only. Assign vsadmin role permissions.

Run this command on your Amazon FSx for NetApp ONTAP cluster to create the service account:

`security login create \` `-vserver <SVM_NAME> \` `-user-or-group-name cv-admin\` `-application http \` `-authmethod password \` `-role vsadmin`

*Replace <SVM\_NAME> with your production SVM name (for example, prod-hana-svm).*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/6114fd2c-a68f-40c6-bf3c-61647b41f173.png)

**HANA backup and restore users: **Commvault uses the HANA Backup User to connect to the HANA SYSTEMDB. The HANA Backup User triggers a database save point and initiates BACKINT log backups. It also updates the backup catalog before an Amazon FSx for NetApp ONTAP snapshot is taken. The HANA Restore User is used to stop and start HANA services. It restores data through BACKINT. It also performs database recovery using the snapshot and log backups.

**BACKUP\_USER permissions:**
+ BACKUP ADMIN
+ DATABASE BACKUP ADMIN
+ CATALOG READ
+ INIFILE ADMIN

**RESTORE\_USER permissions:**
+ BACKUP ADMIN
+ DATABASE BACKUP ADMIN
+ DATABASE RECOVERY OPERATOR
+ CATALOG READ
+ INIFILE ADMIN
+ DATABASE START
+ DATABASE STOP
+ TRACE ADMIN
+ SERVICE ADMIN

##### Step 2: Install NetApp IntelliSnap agent on HANA instances
<a name="step-2-install-netapp-intellisnap-agent-on-hana-instances"></a>

1. Log in to [store.commvault.com](https://store.commvault.com) and download the Linux Platform Commvault Media Kit.

1. Upload the Linux package to an S3 bucket, then download it from there onto the EC2 instances running SAP HANA.

1. Extract the downloaded archive so you have the installer files in a working directory on the host.

1. Move into the package location where the installer resides and launch the silent (non-interactive) installation.

1. Once the package is installed, register the HANA client with the CommServe so the client is recognized and managed by the backup environment.

1. Restart the Commvault agent service so it picks up the new configuration and comes online:

##### Step 3: Configure SnapMirror relationship
<a name="step-3-configure-snapmirror-relationship"></a>

Create volumes on backup Amazon FSx for NetApp ONTAP matching the size of production FSx for ONTAP volumes. Establish the following peer relationships so SnapMirror replicates the snapshot to the backup account.

Run cluster peer on backup Amazon FSx for NetApp ONTAP (destination) with a new passphrase: *Run this command on your backup FSx cluster to initiate the cluster peer:*

`cluster peer create -address-family ipv4 \` `-peer-addrs <peer_clusterIP_1>,<peer_clusterIP_2>` *Replace <peer\_clusterIP\_1> and <peer\_clusterIP\_2> with your production FSx cluster IPs. Also provide a passphrase when creating the cluster peer.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/d528d595-a261-4d8a-a86c-bcc90b698620.png)

 Run cluster peer on production FSx (source) with the same passphrase:

*Run this command on your production FSx cluster to create the cluster peer:*

`cluster peer create -address-family ipv4 \` `-peer-addrs <peer_clusterIP_1>,<peer_clusterIP_2>` *Replace <peer\_clusterIP\_1> and <peer\_clusterIP\_2> with your backup FSx cluster IPs. Provide the passphrase you created in backup FSx cluster.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/ffe14b76-18e1-49c8-9758-e3a56d5882f0.png)

Verify cluster peer is established:

*Run this command on your production FSx cluster to check if cluster peer is showing Available:*

`cluster peer show`

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/fd78f56b-0f01-40d9-8ce9-15fbdc6c0c67.png)

 Setup vserver peer relationship on backup FSx (destination):

*Run this command on your backup FSx cluster to initiate the vserver peer:*

`vserver peer create -vserver <destination_SVM> \ -peer-vserver <source_SVM> \ -peer-cluster <source_FSxID> \ -applications snapmirror`

*Replace <destination\_SVM>, <source\_SVM> and <source\_FSxID> with your backup FSx SVM name, production FSx for ONTAP SVM name and production FSx ID respectively.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/40f451b0-2bdf-4fc4-bf11-cb274d2d747d.png)

 Accept vserver peer relationship on production FSx (source):

*Run this command on your production FSx cluster to accept vserver peer:* `vserver peer accept -vserver <source_SVM> \ -peer-vserver <destination_SVM>`

*Replace <source\_SVM> and <destination\_SVM> with your production FSx SVM name and backup FSx for ONTAP SVM name respectively.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/23a58351-71fc-419e-8fe8-0701344821d2.png)

Verify vserver peer is established:

*Run this command on your production FSx cluster to verify if vserver peer is in peered status:* `vserver peer show`

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/a6b2b4b1-0d26-482f-adfd-92d4905bac9d.png)

Create snapmirror relationship on backup FSx (destination):

*Run this command on your backup FSx cluster to create snapmirror:* `snapmirror create -type XDP \ -source-path <source_SVM>:<source_volume> \ -destination-path <destination_SVM>:<destination_volume>`

*Replace <source\_SVM>, <source\_volume>, <destination\_SVM> and <destination\_volume> with your production FSx SVM name, production FSx volume that needs to be replicated, backup FSx for ONTAP SVM name and destination volume name on backup FSx respectively.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/94d3ae9c-e5d1-4843-bc88-af546487375b.png)

Initialize snapmirror on backup FSx (destination):

*Run this command on your backup FSx cluster to initialize snapmirror:* `snapmirror initialize -destination-path <destination_SVM>:<destination_volume>`

*Replace <destination\_SVM> and <destination\_volume> with your backup FSx SVM name and destination volume name on backup FSx respectively.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/00ee2b45-0523-47a0-a062-2461baa5ab49.png)

Verify snapmirror relationship status:

*Run this command on your backup FSx cluster to check the status of snapmirror:* `snapmirror show`

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/b78d8948-c36c-4931-8df6-b796aecbb1a4.png)

##### Step 4: Configure Commvault CommServe
<a name="step-4--configure-commvault-commserve.40fc8238-2815-5768-be3e-ebc4ca1114de"></a>

This step involves two main stages. First, integrate the underlying Amazon FSx for NetApp ONTAP storage as an array client. Second, you define a plan (policy) that includes both primary and secondary snap copies.

##### Step 4.1: Commvault steps to configure Amazon FSx for NetApp ONTAP backup
<a name="step-4.1--commvault-steps-to-configure-amazon-fsx-for-netapp-ontap-backup.9df52fcd-3482-58da-b597-cfecad433c5d"></a>

You configure the Amazon FSx for NetApp ONTAP SVM as a NetApp Snap Array client. This provides IntelliSnap operations.

##### Add the snap array
<a name="add-the-snap-array.877dec7a-0ab3-5900-bcfe-aff9b62d4a6b"></a>

Navigate to the Commvault Command Center, selecting **Manage > Infrastructure** and then clicking **Arrays**. On the Arrays page, clicking **Add** opens the configuration wizard.

On the General page of the wizard:
+ **Snap vendor:** Select NetApp
+ **Array name:** Enter the FQDN or IP address of the prod-hana-svm (Source). The system must verify that this name resolves consistently across all Commvault components.
+ **Credentials:** Select or add the cv-admin established in Step 1. Adding credentials involves specifying the Credential Name, the User account cv-admin, and the Password in the Add Credential dialog box.

##### Configure Array Access Nodes
<a name="configure-array-access-nodes.fe140db6-3391-5c9a-800d-c027c6e1cff6"></a>

Upon clicking **Next**, the **Array Access Nodes** page appears. Select the Commvault MediaAgents designated as Linux Access Nodes for the SAP HANA host from the available list. These access nodes send management commands to the ONTAP CLI. They also perform necessary metadata collection during the IntelliSnap process.

##### Configure snap configurations
<a name="configure-snap-configurations.b0d0cb18-7019-5f07-bcee-9d0965d8b69c"></a>

The final step in the wizard involves configuring the Snap Configurations. Confirm that you correctly linked the Source and Destination SVMs within the array context. This allows Commvault to recognize the SnapMirror infrastructure established in Step 3.

##### Step 4.2: Create backup policy for Amazon FSx for NetApp ONTAP snapshot backup on Commvault
<a name="step-4.2--create-backup-policy-for-amazon-fsx-for-netapp-ontap-snapshot-backup-on-commvault.b2dc205b-0ab3-5034-b5f6-006bbebae85a"></a>

 A backup plan in Commvault defines the data retention structure for the SAP HANA data volumes. It also defines the replication structure.

##### Create a new backup plan
<a name="create-a-new-backup-plan.e9d621b4-b557-55bb-9115-88b2e7f5accf"></a>

Navigate to **Manage > Plans** and select **Create plan > Backup**. Assign a descriptive name, such as HANA\_IntelliSnap\_Backup.

##### Define storage policies (primary snap copy)
<a name="define-storage-policies--primary-snap-copy-.2363209a-a42f-53bc-9eab-5ea62507e6bd"></a>

In the Storage Policies section, define the primary snapshot target. Click **Add Snap copy.** This opens the configuration dialog:
+ **Name:** Primary\_HANA\_Snap
+ **Storage:** Select the storage associated with the Source Amazon FSx for NetApp ONTAP Array (prod-hana-svm)
+ **Retention rules:** Snapshots are array-based and short-term. Retention is often set by the Number of snap recovery points (e.g., 7 recovery points). The primary storage retains only the latest snapshots.

##### Define the secondary mirror copy (SnapMirror integration)
<a name="define-the-secondary-mirror-copy--snapmirror-integration-.c9b836f6-487e-5086-86f8-51151b244743"></a>

Add a second Snap copy to establish the DR copy. Set Copy Type to Mirror.
+ **Name:** Secondary\_HANA\_Mirror
+ **Source:** Select the primary snapshot copy (Primary\_HANA\_Snap)
+ **Copy Type:** Select Mirror
+ **Provide NetApp SnapMirror Cloud Target:** This toggle must be moved to the right. Activating the NetApp SnapMirror Cloud Target toggle delegates physical data movement to the pre-configured SnapMirror relationship
+ **Storage:** Select the storage associated with the Destination Amazon FSx for NetApp ONTAP Array (backup-hana-svm)
+ **Backups to copy:** Define which backup types trigger the Mirror Copy update. For example, Full IntelliSnap jobs. Since this is a mirror copy, the mirror copy automatically inherits retention rules from the source copy. This maintains synchronized retention across both sites

##### Subclient association
<a name="subclient-association.f2317a72-8fb4-58f0-8504-7ab6fde18560"></a>

Configure the SAP HANA instance within Commvault to use this plan. Select the relevant tenant database subclient. In the Snapshot management tile, activate the **Enable snap backup** toggle. Select the NetApp array engine configured in Step 4.1. This links the backup requirement to the defined storage policy.

##### Step 5: Configure Backint log backup strategy on Commvault
<a name="step-5-configure-backint-log-backup-strategy-on-commvault"></a>

Protecting SAP HANA data volumes with near-instantaneous snapshots reduces the data recovery window compared to traditional backup methods. However, point-in-time transactional consistency requires a dedicated strategy. This uses persistent log backups via the SAP Backint interface.

##### Step 5.1: Implementing persistent log backups
<a name="step-5.1--implementing-persistent-log-backups.5cd0cfa1-a6e9-5b9f-b71e-d31fb30f2bf2"></a>

SAP HANA generates a continuous stream of log files. You must protect these with high frequency.

##### Create log streaming storage policy
<a name="create-log-streaming-storage-policy.f94a8269-81cb-575f-aba7-f3348502490b"></a>

You configure a dedicated Commvault storage policy to transfer backup data to a centralized backup repository. This can be a MediaAgent disk meeting the minimum capacity requirement for the full SAP HANA data volume, log backups, and retention window. Alternatively, it can be a cloud storage library such as Amazon S3. This is distinct from the Amazon FSx for NetApp ONTAP snapshot destination.

##### Enable persistent log backup feature
<a name="enable-persistent-log-backup-feature.57e083b8-0b30-5900-848a-86a9004aa91d"></a>

Apply the nPersistentLogBackup setting to the SAP HANA client computer (EC2 instance) via the CommCell Console or Command Center interface. See Table 1.

|  |  |  |  |
| --- |--- |--- |--- |
| Sl. No | Property | Value | Purpose |
| 1 | Name | nPersistentLogBackup | Controls the persistent log feature |
| 2 | Category | SAPHanaAgent | Scope of the setting, targeting the HANA Agent |
| 3 | Type | Integer | Data type required for the setting |
| 4 | Value | 1 | Enables persistent log backup; Value 0 treats each log file as an independent backup job |

***Table 1:**** Persistent log backup configuration parameters*

##### Configure log backup destination
<a name="configure-log-backup-destination.30c09bfe-9c3b-5adf-9666-db65bbded874"></a>

The SAP HANA instance properties within Commvault must be explicitly configured. Direct the log stream to the dedicated log streaming storage policy created earlier in this step.

##### Step 5.2: Cohesion of snapshot and log protection
<a name="step-5.2--cohesion-of-snapshot-and-log-protection.e2cf1184-1b5f-5378-bf4d-5903171dedc3"></a>

Granular point-in-time recovery depends entirely on perfectly aligning the data snapshot and the log stream. When the IntelliSnap backup runs, it utilizes the SAP Backint interface to quiesce the database. This ensures the storage snapshot captures a consistent state that HANA can recover. This process records a synchronization point in the HANA catalog. During a restore operation, you orchestrate the recovery by initiating the Amazon FSx for NetApp ONTAP snapshot restore. The system then automatically applies the correct log file sequence from the stream-based storage location. This reaches the requested recovery point.

##### Step 6: Test and validate Amazon FSx for NetApp ONTAP snapshot backup
<a name="step-6-test-and-validate-amazon-fsx-for-netapp-ontap-snapshot-backup"></a>

The final phase involves testing to validate operational success. This confirms not only that the solution creates backups, but that you can achieve a full recovery. It confirms that the solution meets the defined 15-minute RTO and 5-minute RPO targets.

##### Step 6.1: Execution of a full IntelliSnap backup job
<a name="step-6.1--execution-of-a-full-intellisnap-backup-job.d8693795-17aa-5523-920a-f97c2aa98cff"></a>

Validation begins by executing a full IntelliSnap backup job. Confirm its successful completion through both the Commvault console and the storage array itself.

##### Initiate backup
<a name="initiate-backup.48ad0527-0974-57dd-82e4-bc4fe1bc36c8"></a>

Navigate to the SAP HANA instance, right-click the subclient, and select **Backup** > **Full**.

##### Commvault job verification
<a name="commvault-job-verification.4fdc168f-e64b-55bb-bbe7-1102f2ad2d34"></a>

Confirm that the Job Controller shows the job completes successfully and registers as an IntelliSnap operation. Verify the successful synchronization of the secondary SnapMirror copy (Mirror Copy) in the job details. This confirms the two-stage protection process (snapshot \+ replication).

##### Storage verification (source Amazon FSx for NetApp ONTAP CLI)
<a name="storage-verification--source-amazon-fsx-for-netapp-ontap-cli-.c69db1bf-8cd8-5412-b76e-1c2964a32a6a"></a>

Confirm the hardware snapshot layer by verifying its existence on the source volume, as described in the Backup Workflow Architecture: `volume snapshot show -vserver <source_SVM> -volume <source_volume>`

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/5afc393e-8dd3-4538-bcb4-5a5b62e2bd8a.png)

*Replace <source\_SVM> and <source\_volume> with your production FSx SVM name and production FSx volume that needs to be replicated.*

 A new snapshot entry bearing a Commvault tag must be present. It should correspond precisely to the job completion time.

##### Step 6.2: Validation of replication success
<a name="step-6.2--validation-of-replication-success.fa1fb1c6-8e5c-5b76-a792-353a3c7892a5"></a>

##### Mirror Copy job validation
<a name="mirror-copy-job-validation.b1c5dcf6-b255-5dde-84e8-cd874b2d7c54"></a>

Within the Commvault Plan configuration, check the status of the **Secondary\_HANA\_Mirror** copy. Confirm that the latest snapshot is synchronized and available. Any delays or failures here indicate a critical vulnerability in the DR strategy.

##### Storage verification (destination Amazon FSx for NetApp ONTAP CLI)
<a name="storage-verification--destination-amazon-fsx-for-netapp-ontap-cli-.bc12001d-468e-5655-a4f2-524c00c8e953"></a>

The SnapMirror relationship status (snapmirror show) on the destination cluster validates the infrastructure. Output of **Snapmirrored** or **Idle **confirms that SnapMirror successfully replicated the snapshot to the DR volume**.**

##### Step 6.3: Test restore workflow (recovery validation)
<a name="step-6.3--test-restore-workflow--recovery-validation-.dc0f99a9-2718-5610-b81e-2e8d93cc93a7"></a>

A successful test restore is the definitive validation of the solution's viability. The test restore validates the cohesion between the snapshot data and the separate log stream.

##### Perform a test restore from the Mirror Copy
<a name="perform-a-test-restore-from-the-mirror-copy.9642caaa-d2bf-54ee-a951-6304f97fca96"></a>

The recovery test simulates a DR event. It explicitly restores the database using the snapshot available on the Secondary\_HANA\_Mirror copy. This validates the disaster recovery configuration. Initiate the restore operation in Commvault. Select the necessary data and specify a different target SAP HANA instance or client. Selecting **Point-in-Time Recovery** is essential. Point-in-Time Recovery triggers Commvault's orchestration functions: it recovers the data volume from the SnapMirror target, then applies the appropriate log backups from the streaming storage repository.

During a DR scenario, SnapMirror eliminates full data streaming restoration, reducing recovery time. A single snapmirror break command via the ONTAP CLI converts the destination volume to read/write. This replaces the extended restoration window that traditional streaming recovery requires with an architecture-native failover operation.

##### Step 6.4: Post-restore verification
<a name="step-6.4--post-restore-verification.853954ff-6a2b-5042-870e-867c57243a70"></a>

Verify that the recovered SAP HANA database starts successfully and you can access it via HANA Studio. Verify transaction data to confirm that you achieved the precise recovery point. This validates the end-to-end data integrity from IntelliSnap to SnapMirror to Backint logs.

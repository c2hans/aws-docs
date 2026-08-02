---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-vmware-ec2-migration-aws-transform.html
---

# Automate VMware-to-Amazon EC2 migration by using the AWS Transform agentic workflow
<a name="automate-vmware-ec2-migration-aws-transform"></a>

*Deepak Kumar, Femi Alabi, and Monowar Chowdhury, Amazon Web Services*

## Summary
<a name="automate-vmware-ec2-migration-aws-transform-summary"></a>

This pattern describes how to migrate on-premises VMware virtual machines (VMs) to Amazon Elastic Compute Cloud (Amazon EC2) by using AWS Transform. AWS Transform uses generative AI to orchestrate and automate the end-to-end migration process, including discovery, network conversion, wave planning, and server rehosting through AWS Transform MGN (formerly AWS Application Migration Service). The pattern covers migrating Windows and Linux servers from an on-premises VMware vSphere environment to Amazon EC2 instances. This pattern focuses on single-account migration, where each job migrates servers to one target AWS account. By using AI-driven automation for traditionally manual tasks such as dependency mapping, application grouping, and migration wave sequencing, this approach reduces migration complexity, time, and risk.

## Prerequisites and limitations
<a name="automate-vmware-ec2-migration-aws-transform-prereqs"></a>

**Prerequisites**
+ An active AWS account with AWS Organizations configured.
+ [AWS IAM Identity Center set up to provide federated access to the AWS Transform web experience.](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html)
+ [A designated discovery account within your AWS organization to store discovery data collected during migration.](https://docs.aws.amazon.com/application-discovery/)
+ [A designated target account within your AWS organization where migrated Amazon EC2 instances will be deployed for this job.](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-connect-target-account.html)
+ Network connectivity between your on-premises VMware environment and AWS (such as [AWS Direct Connect](https://aws.amazon.com/directconnect/) or [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)).
+ Network infrastructure (VPCs, subnets, and security groups) deployed in the target account, either through [AWS Transform network](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network.html) migration or provisioned independently.
+ Access to one of the following [discovery data](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) sources:
+ [AWS Application Discovery Service Agentless Collector deployed in your VMware environment.](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector.html)
+ [The open-source Export for vCenter tool for exporting VM inventory.](https://github.com/awslabs/export-for-vcenter)
+ A manually prepared inventory file with server details in the required format.
+ Administrative access to VMware vCenter Server.
+ Credentials (SSH keys for Linux, WinRM credentials for Windows) for source servers if using automated agent deployment through the MGN connector.

**Limitations**
+ This pattern focuses on single-account migration, where each job migrates servers to one target AWS account. AWS Transform also supports multi-account migration within a single job, but that is outside the scope of this pattern.
+ You can specify one target AWS Region per VMware migration job. To migrate to different target Regions, create separate jobs.
+ Only one inventory import per target account and AWS Region can run at a time. If multiple waves target the same account and Region, imports must be serialized.
+ Only x86 servers are supported. ARM-based servers are not supported.
+ The MGN connector’s AWS Systems Manager Hybrid Activation expires after 30 days. If you need to install the connector on a new machine after expiration, create a new connector.
+ If you stop a running migration job and restart it, the job starts from the beginning and you lose progress. Artifacts created before restarting remain available.
+ AWS Transform supports all AWS commercial Regions as migration targets, excluding: Middle East (Bahrain) and Middle East (UAE)
+ Some AWS services aren't available in all AWS Regions. For Region availability, refer to [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, refer to the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ VMware vSphere 6.5 or later
+ Windows Server 2012 R2 or later
+ Red Hat Enterprise Linux (RHEL) 7.x or later
+ Ubuntu 16.04 or later
+ SUSE Linux Enterprise Server 12 SP5 or later
+ CentOS 7.x or later

For the complete list of supported operating systems, see [Supported operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html) in the AWS Transform MGN documentation.

## Architecture
<a name="automate-vmware-ec2-migration-aws-transform-architecture"></a>

**Source technology stack **
+  On-premises VMware vSphere environment (ESXi hosts, vCenter Server)
+  Virtual machines running Windows or Linux operating systems
+  VMware virtual networking (vSwitches, port groups, distributed switches)
+  VMware storage (Virtual Machine File System, (VMFS), vSAN, NFS datastores)

**Target technology stack **
+  Amazon EC2 instances running natively on AWS
+  Amazon VPC with subnets and security groups
+  Amazon Elastic Block Store (Amazon EBS) for persistent block storage
+  AWS Transform MGN for block-level replication and server rehosting
+  AWS Transform for AI-driven migration orchestration
+  AWS Systems Manager for connector communication and management
+  AWS Secrets Manager for source server credential storage

**Target architecture **

The following diagram shows the high-level AWS Transform VMware migration architecture.

1.  AWS Transform provides a collaborative web workspace where you create and manage the migration job through a chat-based interface.

1.  Discovery data is collected from your on-premises VMware environment using the Agentless Collector, Export for vCenter, or a manual import, and stored in the discovery account.

1.  AWS Transform uses AI to convert your VMware network configuration into an Amazon VPC architecture and generates a migration plan with application grouping and wave assignments.

1.  AWS Replication Agents installed on source servers continuously replicate block-level data to staging area replication servers in the target account.

1.  During testing and cutover, AWS Transform MGN launches Amazon EC2 instances from the replicated data in the target VPC.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7965c128-970b-4482-a730-1e4fdd849dfe/images/56c10889-8ef6-40c0-b5c1-4fdf8862d638.png)

**Automation and scale**
+  AWS Transform provides a chat-based interface where you interact with AI agents using natural language prompts to drive each migration step.
+  The MGN connector automates replication agent deployment across multiple source servers using SSH (Linux) and WinRM (Windows), eliminating the need for manual per-server installation.
+  You can reuse a configured connector across multiple migration waves and across different jobs.
+  For large-scale migrations, organize servers into waves and migrate iteratively. Each wave progresses independently through the migration lifecycle.

## Tools
<a name="automate-vmware-ec2-migration-aws-transform-tools"></a>

**Tools**

AWS services
+  [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) – Provides AI-driven orchestration for the end-to-end migration lifecycle through a chat-based web experience. You interact with the service using natural language prompts, and it guides you through discovery, network conversion, wave planning, and server rehosting. There is no additional charge for using AWS Transform.
+  [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html) – (formerly AWS Application Migration Service). Performs continuous block-level replication from source servers to AWS and manages the test and cutover lifecycle. You can use AWS Transform MGN directly through its console or through the AWS Transform agentic workflow.
+  [AWS Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) – Discovers on-premises server inventory and collects utilization data through the Agentless Collector.
+  [Amazon EC2](https://docs.aws.amazon.com/ec2/) – Provides the target compute instances for migrated workloads.
+  [Amazon VPC ](https://docs.aws.amazon.com/vpc/)– Provides the network isolation and segmentation for migrated servers.
+  [AWS Organizations](https://docs.aws.amazon.com/organizations/) – Manages the multi-account structure (discovery account, target accounts).
+  [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/) – Provides federated access to the AWS Transform web experience.
+  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/) – Enables secure communication between the MGN connector and AWS through Hybrid Activations and SSM documents.
+  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/) – Stores source server credentials used by the MGN connector for automated agent deployment.
+  [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/) – Deploys IAM roles and VPC infrastructure as part of the migration setup.

Other tools
+  [Export for vCenter](https://github.com/awslabs/export-for-vcenter) – An open-source tool that exports VM inventory data from VMware vCenter for use with AWS Transform discovery.
+  [Import/Export for NSX](https://github.com/awslabs/import-export-for-nsx) – An open-source tool that exports VMware NSX network and firewall rule configurations for translation into AWS VPC security groups.

## Best practices
<a name="automate-vmware-ec2-migration-aws-transform-best-practices"></a>
+  Conduct a thorough pre-migration assessment, including application dependency mapping and performance baselines, to ensure accurate wave planning.
+  Use the Agentless Collector or Export for vCenter for automated discovery rather than manually preparing inventory files.
+  Start with a pilot wave of 5–10 non-critical servers to validate the migration process before scaling to production workloads.
+  Use separate AWS accounts for discovery and target deployment in production migrations.
+  Tag all VPC resources (subnets, security groups) in the target account with CreatedBy: AWSTransform and ATWorkspace: <workspace\_id> before starting server migration.
+  Use static IP assignment when applications depend on fixed IP addresses, and configure CIDR transformation if the target subnet uses a different address range.
+  Schedule cutover windows during low-traffic periods to minimize the impact of downtime between source shutdown and cutover instance availability.
+  After successful cutover and verification, finalize the cutover promptly to stop replication and free up source server quota.
+  Use temporary IAM credentials (via via AWS STS AssumeRole) rather than permanent access keys when manually installing replication agents. (Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation).
+  If migrating Active Directory, launch AD servers first in the wave and verify they are running before launching dependent servers.

## Epics
<a name="automate-vmware-ec2-migration-aws-transform-epics"></a>

### Set up the AWS Transform workspace and job
<a name="set-up-the-aws-transform-workspace-and-job"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a workspace in AWS Transform | Sign in to the AWS Transform web application using your IAM Identity Center credentials. On the workspace landing page, provide a meaningful workspace name related to your migration project (for example, VMware-DC1-Migration). Optionally invite collaborators by selecting the \+ icon and assigning roles (administrator, approver, contributor, or view only). | Cloud administrator |
| Create a VMware migration job | In the workspace, choose Create a job. In the chat interface, type VMware to select the VMware migration option. Choose End-to-end migration as the job type. Optionally rename the job by typing a name (for example, VMW-to-EC2 Job \#1). Confirm by typing yes, then choose Create job. AWS Transform generates a step-by-step job plan. | Cloud administrator, Migration lead |
| Connect the discovery account | In the Connect AWS account for on-premises discovery task, enter the AWS account ID for your discovery account. Choose Create Connector, then choose Send to transform. Sign in to the discovery account and approve the connection request using the verification link provided. Verify that the connector status shows Approved in the AWS Transform chat. | Cloud administrator |
| Connect the target account | In the Connect target account task, enter the AWS account ID for the target account for this job and select region. Choose Create Connector. Next, sign in to the target account and approve the connection request. Once the connector request is approved, return to AWS Transform and submit the request. | Cloud administrator |

### Discover the on-premises environment
<a name="discover-the-on-premises-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload discovery data (Option A: RVTools/Export for vCenter) | In the Perform discovery step, choose Choose ZIP file and upload a ZIP archive containing your CSV export from RVTools or the Export for vCenter tool. Choose Send to transform. AWS Transform imports the data and displays a summary with the total number of discovered servers. Review the summary and choose Continue with existing data, then choose Send to transform. | Migration engineer, VMware administrator |
| Use Agentless Collector (Option B: Automated discovery) | In the Perform discovery step, select the Agentless Collector option. Deploy the Application Discovery Service Agentless Collector OVA in your VMware environment. Configure the collector with IAM credentials for the discovery account and connect it to your vCenter Server. AWS Transform automatically identifies the discovered data from the collector. | Migration engineer, VMware administrator |
| Review discovery results | AWS Transform displays the list of discovered servers. Optionally export the server list to compare against your source data. If AWS Transform cannot generate application groupings for all servers, it provides options to collect additional data. Confirm the discovery results to proceed. | Migration engineer |

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the wave plan | AWS Transform provides a wave plan template file. Choose Download file to download it. The file is pre-populated with application names and suggested waves if you used the Agentless Collector. If you used RVTools, manually fill in the application name and wave for each VM. Remove servers that are out of scope from the file. Upload the modified file by choosing Choose file, then choose Send to transform. | Migration lead |
| Configure network migration | AWS Transform generates an AI-driven VPC architecture based on your VMware network configuration. Review the proposed VPC, subnet, and security group mappings in the human-in-the-loop (HITL) review. Approve or request modifications through the chat interface. AWS Transform deploys the network infrastructure in the target account using CloudFormation. | Cloud architect, Network engineer |
| Configure migration defaults | AWS Transform presents EC2 recommendation preferences, replication settings, and launch template parameters. Review the defaults in the HITL review or modify them through the chat interface. These settings apply to the target account and are inherited by all waves. Override specific settings at the wave level if needed. | Migration engineer |

### Migrate servers
<a name="migrate-servers"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the migration wave | Select the wave to migrate. AWS Transform confirms the target account configured in the connector. The service verifies resource tagging and displays any untagged resources for you to tag. Add networking data to the inventory. Configure replication and launch settings through the HITL review or chat interface. Choose the IP assignment strategy (static or dynamic). | Migration engineer |
| Validate and confirm the inventory | AWS Transform prepares the inventory file for review. Download it in CSV or XLSX format. Review server configurations, Amazon EC2 instance type recommendations, target subnets, security groups, and licensing options (BYOL or License Included). Modify as needed and upload the final version. Choose Send to transform to confirm. AWS Transform MGN creates source server records in the target account. | Migration engineer |
| Deploy replication agents | Choose a deployment method when prompted in the chat: 1. MGN connector for automated deployment — set up the connector on a dedicated Linux machine, configure source server credentials in AWS Secrets Manager, and AWS Transform deploys agents automatically. 2. Organization tools (such as Ansible or SCCM) — AWS Transform provides the installation commands with silent-install parameters. 3. Manual installation — AWS Transform provides per-server installation commands with the --user-provided-id parameter.  | Migration engineer, Systems administrator |
| Monitor data replication | AWS Transform monitors replication progress and provides status updates in the chat, including replication status, replication lag, and bandwidth usage. Verify all servers progress from Not ready to Ready for testing. You can pause, resume, or stop replication for individual servers or the entire wave through the chat interface. | Migration engineer |
| Test migrated instances | When prompted, choose to launch test instances for the entire wave or select specific servers by providing their user-provided IDs. AWS Transform launches Amazon EC2 instances and provides instance IDs. Connect to test instances and validate application functionality, network connectivity, and performance. After validation, choose to terminate test instances and mark applications as ready for cutover. | Migration engineer, Systems administrator |
| Perform cutover | Schedule a cutover window during a low-traffic period. Choose to launch cutover instances for the entire wave or selected servers. AWS Transform launches EC2 instances from the latest replicated data and provides instance IDs. Verify cutover instances are functioning correctly. Finalize the cutover through the chat interface — this stops replication and removes agents from source servers. Optionally archive source servers to free quota. | Migration engineer, Application owner |

## Troubleshooting
<a name="automate-vmware-ec2-migration-aws-transform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| MGN connector deployment fails with credential errors | Verify that the credentials stored in AWS Secrets Manager match the required JSON format. For Linux servers, ensure the SSH private key is correctly formatted. For Windows servers, confirm that WinRM is enabled and the provided credentials have administrative access. See MGN connector credentials ([https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-credentials.html](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-credentials.html)). |
| Replication agent installation fails on source servers | Confirm outbound HTTPS (port 443) connectivity from source servers to the AWS Transform MGN endpoint in your target Region. Verify the source server meets minimum requirements (supported OS, available disk space). Confirm the IAM credentials have the AWSApplicationMigrationAgentInstallationPolicy managed policy attached. |
| Servers remain in "Not ready" state for an extended period | Check the replication lag and available network bandwidth between on-premises and AWS. Verify the staging area subnet has sufficient IP capacity and that replication server instances can launch. Review the AWS Transform MGN console for detailed error messages. |
| Test instance fails to boot or application errors occur | Verify the correct Amazon EC2 instance type is assigned (CPU and memory match source requirements). Check that security groups allow required inbound and outbound traffic. Ensure boot-time drivers are compatible with the target instance family. |
| AWS Transform cannot discover a connected account | Verify both the discovery and target accounts are in the same AWS Organizations organization. Ensure the connector acceptance was completed with the correct IAM permissions. Check that the connector status shows Approved in the AWS Transform console. |
| Network infrastructure tagging errors during wave setup | Tag all VPCs, subnets, and security groups in the target account with **CreatedBy: AWSTransform** and **ATWorkspace: <workspace\_id>**. VPCs and subnets created by AWS Transform network migration are tagged automatically. |

## Related resources
<a name="automate-vmware-ec2-migration-aws-transform-resources"></a>

**References**
+ [https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html)
+ [https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware.html](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware.html)
+ [https://docs.aws.amazon.com/transform/latest/userguide/vmware-jobs.html](https://docs.aws.amazon.com/transform/latest/userguide/vmware-jobs.html)** **
+ [https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html)
+ [https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html)
+ [https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)
+ [https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)
+ [https://aws.amazon.com/transform/faq/](https://aws.amazon.com/transform/faq/) **Blog posts and announcements**
+ [https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-mgn-rebrand/](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-mgn-rebrand/)
+ [https://aws.amazon.com/about-aws/whats-new/2025/05/aws-transform-vmware-generally-available/](https://aws.amazon.com/about-aws/whats-new/2025/05/aws-transform-vmware-generally-available/)
+ [https://aws.amazon.com/blogs/migration-and-modernization/simplify-server-migration-to-aws-with-aws-transform-for-vmware/](https://aws.amazon.com/blogs/migration-and-modernization/simplify-server-migration-to-aws-with-aws-transform-for-vmware/)
+ [https://aws.amazon.com/blogs/migration-and-modernization/exporting-network-configuration-data-with-import-export-for-nsx/](https://aws.amazon.com/blogs/migration-and-modernization/exporting-network-configuration-data-with-import-export-for-nsx/)

## Additional information
<a name="automate-vmware-ec2-migration-aws-transform-additional"></a>
+ There is no additional charge to use AWS Transform. You pay only for the underlying AWS resources consumed during migration (Amazon EC2 instances, Amazon EBS volumes, data transfer).
+ This pattern focuses on single-account migration, where each job migrates servers to one target AWS account. AWS Transform also supports multi-account migration within a single job, where servers can target different accounts using the mgn:account-id column in the inventory file. For multi-account guidance, refer to [Migrate servers with AWS Transform.](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html)
+ AWS Transform supports multiple migration job types: end-to-end migration, discovery and migration planning, network migration, landing zone, landing zone with network and server migration, and migration planning with server migration. This pattern covers the end-to-end migration job type. You can dynamically add or remove steps from any job type at any time.
+ You can access AWS Transform MGN in two ways: directly through the MGN console for hands-on control, or through the AWS Transform agentic workflow for automated orchestration. At the rehosting stage, you can switch between these two access methods at any time.
+ AWS Transform uses a chat-based interface where you interact with AI agents using natural language. The service provides human-in-the-loop (HITL) reviews for critical configuration decisions such as network architecture, launch templates, and replication settings. You can configure settings through the HITL pages or directly through the chat.
+ Downtime during cutover is limited to the period between shutting down the source VM and the cutover EC2 instance becoming available. Continuous block-level replication minimizes data loss during this window.
+ For VMware NSX environments, use the [Import/Export for NSX tool to export network and firewall configurations](https://github.com/awslabs/import-export-for-nsx) before starting network migration in AWS Transform.
+ AWS Transform MGN retains all compliance certifications including FedRAMP High, HIPAA, PCI DSS, ISO, and SOC 1, 2, and 3. It is available in all commercial AWS Regions and both GovCloud (US) Regions.
+ A workspace can have up to ten VMware connectors (five discovery connectors and five infrastructure provisioning connectors).

## Attachments
<a name="attachments-7965c128-970b-4482-a730-1e4fdd849dfe"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/7965c128-970b-4482-a730-1e4fdd849dfe/attachments/attachment.zip)

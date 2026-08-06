---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx.html
---

# Deploy SQL Server failover cluster instances on Amazon EC2 and Amazon FSx by using Terraform
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx"></a>

*Mark Hudson and Matt Burgess, Amazon Web Services*

## Summary
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-summary"></a>

This pattern uses Terraform to deploy SQL Server failover cluster instances (FCIs) across Windows Server Failover Cluster (WSFC) nodes on Amazon Elastic Compute Cloud (Amazon EC2). In addition, the pattern uses Amazon FSx shared storage for data and log files.

When SQL Server databases are migrated to AWS, the first choice is Amazon RDS for SQL Server. However, sometimes Amazon RDS for SQL Server isn’t suitable and SQL Server must be deployed on Amazon EC2 in a highly available architecture. In this solution, SQL Server FCIs are installed across WSFC nodes.

The Terraform module included with this pattern provisions up to two Amazon EC2 SQL Server instances. An Amazon FSx for Windows File Server file system acts as the quorum witness and stores shared data and log files. Regardless of the number of instances configured, the SQL Server instance nodes will always create and join an FCI cluster to ensure environmental parity. (Typically, one instance is configured for development and two instances for production environments.) For configurations that use two nodes for high availability, an internal Network Load Balancer is provisioned. The Network Load Balancer uses a health probe configured on the FCI cluster to identify which node is the primary.

## Prerequisites and limitations
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Amazon Virtual Private Cloud (Amazon VPC) with two subnets in separate Availability Zones.
+ Amazon VPC [DHCP option set](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html). Configure the domain name to resolve to your Active Directory domain name and the domain and NetBIOS name servers to point to your Active Directory domain controllers. For more information, see *VPC configuration* in [Additional information](#deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-additional).
+ AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD).
+ Custom Amazon Machine Image (AMI). For more details, see *AMI configuration* in [Additional information](#deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-additional).
+ Amazon Simple Storage Service (Amazon S3) bucket containing the SQL Server ISO image. This prerequisite is only required if using [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) with the provided `component.yaml` file to build the custom AMI.
+ AWS Key Management Service (AWS KMS) encryption key.
+ By default, SQL Server is installed using a developer edition product key. Production systems are expected to use a valid product key passed to the module by the relevant variable.

**Limitations**
+ This solution requires AWS Managed Microsoft AD. However, if you prefer, you can use a self-managed Active Directory implementation instead. To do so, modify the included Amazon FSx Terraform module to remove the `active_directory_id` attribute. Then, add the four attributes that are required for self-managed Active Directory as shown in the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/fsx_windows_file_system).
+ SQL Server is set up to use mixed mode authentication. If you prefer, you can use Windows-only authentication. To do so, in the provided user data script, remove the `/SECURITYMODE` and `/SAPWD` parameters that are supplied to the `setup.exe` command. You can remove the `sql_accounts.tf` file, and you can modify the `instances.tf` file to remove the `sql_sa_password` entry.
+ When deleting a deployed cluster, you must remove the corresponding virtual computer objects and individual computer objects in Active Directory. To remove the objects, use Active Directory administrative tools.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**

This solution was tested with the following versions:
+ Windows Server 2019
+ SQL Server 2019
+ [Terraform v0.13.0](https://developer.hashicorp.com/terraform/language/v1.1.x/upgrade-guides/0-13)

## Architecture
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-architecture"></a>

**Source technology stack**
+ SQL Server

**Target technology stack**
+ SQL Server FCI on WSFC nodes using Amazon EC2
+ Amazon FSx for Windows File Server
+ Amazon S3 bucket
+ AWS Secrets Manager
+ AWS Managed Microsoft AD
+ AWS KMS
+ AWS Identity and Access Management (IAM)

**Target architecture**

The following diagram shows the architecture for this solution.

![Architecture to deploy SQL Server failover cluster instances across Windows Server Failover Cluster nodes on Amazon EC2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/45f3ab19-d240-4353-ab6e-f6e565f537a4/images/0bff16f2-94e7-4e86-91ea-7ab5f3725620.png)

The diagram shows the following:
+ An IAM role providing the EC2 instances access to AWS KMS and Secrets Manager
+ Two SQL Server nodes deployed on Amazon EC2 instances in private subnets across two Availability Zones
+ A Network Load Balancer for facilitating connections to the active SQL Server instance (not deployed when setting up a single node cluster)
+ Amazon FSx for Windows File Server file system deployed in both private subnets for shared storage by the SQL Server nodes
+ Secrets Manager for storing Active Directory and SQL Server credentials and configuration
+ Amazon S3 bucket for storing the SQL Server installation image
+ AWS Managed Microsoft AD for Windows authentication
+ AWS KMS for creating the encryption key

**Automation and scale**

You can automate the deployment of the target architecture by using the Terraform modules that are in the [GitHub repository](https://github.com/aws-samples/cluster-amazon-elastic-compute-cloud-amazon-fsx-microsoft-sql-server). You must modify the `terraform.tfvars` file to include variable values that are specific to your environment. The Amazon S3 bucket, AWS Managed Microsoft AD components, AWS KMS encryption key, and some secrets are prerequisites for this deployment and are not included in the Terraform code.

## Tools
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-tools"></a>

**AWS services**
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud. In this pattern, AWS Managed Microsoft AD is used for Windows Server and SQL Server authentication and for DNS.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down. In this pattern, SQL Server failover cluster instances are installed on Amazon EC2 instances.
+ [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) helps you automate the creation, management, and deployment of customized server images.
+ [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) provides fully managed shared storage on Windows Server. In this pattern, FSx for Windows File Server provides shared storage for SQL Server data and log files and the quorum witness.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data. In this pattern, it’s used to encrypt Secrets Manager secrets, the SQL Server storage on Amazon Elastic Block Store (Amazon EBS) volumes, and the FSx for Windows File Server file system.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. In this pattern, Active Directory credentials for installing and running SQL Server, the `sa` user credentials, and the database connection information are stored in Secrets Manager.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. This pattern uses an Amazon S3 bucket to store the SQL Server installation image.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

** ****Other tools**
+ [Microsoft SQL Server FCIs](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/always-on-failover-cluster-instances-sql-server?view=sql-server-ver15) are installed across Windows Server cluster nodes. In addition, they can be installed across multiple subnets. In this pattern, SQL Server FCI instances are installed across WSFC nodes.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources. In this pattern, Terraform is used to create the resources and configure the SQL Server FCI instances.
+ [Windows Server Failover Clustering](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/windows-server-failover-clustering-wsfc-with-sql-server?view=sql-server-ver15) provides infrastructure features that support the high-availability of hosted server applications such as SQL Server. In this pattern, the FCI nodes make use of WSFC functionality to provide local high availability through redundancy at the instance level.

**Code repository**

The code for this pattern is available in the GitHub [cluster-amazon-elastic-compute-cloud-amazon-fsx-microsoft-sql-server](https://github.com/aws-samples/cluster-amazon-elastic-compute-cloud-amazon-fsx-microsoft-sql-server) repository. The following resources are available in the repository:
+ A `README.md` file that provides an overview of the solution and additional installation and usage information
+ A base set of Terraform configuration files and an Amazon FSx specific module to provision the components for this pattern
+ An instance setup script that is run as an Amazon EC2 user data script
+ A `component.yam`l file that Image Builder can use to create a custom AMI

## Best practices
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-best-practices"></a>

**Security and patching**
+ The AMI prerequisite installations and configurations are the minimum requirements to deploy SQL Server FCI clusters. Additional software and configurations might be required to comply with your organization’s standards and security requirements.
+ After deployment, patch Windows on an ongoing basis. Either directly patch the running instances, or create a new AMI with the latest Windows patches and replace the instances (one at a time) using the new AMI. AWS releases new Windows AMIs monthly that contain the latest operating system patches, drivers, and launch agents. We recommend that you check for the latest AMI when you launch new instances, or when you build your own custom images.
+ The Amazon EC2 instances are configured to allow all outgoing traffic. When deployed in a production environment, outbound rules in the security group should be put in place to restrict this traffic to the required destinations.
+ The FSx for Windows File Server file system can automatically record audit logs for file share and file and folder access and ship them to your desired destination if this is a requirement in your environment.
+ Rotate Secrets Manager secrets automatically on a regular basis. For the Amazon EC2 instance key pair, consider an automated rotation solution as described in [How to use AWS Secrets Manager to securely store and rotate SSH key pairs](https://aws.amazon.com/blogs/security/how-to-use-aws-secrets-manager-securely-store-rotate-ssh-key-pairs/). For the Active Directory credentials and SQL Server `sa` credential secrets, set up automated rotation according to your policies for password management.

**Active Directory management**
+ As part of the FCI cluster, Windows generates a Computer Name Object (CNO) in Active Directory. The CNO responds to DNS requests and forwards traffic to the active SQL node. We do *not* recommend using this Active Directory-provided DNS. The TTL is too high to provide a reasonable failover time and often takes upwards of 5 minutes to reflect the new primary IP address. In contrast, for highly available installations, the internal Network Load Balancer is configured to failover within 30 seconds.
+ An Active Directory domain administrator is required to create the cluster. This requirement is because of the elevated permissions required to create the cluster objects and modify permissions in Active Directory. However, the SQL Server services don’t need to run as a domain administrator. Therefore, we recommend that you create a second Active Directory user for this purpose. However, you can eliminate this user if the services will run as the domain administrator user. In that case, the domain administrator user must be added to the Active Directory administrators group that is created as part of this pattern.

## Epics
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-epics"></a>

### Set up cluster credentials
<a name="set-up-cluster-credentials"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create Active Directory groups. | In AWS Managed Microsoft AD, create the following groups:+ **Cluster administrator group** – This group will be added to the local Administrators group on each cluster node.<br />+ **Cluster remote desktop group** – This group will be added to the local Remote Desktop Users group on each cluster node.<br />For more details, see [Creating an AWS Managed Microsoft AD group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_group.html) in the AWS documentation. | AD administrator |
| Create Active Directory users. | In AWS Managed Microsoft AD, create the following users+ **Domain administrator user** – Use this account to create the cluster.<br />+ **Domain user** – The SQL Server services will use this account to run. Add this user to the cluster administrator group that you created in the previous task.<br />For more details, see [Creating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html) in the AWS documentation. | AD administrator |
| Add Active Directory credentials to secrets. | Use Secrets Manager to create four secrets to store the following information:+ Domain administrator user’s username<br />+ Domain administrator user’s password<br />+ Domain user’s username<br />+ Domain user’s password<br />For more details, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the AWS documentation. | AWS administrator |

### Prepare the environment
<a name="prepare-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Windows AMI. | Create a custom Windows AMI that includes the prerequisite software and configurations. For more details, see [Additional Information](#deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-additional). | AWS administrator, AWS DevOps |
| Install Terraform. | To install Terraform, follow the instructions on the [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) website. | AWS DevOps |
| Clone the repository. | Clone this pattern’s [repository](https://github.com/aws-samples/cluster-amazon-elastic-compute-cloud-amazon-fsx-microsoft-sql-server). For more details, see [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) on the GitHub website. | AWS DevOps |

### Install the cluster
<a name="install-the-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the Terraform variables. | Update the supplied `terraform.tfvars` file to set all variables to values appropriate for your environment.<br />For example, update the `domain_group_administrators` and `domain_group_rdp_users` variables to use your Active Directory domain name and the name of the previously created Active Directory groups. | AWS DevOps |
| Initialize Terraform. | To see the proposed deployment, navigate to the root of the repository. Use the Terraform command line interface (CLI) to run `terraform init` and then run `terraform plan`. | AWS DevOps |
| Deploy resources. | To deploy the SQL cluster and associated resources, use the Terraform CLI to run `terraform apply`. | AWS DevOps, AWS administrator |
| Validate the deployment. | To validate the deployment, use the following steps:1. Connect to one of the deployed Windows Amazon EC2 instances by using Remote Desktop.<br />2. For more details, see [Connect to your Windows instance using RDP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connecting_to_windows_instance.html) in the AWS documentation.<br />3. Open the Windows Failover Cluster Manager. Validate that the cluster was created, and that the SQL Server role was created and is running.<br />4. To test connectivity and authentication with SQL Server, use a database tool such as SQL Server Management Studio to connect to the SQL Server endpoint. (The endpoint value is stored in Secrets Manager.) For more details, see [Connect to Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/connect-sql-server-on-ec2-instance.html) in the AWS documentation. | DBA, AWS systems administrator |

## Troubleshooting
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Terraform provisioning completed but Windows Failover Cluster Manager does not show a cluster has been created or the cluster is in a non-operable state. | The entire installation of the resources and configuration of the clusters can can take 45-60 minutes. After Terraform has completed, the user data script must run to completion, which requires multiple reboots. To monitor progress, you can use the `Checkpoints` directory in the `C:\` drive and the SQL Server installation logs in `C:\Program Data\Microsoft SQL Server\150\Log`. When finished, the **Installation Complete** message is available in the `C:\ProgramData\Amazon\EC2-Windows\Launch\Log\UserdataExecution.log` file. |
| After provisioning a functioning cluster, using Terraform to delete and re-create the cluster does not succeed. Terraform completes, but the cluster is not set up properly. | Part of the provisioning process involves registering machines and virtual objects to Active Directory and Active Directory DNS. When computer names exist for the Amazon EC2 cluster nodes and the cluster node, FCI cannot initialize correctly and will fail provisioning.<br />To fix this issue, perform the following steps: 1. Delete the Amazon EC2 nodes, cluster virtual computer, and cluster id in Active Directory users and computers.<br />2. Delete the DNS entry for the cluster virtual computer in Active Directory DNS.<br />3. Run the following command to delete the cluster id random string Terraform resource `terragrunt destroy -target=random_string.cluster_id`. This action will delete the existing Amazon EC2 instances.<br />4. Run `terraform apply`, and expect the following three new resources: Two FCI Amazon EC2 instances and 1 random string cluster id. |

## Related resources
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-resources"></a>

**AWS documentation**
+ [Create custom images with Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-images.html)
+ [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)
+ [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)
+ [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html)
+ [Creating your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html)

## Additional information
<a name="deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-additional"></a>

**Terraform module information**

This module uses a mixture of AMI configuration and user data configuration to obtain a good mix of provisioning time and stability. During provisioning, Windows requires multiple restarts and waits. A checkpoints method has been implemented to protect against infinite loops during restarts of the persistent user data. User data is configured to be persistent. Therefore, the user data configuration scripts have, and must continue, to be developed to be idempotent. Idempotency streamlines the updating process, allowing for instances to be swapped out during an update cycle without manual configuration to rejoin or re-create FCI clusters.

**SQL Server connection strings and failover clustering**

The module will publish a secret containing the endpoint address that should be used in connection strings for this database. The secret name follows the format `{environment_name}/sqlserver/{cluster_name}/endpoint`. For installations where only one node is used, you can expect this to be the IP address of the Amazon EC2 instance SQL Server interface. For high availability installations (two instances), you can expect this to be the DNS name of the internal Network Load Balancer.

Failover clustering virtual IPs aren’t supported in this module. A virtual IP must remain in the same subnet in order to work. In AWS, a single subnet can’t span multiple Availability Zones. Therefore, the use of virtual IPs would remove the ability for this module to be considered highly available.

Each Amazon EC2 instance is given three private IP addresses. Their usais as follows:
+ **Primary IP for network traffic** – The source IP for egress traffic.
+ **FCI communications** – Used to maintain the state and sync of the failover cluster.
+ **SQL Server (TCP port 1433)** – Listener and also listens for heartbeat traffic to determine which instance is primary.

**VPC configuration**

The [prerequisites ](#deploy-sql-server-failover-cluster-instances-on-amazon-ec2-and-amazon-fsx-prereqs)list a DHCP options set that’s configured to use Active Directory for DNS resolution. However, this prerequisite isn’t a hard requirement. The hard requirement is that the EC2 instances must be able to resolve your Active Directory domain name. Meeting this requirement can be accomplished in other ways, such as by using Amazon Route 53 Resolver endpoints. For more information, see [Integrating your Directory Service’s DNS resolution with Amazon Route 53 Resolvers](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/) (AWS Blog post).

**AMI configuration**

The AMI used in this pattern must contain the following prerequisite software and configurations:

1. Download and expand the SQL Server 2019 installation files into `C:\SQL_Install_media`.

1. Install the following Windows features:
   + `Install-WindowsFeature Failover-Clustering`
   + `Install-WindowsFeature RSAT-AD-PowerShell`
   + `Install-WindowsFeature RSAT-AD-Tools`
   + `Install-WindowsFeature RSAT-Clustering-Mgmt`
   + `Install-WindowsFeature RSAT-Clustering-PowerShell`
   + `Install-WindowsFeature RSAT-Clustering-CmdInterface`

1. Disable the Windows firewall as follows:
   + `Get-NetFirewallProfile | Set-NetFirewallProfile -Enabled False`

1. Enable CredSSP authentication method (replace `<domain>` with your organization’s Windows domain name) as follows:
   + `Enable-WSManCredSSP -Role "Server" -Force`
   + `Enable-WSManCredSSP -Role "Client" -DelegateComputer *.<domain>.com -Force`

1. Set the following registry keys:
   + Allow NTLM authentication credentials:
     + `HKLM:\Software\Policies\Microsoft\Windows\CredentialsDelegation`
       + Name: `AllowFreshCredentialsWhenNTLMOnly`
       + Value: 1
       + Type: `REG_DWORD`
   + Allow local domain computers to use NTLM from PowerShell:
     + Path: `HKLM:\Software\Policies\Microsoft\Windows\CredentialsDelegation\AllowFreshCredentialsWhenNTLMOnly`
       + Name: `1`
       + Value: `wsman/*.<domain>.com`
       + Type: `REG_SZ`

1. Set up the [PowerShell Gallery](https://learn.microsoft.com/en-us/powershell/gallery/overview?view=powershellget-3.x) as follows:
   + `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`
   + `Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force`
   + `Set-PSRepository -Name PSGallery -InstallationPolicy Trusted`

1. Install the following Windows PowerShell modules`*`:
   + `Install-Module -Name ComputerManagementDsc`
   + `Install-Module -Name FailOverClusterDsc`
   + `Install-Module -Name PSDscResources`
   + `Install-Module -Name xSmbShare`
   + `Install-Module -Name xActiveDirectory`
   + `Install-Module -Name SqlServer`

To use Image Builder to create the AMI, follow the instructions in [Create an image pipeline using the EC2 Image Builderconsole wizard](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html) in the Image Builder documentation. To create the recipe’s component with the previous prerequisites, use the following steps:

1. Download the [component.yaml](https://github.com/aws-samples/cluster-amazon-elastic-compute-cloud-amazon-fsx-microsoft-sql-server/blob/main/ami/component.yaml) file from the `ami `folder of the [GitHub repository](https://github.com/aws-samples/cluster-amazon-elastic-compute-cloud-amazon-fsx-microsoft-sql-server).

1. Copy the contents into a new Image Builder component.

1. Update the following placeholders with your information:
   + `<domain>` – Your Active Directory domain name
   + `<bucket_name>` – Name of the Amazon S3 bucket that contains the SQL Server image

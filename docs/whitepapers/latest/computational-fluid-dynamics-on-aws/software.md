---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/software.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Software
<a name="software"></a>

## Installation
<a name="installation"></a>

 CFD software can either be installed into a base AMI, or it can be used from prebuilt AMIs from the AWS Marketplace. If installing into a base AMI, a custom AMI can be created to launch new instances with the software already installed. The [AWS Marketplace](https://aws.amazon.com/marketplace) offers a listing of software from individual software vendors, which offer software included with AWS services. Finally, you can also add the installation to the cluster deployment scripts and run them at cluster creation.

## Licensing
<a name="licensing"></a>

 Many commercial CFD solvers are licensed and may require access to a license server, such as [FlexNet Publisher](https://www.openlm.com/knowledge-base/flexera-flexlm-flexnet-publisher/). Licensing software in the cloud is much like licensing with any other cluster. If a license server is necessary, you can configure your networking to use an existing on-premises server, or you can host the license server on the cloud.

 If hosting the license server on AWS, burstable general-purpose T instances in small sizes, such as micro, can be used for cost-effective hosting. A Reserved Instance purchase for the license server provides further cost savings.

 The FlexNet Publisher license relies on the network interface’s MAC address. The easiest way to retrieve the new MAC address for your license is to launch the instance and retrieve the MAC address before the license is issued. You can preserve the MAC address by changing the [ending behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#change_term_behavior) to prevent deletion of the network interface if the instance is ever terminated. When hosting your own license server, confirm that the security group for the license-server instance allows connectivity on the appropriate ports required by the software package.

 If accessing an on-premises license server, create an [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) for your Virtual Private Cloud (VPC), or alternatively, if on-premises firewalls allow, you may be able to access the on-premises license server through SSH tunneling.

 Cloud-friendly licensing through power-on-demand licensing keys is also growing in popularity and relies on submitting a job with a key provided by the software provider.

## Setup
<a name="setup"></a>

 There are multiple strategies for setting up software in clusters. The most widely used examples are below:

### Create a custom AMI
<a name="create-a-custom-ami"></a>

 This method features the shortest application startup time and avoids potential bottlenecks when accessing a single shared resource. This is the preferred means of distribution for large-scale runs (tens of thousands of MPI ranks) or applications that must load a large number of shared libraries. A drawback is the larger AMI size, which incurs more cost for [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS).

### Share an Amazon EBS volume via NFS
<a name="share-an-amazon-ebs-volume-via-nfs"></a>

 This method installs the necessary software into a single Amazon EBS volume, creates an NFS export on a single instance, and mounts the NFS share on all of the compute instances. This approach reduces the Amazon EBS footprint because only one Amazon EBS volume must be created for the software. This method is useful for large software packages and moderate scale runs (up to thousands of MPI ranks).

 To optimize input/output (I/O) performance, different EBS volume types are available offering different performance characteristics. A tradeoff with this method is a small amount of added network traffic and a potential bottleneck with a single instance hosting the NFS share. Ensuring a larger NFS host instance with additional network capabilities mitigates these concerns.

 To make this approach repeatable, the exported NFS directory can be decoupled from the root volume, stored on a separate [Amazon EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html), and created from an [Amazon EBS snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html). This approach is similar to the custom AMI method, but instead it isolates software from the root volume. An additional Amazon EBS volume is created from an Amazon EBS snapshot at instance launch and is mounted as an additional disk to the compute instance. The snapshot used to create the volume contains the software installation. Decoupling the user software from operating system updates that are necessary on the root volume reduces the complexity of maintenance. Furthermore, the user can rely on the latest AMI releases for the compute instances, which provide an up-to-date system without maintaining a custom AMI.

### Use a managed shared file system
<a name="use-a-managed-shared-file-system"></a>

 This approach installs the CFD software into an AWS managed file system service, such as Amazon FSx for Lustre or [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS), and mounts the shared file system on all of the compute instances. Amazon FSx for Lustre provides a high-performance, parallel file system optimized for HPC workloads. Lustre is optimized for simultaneous access, and its performance can be scaled independently from any single instance size.

 FSx for Lustre works natively with Amazon S3 and can be automatically populated with data residing in S3, which enables users to have a Lustre file system running only while compute jobs are active and easily discard it afterwards.

 Amazon EFS provides a simple, scalable, fully managed elastic NFS file system that can be used as a location for home directories. However, EFS is not recommended for other aspects of a CFD cluster, such as hosting simulation data or compiling a solver, due to performance considerations.

## Maintenance
<a name="maintenance"></a>

 New feature releases and patches to existing software are a frequent need in the CFD application workflow. All distribution strategies can be fully automated. When using the AMI or Amazon EBS snapshot strategy, the software update cycle can be isolated from the application runs. Once a new AMI or snapshot has been created and tested, the cluster is reconfigured to pick up the latest version. Software updates cycles in the strategies using file sharing via NFS or FSx for Lustre must be coordinated with application runs because a live system is being altered.

 In general, automating CFD application installation with scripting tools is recommended and is usually referred to as a Continuous Integration/Continuous Deployment (CI/CD) pipeline on AWS. The automation process reduces the manual processes required to build and deploy new software and security patches to HPC systems. This is useful if you want to use the latest features in software packages with fast update cycles. You can read more about CI/CD pipelines in the [AWS Continuous Delivery documentation](https://aws.amazon.com/devops/continuous-delivery/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

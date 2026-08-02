---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-resources-wavelength-zone-using-terraform.html
---

# Deploy resources in an AWS Wavelength Zone by using Terraform
<a name="deploy-resources-wavelength-zone-using-terraform"></a>

*Zahoor Chaudhrey and Luca Iannario, Amazon Web Services*

## Summary
<a name="deploy-resources-wavelength-zone-using-terraform-summary"></a>

[AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html) helps you build infrastructure that is optimized for Multi-Access Edge Computing (MEC) applications. *Wavelength Zones* are AWS infrastructure deployments that embed AWS compute and storage services within communications service providers’ (CSP) 5G networks. Application traffic from 5G devices reaches application servers running in Wavelength Zones without leaving the telecommunications network. The following facilitate network connectivity through Wavelength:
+ **Virtual private clouds (VPCs)** – VPCs in an AWS account can extend to span multiple Availability Zones, including Wavelength Zones. Amazon Elastic Compute Cloud (Amazon EC2) instances and related services appear as part of your Regional VPC. VPCs are created and managed in [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
+ **Carrier gateway** – A carrier gateway enables connectivity from the subnet in the Wavelength Zone to the CSP network, the internet, or the AWS Region through the CSP’s network. The carrier gateway serves two purposes. It allows inbound traffic from a CSP network in a specific location, and it allows outbound traffic to the telecommunications network and the internet.

This pattern and its associated Terraform code help you launch resources, such as Amazon EC2 instances, Amazon Elastic Block Store (Amazon EBS) volumes, VPCs, subnets, and a carrier gateway, in a Wavelength Zone.

## Prerequisites and limitations
<a name="deploy-resources-wavelength-zone-using-terraform-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An integrated development environment (IDE)
+ [Opt in](https://docs.aws.amazon.com/wavelength/latest/developerguide/get-started-wavelength.html#enable-zone-group) to the target Wavelength Zone
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Terraform version 1.8.4 or later, [installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) (Terraform documentation)
+ Terraform AWS Provider version 5.32.1 or later, [configured](https://hashicorp.github.io/terraform-provider-aws/) (Terraform documentation)
+ Git, [installed](https://github.com/git-guides/install-git) (GitHub)
+ [Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) to create Amazon VPC, Wavelength, and Amazon EC2 resources

**Limitations**

Not all AWS Regions support Wavelength Zones. For more information, see [Available Wavelength Zones](https://docs.aws.amazon.com/wavelength/latest/developerguide/available-wavelength-zones.html) in the Wavelength documentation.

## Architecture
<a name="deploy-resources-wavelength-zone-using-terraform-architecture"></a>

The following diagram shows how you can create a subnet and AWS resources in a Wavelength Zone. VPCs that contain a subnet in a Wavelength Zone can connect to a carrier gateway. A carrier gateway allows you to connect to the following resources:
+ 4G/LTE and 5G devices on the telecommunication carrier's network.
+ Fixed wireless access for select Wavelength Zone partners. For more information, see [Multi-access AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/multi-access.html).
+ Outbound traffic to public internet resources.

![A carrier gateway connects AWS resources in the Wavelength Zone to the CSP network.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8c507de1-208c-4563-bb58-52388ab2fa6d/images/a4cc0699-0cbc-4f15-ab14-3ae569ced7f4.png)

## Tools
<a name="deploy-resources-wavelength-zone-using-terraform-tools"></a>

**AWS services**
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
+ [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html) extends AWS Cloud infrastructure to telecommunication providers’ 5G networks. This helps you build applications that deliver ultra-low latencies to mobile devices and end users.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [Creating AWS Wavelength Infrastructure using Terraform](https://github.com/aws-samples/terraform-wavelength-infrastructure) repository. The Terraform code deploys the following infrastructure and resources:
+ A VPC
+ A Wavelength Zone
+ A pubic subnet in the Wavelength Zone
+ A carrier gateway in the Wavelength Zone
+ An Amazon EC2 instance in the Wavelength Zone

## Best practices
<a name="deploy-resources-wavelength-zone-using-terraform-best-practices"></a>
+ Before deploying, confirm that you're using the latest versions of Terraform and the AWS CLI.
+ Use a continuous integration and continuous delivery (CI/CD) pipeline to deploy IaC. For more information, see [Best practices for managing Terraform State files in AWS CI/CD Pipeline](https://aws.amazon.com/blogs/devops/best-practices-for-managing-terraform-state-files-in-aws-ci-cd-pipeline/) on AWS Blogs.

## Epics
<a name="deploy-resources-wavelength-zone-using-terraform-epics"></a>

### Provision the infrastructure
<a name="provision-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Enter the following command to clone the [Creating AWS Wavelength Infrastructure using Terraform](https://github.com/aws-samples/terraform-wavelength-infrastructure) repository to your environment.<br />`git clone git@github.com:aws-samples/terraform-wavelength-infrastructure.git` | DevOps engineer |
| Update the variables. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-resources-wavelength-zone-using-terraform.html) | DevOps engineer, Terraform |
| Initialize the configuration. | Enter the following command to initialize the working directory.<pre>terraform init</pre> | DevOps engineer, Terraform |
| Preview the Terraform plan. | Enter the following command to compare the target state against the current state of your AWS environment. This command generates a preview of the resources that will be configured.<pre>terraform plan</pre> | DevOps engineer, Terraform |
| Verify and deploy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-resources-wavelength-zone-using-terraform.html) | DevOps engineer, Terraform |

### Validate and clean up
<a name="validate-and-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the infrastructure deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-resources-wavelength-zone-using-terraform.html) | AWS DevOps, DevOps engineer |
| (Optional) Clean up the infrastructure. | If you need to delete all of the resources that were provisioned by Terraform, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-resources-wavelength-zone-using-terraform.html) | DevOps engineer, Terraform |

## Troubleshooting
<a name="deploy-resources-wavelength-zone-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Connectivity to Amazon EC2 instances in the AWS Region. | See [Troubleshoot connecting to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html) or [Troubleshoot connecting to your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/troubleshooting-windows-instances.html). |
| Connectivity to Amazon EC2 instances in the Wavelength Zone. | See [Troubleshoot SSH or RDP connectivity to my EC2 instances launched in a Wavelength Zone](https://repost.aws/knowledge-center/ec2-wavelength-zone-connection-errors). |
| Capacity in the Wavelength Zone. | See [Quotas and considerations for Wavelength Zones](https://docs.aws.amazon.com/wavelength/latest/developerguide/wavelength-quotas.html). |
| Mobile or carrier connectivity from the carrier network to the AWS Region. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-resources-wavelength-zone-using-terraform.html) |

## Related resources
<a name="deploy-resources-wavelength-zone-using-terraform-resources"></a>
+ [What is AWS Wavelength?](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html)
+ [How AWS Wavelength works](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html)
+ [Resilience in AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/disaster-recovery-resiliency.html)

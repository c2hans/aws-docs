---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-region-ipam-architecture.html
---

# Create a hierarchical, multi-Region IPAM architecture on AWS by using Terraform
<a name="multi-region-ipam-architecture"></a>

*Donny Schreiber, Amazon Web Services*

## Summary
<a name="multi-region-ipam-architecture-summary"></a>

*IP address management (IPAM)* is a critical component of network management, and it becomes increasingly complex as organizations scale their cloud infrastructure. Without proper IPAM, organizations risk IP address conflicts, wasted address space, and complex troubleshooting that can lead to outages and application downtime. This pattern demonstrates how to implement a comprehensive IPAM solution for AWS enterprise environments by using HashiCorp Terraform. It helps organizations to create a hierarchical, multi-Region IPAM architecture that facilitates centralized IP address management across all AWS accounts in an [AWS organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organization-structure).

This pattern helps you implement [Amazon VPC IP Address Manager](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) with a sophisticated four-tier pool hierarchy: top-level pool, Regional pools, business unit pools, and environment-specific pools. This structure supports proper IP address governance while enabling delegation of IP management to appropriate teams within the organization. The solution uses AWS Resource Access Manager (AWS RAM) to seamlessly share IP Address Manager pools across the organization. AWS RAM centralizes and standardizes IPAM specifications, which teams can build upon across all managed accounts.

This pattern can help you achieve the following:
+ Automate IP address allocation across AWS Regions, business units, and environments.
+ Enforce organizational network policies through programmatic validation.
+ Scale network infrastructure efficiently as business requirements evolve.
+ Reduce operational overhead through centralized management of IP address spaces.
+ Accelerate cloud-native workload deployments with self-service CIDR range allocation.
+ Prevent address conflicts through policy-based controls and validation.

## Prerequisites and limitations
<a name="multi-region-ipam-architecture-prereqs"></a>

**Prerequisites**
+ One or more AWS accounts, managed as an organization in AWS Organizations.
+ A network hub or network management account that will serve as the IP Address Manager delegated administrator.
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ Terraform version 1.5.0 or later, [installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).
+ AWS Provider for Terraform, [configured](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).
+ Permissions to manage [IP Address Manager](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam.html), [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam.html), and [virtual private clouds (VPCs)](https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html), configured in AWS Identity and Access Management (IAM).

**Limitations**
+ IP Address Manager is subject to [service quotas](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html). The default service quota for pools is 50 per scope. Running this deployment for 6 Regions, 2 business units, and 4 environments would create 67 pools. Therefore, a quota increase might be necessary.
+ Modifying or deleting IP Address Manager pools after resources have been allocated can cause dependency issues. You must [release the allocation](https://docs.aws.amazon.com/vpc/latest/ipam/release-alloc-ipam.html) before you can delete the pool.
+ In IP Address Manager, [resource monitoring](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) can experience a slight delay in reflecting resource changes. This delay can be approximately 20 minutes.
+ IP Address Manager cannot automatically enforce IP address uniqueness across different scopes.
+ Custom tags must adhere to [AWS tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). For example, each key must be unique and cannot begin with `aws:`.
+ There are [considerations and limitations](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org-considerations.html) when integrating IP Address Manager with accounts outside of your organization.

## Architecture
<a name="multi-region-ipam-architecture-architecture"></a>

**Target architecture**

*IP Address Manager configuration and pool hierarchy*

The following diagram shows the logical constructs of the target architecture. A *scope* is the highest-level container in IP Address Manager. Each scope represents the IP address space for a single network. The *pools* are collections of contiguous IP address ranges (or CIDR ranges) within the scope. Pools help you organize your IP addresses according to your routing and security needs. This diagram shows four hierarchical levels of pools: a top-level pool, Regional pools, business unit pools, and environment pools.

![A private scope and four levels of pools in a single AWS Region in a Network account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/780e344e-37f7-4b70-8d7c-94ec67a29305/images/1e23b2a7-a274-4a19-9097-61d8a31dfbf8.png)

This solution establishes a clear hierarchy of IP Address Manager pools:

1. The top-level pool encompasses the entire organizational IP address space, such as `10.176.0.0/12`.

1. The Regional pools are for Region-specific allocations, such as `10.176.0.0/15` for `us-east-1`.

1. The business unit pools are domain-specific allocations within each AWS Region. For example, the finance business unit in the `us-east-1` Region might have `10.176.0.0/16`.

1. The environment pools are purpose-specific allocations for different environments. For example, the finance business unit in the `us-east-1` Region might have `10.176.0.0/18` for a production environment.

This deployment topology distributes IP Address Manager resources geographically while maintaining centralized control. The following are its features:
+ IP Address Manager is deployed in a single primary AWS Region.
+ Additional Regions are registered as [operating regions](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-region.html), where IP Address Manager can manage resources.
+ Each operating region receives a dedicated address pool from the top-level pool.
+ Resources in all operating regions are centrally managed through IP Address Manager in the primary Region.
+ Each Regional pool has a locale property tied to its Region to help you properly allocate resources.

*Advanced CIDR range validation*

This solution is designed to prevent deployment of invalid configurations. When you deploy the pools through Terraform, the following are validated during the Terraform plan phase:
+ Validates that all environment CIDR ranges are contained within their parent business unit CIDR ranges
+ Confirms that all business unit CIDR ranges are contained within their parent regional CIDR ranges
+ Verifies that all Regional CIDR ranges are contained within the top-level CIDR ranges
+ Checks for overlapping CIDR ranges within the same hierarchy level
+ Validates proper mapping of environments to their respective business units

*CIDR range allocation*

The following diagram shows an example of how developers or administrators can create new VPCs and allocate IP addresses from the pool levels.

![A private scope and four levels of pools in a single AWS Region in a Network account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/780e344e-37f7-4b70-8d7c-94ec67a29305/images/7c3de2e3-e71b-4fc0-abcd-7e88cfab5c87.png)

The diagram shows the following workflow:

1. Through the AWS Management Console, the AWS CLI, or through infrastructure as code (IaC), a developer or administrator requests the next available CIDR range in the `AY3` environment pool.

1. IP Address Manager allocates the next available CIDR range in that pool to the `AY3-4` VPC. This CIDR range can no longer be used.

**Automation and scale**

This solution is designed for scalability as follows:
+ **Regional expansion** – Add new Regions by extending the Terraform configuration with additional Regional pool entries.
+ **Business unit growth** – Support new business units by adding them to the BU configuration map.
+ **Environment flexibility** – Configure different environment types, such as development or production, based on organizational needs.
+ **Multi-account support** – Share pools across all accounts in your organization through AWS RAM.
+ **Automated VPC provisioning** – Integrate with VPC provisioning workflows to automate CIDR range allocation.

The hierarchical structure also allows for different scales of delegation and control, such as the following:
+ Network administrators might manage the top-level and Regional pools.
+ Business unit IT teams might have delegated control of their respective pools.
+ Application teams might consume IP addresses from their designated environment pools.

**Note**
You can also integrate this solution with [AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html). For more information, see *Integration with AFT* in the [Additional information](#multi-region-ipam-architecture-additional) section of this pattern.

## Tools
<a name="multi-region-ipam-architecture-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across AWS accounts to reduce operational overhead and provide visibility and auditability.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. [IP Address Manager](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) is a feature of Amazon VPC. It helps you plan, track, and monitor IP addresses for your AWS workloads.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.

**Code repository**

The code for this pattern is available in the [Sample Terraform Implementation for Hierarchical IPAM on AWS](https://github.com/aws-samples/sample-amazon-vpc-ipam-terraform)** **repository on GitHub. The repository structure includes:
+ **Root module** – Deployment orchestration and input variables.
+ **IPAM module** – Core implementation of the architecture described in this pattern.
+ **Tags module** – Standardized tagging for all resources.

## Best practices
<a name="multi-region-ipam-architecture-best-practices"></a>

Consider the following best practices for network planning:
+ **Plan first** – Thoroughly plan your IP address space before deployment. For more information, see [Plan for IP address provisioning](https://docs.aws.amazon.com/vpc/latest/ipam/planning-ipam.html).
+ **Avoid overlapping CIDR ranges** – Make sure that CIDR ranges at each level do not overlap.
+ **Reserve buffer space** – Always allocate larger CIDR ranges than immediately needed to accommodate growth.
+ **Document IP address allocation** – Maintain documentation of your IP address allocation strategy.

Consider the following deployment best practices:
+ **Start with non-production** – Deploy in non-production environments first.
+ **Use Terraform state management** – Implement remote state storage and locking. For more information, see [State storage and locking](https://developer.hashicorp.com/terraform/language/state/backends) in the Terraform documentation.
+ **Implement version control** – Version control all Terraform code.
+ **Implement CI/CD integration** – Use continuous integration and continuous delivery (CI/CD) pipelines for repeatable deployments.

Consider the following operational best practices:
+ **Enable auto-import** – Configure an IP Address Manager pool to automatically discover and import existing resources. Follow the instructions in [Edit an IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/mod-pool-ipam.html) to turn on auto-import.
+ **Monitor IP address utilization** – Set up alarms for IP address utilization thresholds. For more information, see [Monitor IPAM with Amazon CloudWatch](https://docs.aws.amazon.com/vpc/latest/ipam/cloudwatch-ipam.html).
+ **Audit regularly** – Periodically audit IP address usage and compliance. For more information, see [Tracking IP address usage in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tracking-ip-addresses-ipam.html).
+ **Clean up unused allocations** – Release IP address allocations when resources are decommissioned. For more information, see [Deprovision CIDRs from a pool](https://docs.aws.amazon.com/vpc/latest/ipam/depro-pool-cidr-ipam.html).

Consider the following security best practices:
+ **Implement least privilege** – Use IAM roles with the minimum required permissions. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) and [Identity and access management in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam.html).
+ **Use service control policies** – Implement service control policies (SCPs) to enforce IP Address Manager usage in your organization. For more information, see [Enforce IPAM use for VPC creation with SCPs](https://docs.aws.amazon.com/vpc/latest/ipam/scp-ipam.html).
+ **Control resource sharing** – Carefully manage the scope of IP Address Manager resource sharing in AWS RAM. For more information, see [Share an IPAM pool using AWS RAM](https://docs.aws.amazon.com/vpc/latest/ipam/share-pool-ipam.html).
+ **Enforce tagging** – Implement mandatory tagging for all resources related to IP Address Manager. For more information, see *Tagging strategy* in the [Additional information](#multi-region-ipam-architecture-additional) section.

## Epics
<a name="multi-region-ipam-architecture-epics"></a>

### Set up a delegated administrator account for IP Address Manager
<a name="set-up-a-delegated-administrator-account-for-ip-address-manager"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable AWS Organizations features. | Make sure that AWS Organizations has all features enabled. For instructions, see [Enabling all features for an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the AWS Organizations documentation. | AWS administrator |
| Enable resource sharing in AWS RAM. | Using the AWS CLI, enter the following command to enable AWS RAM resource sharing for your organization:<pre>aws ram enable-sharing-with-aws-organization</pre><br />For more information, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the AWS RAM documentation. | AWS administrator |
| Designate an administrator for IP Address Manager. | From the organization’s management account, using the AWS CLI, enter the following command, where `123456789012` is the ID of the account that will administer IP Address Manager:<pre>aws ec2 enable-ipam-organization-admin-account \<br />    --delegated-admin-account-id 123456789012</pre>Typically, a network or network hub account is used as the delegated administrator for IP Address Manager.<br />For more information, see [Integrate IPAM with accounts in an AWS Organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html) in the IP Address Manager documentation. | AWS administrator |

### Deploy the infrastructure
<a name="deploy-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the network architecture. | Define and document your network architecture, including the CIDR ranges for Regions, business units, and environments. For more information, see [Plan for IP address provisioning](https://docs.aws.amazon.com/vpc/latest/ipam/planning-ipam.html) in the IP Address Manager documentation. | Network engineer |
| Clone the repository. | 1. Enter the following command to clone the repository to your local workstation:<pre>git clone https://github.com/aws-samples/sample-amazon-vpc-ipam-terraform.git</pre><br />2. Enter the following command to navigate into the `terraform` directory. | DevOps engineer |
| Configure the variables. | 1. Open the **terraform.tfvars** file.<br />2. Configure the variables for your IP Address Manager deployment. For an example of a completed file, see [terraform.tfvars.example](https://github.com/aws-samples/sample-amazon-vpc-ipam-terraform/blob/main/terraform/terraform.tfvars.example) in the code repository.<br />3. Save and close the **terraform.tfvars** file. | Network engineer, Terraform |
| Deploy the IP Address Manager resources. | 1. Enter the following command to initialize Terraform:<pre>terraform init</pre><br />2. Enter the following command to generate an execution plan:<pre>terraform plan</pre><br />3. Review the plan, and validate the resources and infrastructure components that will be created.<br />4. Enter the following command to deploy the infrastructure:<pre>terraform apply</pre><br />5. When prompted, enter **yes** to confirm the deployment.<br />6. Wait until the deployment is completed. | Terraform |
| Validate the deployment. | 1. Log into your AWS account, and then open the [IP Address Manager console](https://console.aws.amazon.com/ipam/).<br />2. In the navigation pane, choose **Pools**.<br />3. In the list of pools, verify that the pools you configured have been created.<br />4. Open the [AWS RAM console](https://console.aws.amazon.com/ram/home).<br />5. Verify that the IP Address Manager resources have been shared. Follow the instructions in [Viewing resource shares that you created](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-rs.html) in the AWS RAM documentation. | General AWS, Network engineer |

### Create VPCs and set up monitoring
<a name="create-vpcs-and-set-up-monitoring"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | Follow the steps in [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the Amazon VPC documentation. When you reach the step to choose a CIDR range for the VPC, allocate the next available from one of your Regional, business unit, and environment pools. | General AWS, Network administrator, Network engineer |
| Validate the CIDR range allocation. | 1. Open the [IP Address Manager console](https://console.aws.amazon.com/ipam/).<br />2. In the navigation pane, choose **Dashboard**.<br />3. In the dashboard, verify that the CIDR range has been allocated to the VPC that you created. | General AWS, Network administrator, Network engineer |
| Monitor IP Address Manager. | Configure monitoring and alarms related to the allocation of IP Address Manager resources. For more information and instructions, see [Monitor IPAM with Amazon CloudWatch](https://docs.aws.amazon.com/vpc/latest/ipam/cloudwatch-ipam.html) and [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) in the IP Address Manager documentation. | General AWS |
| Enforce use of IP Address Manager. | Create a service control policy (SCP) in AWS Organizations that requires members in your organization to use IP Address Manager when they create a VPC. For instructions, see [Enforce IPAM use for VPC creation with SCPs](https://docs.aws.amazon.com/vpc/latest/ipam/scp-ipam.html) in the IP Address Manager documentation. | General AWS, AWS administrator |

## Troubleshooting
<a name="multi-region-ipam-architecture-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Terraform fails with IP Address Manager resource not found | Make sure that the IP Address Manager administrator account is properly delegated and that your AWS Provider is authenticated to that account. |
| CIDR range allocation fails | Check that the requested CIDR range fits within the available range of the IP Address Manager pool and doesn't overlap with existing allocations. |
| AWS RAM sharing issues | Verify that resource sharing is enabled for your AWS Organization. Verify that the correct principal, the organization Amazon Resource Name (ARN), is used in the AWS RAM share. |
| Pool hierarchy validation errors | Make sure that the child pool CIDR ranges are properly contained within their parent pool CIDR ranges and don't overlap with sibling pools. |
| IP Address Manager quota limit exceeded | Request a quota increase for IP Address Manager pools. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. |

## Related resources
<a name="multi-region-ipam-architecture-resources"></a>

**AWS service documentation**
+ [Amazon VPC IP Address Manager documentation](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
+ [AWS Resource Access Manager documentation](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
+ [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)

**AWS blog posts**
+ [Managing IP pools across VPCs and Regions using Amazon VPC IP Address Manager](https://aws.amazon.com/blogs/networking-and-content-delivery/managing-ip-pools-across-vpcs-and-regions-using-amazon-vpc-ip-address-manager/)
+ [Network address management and auditing at scale with Amazon VPC IP Address Manager](https://aws.amazon.com/blogs/aws/network-address-management-and-auditing-at-scale-with-amazon-vpc-ip-address-manager/)

**Videos and tutorials**
+ [AWS re:Invent 2022: Best practices for Amazon VPC design and IPAM (NET310)](https://www.youtube.com/watch?v=XrEHsy_8RYs)
+ [AWS re:Invent 2022: Advanced VPC design and new capabilities (NET401)](https://www.youtube.com/watch?v=tbXTVpwx87o)

## Additional information
<a name="multi-region-ipam-architecture-additional"></a>

**Integration with AFT**

You can integrate this solution with AWS Control Tower Account Factory for Terraform (AFT) to make sure that newly provisioned accounts automatically receive proper network configurations. By deploying this IPAM solution in your network hub account, new accounts created through AFT can reference the shared IP Address Manager pools when you create VPCs.

The following code sample demonstrates AFT integration in an account customization by using AWS Systems Manager Parameter Store:

```
# Get the IP Address Manager pool ID from Parameter Store
data "aws_ssm_parameter" "dev_ipam_pool_id" {
  name = "/org/network/ipam/finance/dev/pool-id"
}

# Create a VPC using the IP Address Manager pool
resource "aws_vpc" "this" {
  ipv4_ipam_pool_id   = data.aws_ssm_parameter.dev_ipam_pool_id.value
  ipv4_netmask_length = 24

  tags = {
    Name = "aft-account-vpc"
  }
}
```

**Tagging strategy**

The solution implements a comprehensive tagging strategy to facilitate resource management. The following code sample demonstrates how it is used:

```
# Example tag configuration
module "tags" {
  source = "./modules/tags"

  # Required tags
  product_name  = "enterprise-network"
  feature_name  = "ipam"
  org_id        = "finance"
  business_unit = "network-operations"
  owner         = "network-team"
  environment   = "prod"
  repo          = "https://github.com/myorg/ipam-terraform"
  branch        = "main"
  cost_center   = "123456"
  dr_tier       = "tier1"

  # Optional tags
  optional_tags = {
    "project"    = "network-modernization"
    "stack_role" = "infrastructure"
  }
}
```

These tags are automatically applied to all IP Address Manager resources. This facilitates consistent governance, cost allocation, and resource management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/architecture-design.html
---

# Architecture design
<a name="architecture-design"></a>

This section provides high-level guidance on how to meet the recommended infrastructure requirements from SAS and how to design your AWS architecture for a SAS deployment.

## SAS requirements
<a name="sas-requirements"></a>

SAS provides official guidelines for all the major technical infrastructure components for deploying SAS 9.4. We recommend that you familiarize yourself with these technical system requirements as part of your migration planning process. For more information regarding SAS I/O requirements, see [Best Practices for Configuring your IO Subsystem for SAS® 9 Applications](https://support.sas.com/resources/papers/proceedings16/SAS6761-2016.pdf) in the SAS documentation.

## AWS architecture design
<a name="aws-arch-design"></a>

Designing the right architecture for your SAS environment is critical to the success of your SAS deployment. This section provides an overview of a recommended AWS architecture that separates SAS environments into the following AWS accounts:
+ An account dedicated to your SAS production environment
+ An account dedicated to your SAS integration environment (for testing)
+ A shared account dedicated to infrastructure management

It's a best practice to separate these environments so that you can independently test and validate changes before promoting changes from the test environment to the production environment. The following diagram illustrates the decoupling architecture.

![Architecture diagram for decoupling data storage](https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/images/guide-img/f83bb357-cf26-4b94-abb6-1bd9d91feaa4/images/ba4ef9c9-67c9-4ce5-83cf-1be3b1148313.png)

The two accounts include user-facing Citrix terminal servers. End users in your organization can connect to these terminal servers by using a Citrix client or the Citrix web publishing portal, and then launch the SAS Enterprise Guide SAS client. The shared infrastructure management account can include all the automation and CI/CD tooling that's required for deploying your infrastructure components into each AWS account and AWS Region.

The SAS client connects to the SAS server that's running within the same network. Both servers have access to a dedicated high-performance shared storage file server: FSx for Windows File Server. The servers and file server are joined to your on-premises Microsoft Active Directory environment. This enables operational IT to centralize access management. Additionally, you can base the patch management in this environment on your existing on-premises software distribution, patch management solution, and the Citrix terminal server infrastructure.

This architecture doesn't use bastion hosts, implemented as additional Amazon Elastic Compute Cloud (Amazon EC2) instances, for console and direct management. All EC2 instances are configured to use AWS Systems Manager Fleet Manager in case the administrative Citrix access doesn't work. Fleet Manager, a capability of AWS Systems Manager, provides an interface that helps you to remotely manage nodes running on AWS or in on-premises environments. For more information, see [AWS Systems Manager Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet.html) in the AWS Systems Manager User Guide.

The VPC is part of the landing zone's hub and spoke network. The network provides on-premises, internet breakout, and other external connectivity centrally.

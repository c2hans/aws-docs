---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/security-assurance-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security Assurance on AWS
<a name="security-assurance-aws"></a>

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment. As shown in the chart below, this differentiation of responsibility is commonly referred to as Security “of” the Cloud versus Security “in” the Cloud.

![A chart showing the shared responsibility model between AWS and cusotmers.](http://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/images/shared-responsibility-model.png)

## Security of the Cloud
<a name="security-of-the-cloud"></a>

The following resources can be used to help you ensure security of your cloud environment:

### AWS Global Infrastructure
<a name="aws-global-infrastructure"></a>

The AWS Global Infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

### AWS Compliance Programs
<a name="aws-compliance-programs"></a>

The [AWS Compliance Program](https://aws.amazon.com/compliance/programs/) is used by customers to understand the robust controls in place at AWS that maintain security and compliance in the cloud. IT standards that AWS comply with are broken out by [Certifications and Attestations](https://aws.amazon.com/compliance/programs/#Certifications_.2F_Attestations.3A); [Laws/Regulations](https://aws.amazon.com/compliance/programs/#Laws_.2F_Regulations.3A); [Privacy](https://aws.amazon.com/compliance/programs/#Privacy); and [Alignments/Frameworks](https://aws.amazon.com/compliance/programs/#Alignments_.2F_Frameworks.3A). You can use this information in the compliance programs as inputs and guides to build your own compliance program for how your organization can use AWS.

### AWS Artifact
<a name="aws-artifact"></a>

[AWS Artifact](https://aws.amazon.com/artifact) provides a central resource for AWS security and compliance reports including Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies that validate the implementation and operating effectiveness of AWS security controls. You can use the reports available in AWS Artifact as inputs to questions that are a part of your internal supplier due diligence processes, as part of overall governance of the use of cloud services.

AWS Artifact Agreements enable you to use the AWS Management Console to review, accept, and manage agreements for your AWS account or AWS Organizations. An example of such an agreement is the Business Associate Addendum (BAA). A BAA typically is required for companies that are subject to the Health Insurance Portability and Accountability Act (HIPAA).

## AWS services to help govern your AWS environment
<a name="identity-security-compliance-services"></a>

The following resources can be used to help govern your AWS environment:

### AWS Organizations
<a name="aws-organizations"></a>

AWS Organizations allows you to centrally govern your AWS accounts. You can perform account management activities at scale by consolidating multiple AWS accounts into a single organization. You can leverage the multi-account management services available in AWS Organizations with many AWS services to perform tasks on all accounts that are members of your organization. AWS Organizations includes service control policies (SCPs) that you can use to provide centralized control over all accounts in your organization.

### AWS Control Tower
<a name="aws-control-tower"></a>

[AWS Control Tower](https://aws.amazon.com/controltower) is a managed service that orchestrates the set up and deployment of guardrails across the AWS accounts in AWS Organizations. If you are building a new AWS environment, starting out on your journey to AWS, or starting a new cloud initiative, AWS Control Tower can help you get started quickly with built-in governance and best practices.

### AWS Solutions
<a name="aws-solutions"></a>

[AWS Solutions](https://aws.amazon.com/solutions) can help you implement the capability automatically where services are not available at the moment, please reach out to your account team for additional information on what types of solutions are available for your business needs.
+ [AWS Compliance Solutions Guide](https://aws.amazon.com/compliance/solutions-guide)
+ [AWS Partner Solutions for Governance, Risk, and Compliance](https://aws.amazon.com/financial-services/partner-solutions/risk/)
+ [AWS Public Sector Partner Program](https://aws.amazon.com/partners/programs/public-sector/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/security-governance.html
---

# Establish security and governance for each CSP
<a name="security-governance"></a>

Because of the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), FIs that adopt cloud services can reduce administrative burden by offloading some of the responsibility for infrastructure security to the CSP. FIs can benefit from purpose-built, cloud-native security services that offer features that are often unavailable, difficult to manage, or cost-prohibitive in an on-premises environment. A successful cloud security and governance strategy enables IT and security teams to focus on building systems that are secure by design, helps the FI rapidly adapt to evolving mission requirements, and provides staff with secure environments for innovation.

The best practice for security and governance is to make it easy for users to do the right thing. This is why automation, partner solutions, orchestration, and proper controls are critical to a multicloud operating model.

The following sections discuss best practices for establishing security and governance in a multicloud environment. For information about AWS services for the financial services industry, see [Security, Compliance, and Governance for Financial Services](https://aws.amazon.com/financial-services/security-compliance/) on the AWS website.

## Compliance networks
<a name="compliance"></a>

FIs must adhere to many regulatory requirements, and these are often specific to the markets and jurisdictions that the FI operates in. Regulations can include the Payment Card Industry Data Security Standard (PCI DSS), the European Union's Digital Operational Resilience Act (DORA), National Institute of Standards and Technology (NIST) compliance frameworks, and many others. Every regulation is distinct and might apply only to certain workloads. Consider the requirements for each workload and make sure that you can meet them in its cloud environment. Make sure that you understand your responsibilities compared with the cloud provider's responsibilities in each environment.

## Supporting compliance without inhibiting innovation
<a name="innovation"></a>

We recommend that you embed security controls in self-service systems that enable users to rapidly deploy cloud environments with minimal intervention from IT teams. These self-service systems might take the form of service catalogs, where infrastructure can be vended with preset, vetted patterns, or common templates that are written by using infrastructure as code (IaC) products such as HashiCorp Terraform or the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/).

You might choose to manage compliance for each provider separately or use custom-built or AWS Partner solutions that centralize management across providers.

## Assessing and controlling cost and usage
<a name="cost-usage"></a>

Establish cost visibility and control mechanisms to gain insight into cloud services that are in use, who the cloud resources belong to, the purpose of those cloud resources, what potential cost savings can be achieved by optimizing consumption, and which geographies your workloads are deployed in. You can increase your firm's return on investment by partnering with your CSP to migrate and modernize mission-critical systems. You can negotiate enterprise-level agreements, benefit from volume pricing, and take advantage of the CSP's expertise. To manage costs across multiple providers, consider how you can aggregate and analyze cost and usage from each provider, either by using in-house processes and tooling, or by using AWS Partner solutions. Establish a core cloud financial operations (FinOps) function in your organization, and dedicate resources to evangelizing and implementing capabilities for cloud cost management and optimization.

## Managing user permissions
<a name="permissions"></a>

You must identify the core needs of your users and confirm that there are appropriate mechanisms in place to grant and revoke access to cloud services. Different types of users require different types of access to cloud services. You should have tooling in place to centrally manage these identities in an automated way across all your cloud environments, and use established processes to identify, grant, and revoke permissions as roles and responsibilities change over time. The best practice is to use automation to review and report on privileges at least every 90 days. For information on identities and access, see [Identity federation and single sign-on](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-education-hybrid-multicloud/identity-sso.html) in the guide *Building a strategy for single, hybrid, and multicloud in education*.

## Integrating new systems with your identity management solution
<a name="integration"></a>

FIs should make it easy to integrate new systems with their identity management systems (for example, Microsoft Entra ID, Okta, or Ping Identity). This gives the organization the flexibility to support a variety of mission-critical functions by allowing stakeholders to buy and build systems that can easily be integrated into the identity management system. When you simplify the integration process, your stakeholders will be less likely to use their own access control measures, which might not enforce security best practices such as single sign-on, passkeys, and multi-factor authentication (MFA). Your identity management system should interoperate with the necessary systems through native integrations or industry-standard protocols, so it can support easy adoption across multiple CSPs.

## Effective incident detection and response
<a name="incident-detection"></a>

To detect and respond to cyberattacks effectively, use a dual approach:
+ Focus your efforts on preventive measures and security controls that are automatically embedded in cloud environments, including adoption of CSP-specific services if necessary.
+ Implement detection capabilities that help cyber incident responders detect, contain, and mitigate security breaches in a timely fashion, including the ability to isolate CSPs from one another if a breach occurs.

Perform regular simulations for attack scenarios, such as game days, tabletop exercises, and disaster recovery drills, so your people, processes, and technology are tested and ready across all your cloud environments. This includes simulating an attack on a single provider and analyzing the potential unintended impact to other providers.

## Mapping data classifications to CSPs
<a name="data-classifications"></a>

Every FI has a data classification standard. Typically, this includes a data label such as *Personally Identifiable Information (PII)*, *Classified*, *Private*, or *Confidential*. These labels might include metadata, depending on the data and workload. The scope of discovery, audit, data access patterns, and controls will be mapped to your business's unique requirements. In a multicloud environment, establish mechanisms to ensure that each environment is vetted to process data based on its classification before data transmission. Prevent data processing in unauthorized or unintended environments that inadvertently expands the scope of compliance. For example, you might have a payment processing application on AWS that is PCI-compliant, but it might be associated with workloads in other CSPs that are not PCI-compliant.

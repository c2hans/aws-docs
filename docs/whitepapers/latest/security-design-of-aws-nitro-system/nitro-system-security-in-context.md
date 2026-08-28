---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/nitro-system-security-in-context.html
---

# Nitro System security in context
<a name="nitro-system-security-in-context"></a>

 The Nitro System design features discussed in this paper operate in the context of the full set of robust controls in place at AWS to maintain security and data protection in the AWS Cloud. In this section we will provide a high-level overview of relevant AWS security and compliance practices. As an AWS customer you inherit all the best practices of AWS policies, architecture, and operational processes built to satisfy the requirements of our most security-sensitive customers.

 AWS environments are continuously audited, with [certifications from accreditation bodies across geographies and verticals](https://aws.amazon.com/compliance/programs/). AWS Outposts also offers the ability, where required, for customers to run AWS compute, storage, database, and other services locally on Nitro System based hardware located in their own facilities.

## Infrastructure security
<a name="infrastructure-security"></a>

 Security at AWS starts with our core infrastructure—the hardware, software, networking, and facilities that run AWS Cloud services. Custom-built for the cloud and designed to meet the most stringent security requirements in the world, our infrastructure is monitored 24/7 to help ensure the confidentiality, integrity, and availability of your customer data. With AWS you can build on the most secure global infrastructure, knowing you always own your customer data, including the ability to encrypt it, move it, and manage retention.

### Physical access
<a name="physical-access"></a>

 Physical access to AWS data centers is strictly controlled, both at the perimeter and at building entry points by professional security staff using video surveillance, two-factor and biometric authentication, intrusion detection systems, and other electronic means. Authorized staff must pass two-factor authentication a minimum of two times to access data center floors. All visitors are required to present identification and are signed in and continually escorted by authorized staff. AWS only provides data center access and information to employees and contractors who have a legitimate business need for such privileges.

 When an employee no longer has a business need for these privileges, his or her access is immediately revoked, even if they continue to be an employee of Amazon or Amazon Web Services. All physical access to data centers by AWS employees is logged and audited routinely.

### Media sanitization
<a name="media-sanitization"></a>

 Media storage devices used to store customer data are classified by AWS as Critical. AWS has exacting standards on how to install, service, and eventually destroy the devices when they are no longer useful. When a storage device has reached the end of its useful life, AWS decommissions media using techniques detailed in [NIST 800-88](https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final). Media that stored customer data is not removed from AWS control until it has been securely decommissioned.

### Data protection
<a name="data-protection"></a>

 All data flowing across the AWS global network that interconnects our data centers and Regions is automatically encrypted at the physical layer before it is transmitted between our secured facilities. Additional encryption layers exist as well; for example, all inter-Region VPC peering traffic, and customer or service-to-service TLS connections. We provide tools that allow you to easily encrypt your customer data in transit and at rest to help ensure that only authorized users can access it, using keys you control managed by AWS KMS, or managing your encryption keys with [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) using [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final) Level 3 validated HSMs.

 We also give you the control and visibility you need to help you comply with regional and local data privacy laws and regulations. The design of our global infrastructure allows you to choose Regions in which your customer data is physically located, helping you meet data residency requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/platform-arch.html
---

# Platform architecture
<a name="platform-arch"></a>

**Establish and maintain guidelines, principles, patterns, and guardrails for your cloud environment.**

A [well-architected](https://aws.amazon.com/architecture/well-architected/)[ cloud environment](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html) helps you accelerate implementation, reduce risk, and drive cloud adoption. The platform architecture capability creates consensus within your organization for enterprise standards that drive cloud adoption. You define best practice blueprints and guardrails to facilitate authentication, security, networking, and logging and monitoring. Additionally you take into consideration and plan for workloads you might need to retain on premises due to latency, data processing, or data residency requirements and evaluate hybrid cloud use cases  such as cloud bursting, backup and disaster recovery to the cloud, distributed data processing, and edge computing.

## Start
<a name="platform-arch-start"></a>

### Define a multi-account strategy
<a name="define-a-multi-account-strategy.b1008fd8-9c1d-5969-9f09-c7f4aed192b2"></a>

A good [multi-account strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) considers scale and operational eﬃciency concerns. This means [isolating your workloads](https://aws.amazon.com/solutions/guidance/workload-isolation-on-aws/) into a logical pattern that best meets your operational needs. We suggest that you start with a foundational set of accounts to accommodate centralized and decentralized services in your enterprise.** **You can centralize security, financial, and operational functions to effectively manage and govern your distributed and autonomous teams and accounts. You will want to align across your organization to understand how the platform and your workloads will be segmented and managed. Understanding this structure helps you ensure that security principles are in place  for authentication and authorization while aligning to evolving acceptable use policies for the platform.

### Define preventative controls
<a name="define-preventative-controls.1d9fb8a9-6f55-5a85-9f50-312b394a7838"></a>

Plan for a secure, multi-account environment with an embedded set of default controls (*guardrails*). Begin to understand and use a mechanism such as [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to manage service use across your organization, including the AWS Regions that are available for consumption within your cloud platform. Policies provide a centralized mechanism for controlling the maximum permissions available for all accounts and ensuring that they adhere to the organization's access control guidelines.

### Define organizational unit structure
<a name="define-organizational-unit-structure.9e2fa010-d56a-5a1c-87bc-b1f67282e2b7"></a>

Organizational units (OUs) serve as a practical way to manage and categorize accounts based on regulatory requirements and software development lifecycle (SDLC) environments. By using OUs, organizations streamline the process of applying for appropriate policies and permissions across their cloud infrastructure. [Workload OUs](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/workloads-ou.html) are specifically designed for accounts that support application infrastructure resources, and ensure that the right policies are enforced. Using OUs and SCPs help enhance your organization's cloud infrastructure's security and compliance while also ensuring the smooth operation of your applications and services. This ultimately leads to a more efficient and robust cloud adoption process.

### Define network connectivity
<a name="define-network-connectivity.fcd06ab0-0fe3-575e-9fb0-e04d01b37eb3"></a>

[Network connectivity](https://aws.amazon.com/solutions/guidance/network-connectivity-on-aws/) is a crucial aspect of any cloud infrastructure that supports the creation of secure, scalable, and highly available networks to support applications and workloads. A well-designed network provides consistently high performance and ensures seamless operations across different environments.

When you design your network architecture, consider if you have workloads that you want to retain [on premises](https://aws.amazon.com/hybrid/) due to latency, data processing, or data residency requirements. By evaluating hybrid cloud [use cases](https://d1.awsstatic.com/whitepapers/hybrid-cloud-with-aws.pdf) such as cloud bursting, backup and disaster recovery to the cloud, distributed data processing, and edge computing, you can identify the key requirements for the following aspects:
+ **Connectivity to and from the internet. **This aspect involves providing secure and reliable connections between your applications or workloads and the internet. This connectivity is essential for facilitating access to web-based resources, enabling communications between users and applications, and ensuring that your services are accessible to the public when needed.
+ **Connectivity across your cloud environments. **This area focuses on establishing robust connections among various components and services within your cloud infrastructure. It ensures that data and resources are easily shared and accessed across different cloud services, promoting efficient collaboration and smoother operations. A key consideration here is your use of [virtual private clouds (VPCs)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). To keep things simple, consider creating standards on how VPCs are created and tracked. Consider creating these standards programmatically, and plan to use an IP address management ([IP address management (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) Allocate enough IP space to allow for growth, and design subnet structures for easy troubleshooting when using multiple Availability Zones. Make sure to follow [security best practices for VPCs ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)when you design and implement network connectivity.
+ **Connectivity between your on-premises network and your cloud environments. **This aspect deals with the integration of your on-premises infrastructure with your cloud-based environment. By creating secure and reliable connections between the two, organizations benefit from the advantages of hybrid architectures. For example, you can use on-premises resources and cloud services simultaneously for improved performance, scalability, and cost optimization.

By addressing these three key areas of network connectivity, you can build a robust cloud infrastructure that supports your applications and workloads effectively, so you can capitalize on the benefits of cloud adoption. Take note of networking requirements, and create a simple design that enables you to scale in accordance with your multi-account strategy.

### Define DNS strategy
<a name="define-dns-strategy.ae6707db-13c9-5b14-a252-8cae24371a29"></a>

A well-planned DNS strategy helps you avoid complications as your cloud environments grow. If you maintain on-premises DNS capabilities, we recommend that you design [hybrid DNS architectures ](https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/hybrid-cloud-dns-options-for-vpc.html)that use on-premises DNS infrastructure along with cloud DNS for any cloud-based DNS requirements. Integrate DNS resolution with on-premises DNS environments by using resolver endpoints and forwarding rules. Use private hosted zones to hold information about how you want cloud DNS to respond to queries for a domain and its subdomains within one or more networks.

### Define tagging standards
<a name="define-tagging-standards.06f15b46-a9ad-5aa3-af3a-152253d3ee62"></a>

Tagging resources is an essential practice to manage costs effectively and identify ownership of resources. Consider how your organization will further allow consumption in the cloud, including the use of specific services within the platform. Define a tagging strategy that tracks which resources are being deployed by which teams. Take inputs from the [AWS CAF Operations perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/aws-caf-operations-perspective.html) and use tags to automate tasks for your deployed infrastructure.

Additionally, by tagging resources with relevant metadata, you can group and track your spending based on your organizational requirements dictated in the Cloud Financial Management (CFM) capability in the [AWS CAF Governance perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/cloud-financial-management.html). Identify a mechanism for reporting that supports your accounting and financial practices, including actions to be taken when financial policies are violated.

### Define an observability strategy
<a name="define-an-observability-strategy.dffe5aeb-4d52-5ae0-97ce-9de1f6399712"></a>

Establishing an observability strategy is a critical step toward optimizing and securing your cloud architecture. This strategy revolves around transforming the metrics and logs produced by your cloud services into actionable insights for strategic decision-making. Prioritize monitoring key performance indicators and setting up alerts to preemptively address potential issues. To prevent tool proliferation, optimize costs, and focus on what matters most to your organization, incorporate this observability strategy across both your platform and applications. For further guidance, see our presentation on [Developing an observability strategy](https://www.youtube.com/watch?v=Ub3ATriFapQ) (AWS re:Invent 2022).

## Advance
<a name="platform-arch-advance"></a>

### Define proactive and detective controls
<a name="define-proactive-and-detective-controls.d249f567-5aa8-5449-aa0e-a33815de1b0a"></a>

To advance, your organization must identify the need for proactive and detective controls (*guardrails*) within the environment. Create policies that deﬁne the guardrails or limits that roles and users have in the accounts located within an organizational unit (OU). Review any default detective guardrails for the platform, and choose which guardrails to apply. Create additional preventive and detective controls as required, and group them by OUs to align them to your multi-account strategy. Consider which organizational tools and mechanisms you need to inspect non-compliant resources that are identified by detective controls.

### Define standards for service onboarding
<a name="define-standards-for-service-onboarding.ed90cb96-9983-5123-82c0-25f685a65cac"></a>

Create standards for the acceptable use of the platform and the patterns associated with service consumption and how that will be governed. Consider which initial services are allowed for use. Create a document that outlines these standards and publish them to users and operators of the platform. Ensure that these standards adapt over time to meet the changing objectives of the organization and the evolving capabilities of cloud computing.

### Define patterns and principles
<a name="define-patterns-and-principles.7fa853b9-0efd-530a-8c97-aaec5a2d59fc"></a>

Consider which architectural patterns will be allowed within your organization by using inputs from application owners, and begin to define blueprints for standardization. Standardization allows for greater governance and lower administrative burden as you scale in the cloud. Define patterns that will use infrastructure as code (IaC) and plan for a simplified deployment model by using a service catalog that's integrated into your change control processes and IT service management (ITSM) systems. Define how these blueprints will be used and the circumstances for allowing exceptions. Plan for those exceptions and their governance, with considerations for authentication, security monitoring, and guardrails.

## Excel
<a name="platform-arch-excel"></a>

### Define remediation patterns
<a name="define-remediation-patterns.ab5d7c9c-3c15-52cd-9a8b-c0356e697ab6"></a>

Consider how to annotate and prioritize your detective guardrail ﬁndings so they can be remediated in accordance with your security and compliance frameworks. Plan to use automation to detect out-of-policy provisioning of resources, including those that violate budgetary and tagging policies. Identify the capabilities needed to set and measure service-level objectives while updating your runbooks and playbooks. Set periodic reviews of these practices and a feedback mechanism to capture data related to platform evolution. Define mechanisms to create and update runbooks and playbooks accordingly.

### Communicate and refine policies
<a name="communicate-and-refine-policies.0ece4a2f-0f6c-54bf-98c2-8fa10b589ad3"></a>

Create a centralized content management system for all documentation and distribute it to the users and operators of the platform. Create a mechanism to capture feedback for future consideration on changes to the policy.

### Understand financial management capabilities
<a name="understand-financial-management-capabilities.c168bb24-88de-51e3-8fdf-d182b7a6af30"></a>

Organizations thrive when they maintain a transparent and comprehensive understanding of their budget. This empowers them to make well-informed decisions, allocate resources efficiently, and accomplish their strategic objectives. A clear view of the budget helps organizations excel by facilitating informed decision-making, effective resource allocation, cost control, performance measurement, and the maintenance of accountability and compliance. This ultimately results in a more efficient, financially stable, and prosperous organization. When you have a successful tagging strategy, you can use cost filters in [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to filter expenses based on resource tags. This helps you create a budget that's tailored to specific projects, departments, environments, or other criteria, further enhancing financial management capabilities. You can associate [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) and [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) with tags to drive financial insights and transparency when reporting on cost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

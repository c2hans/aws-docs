---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/cloud-governance-on-aws-how-to-choose.html
---

# Choosing an AWS cloud governance service
<a name="cloud-governance-on-aws-how-to-choose"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS cloud governance services are the best fit for your organization. |
| **Last updated** | December 23, 2024 |
| **Covered services** | + [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)<br />+ [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)<br />+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)<br />+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)<br />+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)<br />+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)<br />+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)<br />+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) <br />+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)<br />+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)<br />+ [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)  |

## Introduction to AWS cloud governance
<a name="introduction"></a>

 Cloud governance is a set of rules, processes, and reports that helps you align your AWS Cloud use toward your business objectives.

 This covers security, by enabling multi-account strategies, continuous monitoring, and control policies. It covers compliance, by automating checks, reporting, and remediation. It covers operations, by applying controls enterprise wide. It covers identity by centralizing identity and access management at scale. It covers cost, by facilitating usage reports and policy enforcement. And it covers resilience, by helping integrate assessments and testing into CI/CD pipelines for validation.

 We offer a range of services to help you set up, manage, monitor, and control the use of accounts, services, and resources in the cloud, thereby implementing cloud governance best practices.

 The guide is designed to help you decide which AWS cloud governance services are the best fit for your organization, to strengthen operational resilience, optimize costs, and build controls to help comply with regulations or corporate standards, while maintaining development speed and accelerating innovation.

[![AWS Videos](http://img.youtube.com/vi/U0y9l5V3mMQ?start=131&end=501/0.jpg)](http://www.youtube.com/watch?v=U0y9l5V3mMQ?start=131&end=501)

## Understand AWS cloud governance
<a name="understand"></a>

![Diagram showing AWS services used in cloud governance applications, including defining requirements, deploying and operating, and measuring and assessing.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/cloudgov-understanding.png)

 The previous diagram shows how cloud governance draws on multiple AWS services, which allow you to define your governance requirements, deploy and operate your systems, and measure and assess their performance. The services provide built-in governance control, resource provisioning to align with your governance policies, and operations tools to help you monitor and manage your environment.

 Harnessing AWS cloud governance services helps you ensure your cloud use supports your business objectives, Specifically, they enable you to improve speed and agility for developers, operate in a dynamic regulatory environment, streamline mergers and acquisitions, and strengthen operational resilience:
+  **Improve speed and agility for developers —** Quickly spin new environments through APIs making sure your developers are not waiting on weeks long provisioning cycles, and accelerate provisioning of CI/CD pipeline. Find and prevent defects early in the software delivery process, using pre-built controls and rules, and infrastructure-as-code templates for provisioning common resources efficiently.
+  **Operate in a dynamic regulatory environment —** Create always-on boundaries to protect and control access to data across AWS, codify your compliance requirements, and automate the assessment of your resource configurations across your organization.
+  **Streamline mergers and acquisitions —** Migrate workloads faster by building a secure, well-architected, multi-account environment. Centralize account creation, allocate resources, group accounts, and apply governance policies and controls easily and quickly. Adopt a programmatic approach to multi-account management at scale.
+  **Strengthen operational resilience —** Set up a secure, well-architected, resilient multi-account environment quickly. Run assessments of your workloads to uncover potential resilience-related weaknesses. Conducts automated checks against five key areas – cost optimization, performance, security, fault tolerance, and service limits – and receive recommendations that enable you to follow known best practices.
+  **Optimize costs —** Visualize, understand, and manage costs and usage over time. Continuously analyze resource utilization, identify underutilized resources, and terminate idle resources.

 Cloud governance best practices can effectively be built in when you set up and operate your workloads on AWS. Interoperable services help you achieve consistent, centralized governance over your IT estate, including AWS and third-party products. Breadth and depth of controls across AWS services help you meet evolving regulatory requirements and minimize security risks.

## Consider AWS cloud governance criteria
<a name="consider"></a>

 The following section outlines some of the key criteria to consider when choosing a cloud governance strategy. In particular, it discusses the different kinds of cloud environment, control regime, and developer support opportunities that might be applicable to your organization and business objectives.

------
#### [ Multi-account strategy ]

 **What it is:** Implementing cloud environment best practices hinges on adopting a secure multi-account strategy. Use accounts as building blocks, and group them into [organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html#:~:text=You%20can%20use%20organizational%20units,OU%20automatically%20inherit%20the%20policy.), such as foundational OUs for security and infrastructure, and additional OUs for sandboxing and workloads.

 **Why it matters:** A multi-account strategy provides natural boundaries and isolation in your cloud environment. This in turn allows you to manage quotas and account limits, automate the provisioning and customization of accounts, and apply the principle of least privilege by restricting access to your management account. It enables visibility to track user activity and risk across your environment. Your multi-account strategy acts as the foundation on which you can build for migration projects or organizational changes like mergers and acquisitions.

 Use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to consolidate multiple AWS accounts into an organization, which you can use to allocate resources, group accounts, and apply governance policies.

 Use [AWS Control Tower](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-CTower.html) as an orchestration service, layered on top of AWS Organizations, to help structure your AWS estate, and extend governance over OUs and your multi-account environment.

------
#### [ Controls management best practices ]

 **What it is:** Implementing controls management best practices can include a range of approaches. Detective controls catch resources that violate defined security policies. Preventive controls protect security baselines by blocking specific actions. And proactive control scan resources before they are provisioned, stop non-compliant code from being deployed, and instruct developers to remediate them. Interoperable AWS services give you centralized governance and control over your entire IT estate, including AWS and third-party products, as you grow into new markets.

 **Why it matters:** Controls management best practices allow you to programmatically implement controls at scale, and automatically configure compliance or remediate non-compliance. This is particularly important if your organization operates in a regulated industry, such healthcare, life sciences, financial services, or the public sector, where specific regulatory frameworks apply, or adheres to specific corporate standards, or data residency and digital sovereignty requirements.

 Consider opportunities for orchestrating multiple AWS services to ensure your organization's security and compliance needs, using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), defining configuration settings and detecting deviation from them, using [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), and auditing AWS usage and compliance with regulations and industry standards, with [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html).

------
#### [ Cloud governance for developers ]

 **What it is:** Implementing cloud governance best practices for developers can include using infrastructure as code (IaC) to ensure repeatability and consistency in their work, and establishing processes to detect security vulnerabilities.

 **Why it matters:** This helps teams move fast while being confident in their governance processes. It gives developers a single source of truth that can be deployed to the whole stack, infrastructure that they can replicate, redeploy, and repurpose, the ability to control versioning on infrastructure and applications together, and a choice of self-service actions.

 Cloud governance for developers can also involve detecting security vulnerabilities in code. This helps them improve code quality, identify critical issues, ensure consistent release pipelines, and launch projects with blueprints.

 Consider how you might provide builders with pre-approved infrastructure-as-code templates, and corresponding IAM policies that dictate who, where, and how they can be used, using an AWS service like [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html).

------
#### [ Scalability and flexibility ]

 **What it is:** Choose AWS services that will help your cloud governance measures grow seamlessly with your infrastructure and adapt to evolving requirements. Consider how your organization will grow, and how fast.

 **Why it matters:** Considering scalability and flexibility helps you ensure that your cloud governance arrangements are robust, responsive, and capable of supporting dynamic business environments.

 To help you scale quickly, AWS Control Tower orchestrates the capabilities of several other [AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations and AWS IAM Identity Center, to build a landing zone in less than an hour. Control Tower sets up and manages resources on your behalf.

 AWS Organizations enables you to manage [40\+ services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)' resources across multiple accounts. This gives individual application teams the flexibility and visibility to manage cloud governance needs that are specific to their workload, while also giving them visibility to centralized teams.

------

## Choose an AWS cloud governance service
<a name="choose"></a>

 Now you know the criteria by which you will be evaluating your cloud governance options, you are ready to choose which AWS cloud governance service may be a good fit for your organizational needs. The following table highlights which services are optimized for which circumstances. Use it to help determine the service that is the best fit for your organization and use case.

|  Type of use case  |  When would you use it?  |  Recommended service  |
| --- | --- | --- |
|  Defining requirements  |  To provide on-demand downloads of AWS security and compliance documents.  |  [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)  |
|  Deploying and operating  |  To speed up cloud provisioning with infrastructure as code.  |  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)  |
|   |  To represent your ideal configuration settings and detect if AWS resources drift from it.  |  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)  |
|   |  To setup and orchestrate multiple AWS services on your behalf while helping you meet the security and compliance needs of your organization.  |  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)  |
|   |  To consolidate multiple AWS accounts into an organization, which you can use to allocate resources, group accounts, apply governance policies, and manage centrally and at scale.  |  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)  |
|   |  To run automated and continuous checks against the rules in a set of supported security standards.  |  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)  |
|   |  To provide builders with pre-approved infrastructure-as-code templates, and corresponding IAM policies, that dictate who, where, and how they can be used.  |  [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html)  |
|   |  To provide secure end-to-end management of resources on AWS and in multicloud and hybrid environments.  |  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)  |
|  Measuring and assessing  |  To audit AWS usage and assess risking and compliance with regulations and industry standards.  |  [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)  |
|   |  To enable operational and risk auditing, governance, and compliance of your AWS account.  |  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)  |
|   |  To monitor your AWS resources and the applications you run on AWS in real time.  |  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)  |
|   |  To manage software licenses from vendors centrally across AWS and your on-premises environments.  |  [AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)  |
|   |  To evaluate usage and configuration against best practices.  |  [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)  |

## Use an AWS cloud governance service
<a name="use"></a>

 You should now have a clear understanding of what each AWS cloud governance service does, and which ones might be right for you.

 To explore how to use and learn more about each of the available AWS cloud governance services, we have provided a pathway to explore how each of them works. The following sections provide links to in-depth documentation, hands-on tutorials, and other resources to get you started.

------
#### [ AWS Artifact ]
+ **Getting started with AWS Artifact**

  Download security and compliance reports, manage legal agreements, and manage notifications.

   [Explore the guide »](https://docs.aws.amazon.com/artifact/latest/ug/getting-started.html)
+ **Managing agreements in AWS Artifact**

  Use the AWS Management Console to review, accept, and manage agreements for your account or organization.

   [Explore the guide »](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)
+ **Prepare for an Audit in AWS Part 1 – AWS Audit Manager, AWS Config, and AWS Artifact**

  Use AWS services services to help you automate the collection of evidence that's used in audits.

   [Read the blog »](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-1-aws-audit-manager-aws-config-and-aws-artifact/)

------
#### [ AWS Audit Manager ]
+  **Getting started with AWS Audit Manager**

   Enable Audit Manager by using the AWS Management Console, the Audit Manager API, or the AWS CLI.

   [Explore the guide »](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html)
+  **Tutorial for Audit Owners: Creating an assessment**

   Create an assessment by using the Audit Manager Sample Framework.

   [Get started with the tutorial »](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-audit-owners.html)
+  **Tutorial for Delegates: Reviewing a control set**

   Review a control set that was shared with you by an audit owner in Audit Manager.

   [Get started with the tutorial »](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-delegates.html)

------
#### [ AWS CloudTrail ]
+  **View event history**

   Review the AWS API activity in your AWS account for services that support CloudTrail.

   [Get started with the tutorial »](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html)
+  **Create a trail to log management events**

   Create a trail to log management events in all Regions.

   [Get started with the tutorial »](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html)

------
#### [ AWS Config ]
+  **AWS Config features**

   Explore the resource tracking capabilities of AWS Config, from configuration histories and snapshots to customizable rules and conformance packs.

   [Explore the guidance »](https://aws.amazon.com/config/features/)
+  **How AWS Config Works**

   Dive deeper on AWS Config, and learn how the service discovers and tracks resources, and delivers configuration items through various channels.

   [Explore the guide »](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html)
+  **Risk and Compliance workshop**

   Automate controls by using AWS Config and AWS Managed Config Rules.

   [Explore the workshop »](https://catalog.us-east-1.prod.workshops.aws/workshops/dd2bea89-dc7a-4bda-966a-70b4ff6e90e0/en-US/3-detective-controls-config/1-config-setup)
+  **AWS Config Rule Development Kit library: Build and operate rules at scale**

   Use the Rule Development Kit (RDK) to build a custom AWS Config rule and deploy it with the RDKLib.

   [Read the blog »](https://aws.amazon.com/blogs/mt/aws-config-rule-development-kit-library-build-and-operate-rules-at-scale/)

------
#### [ AWS Control Tower ]
+  **Getting started with AWS Control Tower**

   Learn how to set up your landing zone using the AWS Control Tower console or APIs.

   [Explore the guide »](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)
+  **AWS Control Tower controls management workshop**

   Learn how to set up governance on your multi-account environment to align with AWS best practices and common compliance frameworks.

   [Explore the workshop »](https://catalog.workshops.aws/control-tower/en-US/controls)
+  **Modernizing Account Management with Amazon Bedrock and AWS Control Tower**

   Provision a security tooling account and leverage generative AI to expedite the AWS account setup and management process.

   [Read the blog »](https://aws.amazon.com/blogs/mt/modernizing-account-management-with-amazon-bedrock-and-aws-control-tower/)
+  **Building a well-architected AWS GovCloud (US) environment with AWS Control Tower**

   Set up your governance in the AWS GovCloud (US) Regions, including governing your AWS workloads by using Organizational Units (OUs) and AWS accounts.

   [Read the blog »](https://aws.amazon.com/blogs/mt/building-a-well-architected-aws-govcloud-us-environment-with-aws-control-tower/)

------
#### [ AWS Organizations ]
+  **Getting started with AWS Organizations**

   Learn how to start using AWS Organizations, including reviewing terminology and concepts, using consolidated billing, and applying organization policies.

   [Explore the guide »](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html)
+  **Creating and configuring an organization**

   Create your organization and configure it with two AWS member accounts.

   [Get started with the tutorial »](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html)
+  **Organizing Your AWS Environment Using Multiple Accounts**

   Learn how using multiple AWS accounts can help isolate and manage your business applications and data, and optimize across the AWS Well-Architected Framework pillars.

   [Read the whitepaper »](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
+  **Services that work with AWS Organizations**

   Understand which AWS services services you can use with AWS Organizations and the benefits of using each service on an organization-wide level.

   [Explore the guide »](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)
+  **Best Practices for Organizational Units with AWS Organizations**

   Dive deep into the recommended architecture of AWS best practices when building your organization, for OU structure and specific implementation examples.

   [Read the blog »](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/?org_product_gs_OUBlog)
+  **Achieving operational excellence with design considerations for AWS Organizations SCPs**

   Learn how SCPs help control access to AWS services and resources provisioned across multiple accounts created within an organization.

   [Read the blog »](https://aws.amazon.com/blogs/mt/achieving-operational-excellence-with-design-considerations-for-aws-organizations-scps/)

------
#### [ AWS Security Hub CSPM ]
+  **Enabling AWS Security Hub CSPM**

   Enable AWS Security Hub CSPM with AWS Organizations or in a standalone account.

   [Explore the guide »](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html)
+  **Cross-Region aggregation**

   Aggregate AWS Security Hub CSPM findings from multiple AWS Regions to a single aggregation Region.

   [Explore the guide »](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html)
+  **AWS Security Hub CSPM workshop**

   Learn how to use AWS Security Hub CSPM and to manage and improve the security posture of your AWS environments.

   [Explore the workshop »](https://catalog.workshops.aws/security-hub/en-US)
+  **Three recurring Security Hub CSPM usage patterns and how to deploy them**

   Learn about the three most common AWS Security Hub CSPM usage patterns and how to improve your strategy for identifying and managing findings.

   [Read the blog »](https://aws.amazon.com/blogs/security/three-recurring-security-hub-usage-patterns-and-how-to-deploy-them/)

------

## Explore AWS cloud governance resources
<a name="explore"></a>

 **Architecture diagrams**

 Explore reference architecture diagrams to help you develop your security, identity, and governance strategy.

[ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all)

 **Whitepapers**

 Explore whitepapers for more insights and best practices on choosing, implementing, and using the security, identity, and governance services that best fit your organization.

 [Explore whitepapers](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all)

 **Solutions**

 Use these solutions to further develop and refine your security, identity, and governance strategy.

 [Explore solutions](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all)

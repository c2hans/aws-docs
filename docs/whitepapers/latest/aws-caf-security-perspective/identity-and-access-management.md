---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/identity-and-access-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Identity and access management
<a name="identity-and-access-management"></a>

**Note**
 Securely manage human and machine identities and their permissions to cloud services and resources.

 [https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-and-access-management.html](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-and-access-management.html) determines who has access to what in AWS. You need robust identity and permissions management to make sure that the right people, machines, and services have access to the right resources under the right conditions.

 In this section, we're focused on how people and machines access your AWS accounts and resources; identity and access management for the applications you deploy in AWS is a topic for another paper.

 The scope of this topic extends beyond the AWS Identity and Access Management IAM service itself, to include all of the identity-related controls and features in AWS. Even if you don't use every capability, a comprehensive perspective will verify that your identity and access management practices remain scalable and responsive to business needs.

 Identity and access-related decisions for AWS will be made continuously by a variety of stakeholders throughout the enterprise. Define and communicate a strategy to inform those decisions. Your strategy might include:
+  **Objectives** - The desired outcomes of your IAM strategy
+  **Tenets** - Guiding principles so that delegated decisions support your objectives
+  **Delegation model** - To align stakeholder understanding of roles and responsibilities for access management (such as a RACI matrix)

 **Sample objectives**
+  Provide a safe place for builders to experiment, fail, and innovate at speed. This includes tools to quickly determine how and why their access is limited, and where to get help when needed.
+  Minimize the possibility of over provisioning permissions and enforce separation of duties to satisfy risk appetite, best practices, compliance, and regulatory requirements.
+  Focus your security experts on high-impact outcomes that only humans can deliver; automate the rest, such as guardrails checking roles and policy creation and changes.
+  Nearly continuous compliance: automate attestation and reporting, to deliver on-demand the insights that auditors and leaders need. An example is [security in the CI/CD pipeline](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html), and a Professional Services offering for Automated Continuous Compliance focused on GxP in Healthcare and Life Sciences.

 **Sample tenets**
+  **Guardrails, not gates** - Design controls to minimize friction around AWS Identity and Access Management in AWS. Use centralized, blocking, manual workflows only when there is no safe alternative. Strive for self-service.
+  **Security as code (SaC)** - Publish your security baseline as consumable code. Enforce governance in the toolchain. Make the best developer experience a side effect of strong security outcomes.
+  **Adopt the principle of *[least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)*** - This is a process of continuous improvement. [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies). Use automation, detective controls, and analytics to continually rightsize permissions for each role and environment.
+  **Keep people away from data** - At each stage of your software development lifecycle (SDLC), implement [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), mechanisms, and tools to decrease the need for direct access to data stores.
+  **Use [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) like AWS IAM roles by default** - Static users, passwords, and access keys are a last resort, issued by exception only. Where static credentials are used, secure them in a purpose-built secrets management system and [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials).

 **Sample delegation model**

 Delegation of responsibility for overlapping access controls is key to achieving [https://csrc.nist.gov/glossary/term/defense_in_depth](https://csrc.nist.gov/glossary/term/defense_in_depth). Using AWS IAM, you can avoid delays, mistakes, and missed opportunities that may come with fully centralized access management. As you consider who should be responsible for what, and where to implement particular controls, keep in mind the following:
+  Access management for *people* needs a different approach than access management for *machines and services*.
+  Changes should be approved and made by people with the best knowledge of the business and data being protected.
+  Agility and scalability require that developers and data custodians understand [permissions management in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html).
+  Permissions policy space in AWS is finite – use the best policy type for each control and make efficient use of all available policy types.

   Policy maximum size is one the few AWS service quotas that cannot be increased from defaults. For more details:
  +  Watch [Choosing the Right Mix of AWS IAM Policies for Scale](https://www.youtube.com/watch?v=o1bfA0SIxBk&secd_iam9) (video)
  +  Read [IAM Policy Types - How and When to Use Them](https://aws.amazon.com/blogs/security/iam-policy-types-how-and-when-to-use-them/?secd_iam8) (blog)

 Review sample access controls delegation model (R = responsible) in the following table.

|  AWS access control mechanism  |  Central cloud governance team  |  Central cloud IAM/ engineering team  |  Central security team  |  Workload /resource owners  |  AWS account owner  |
| --- | --- | --- | --- | --- | --- |
|  Organization structure  |  R  |   |   |   |   |
|  Organization policies (SCPs, AWS Control Tower Guardrails)  |  R  |   |   |   |   |
|  Identity policies for baseline human access  |   |  R  |   |   |   |
|  Identity policies for baseline account controls & services  |   |  R  |   |   |   |
|  Permissions boundaries  |   |   |  R  |   |   |
|  Resource policies for workloads  |   |   |   |  R  |   |
|  Identity policies for workloads  |   |   |   |  R  |   |
|  AWS account root password  |   |   |  R  |   |   |
|  AWS account root MFA token  |   |   |   |   |  R  |

 The example delegation model in Table 1 shows *separation of duties,* which makes it hard for any lone actor to circumvent all of the access controls that protect your AWS environment. Your teams may vary, but *no single team or person* should have authority over all of the access controls shown.

## Use AWS services for orchestration
<a name="use-aws-services-for-orchestration"></a>

 AWS often offers more than one solution to common problems. Sometimes this arises from customer feedback, which leads to the launch of new higher-level features to orchestrate existing lower-level ones. Two such examples are [AWS Control Tower](https://aws.amazon.com/controltower/) and [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/), which are offered at no extra charge. The costs of a custom solution will outweigh the benefits for most customers in the long term, especially as AWS continues to innovate.

 **Start**

 Bootstrap identity and access management for your AWS environment.

 **Credential management**

 AWS account root user management is the first capability needed to secure your AWS accounts. Your most sensitive AWS account is the one designated as your [AWS Organizations](https://aws.amazon.com/organizations/) management account and [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html). All AWS account root users, *especially* the management account root user, need a strong password in addition to multi-factor authentication (MFA). [https://docs.aws.amazon.com/accounts/latest/reference/best-practices-root-user.html#bp-root-limit-tasks](https://docs.aws.amazon.com/accounts/latest/reference/best-practices-root-user.html#bp-root-limit-tasks) and should be controlled by two people. For example, the individual or team that controls the root password of an AWS account should not also control its MFA token. Use a trusted password/privileged access management (PAM) solution to secure these secrets. Understand and periodically exercise the procedures for resetting AWS account [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys_retrieve.html#reset-root-password](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys_retrieve.html#reset-root-password) and [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html?icmpid=docs_iam_console#root-mfa-lost-or-broken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html?icmpid=docs_iam_console#root-mfa-lost-or-broken).

 Add MFA immediately to all accounts that allow password-based login to AWS. Use your existing enterprise MFA solution, if possible. For AWS account root users and IAM-users;, configure MFA in AWS IAM. For federated users, configure MFA in your existing identity provider (IdP) or in AWS IAM Identity Center. Treat static AWS IAM credentials as toxic and prohibit them by default. People access AWS through federated authorization. Evaluate [https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/) for on-premises or other non-AWS systems that need access to your AWS environment. Question vendors whose products require static IAM-users; and access keys; issue them only as a last resort and under a formal exception process, with automatic expiration.

 **Federation**

 To do anything in AWS, you first must grant access to the people who will build the foundation (landing zone) on which everything else is deployed. Federate your IdP with AWS. In this way, any [https://csrc.nist.gov/glossary/term/risk_adaptive_adaptable_access_control](https://csrc.nist.gov/glossary/term/risk_adaptive_adaptable_access_control), entitlements management, compliance, and reporting capabilities associated with your IdP will apply to AWS as well. The recommended approach is to [https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-connect-id-source-ad-idp-specify-user.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-connect-id-source-ad-idp-specify-user.html). AWS IAM Identity Center expands the capabilities of AWS Identity and Access Management (IAM) to centralize the administration of workforce access to AWS accounts. With Identity Center, you administer all human users and their permissions for your AWS Organizations in one place.

 When enabled in your management account, AWS IAM Identity Center is deployed in the currently selected AWS Region only. This choice does not limit access to other AWS Regions. However, if your chosen Identity Center Region were unavailable, your users would be unable to access Identity Center to authenticate to AWS or [https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html). Consider the risks of such an event and create a backup access plan that satisfies your [https://docs.aws.amazon.com/singlesignon/latest/userguide/resiliency-regional-behavior.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/resiliency-regional-behavior.html).

 Whatever federation solution you choose, you must define the [job functions, roles, and responsibilities](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/define-functions-and-responsibilities-to-manage-your-environment.html) that team members will use to do their work in AWS. Start simple and iterate. In the beginning, no more than two to three roles should be necessary. If you use AWS Control Tower to deploy a landing zone (see the following section), you can get started by using its default roles. Keep in mind the [https://martinfowler.com/bliki/Yagni.html](https://martinfowler.com/bliki/Yagni.html) and resist the urge to create several job or task-specific roles until you know how they'll be used. Role and policy sprawl can quickly become technical debt that can weaken your security posture and complicate audit and compliance matters.

 **Landing zone**

 Each AWS account is a security boundary for the identities and resources that it contains. This is why you need a multi-account strategy as described in the AWS whitepaper [https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html). Create a landing zone by configuring a multi-account environment according to AWS best practices and your business requirements. Workloads are then deployed atop the landing zone.

 For every AWS account in your landing zone, you'll need a consistent baseline configuration including a default set of permissions for people and services. Some elements of the baseline will be constants, but overall composition will vary depending on the purpose of the target AWS account. For example, non-production accounts should allow developers freedom to experiment, while production accounts should restrict all unnecessary services and actions. In either case, [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) should be enabled in every account, regardless of its purpose. Enforce using various types of AWS IAM policies that work together with orchestrated management.

 The preferred way to deploy and manage your landing zone is using AWS Control Tower. Control Tower automates AWS account creation and baseline configuration. It gives you a practical set of default permissions to start, and consistent governance across all of your AWS accounts as your needs evolve. Follow guidance in this AWS whitepaper *[Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html).* This embodies AWS best practices based on years of feedback and learning from our most successful customers.

 **Guardrails**

 [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) are a powerful tool for simplifying permissions management across your AWS Organizations. SCPs restrict permissions at the AWS account level, unlike other IAM policies that apply to individual identities or resources. To make efficient use of SCPs, you must organize your AWS accounts in a [https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/recommended-ous-and-accounts.html](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/recommended-ous-and-accounts.html) and apply SCPs to those OUs.

 Use SCPs for coarse-grained controls that don't change often. SCPs can impact multiple AWS accounts, and modification requires access to the management account. Therefore, updates should be strictly controlled, tested to the extent practical, and relatively infrequent as mistakes could interrupt all users and workloads in the specific OU.

 A good SCP use case is to restrict access to AWS Regions where your company doesn't operate. You can implement *[Regional restrictions directly in SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-deny-region)s* or use the [https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) in AWS Control Tower. Another good use of SCPs (and AWS Control Tower default) is to prevent local changes to resources that are deployed as part of your configuration baseline. Refer to [https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-controls.html](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-controls.html) and [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html) documentation for more information.

 Start using SCPs immediately. The risk of deploying major control changes via SCPs can be high, so it's best to start simple. Take an iterative approach to both the controls you implement and associated testing and deployment procedures. That way, when you need to make significant control change using SCPs, you'll have the mechanisms in place to do it safely and confidently.

 **Advance**

 Establish programs, procedures, and automation to govern identity and access management.

 **Metrics and monitoring**

 As soon as your initial landing zone is deployed, begin measuring your identity and access controls in AWS. Understanding current state (benchmarking) is the first step toward continuous improvement. It's important to measure cost-effectively, objectively, and consistently. Focus on fundamentals and measure things that are relevant to your security decision makers.

 [AWS Foundational Security Best Practices Standard](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) (FSBP) is a good place to start. FSBP defines IAM best practice controls that should be monitored in all of your AWS accounts. Compliance with FSBP IAM controls alone is not sufficient. Non-compliance means that key controls are either missing or ineffective and in need of prompt attention. Monitoring FSBP compliance is a [push-button operation](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html#securityhub-standard-enable-console) in AWS Security Hub CSPM.

 Create an [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) with your AWS Organization as the zone of trust, then monitor the findings. [https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-resource-identification](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-resource-identification) show when your AWS resources grant access to external principals. In other words, Access Analyzer findings help you identify security risks due to unintended access.

 An Access Analyzer finding indicates that the resource in the finding allows access to an external entity. (Access Analyzer findings do not tell you if external access has occurred.)This could be intentional, such as access granted to a vendor or partner, or it could be unintentional. It's important to investigate all active findings promptly so you can correct misconfigurations and prevent unauthorized access. [Use archive rules](https://aws.amazon.com/blogs/security/how-to-automatically-archive-expected-iam-access-analyzer-findings/) to hide findings related to expected, authorized access.

 Implement an organization-wide detective control that alerts on logins by AWS account root users. Triage each alert immediately. Any alert that can't be correlated to an approved change request should be escalated immediately to your security incident response team. Establish a program to remove all unnecessary root access, including weekly reporting and reviews by your CISO to drive compliance.

 **Security as code**

 Security as code (SaC) is an extension of the [infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) (IaC) concept, which says that security controls are codified in templates and managed as software. When modified templates are committed, automation verifies, tests, and deploys the updated controls to your AWS environment in a reliable, repeatable way.

 As reflected in the sample delegation model shown in Table 1 preceding:
+  Developers manage IAM resources for their application as part of its infrastructure code.
+  Separate, central teams manage IAM resources that span your AWS environment (for example, SCPs, permissions sets, baseline roles, and policies) as standalone workloads or as components of a *security baseline* workload.

 This approach lets you apply consistent governance via [https://pipelines.devops.aws.dev/](https://pipelines.devops.aws.dev/), without the concentration risk of a central team that creates or approves all AWS permissions. To begin, you must get all IAM resources (for example, roles, policies, service configurations, and others) codified and stored in an enterprise-managed version control system. Ideally, your version control system should support fine-grained access control, code review, approval workflows, and simplified CI/CD integration. Now that you're relying on a decentralized IAM model, use those features to implement preventive controls that enforce separation of duties and [stop policy violations before they reach AWS](https://aws.amazon.com/blogs/security/validate-iam-policies-in-cloudformation-templates-using-iam-access-analyzer/).

 For example, consider a version control repository that contains templates defining IAM policies/permission sets used by common roles in all your AWS accounts. Block all direct commits to the repository by default and require merge requests to be peer reviewed before being merged. Configure the merge process to initiate a pipeline that uses [AWS IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) to check the updated IAM policies, blocking the pipeline if problems are found. When the problems are resolved by a subsequent commit, the pipeline can continue through remaining stages and deploy the updated policies.

 [Permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/) (PB) enable you to safely delegate authority over IAM roles. A PB is an advanced policy type that sets the maximum permissions available to an identity, regardless of what's allowed in any other attached policies. Because PB can be independently controlled, you can use them to enforce conditions that can't be overridden elsewhere by delegates. Prevent over permissive access creation by developers in the identity policies. Grant them permission to use IAM, but add conditions requiring attachment of a specific PB to any role they create or update. If the PB is missing, AWS IAM will prevent the change.

 Use [https://aws.amazon.com/cdk/](https://aws.amazon.com/cdk/) to generate the roles and policies needed by your applications. You can attach a permissions boundary to all roles in an application with just a few lines of code. CDKs [https://docs.aws.amazon.com/cdk/v2/guide/constructs.html](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html) also lets you create a library of AWS resources customized to your security policies and environment, which developers can then consume as usual. Include [https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/](https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/) in your constructs to encourage best practices. CDK is a powerful tool for decentralized governance enforcement.

 **Least privilege automation**

 At scale, least privilege is a pursuit that requires automation to drive continuous improvements. Take an iterative approach, using preventive and detective controls to rightsize permissions throughout your SDLC.

 To refine permissions for a role, use [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to generate a policy template based on the role's access history, as captured in AWS CloudTrail. Then use AWS IAM Access Analyzer policy validation in your CI/CD pipelines to validate policies against grammar and best practices, before deployment. Together, these features take the guesswork out of creating initial permissions and periodically rightsize them to maintain least privilege.

 AWS IAM features like [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html), [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html), [https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html), [https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html), and [https://docs.aws.amazon.com/IAM/latest/UserGuide/example_iam_GetAccountAuthorizationDetails_section.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/example_iam_GetAccountAuthorizationDetails_section.html) provide valuable data about identities, permissions, and access history in AWS. You can also collate, enrich, and analyze outputs using services like [Amazon Athena](https://aws.amazon.com/athena/), [AWS Glue](https://aws.amazon.com/glue/), and [Quick](https://aws.amazon.com/quicksight/) to identify more opportunities to rightsize permissions and strengthen your security posture. Products from AWS Partners such as [https://partners.amazonaws.com/partners/0010L00001w1CzcQAE/Sonrai%20Security,%20Inc.](https://partners.amazonaws.com/partners/0010L00001w1CzcQAE/Sonrai%20Security,%20Inc.) and [https://partners.amazonaws.com/partners/0010h00001e7la0AAA/Ermetic](https://partners.amazonaws.com/partners/0010h00001e7la0AAA/Ermetic) can go further to produce sophisticated, identity, and access related insights that can help make faster, risk-informed decisions.

 **Excel**

 Focus on efficiency, continuous improvements, and operational excellence.

 **Zero Trust**

 AWS has long led with a [https://aws.amazon.com/security/zero-trust/](https://aws.amazon.com/security/zero-trust/), using Transport Layer Security (TLS) and [https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate and authorize every single API call, regardless of its origin. AWS capabilities enable you to implement Zero Trust concepts for your part of the AWS Shared Responsibility Model. But Zero Trust is not a universal solution. For more details:
+  Read [Zero Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/) (blog)
+  Watch [Zero Trust on AWS: Steve Schmidt, VP of Security Engineering & CISO, AWS (11:12)](https://youtu.be/lf_QANMFDfU) (video)

Security controls should be chosen based on the use case and business value of the assets to be protected.

## Data perimeter
<a name="data-perimeter"></a>

 Build a [https://aws.amazon.com/identity/data-perimeters-on-aws/](https://aws.amazon.com/identity/data-perimeters-on-aws/) to protect your AWS accounts and resources. A data perimeter overlays your existing, fine-grained controls with coarse-grained ones that allow access only if a request exclusively involves trusted identities, trusted resources, and expected networks. To establish a data perimeter, implement preventive controls that restrict access from outside of your AWS Organizations boundary. Those permissions are applied primarily using SCPs, [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html), and [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies). For detailed guidance and examples, see the AWS whitepaper [https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html).

 **ABAC**

 As you scale and implement more sophisticated authorization strategies, some permissions management use cases can be simplified by using [https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html). ABAC is part of IAM, and you can use ABAC, role-based access control (RBAC), or both together based on your needs. Implement ABAC in AWS by attaching tags to IAM entities like roles and users, and to resources like [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instances or [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) keys. Then write policies that allow or deny access, based on the values of those tags. In the case of a data perimeter, use ABAC to exempt specific users or roles from specific controls, without making high-risk policy changes.

 If consistent resource tagging is already in place, ABAC will be easier to implement. [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html) and [detective controls](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) for enforcement. Don't wait until you need ABAC to get started with tag governance. With ABAC, tags are a *key* element of your authorization security controls. Implement [trust policies over your IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/). Tag values can be set statically on IAM entities or you can use [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html). For federated/human user access, [https://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html) across all of your AWS accounts and Region

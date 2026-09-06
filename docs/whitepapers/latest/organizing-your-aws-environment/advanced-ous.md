---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/advanced-ous.html
---

# Advanced OUs
<a name="advanced-ous"></a>

## Individual Business Users OU
<a name="individual-business-users-ou"></a>

 The Individual Business Users OU houses accounts for individual business users and teams who need access to directly manage AWS resources outside the context of resources managed within your Workloads OU.

 In some cases, you can consider a small number of AWS resources as something other than a workload. For example, a business team might require write access to Amazon S3 buckets to share marketing videos and data with a business partner. In these cases, you might choose to manage these resources in accounts within the individual business users OU rather than in accounts in the Workloads OU.

### Controls
<a name="controls"></a>

 We recommend that you apply a combination of SCPs and IAM permissions to this OU and authorized users. This ensures that only those AWS services, resources, and actions needed are granted. Depending on the nature of the use cases, you can apply controls to individual accounts in this OU.

### Services that do not require direct user access to accounts
<a name="services-that-do-not-require-direct-user-access-to-accounts"></a>

 The individual business users OU does not apply when users can authenticate and be authorized to interact with applications and services without requiring direct access to an account. For example, business users often need access to Quick for business intelligence (BI) purposes.

 Assuming that you consider your QuickSight-based BI capability a workload, you can position the QuickSight resources and data in a workloads account in the Workloads OU. In this case, BI users are authorized to access the QuickSight service directly without needing access at the account level.

## Deployments OU
<a name="deployments-ou"></a>

 The Deployments OU contains resources and workloads that support how you build, validate, promote, and release changes to your workloads. You might already be using continuous integration/continuous delivery (CI/CD) capabilities to help manage and automate how changes to various types of source code are processed.

### Using CI/CD capabilities residing outside of your AWS environment
<a name="using-cicd-capabilities-residing-outside-of-your-aws-environment"></a>

 If you already use on-premises and/or managed CI/CD and related capabilities that reside outside of your AWS environment and you do not expect to use and/or manage CI/CD services within your AWS environment in the near term, you might not immediately need to establish the Deployments OU and an associated set of CI/CD oriented accounts.

 In this scenario, you must work through any access and potential network connectivity dependencies between your CI/CD capabilities residing outside of your AWS environment and your workloads environments in AWS.

### Separating CI/CD management capabilities from workloads
<a name="separating-cicd-management-capabilities-from-workloads"></a>

 If you intend to deploy and/or manage your own CI/CD capabilities in AWS or use AWS managed CI/CD services, we recommend that you use a set of production deployment accounts within the Deployments OU to house the CI/CD management capabilities.

 Reasons for separating your CI/CD management capabilities from your workload environments include:
+  **Critical roles played by CI/CD capabilities** — Your CI/CD capabilities are responsible for orchestrating quality validation, security compliance checks, building and publishing production candidate artifacts, promoting artifacts, and ultimately triggering release of artifacts to production environment.

   Given the critical nature of these roles, it's important that you can apply appropriate policies and operational practices to your CI/CD capabilities that are different than those applied to your workload environments.

   For example, your CI jobs and CD pipelines typically need write access to publish and promote candidate artifacts to an artifact management service. However, your production workload environments should only require read access to artifact management services in order to obtain the already built and promoted artifacts.
+  **CD pipelines affect non-production and production workload environments** – When CD pipelines orchestrate the validation of changes and ultimately trigger the release of changes to production, the pipelines often need to access workloads residing in both non-production test and production workload environments. For example, if you manage your CI/CD capabilities in your production workload environments, then you must allow the production workload environments to access your non-production environments. By centralizing your CI/CD capabilities in your CI/CD accounts, you can avoid enabling your production workload environments access to non-production environments.
+  **CI/CD capabilities depend on unique tooling** – Your CI/CD management capabilities, CI jobs, and CD pipelines often depends on tools that are different from those required to run and operate your workloads. Limiting the use of these tools to your CI/CD accounts can help you reduce the complexity and attack surface of your workload environments.

### Running CI jobs and CD build stages in deployment accounts
<a name="running-ci-jobs-and-cd-build-stages-in-deployment-accounts"></a>

 Because CI jobs and CD pipeline build stages are responsible for generating formal candidate artifacts, we recommend that you perform these activities in a production environment. Rather than perform these activities in your production workload environments, we recommend that you run them in your production CI/CD accounts.

## Business Continuity OU
<a name="business-continuity-ou"></a>

**Note**
 The Business Continuity OU is an advanced use-case topic where your AWS Organization requires data isolation and data residency controls based on unique workloads requirements. In general, most cross account disaster recovery strategies can be implemented through using the Backup account within the Infrastructure OU.

 The Business Continuity OU is intended to help teams implement a cross-account disaster recovery strategy. The data is as close to air-gapped as possible and the OU has no workload resources. This creates a secure data bunker to help protect your organization and allow for recovery from severe disasters like ransomware. The secure data bunker should only be accessed when the disaster recovery data for a workload is unavailable, untrustworthy, or destroyed.

 The Business Continuity OU does not replace normal disaster recovery plans of your workloads. It's an additional layer of protection that is meant to enhance the resiliency of your organization. General recommendations for disaster recovery for workloads can be found in [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html).

 For organizations that have data residency requirements and are in a geographical area that has only a single AWS Region available, using [AWS Outposts](https://aws.amazon.com/outposts/) can assist in maintaining compliance. The blog [Ensure Workload Resiliency and Comply with Data Residency Requirements with AWS Outposts](https://aws.amazon.com/blogs/architecture/ensure-workload-resiliency-and-comply-with-data-residency-requirements-with-aws-outposts/).

### Controls
<a name="controls-1"></a>

 For the Business Continuity OU to be a secure data bunker, access should be heavily restricted to prevent the data from being compromised. Ideally, users with access to the data within the Business Continuity OU should not have access to the regular environment and users with access to the regular environment should not have access to the Business Continuity OU. Apply a combination of SCPs and IAM permissions to this OU and authorized users to ensure that only those AWS services, resources, and actions needed are granted.

### Additional considerations
<a name="additional-considerations"></a>
+  Place restrictions on the Backup Administrator role so that backup policies for the Business Continuity OU are not altered.
+  Implement monitoring notifications to confirm that backups have not been interrupted. Refer to the documentation on [AWS Backup monitoring.](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html)
+  Require all Backup Vaults use [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) in Compliance mode with a minimum retention of 14 days or more.
+  Audit backups regularly to ensure compliance of your backup policies. Refer to the documentation on [AWS Backup Audit Manager.](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html)

### Example structures
<a name="example-structures"></a>

 In this example, a company, Rainbows, has a starter AWS environment that follows the production starter organization guidance. Rainbows has three workloads called A, B, and C. They have separate testing and production accounts for each. The data for workloads A and B are non-sensitive and unregulated. However, the data for workload C is highly sensitive and regulated and must be isolated from other workload data.

 Following is an example of the Business Continuity OU for the Rainbows company. Because the data for workloads A and B is non-sensitive and unregulated, you can keep it in the same business continuity (`bc`) account, `bc-workload-test-data` and `bc-workload-prod-data`. However, for workload C, the business continuity data is isolated in separate accounts, `bc-workload-c-test-data` and `bc-workload-c-prod-data`, because the workload is highly sensitive and regulated.

**Note**
 Some companies choose to keep each workload's data separated in individual accounts for an enhanced security posture, regardless of a regulatory or compliance need.

![Diagram showing Business Continuity OU example structure](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-business-continuity-ou.png)

## Organizing workload-oriented OUs
<a name="organizing-workload-oriented-ous"></a>

 The recommended **Security OU and accounts, Infrastructure OU and accounts, Workloads OU, and Deployments OU** are top-level OUs that contain workloads. This section outlines considerations for organizing these workload-oriented OUs.

**Topics**
+ [Workloads and environments](#workloads-and-environments)
+ [Workloads](#workloads)
+ [Workload environments](#workload-environments)
+ [Workload accounts](#workload-accounts)
+ [Production and non-production workload environments](#production-and-non-production-workload-environments)
+ [Workload dependencies across environments](#workload-dependencies-across-environments)
+ [Production environments accessing non-production](#production-environments-accessing-non-production)
+ [Non-production environments accessing dependencies](#non-production-environments-accessing-dependencies)

### Workloads and environments
<a name="workloads-and-environments"></a>

 This section defines basic terms and concepts related to workloads. Becoming aware of these concepts helps you understand our recommendations for organizing your workload-oriented OUs.

### Workloads
<a name="workloads"></a>

 Many of your top-level OUs will house collections of applications, cloud resources, and data in the form of workloads. A workload is a discrete collection of components and data that you manage. A workload can be a commercial off-the-shelf (COTS) application or your own custom application and data service.

![Diagram showing the composition of a workload](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/workload-composition.png)

### Workload environments
<a name="workload-environments"></a>

 For a given type of workload, you typically have multiple instances. This setup means that you can experiment, develop, and test changes to the workload before you promote and deploy those changes to the production instances of the workload. A given instance of a workload is a *workload environment.*

 Whether your workload is a COTS application, a custom application, a custom data service, or a foundational security or infrastructure capability, you often need separate non-production workload environments to support your software development lifecycle (SDLC) processes. You can have multiple SDLC processes depending on the diversity of your workload portfolio and your company organization.

 The following example shows multiple environments of a workload across non-production test and production workload environments.

![Diagram showing example of multiple environments of a workload](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/multiple-environments-of-a-workload.png)

 With COTS applications, you might not perform custom development, apart from implementing custom integrations with your own systems. However, you can experiment with and formally test new versions of the COTS applications in non-production environments before deploying them to production.

### Workload accounts
<a name="workload-accounts"></a>

 In your on-premises context, you can refer to the places where your workloads reside as hosting environments. For example, you might have a dedicated production hosting environment in which your production workload environments reside.

 In AWS, each of your workload environments is typically contained in an account, where each account is similar to a distinct hosting environment.

 Depending on how you choose to scope your workload accounts, you might have a single workload environment per account. Or, you might have multiple workload environments and perhaps multiple workload types in the same workloads account.

 The following diagram shows two degrees of scoping production workload accounts. In one example, a workload account is dedicated to a single workload environment. In the other example, multiple workload types reside in a single production workload account.

![Diagram showing example workload accounts with different degrees of scoping](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-workload-accounts.png)

### Production and non-production workload environments
<a name="production-and-non-production-workload-environments"></a>

 We recommend that you isolate production workload environments and data in production accounts housed within production OUs, under your top-level workload-oriented OUs. Apart from production OUs, we recommend that you define one or more non-production OUs that contain accounts and workload environments that are used to develop and test workloads.

### Workload dependencies across environments
<a name="workload-dependencies-across-environments"></a>

 When you consider the structure of your workload-oriented OUs, you should decide on the extent to which you expect access between production and non-production environments.

### Production environments accessing non-production
<a name="production-environments-accessing-non-production"></a>

 Generally, workloads deployed to your production environments should not depend on workloads contained in your non-production environments.

### Non-production environments accessing dependencies
<a name="non-production-environments-accessing-dependencies"></a>

 In non-production environments, it is common for workloads to depend on stable shared application, data, and infrastructure services. Where feasible, we recommend that these shared services be non-production test instances. These non-production test instances should use test data so that your non-production workloads do not depend on access to your production environments and data.

 For example, you can configure workloads in a non-production test environment that depend on integrating with a data service to use a stable, shared test instance of the service that is populated with test data.

 However, in some cases non-production environments might need access to production shared services. For example, it's typical for non-production development and test environments to require read-only access to shared source code and artifact management services. Providing access to these shared services enables you to deploy candidate and promoted changes and artifacts to your non-production environments in support of development and testing activities.

## OU structure for non-production environments
<a name="ou-structure-for-non-production-environments"></a>

 You can use OUs to organize your non-production environments in a couple ways.

### Option A: Common controls across non-production environments
<a name="option-a-common-controls-across-non-production-environments"></a>

 When non-production workloads require the same set of overall access policies or benefit from being operationally managed together, you can define a single NonProd OU to contain all the accounts that support non-production forms of your workloads.

 The following example shows the Workloads OU where a Prod child OU contains production accounts and workloads, and a NonProd child OU combines both development and test accounts and workloads.

![Diagram showing example Workloads OU with common policies across a NonProd child OU](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-workloads-ou-common-policies.png)

### Option B: Different controls across non-production environments
<a name="option-b-different-controls-across-non-production-environments"></a>

 Sometimes your process for developing and testing changes involves workload environments that have fundamentally different access policies or ways in which you manage and apply foundational resources. In these cases, it makes sense to create distinct OUs to support these diverse requirements.

 For example, you want to support development environments that provide teams with more freedom to experiment, iterate, and develop largely on their own (rather than more formally managed and controlled production-like test environments). In this case, overall access policies and management of baseline resources for the development environments is significantly different than those used to support test environments. It makes sense for you to create a distinct OU for development work and another OU for your test workloads.

 The following example represents a simple form of this structure where Test and Dev OUs reside adjacent to the recommended Prod OU.

![Diagram showing example Workloads OU with different policies for Test and Dev child OUs](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-workloads-ou-diff-policies.png)

 The preceding example shows two different approaches to scoping development environment accounts. One approach is where development environments are aligned with the same groupings of workloads as used in test and production OUs. The other approach is one in which development environments are aligned based on teams.

## Extended workload-oriented OU structure
<a name="extended-workload-oriented-ou-structure"></a>

 An extended form of the workload-oriented OU structure can be used to support cases in which you need to either organize workloads for visibility and management purposes or apply different security and operational policies to either a workload or group of related workloads.

 When workloads have diverse security and operational policy requirements, you cannot effectively manage controls and other controls at the level of the workload-oriented OU. By adding child OUs to a workload-oriented OU, you can group related workloads in the same child OU. You can then apply distinct security and operational policies to the child OUs.

 For example, a workload or a group of related workloads might benefit from having a distinct allow list of AWS services that is implemented via a service control policy (SCP). This policy might be different than the requirements associated with other workloads. Rather than applying the SCP to each of the related workload accounts, it is recommended that you apply the SCP to an OU that groups the related accounts.

### Grouping related workloads
<a name="grouping-related-workloads"></a>

 When you have groups of related workloads that require the same overall set of security and operational policies, you can create a child OU for each group of workloads.

 For example, if you manage a series of database services that are shared across your organizations and have common security and operational policy requirements, you might find value in grouping those data services under a common child OU.

![Diagram showing a group of workloads with distinct policy requirements](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/group-of-workloads-with-distinct-policy-rqmts.png)

 The following example represents a shared backup capability you can provide across your AWS environment. If this capability requires a set of security and operational policies that are distinct from other infrastructure workloads, then you can allocate a distinct OU for this workload.

![Diagram showing a single workload with distinct policy requirements](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/single-workload-with-distinct-policy-rqmts.png)

### Separating business units with significantly different policies
<a name="separating-business-units-with-significantly-different-policies"></a>

 If you have largely autonomous business units (BUs) that manage workloads in your common AWS organization and the BUs have significantly different security and operational policies, you can create a child OU under your Workloads OU for each BU.

 In the following example, each BU is provided with its own OU so that different SCPs and/or operational policies can be applied independently from the other OUs.

![Diagram showing an example business unit separation](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-business-unit-separation.png)

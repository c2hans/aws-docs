---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/guidance-overview.html
---

# Guidance overview
<a name="guidance-overview"></a>

**Note**
Publication date: *November 2022 (last update: September 2026)*. Check the [CHANGELOG.md](https://github.com/aws-solutions-library-samples/account-assessment-for-aws-organizations/blob/main/CHANGELOG.md) file in the GitHub repository to see all notable changes and updates to the software.

This guidance allows customers to better understand [AWS Organizations](https://aws.amazon.com/organizations/) dependencies by finding [trusted access enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) AWS services, delegated admin accounts, and identity-based, resource-based and service control policies.

Businesses are increasing their adoption of AWS Organizations to easily create accounts, allocate resources, create group accounts, and apply governance policies to accounts or groups. However, when businesses need to consolidate AWS Organizations or move AWS accounts between AWS Organizations, system administrators are often challenged to clearly understand the business impact of their account integrations. The process to manually evaluate AWS Organizations dependencies can be time consuming—​potentially involving reviews of tens or even hundreds of AWS resources of individual accounts.

The Guidance for Account Assessment for AWS Organizations performs the following functions:
+ Programmatically scans all AWS accounts in an AWS Organization for identity-based, resource-based and service control policies.
+ Presents scan results in a web user interface (web UI) that tracks resources in your AWS Organization.
+ Enables the user to search through the scanned policies and find conditions, dependencies and specific actions in your policies across your AWS organization.
+ Runs the policy scan daily to keep the information about your policies up to date.

This implementation guide provides an overview of the Guidance for Account Assessment for AWS Organizations, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the guidance to the Amazon Web Services (AWS) Cloud.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this guidance.<br />The estimated baseline cost for running this guidance in the US East (Northern Virginia) Region is USD $45 per month, depending on your specific implementation. |  [Cost](cost.md)  |
| Understand the security considerations for this guidance. |  [Security](security.md)  |
| Know how to plan for quotas for this guidance. |  [Quotas](quotas.md)  |
| Know which AWS Regions are supported for this guidance. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| Deploy the guidance from source by using the AWS Cloud Development Kit (AWS CDK). |  [Deploy the guidance](deploy-the-guidance.md)  |
| Access the source code and contribute customizations. |  [GitHub repository](https://github.com/aws-solutions-library-samples/account-assessment-for-aws-organizations)  |

This guide is intended for solution architects, DevOps engineers, data scientists, and cloud professionals who want to implement Guidance for Account Assessment for AWS Organizations in their environment.

**Important**
We designed this guidance to aggregate scan findings for customers. This guidance does not check the validity or correctness of your underlying resource-based policies. When changing policies that allow account migration to another AWS Organization, we recommend:
Verifying that your policies work as intended before making changes.
Using [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) [Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to verify that your policies achieve your required permissions.
Reviewing and updating the [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) policy element to meet your security requirements. Do not delete the `Condition` without reviewing the underlying impact.
Engaging with AWS Solutions Architects, Technical Account Managers, and AWS Professional Services to review your AWS Organizations-based dependencies identified by the guidance before initiating account migration.

**Note**
Dependencies outside the scope of this guidance can impact the account migration between AWS Organizations (for example, [quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html), resources shared by [AWS Resource Access Manager](https://aws.amazon.com/ram/) [AWS RAM], and service-managed CloudFormation [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)).

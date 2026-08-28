---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/next-steps.html
---

# Next steps
<a name="next-steps"></a>

You can use the information and examples in this guide to start applying the principle of least privilege in your organization. We recommend that you review the additional resources in the [Resources](resources.md) section, which contains documentation references and tools that can help you refine your policies.

This guide is intended to help you start implementing least-privilege access for AWS CloudFormation. However, there are additional types of policies that can help you strengthen the principle of least-privilege in your organization. Based on your environment and business requirements, you might want to implement additional controls that are not discussed in this guide. As a next step and for more information, we recommend that you review the following topics related to least privilege and configuring access and permissions:
+ [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
+ [Service control policies (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
+ [Roles for cross-account access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html#role_cross-account)
+ [Identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html#id-federation)
+ [Viewing last accessed information for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html)

The following tools can help you monitor least-privilege access and permissions for CloudFormation:
+ [AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
+ You can use the [Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html) tab in the AWS Identity and Access Management (IAM) console to identify excessive permissions for IAM identities. For an example, see [Tighten S3 permissions for your IAM users and roles using access history of S3 actions](https://aws.amazon.com/blogs/security/tighten-s3-permissions-iam-users-and-roles-using-access-history-s3-actions/) (AWS blog post).
+ You can use a linting tool, such as [cfn-policy-validator](https://github.com/awslabs/aws-cloudformation-iam-policy-validator) (GitHub), to help identify excessive permissions.

When you are comfortable with creating and managing CloudFormation permissions, it is recommended that you use continuous integration and continuous delivery (CI/CD) pipelines to deploy your CloudFormation templates. This reduces the risk of human errors and speeds up your deployment process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

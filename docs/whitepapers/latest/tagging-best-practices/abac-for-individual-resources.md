---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/abac-for-individual-resources.html
---

# ABAC for individual resources
<a name="abac-for-individual-resources"></a>

 IAM Identity Center users and IAM roles support attribute-based access control (ABAC), which allows you to define access to operations and resources based on tags. ABAC helps reduce the need to update permission policies and helps you to base access off of employee attributes from your corporate directory. If you are already using a multi-account strategy, ABAC can be used in addition to role-based access control (RBAC) to provide multiple teams operating in the same account granular access to different resources. For example, IAM Identity Center users or IAM roles can include conditions to limit access to specific Amazon EC2 instances which otherwise would have to be explicitly listed in each policy in order to access them.

 Since an ABAC authorization model depends on tags for access to operations and resources, it is important to provide guardrails to prevent unintended access. SCPs can be used to protect tags across your organization by only allowing tags to be modified under certain conditions. The blogs [Securing resource tags used for authorization using a service control policy in AWS Organizations](https://aws.amazon.com/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/) and [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) provide information on how to implement this.

 Where long-lived Amazon EC2 instances are being used to support more traditional operations practices then this approach can be utilized, the blog [Configure IAM Identity Center ABAC for Amazon EC2 instances and Systems Manager Session Manager](https://aws.amazon.com/blogs/security/configure-aws-sso-abac-for-ec2-instances-and-systems-manager-session-manager/) discusses this form of attribute based access control in more detail. As mentioned earlier, not all resource types support tagging, and of those that do, not all support enforcement using tag policies, so it’s a good idea to evaluate this prior to starting to implement this strategy on an AWS account.

To learn about services that support ABAC, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

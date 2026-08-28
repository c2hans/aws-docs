---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_permissions_least_privileges.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP02 Grant least privilege access
<a name="sec_permissions_least_privileges"></a>

Grant only the access that identities require by allowing access to specific actions on specific AWS resources under specific conditions. Rely on groups and identity attributes to dynamically set permissions at scale, rather than defining permissions for individual users. For example, you can allow a group of developers access to manage only resources for their project. This way, when a developer is removed from the group, access for the developer is revoked everywhere that group was used for access control, without requiring any changes to the access policies.

 **Common anti-patterns:**
+ Defaulting to granting users administrator permissions.
+ Using the root user for day-to-day activities.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Establishing a principle of [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) ensures that identities are only permitted to perform the most minimal set of functions necessary to fulfill a specific task, while balancing usability and efficiency. Operating on this principle limits unintended access and helps ensure that you can audit who has access to which resources. In AWS, identities have no permissions by default except for the root user. The credentials for the root user should be tightly controlled and only be used for [tasks that require root user credentials](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html).

You use policies to explicitly grant permissions attached to IAM or resource entities, such as an IAM role used by federated identities or machines, or resources (for example, S3 buckets). When you create and attach a policy, you can specify the service actions, resources, and conditions that must be true for AWS to allow access. AWS supports a variety of conditions to help you scope down access. For example, using the `PrincipalOrgID` [condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html), the identifier of the AWS Organizations is verified so access can be granted within your AWS Organization.

You can also control requests that AWS services make on your behalf, such as AWS CloudFormation creating an AWS Lambda function by using the `CalledVia` condition key. You should layer different policy types to effectively limit the overall permissions within an account. For example, you can allow your application teams to create their own IAM policies, but use a [Permission Boundary](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/) to limit the maximum permissions they can grant.

There are several AWS capabilities to help you scale permission management and adhere to the principle of least privilege. [Attribute Based Access control](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/) allows you to limit permissions based on the *[tag](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)* of a resource, for making authorization decisions based on the tags applied to the resource and the calling IAM principal. This enables you to combine your tagging and permissions policy to achieve fine-grained resource access without needing many custom policies.

Another way to accelerate creating a least privilege policy, is to base your policy on CloudTrail permissions after an activity runs. [AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) (IAM Access Analyzer) can automatically generate an IAM policy based on activity. You can also use IAM Access Analyzer at the Organization or individual account level to [track the last accessed information for a particular policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html).

Establish a cadence of reviewing these details and removing unneeded permissions. You should establish permissions guardrails within your AWS Organization to control the maximum permissions within any member account. Services such as [AWS Control Tower have prescriptive managed preventative controls](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails.html) and allow you to define your own controls.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
+  [Techniques for writing least privilege IAM policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/)
+  [IAM Access Analyzer makes it easier to implement least privilege permissions by generating IAM policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
+  [Delegate permission management to developers by using IAM permissions boundaries](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/)
+  [Refining Permissions using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)
+  [IAM policy types and when to use them](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
+  [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
+  [Guardrails in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails.html)
+  [Zero Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/)
+  [How to implement the principle of least privilege with CloudFormation StackSets](https://aws.amazon.com/blogs/security/how-to-implement-the-principle-of-least-privilege-with-cloudformation-stacksets/)

 **Related videos:**
+  [Next-generation permissions management](https://www.youtube.com/watch?v=8vsD_aTtuTo)
+  [Zero Trust: An AWS perspective](https://www.youtube.com/watch?v=1p5G1-4s1r0)
+  [How can I use permissions boundaries to limit users and roles to prevent privilege escalation?](https://www.youtube.com/watch?v=omwq3r7poek)

 **Related examples:**
+  [Lab: IAM permissions boundaries delegating role creation](https://wellarchitectedlabs.com/Security/300_IAM_Permission_Boundaries_Delegating_Role_Creation/README.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

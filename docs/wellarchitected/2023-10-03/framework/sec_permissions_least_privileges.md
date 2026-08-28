---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_permissions_least_privileges.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP02 Grant least privilege access
<a name="sec_permissions_least_privileges"></a>

 It's a best practice to grant only the access that identities require to perform specific actions on specific resources under specific conditions. Use group and identity attributes to dynamically set permissions at scale, rather than defining permissions for individual users. For example, you can allow a group of developers access to manage only resources for their project. This way, if a developer leaves the project, the developer’s access is automatically revoked without changing the underlying access policies.

**Desired outcome:** Users should only have the permissions required to do their job. Users should only be given access to production environments to perform a specific task within a limited time period, and access should be revoked once that task is complete. Permissions should be revoked when no longer needed, including when a user moves onto a different project or job function. Administrator privileges should be given only to a small group of trusted administrators. Permissions should be reviewed regularly to avoid permission creep. Machine or system accounts should be given the smallest set of permissions needed to complete their tasks.

**Common anti-patterns:**
+  Defaulting to granting users administrator permissions.
+  Using the root user for day-to-day activities.
+  Creating policies that are overly permissive, but without full administrator privileges.
+  Not reviewing permissions to understand whether they permit least privilege access.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 The principle of [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) states that identities should only be permitted to perform the smallest set of actions necessary to fulfill a specific task. This balances usability, efficiency, and security. Operating under this principle helps limit unintended access and helps track who has access to what resources. IAM users and roles have no permissions by default. The root user has full access by default and should be tightly controlled, monitored, and used only for [tasks that require root access](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html).

 IAM policies are used to explicitly grant permissions to IAM roles or specific resources. For example, identity-based policies can be attached to IAM groups, while S3 buckets can be controlled by resource-based policies.

 When creating an IAM policy, you can specify the service actions, resources, and conditions that must be true for AWS to allow or deny access. AWS supports a variety of conditions to help you scope down access. For example, by using the `PrincipalOrgID` [condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html), you can deny actions if the requestor isn’t a part of your AWS Organization.

 You can also control requests that AWS services make on your behalf, such as AWS CloudFormation creating an AWS Lambda function, using the `CalledVia` condition key. You should layer different policy types to establish defense-in-depth and limit the overall permissions of your users. You can also restrict what permissions can be granted and under what conditions. For example, you can allow your application teams to create their own IAM policies for systems they build, but must also apply a [Permission Boundary](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/) to limit the maximum permissions the system can receive.

 **Implementation steps**
+  **Implement least privilege policies**: Assign access policies with least privilege to IAM groups and roles to reflect the user’s role or function that you have defined.
  +  **Base policies on API usage**: One way to determine the needed permissions is to review AWS CloudTrail logs. This review allows you to create permissions tailored to the actions that the user actually performs within AWS. [IAM Access Analyzer can automatically generate an IAM policy based](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/) [on activity](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/). You can use IAM Access Advisor at the organization or account level to [track](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) [the last accessed information for a particular policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html).
+  **Consider using [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html).** When starting to create fine-grained permissions policies, it can be difficult to know where to start. AWS has managed policies for common job roles, for example billing, database administrators, and data scientists. These policies can help narrow the access that users have while determining how to implement the least privilege policies.
+  **Remove unnecessary permissions:** Remove permissions that are not needed and trim back overly permissive policies. [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) can help fine-tune permissions policies.
+  **Ensure that users have limited access to production environments:** Users should only have access to production environments with a valid use case. After the user performs the specific tasks that required production access, access should be revoked. Limiting access to production environments helps prevent unintended production-impacting events and lowers the scope of impact of unintended access.
+ **Consider permissions boundaries:** A permissions boundary is a feature for using a managed policy that sets the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries.
+  **Consider [resource tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) for permissions:** An attribute-based access control model using resource tags allows you to grant access based on resource purpose, owner, environment, or other criteria. For example, you can use resource tags to differentiate between development and production environments. Using these tags, you can restrict developers to the development environment. By combining tagging and permissions policies, you can achieve fine-grained resource access without needing to define complicated, custom policies for every job function.
+  **Use [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) for AWS Organizations.** Service control policies centrally control the maximum available permissions for member accounts in your organization. Importantly, service control policies allow you to restrict root user permissions in member accounts. Also consider using AWS Control Tower, which provides prescriptive managed controls that enrich AWS Organizations. You can also define your own controls within Control Tower.
+  **Establish a user lifecycle policy for your organization:** User lifecycle policies define tasks to perform when users are onboarded onto AWS, change job role or scope, or no longer need access to AWS. Permission reviews should be done during each step of a user’s lifecycle to verify that permissions are properly restrictive and to avoid permissions creep.
+  **Establish a regular schedule to review permissions and remove any unneeded permissions:** You should regularly review user access to verify that users do not have overly permissive access. [AWS Config](https://aws.amazon.com/config/) and IAM Access Analyzer can help when auditing user permissions.
+ **Establish a job role matrix:** A job role matrix visualizes the various roles and access levels required within your AWS footprint. Using a job role matrix, you can define and separate permissions based on user responsibilities within your organization. Use groups instead of applying permissions directly to individual users or roles.**  **

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html?ref=wellarchitected#grant-least-privilege)
+  [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
+  [Techniques for writing least privilege IAM policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/)
+  [IAM Access Analyzer makes it easier to implement least privilege permissions by generating IAM](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/) [policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
+  [Delegate permission management to developers by using IAM permissions boundaries](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/)
+  [Refining Permissions using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)
+  [IAM policy types and when to use them](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
+  [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
+  [Guardrails in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails.html)
+  [Zero Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/)
+  [How to implement the principle of least privilege with CloudFormation StackSets](https://aws.amazon.com/blogs/security/how-to-implement-the-principle-of-least-privilege-with-cloudformation-stacksets/)
+  [Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html?ref=wellarchitected)
+ [Reducing policy scope by viewing user activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html?ref=wellarchitected)
+  [View role access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html?ref=wellarchitected#roles-delete_prerequisites)
+  [Use Tagging to Organize Your Environment and Drive Accountability](https://docs.aws.amazon.com/aws-technical-content/latest/cost-optimization-laying-the-foundation/tagging.html?ref=wellarchitected)
+  [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/?ref=wellarchitected)
+  [Tagging AWS resources](https://aws.amazon.com/premiumsupport/knowledge-center/quicksight-iam-identity-center/)

 **Related videos:**
+  [Next-generation permissions management](https://www.youtube.com/watch?v=8vsD_aTtuTo)
+  [Zero Trust: An AWS perspective](https://www.youtube.com/watch?v=1p5G1-4s1r0)

 **Related examples:**
+  [Lab: IAM permissions boundaries delegating role creation](https://wellarchitectedlabs.com/Security/300_IAM_Permission_Boundaries_Delegating_Role_Creation/README.html)
+  [Lab: IAM tag based access control for EC2](https://wellarchitectedlabs.com/Security/300_IAM_Tag_Based_Access_Control_for_EC2/README.html?ref=wellarchitected)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

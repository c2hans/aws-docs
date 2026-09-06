---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_permissions_lifecycle.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP06 Manage access based on lifecycle
<a name="sec_permissions_lifecycle"></a>

 Integrate access controls with operator and application lifecycle and your centralized federation provider. For example, remove a user’s access when they leave the organization or change roles.

As you manage workloads using separate accounts, there will be cases where you need to share resources between those accounts. We recommend that you share resources using [AWS Resource Access Manager (AWS RAM)](http://aws.amazon.com/ram/). This service allows you to easily and securely share AWS resources within your AWS Organizations and Organizational Units. Using AWS RAM, access to shared resources is automatically granted or revoked as accounts are moved in and out of the Organization or Organization Unit with which they are shared. This helps ensure that resources are only shared with the accounts that you intend.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Implement a user access lifecycle policy for new users joining, job function changes, and users leaving so that only current users have access.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)
+  [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
+  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
+  [Remove unnecessary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#remove-credentials)
+  [Working with Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)

 **Related videos:**
+  [Become an IAM Policy Master in 60 Minutes or Less](https://youtu.be/YQsK4MtsELU)
+  [Separation of Duties, Least Privilege, Delegation, and CI/CD](https://youtu.be/3H0i7VyTu70)

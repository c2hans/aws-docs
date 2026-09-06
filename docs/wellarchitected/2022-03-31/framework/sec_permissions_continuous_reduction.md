---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_permissions_continuous_reduction.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP04 Reduce permissions continuously
<a name="sec_permissions_continuous_reduction"></a>

 As teams and workloads determine what access they need, remove permissions they no longer use and establish review processes to achieve least privilege permissions. Continuously monitor and reduce unused identities and permissions.

Sometimes, when teams and projects are just getting started, you might choose to grant broad access (in a development or test environment) to inspire innovation and agility. We recommend that you evaluate access continuously and, especially in a production environment, restrict access to only the permissions required and achieve least privilege. AWS provides access analysis capabilities to help you identify unused access. To help you identify unused users, roles, permissions, and credentials, AWS analyzes access activity and provides access key and role last used information. You can use the [last accessed timestamp](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html) to [identify unused users and roles](http://aws.amazon.com/blogs/security/identify-unused-iam-roles-remove-confidently-last-used-timestamp/), and remove them. Moreover, you can review service and action last accessed information to identify and [tighten permissions for specific users and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html). For example, you can use last accessed information to identify the specific Amazon Simple Storage Service(Amazon S3) actions that your application role requires and restrict access to only those. These features are available in the AWS Management Console and programmatically to enable you to incorporate them into your infrastructure workflows and automated tools.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Configure AWS Identify and Access Management (IAM) Access Analyzer: AWS IAM Access Analyzer helps you identify the resources in your organization and accounts, such as Amazon Simple Storage Service (Amazon S3) buckets or IAM roles, that are shared with an external entity.
  + [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)
+  [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
+  [Remove unnecessary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#remove-credentials)
+  [Working with Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)

 **Related videos:**
+  [Become an IAM Policy Master in 60 Minutes or Less](https://youtu.be/YQsK4MtsELU)
+  [Separation of Duties, Least Privilege, Delegation, and CI/CD](https://youtu.be/3H0i7VyTu70)

---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_permissions_emergency_process.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP03 Establish emergency access process
<a name="sec_permissions_emergency_process"></a>

 A process that allows emergency access to your workload in the unlikely event of an automated process or pipeline issue. This will help you rely on least privilege access, but ensure users can obtain the right level of access when they require it. For example, establish a process for administrators to verify and approve their request, such as an emergency AWS cross-account role for access, or a specific process for administrators to follow to validate and approve an emergency request.

 **Common anti-patterns:**
+ Not having an emergency process in place to recover from an outage with your existing identity configuration.
+ Granting long term elevated permissions for troubleshooting or recovery purposes.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Establishing emergency access can take several forms for which you should be prepared. The first is a failure of your primary identity provider. In this case, you should rely on a second method of access with the required permissions to recover. This method could be a backup identity provider or a user. This second method should be [tightly controlled, monitored, and notify](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/) in the event it is used. The emergency access identity should source from an account specific for this purpose and only have permissions to assume a role specifically designed for recovery.

 You should also be prepared for emergency access where temporary elevated administrative access is needed. A common scenario is to limit mutating permissions to an automated process used for deploying changes. In the event that this process has an issue, users might need to request elevated permissions to restore functionality. In this case, establish a process where users can request elevated access and administrators can validate and approve it. The implementation plans detailing the best practice guidance for pre-provisioning access and setting up emergency, *break-glass*, roles are provided as part of [SEC10-BP05 Pre-provision access](sec_incident_response_pre_provision_access.md).

## Resources
<a name="resources"></a>

 **Related documents:**
+ [Monitor and Notify on AWS](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity)
+ [Managing temporary elevated access](https://aws.amazon.com/blogs/security/managing-temporary-elevated-access-to-your-aws-environment/)

 **Related video:**
+  [Become an IAM Policy Master in 60 Minutes or Less](https://youtu.be/YQsK4MtsELU)

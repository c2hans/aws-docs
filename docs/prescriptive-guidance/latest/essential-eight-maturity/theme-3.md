---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-3.html
---

# Theme 3: Manage mutable infrastructure with automation
<a name="theme-3"></a>

**Essential Eight strategies covered**: Application control, patch applications, and patch operating systems

Similar to immutable infrastructure, you manage mutable infrastructure as IaC, and you modify or update this infrastructure through automated processes. Many of the implementation steps for immutable infrastructure also apply to mutable infrastructure. However, for mutable infrastructure, you must also implement manual controls to make sure that modified workloads still follow best practices.

For mutable infrastructure, you can automate patch management by using [Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html), a capability of AWS Systems Manager. Enable Patch Manager in all accounts in your AWS organization.

Prevent direct SSH and RDP access and require users to use [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) or [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html), which are also capabilities of Systems Manager. Unlike SSH and RDP, these capabilities can log system access and changes.

To monitor and report on compliance, you must perform ongoing reviews of patch compliance. You can use AWS Config rules to make sure that all Amazon EC2 instances are managed by Systems Manager, have the required permissions and installed applications, and are in patch compliance.

## Related best practices in the AWS Well-Architected Framework
<a name="theme-3-best-practices"></a>
+ [SEC06-BP03 Reduce manual management and interactive access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_compute_reduce_manual_management.html)
+ [SEC06-BP05 Automate compute protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_auto_protection.html)

## Implementing this theme
<a name="theme-3-implementation"></a>

### Automate patching
<a name="automate-patching.50d301d2-fa49-59d0-bbea-bbb82c14cd1f"></a>
+ Implement the steps in [Enable Patch Manager in all accounts in your AWS organization](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/design-standard.html)
+ For all [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances, include the `CloudWatchAgentServerPolicy` and `AmazonSSMManagedInstanceCore` in the [instance profile or IAM role](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) that Systems Manager uses to access your instance

### Use automation rather than manual processes
<a name="use-automation-rather-than-manual-processes.3d63a97f-8c12-5979-9682-58b8ca3839e2"></a>
+ Implement the guidance in [Implement AMI and container build pipelines](theme-2.md#theme-2-implementation) in *Theme 2: Manage immutable infrastructure through secure pipelines*
+ Use [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) or [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) instead of direct Secure Shell (SSH) or Remote Desktop Protocol (RDP) access

### Use automation to install the following on Amazon EC2 instances
<a name="use-automation-to-install-the-following-on-9999999999999999ec2--instances.3416780e-3235-5762-a4d4-7ae96170dfd7"></a>
+ [AWS Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html), which is used for instance discovery and management
+ Security tools for application control, such as Security-Enhanced Linux (SELinux), File Access Policy Daemon (fapolicyd), or [OpenSCAP](https://www.open-scap.org/)
+ [Amazon CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html), which is used for logging

### Use peer review before each release to verify that changes meet security guidelines
<a name="use-peer-review-before-each-release-to-verify-that-changes-meet-security-guidelines.524c57b0-e216-53df-898d-2533f014f8b5"></a>
+ IAM policies that are too permissive, such as those that use wildcards or that don't follow least-privilege permissions
+ Security group rules that are too permissive, such as those that use wildcards or allow SSH access
+ Access logs that aren't enabled
+ Encryption that isn't enabled
+ Hard-coded passwords

### Use identity-level controls
<a name="use-identity-level-controls.e8fc97de-3f4c-55c0-8940-ef66a9968f6f"></a>
+ To require that users modify resources through automated processes and prevent manual configuration, allow read-only permissions for roles that users can assume
+ Grant permissions to modify resources only to service roles, such as the role used by Systems Manager

### Implement vulnerability scanning
<a name="implement-vulnerability-scanning.ea3e0e15-a1fc-59ca-8b15-e6837e57a390"></a>
+ Implement the guidance in [Implement vulnerability scanning](theme-2.md#theme-2-implementation) in *Theme 2: Manage immutable infrastructure through secure pipelines*
+ Scan your Amazon EC2 instances by using Amazon Inspector

## Monitoring this theme
<a name="theme-3-monitoring"></a>

### Monitor patch compliance on an ongoing basis
<a name="monitor-patch-compliance-on-an-ongoing-basis.9b2de38f-372a-5ff5-85bb-74b283eca3b1"></a>
+ [Report on patch compliance by using automation and dashboards](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/design-standard.html)
+ Implement a mechanism to review dashboards for patch compliance

### Monitor IAM and logs on an ongoing basis
<a name="monitor-9999999999999999iam--and-logs-on-an-ongoing-basis.22cb75c6-d75f-50fe-ac5f-e96275c12745"></a>
+ Periodically review your IAM policies to make sure that:
  + Only deployment pipelines have direct access to resources
  + Only approved services have direct access to data
  + Users don't have direct access to resources or data
+ Monitor AWS CloudTrail logs to make sure that users are modifying resources through pipelines and aren't directly modifying resources or accessing data
+ Periodically review AWS Identity and Access Management Access Analyzer findings
+ Set up an alert to notify you if the root user credentials for an AWS account are used

### Implement the following AWS Config rules
<a name="implement-the-following-9999999999999999cc--rules.791a64be-f634-50ce-99f4-74ef822e61fd"></a>
+ `EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK`
+ `EC2_INSTANCE_MANAGED_BY_SSM`
+ `EC2_MANAGEDINSTANCE_APPLICATIONS_REQUIRED - SELinux/fapolicyd/OpenSCAP, Amazon CloudWatch agent`
+ `EC2_MANAGEDINSTANCE_APPLICATIONS_BLACKLISTED - any unsupported applications`
+ `IAM_ROLE_MANAGED_POLICY_CHECK - Amazon CloudWatch Logs, AWS Systems Manager`
+ `EC2_MANAGEDINSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK`
+ `REQUIRED_TAGS`
+ `RESTRICTED_INCOMING_TRAFFIC - 22, 3389`

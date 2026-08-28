---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-3.html
---

# Theme 3: Manage mutable infrastructure with automation
<a name="theme-3"></a>

**Essential Eight strategies covered**: Application control, patch applications, patch operating systems

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
<a name="automate-patching.46b68614-48c2-5e36-bd9b-5017c8444896"></a>
+ Implement the steps in [Enable Patch Manager in all accounts in your AWS organization](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/design-standard.html)
+ For all EC2 instances, include the `CloudWatchAgentServerPolicy` and `AmazonSSMManagedInstanceCore` in the [instance profile or IAM role](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) that Systems Manager uses to access your instance

### Use automation rather than manual processes
<a name="use-automation-rather-than-manual-processes.29b4efe4-5889-50f5-ab85-242e07aaee82"></a>
+ Implement the guidance in [Implement AMI and container build pipelines](theme-2.md#theme-2-implementation) in *Theme 2: Manage immutable infrastructure through secure pipelines*
+ Use [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) or [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) instead of direct SSH or RDP access

### Use automation to install the following on EC2 instances
<a name="use-automation-to-install-the-following-on-ec2-instances.58a8dd36-e450-5fbc-8c51-a32cfd39bf1e"></a>
+ [AWS Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html), which is used for instance discovery and management
+ Security tools for application control, such as [Security Enhanced Linux (SELinux)](https://github.com/SELinuxProject) (GitHub), [File Access Policy Daemon (fapolicyd)](https://github.com/linux-application-whitelisting/fapolicyd/blob/main/README.md) (GitHub), or [OpenSCAP](https://www.open-scap.org/)
+ [Amazon CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html), which is used for logging

### Use peer review before any release to ensure that changes are meeting best practices
<a name="use-peer-review-before-any-release-to-ensure-that-changes-are-meeting-best-practices.57742448-b6f3-536e-b7cb-0cbd73dc12d3"></a>
+ IAM policies that are too permissive, such as those that use wildcards
+ Security group rules that are too permissive, such as those that use wildcards or allow SSH access
+ Access logs that aren't enabled
+ Encryption that isn't enabled
+ Password literals
+ Secure IAM policies

### Use identity-level controls
<a name="use-identity-level-controls.e8fc97de-3f4c-55c0-8940-ef66a9968f6f"></a>
+ To require that users modify resources through automated processes and prevent manual configuration, allow read-only permissions for roles that users can assume
+ Grant permissions to modify resources only to service roles, such as the role used by Systems Manager

### Implement vulnerability scanning
<a name="implement-vulnerability-scanning.f5e25b9a-5b73-5957-80cf-1658c104215a"></a>
+ Implement the guidance in [Implement vulnerability scanning](theme-2.md#theme-2-implementation) in *Theme 2: Manage immutable infrastructure through secure pipelines*
+ Scan your EC2 instances by using Amazon Inspector

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
<a name="implement-the-following-9999999999999999cc--rules.2b6a5b44-d3c8-5095-bf1f-8c68ee2ae6b7"></a>
+ `EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK`
+ `EC2_INSTANCE_MANAGED_BY_SSM`
+ `EC2_MANAGEDINSTANCE_APPLICATIONS_REQUIRED - SELinux/fapolicyd/OpenSCAP, CW Agent`
+ `EC2_MANAGEDINSTANCE_APPLICATIONS_BLACKLISTED - any unsupported apps`
+ `IAM_ROLE_MANAGED_POLICY_CHECK - CW Logs, SSM`
+ `EC2_MANAGEDINSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK`
+ `REQUIRED_TAGS`
+ `RESTRICTED_INCOMING_TRAFFIC - 22, 3389`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/iam-roles.html
---

# IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users in the AWS Cloud. This solution creates IAM roles that grant the solution’s automated functions access to perform remediation actions within a narrow scope set of permissions specific to each remediation.

The admin account’s Step Function is assigned to the SO0111-ASR-Orchestrator-Admin role. Only this role is allowed to assume the SO0111-Orchestrator-Member in each member account. The member role is allowed by each remediation role to pass it to the AWS Systems Manager service to run specific remediation runbooks. Remediation role names begin with SO0111, followed by a description matching the name of the remediation runbook. For example, SO0111-RemoveVPCDefaultSecurityGroupRules is the role for the ASR-RemoveVPCDefaultSecurityGroupRules remediation runbook.

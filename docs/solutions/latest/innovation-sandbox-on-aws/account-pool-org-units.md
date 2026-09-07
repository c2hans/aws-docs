---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-pool-org-units.html
---

# AccountPool Organizational Units
<a name="account-pool-org-units"></a>

![Diagram showing the AccountPool OU structure with Available Active Frozen Cleanup Quarantine Entry and Exit OUs](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/organizational-units.drawio.png)

**AccountPool OUs**
The AccountPool Organizational Unit (OU) structure defines the sandbox account lifecycle through the solution, and allows for Service Control Policies (SCPs) to restrict actions within the accounts at different phases of the account lifecycle.

![AccountPool OUs list in the AWS Organizations console](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/isb-accountpool-ou.png)

**AccountPool OUs list**
The following OUs are created when the solution is deployed:

| Organizational Unit (OU) | Description |
| --- | --- |
|  *<nameSpace>* \_InnovationSandboxAccountPool | Parent OU that all other solution OUs are contained in. |
| Active | Sandbox accounts that are associated with an active lease (claimed). |
| Available | Sandbox accounts that are available for lease (unclaimed). |
| CleanUp | Sandbox accounts that are currently in cleanup. |
| Entry | Staging OU for accounts that are to be registered with the solution. |
| Exit | Staging OU for accounts that have been ejected from the solution. |
| Frozen | Sandbox accounts where the users access has been revoked, but administrators still have access in order to review resources within the account. |
| Quarantine | Sandbox accounts that have failed the cleanup process because of an undeletable resource, were detected as solution state drift, or were manually quarantined by an administrator, and need remediation from an administrator. |

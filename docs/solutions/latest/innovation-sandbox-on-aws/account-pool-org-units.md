---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-pool-org-units.html
---

# AccountPool Organizational Units
<a name="account-pool-org-units"></a>

![organizational units](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/organizational-units.png)

**AccountPool OUs**
The AccountPool Organizational Unit (OU) structure defines the sandbox account lifecycle through the solution, and allows for Service Control Policies (SCPs) to restrict actions within the accounts at different phases of the account lifecycle.

![isb accountpool ou](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/isb-accountpool-ou.png)

**AccountPool OUs list**
The following OUs are created when the solution is deployed:

| Organizational Unit (OU) | Description |
| --- | --- |
|  *<nameSpace>* \_InnovationSandboxAccountPool | Parent OU that all other solution OUs are contained in. |
| Active | Sandbox accounts that are associated with an active lease (claimed). |
| Available | Sandbox accounts that are available for lease (unclaimed). |
| CleanUp | Sandbox accounts that are currently in clean-up. |
| Entry | Staging OU for accounts that are to be registered with the solution. |
| Exit | Staging OU for accounts that have been ejected from the solution. |
| Frozen | Sandbox accounts where the users access has been revoked, but administrators still have access in order to review resources within the account. |
| Quarantine | Sandbox accounts that have failed the clean-up process due to an undeletable resource or was detected as solution state drift and needs manual remediation from an administrator. |

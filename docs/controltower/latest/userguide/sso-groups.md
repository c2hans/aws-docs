---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/sso-groups.html
---

# IAM Identity Center Groups for AWS Control Tower
<a name="sso-groups"></a>

AWS Control Tower offers preconfigured groups to organize users that perform specific tasks in your accounts. You can add users and assign them to these groups directly in IAM Identity Center. Doing so matches permission sets to users in groups within your accounts. For the latest guidance and best practices on configuring your groups, see [Best practices](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html#delegated-admin-best-practices) in the *IAM Identity Center User Guide*.

The following groups are created when you set up your landing zone.

**AWSAccountFactory**

| Account | Permission sets | Description |
| --- | --- | --- |
| Management account | AWSServiceCatalogEndUserAccess | This group is only used in this account to provision new accounts using Account Factory. |

**AWSServiceCatalogAdmins**

| Account | Permission sets | Description |
| --- | --- | --- |
| Management account | AWSServiceCatalogAdminFullAccess | This group is only used in this account to make administrative changes to Account Factory. Users in this group can't provision new accounts unless they're also in the AWSAccountFactory group. |

**AWSControlTowerAdmins**

| Account | Permission sets | Description |
| --- | --- | --- |
| Management account | AWSAdministratorAccess | Users of this group in this account are the only ones that have access to the AWS Control Tower console. |
| Log archive account | AWSAdministratorAccess | Users have administrator access in this account. |
| Audit account | AWSAdministratorAccess | Users have administrator access in this account. |
| Member accounts | AWSOrganizationsFullAccess | Users have full access to Organizations in this account. |

**AWSSecurityAuditPowerUsers**

| Account | Permission sets | Description |
| --- | --- | --- |
| Management account | AWSPowerUserAccess | Users can perform application development tasks and can create and configure resources and services that support AWS aware application development. |
| Log archive account | AWSPowerUserAccess | Users can perform application development tasks and can create and configure resources and services that support AWS aware application development. |
| Audit account | AWSPowerUserAccess | Users can perform application development tasks and can create and configure resources and services that support AWS aware application development. |
| Member accounts | AWSPowerUserAccess | Users can perform application development tasks and can create and configure resources and services that support AWS aware application development. |

**AWSSecurityAuditors**

| Account | Permission sets | Description |
| --- | --- | --- |
| Management account | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in this account. |
| Log archive account | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in this account. |
| Audit account | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in this account. |
| Member accounts | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in this account. |

**AWSLogArchiveAdmins**

| Account | Permission sets | Description |
| --- | --- | --- |
| Log archive account | AWSAdministratorAccess | Users have administrator access in this account. |

**AWSLogArchiveViewers**

| Account | Permission sets | Description |
| --- | --- | --- |
| Log archive account | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in this account. |

**AWSAuditAccountAdmins**

| Account | Permission sets | Description |
| --- | --- | --- |
| Audit account | AWSAdministratorAccess | Users have administrator access in this account. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

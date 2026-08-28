---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-hsm-type-modification.html
---

# Cluster HSM type migration
<a name="cluster-hsm-type-modification"></a>

AWS CloudHSM offers the ability to change the HSM type of an existing cluster. Review the table on this page to determine whether the HSM type modification is allowed.

For more information on the types of HSMs supported and their features please refer to [HSM types in AWS CloudHSM](hsm-types.md).

**Note**
You cannot change the FIPS mode of a cluster during this operation.

| From | To | Comment |
| --- | --- | --- |
| hsm1.medium | hsm2m.medium | Allowed |
| hsm2m.medium | hsm1.medium | Conditional. You can roll back from hsm2m.medium to hsm1.medium within 24 hours of the start of a migration. |

**Topics**
+ [Migrating from hsm1.medium to hsm2m.medium](hsm1-to-hsm2-migration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

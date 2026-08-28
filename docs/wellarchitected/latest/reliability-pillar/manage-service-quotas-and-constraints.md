---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/manage-service-quotas-and-constraints.html
---

# Manage service quotas and constraints
<a name="manage-service-quotas-and-constraints"></a>

 For cloud-based workload architectures, there are service quotas (which are also referred to as service limits). These quotas exist to prevent accidentally provisioning more resources than you need and to limit request rates on API operations so as to protect services from abuse. There are also resource constraints, for example, the rate that you can push bits down a fiber-optic cable, or the amount of storage on a physical disk.

 If you are using AWS Marketplace applications, you must understand the limitations of those applications. If you are using third-party web services or software as a service, you must be aware of those limits also.

**Topics**
+ [REL01-BP01 Aware of service quotas and constraints](rel_manage_service_limits_aware_quotas_and_constraints.md)
+ [REL01-BP02 Manage service quotas across accounts and regions](rel_manage_service_limits_limits_considered.md)
+ [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel_manage_service_limits_aware_fixed_limits.md)
+ [REL01-BP04 Monitor and manage quotas](rel_manage_service_limits_monitor_manage_limits.md)
+ [REL01-BP05 Automate quota management](rel_manage_service_limits_automated_monitor_limits.md)
+ [REL01-BP06 Ensure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel_manage_service_limits_suff_buffer_limits.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

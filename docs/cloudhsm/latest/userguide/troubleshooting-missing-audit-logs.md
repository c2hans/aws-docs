---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-missing-audit-logs.html
---

# Missing AWS CloudHSM audit logs in CloudWatch
<a name="troubleshooting-missing-audit-logs"></a>

If you created an AWS CloudHSM cluster before January 20th, 2018, you will need to manually configure a [service-linked role](service-linked-roles.md) in order to enable the delivery of that cluster's audit logs. For instructions on how to enable a service-linked role on an HSM cluster, see [Understanding Service-Linked Roles](service-linked-roles.md), as well as [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the IAM User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

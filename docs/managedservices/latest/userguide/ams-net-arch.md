---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/ams-net-arch.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Network architecture
<a name="ams-net-arch"></a>

AWS Managed Services (AMS) offers two network architectures:
+ Multi-account landing zone (MALZ): provides common services - such as access, end point security, networking - from shared accounts for workloads that are deployed in separate member accounts.
+ Single-account landing zone (SALZ): provides self contained accounts where common services such as access, end point security, networking are deployed in the same account as the workload. It is recommended for workloads that require a high level of isolation as it incurs higher AWS costs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

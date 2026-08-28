---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-14.html
---

# 14 – Select the optimal storage solution
<a name="design-principle-14"></a>

 **How do you select the optimal storage solutions for your SAP workloads?** How you configure this storage will impact the performance of your system. AWS offers a wide range of services, including block, file, and object storage, to meet the storage needs of your SAP databases, applications, and backups. We recommend following the guidelines that have been benchmarked and certified by SAP. For SAP HANA, there are very specific guidelines. Other databases will require more analysis to match your workload.

| ID | Priority | Best Practice |
| --- | --- | --- |
| ☐ BP 14.1 | Required | Create mount points and volume associations to align with function |
| ☐ BP 14.2 | Required | Select and configure Amazon EBS types aligned with performance requirements |
| ☐ BP 14.3 | Recommended | Evaluate Amazon EFS and Amazon FSx performance suitability for your SAP use case |
| ☐ BP 14.4 | Recommended | Consider memory as an alternative to storage |
| ☐ BP 14.5 | Recommended | Choose appropriate backup solutions and schedule |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

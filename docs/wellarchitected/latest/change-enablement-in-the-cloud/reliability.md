---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/change-enablement-in-the-cloud/reliability.html
---

# Reliability
<a name="reliability"></a>

 Change implementation can have a direct impact on the availability of workloads and the ability to recover from major incidents or disasters. Change automation is foremost in maximizing application availability. If you have any manual processes, you lose critical time awaiting those manual actions. Theoretically, the smaller in size a change is, the lower the potential impact of that change on the business.

 Use deployment patterns that reduce risk, such as blue-green or canary deployments. Perform comprehensive testing in pipelines, including load, performance under load, and resiliency testing. Effective monitoring of the key performance indicators (KPIs) is a requirement, and automated rollback should be initiated if those KPIs indicate thresholds are likely to be exceeded.

 Testing disaster recovery thoroughly helps you meet recovery objectives. Use automation to backup data. Regularly restore and recover to validate your recovery process and procedures.

 These considerations improve the reliability of workloads and decrease business risk. Cloud change enablement practices should reflect this reduction in risk, and organizations should consider that because the risk is minimized, and reversible, they can be processed as standard changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

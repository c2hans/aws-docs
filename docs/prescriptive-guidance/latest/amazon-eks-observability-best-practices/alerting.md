---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/alerting.html
---

# Alerting in Amazon EKS
<a name="alerting"></a>

Alerting is a critical component of managing and maintaining applications that run on Amazon EKS. It serves as an early warning system that notifies operators and developers about potential issues, anomalies, or performance degradations before they escalate into serious problems that could impact service availability or user experience. Alerting involves monitoring various aspects of the Kubernetes cluster, including:
+ Infrastructure health
+ Application performance
+ Container metrics
+ Custom business metrics

Effective alerting in Amazon EKS goes beyond simply setting up notifications. It requires a well-thought-out strategy that balances the need for timely information with the the potential for alert fatigue. This strategy should:
+ Define meaningful thresholds and conditions.
+ Prioritize alerts based on severity and impact.
+ Implement proper routing and escalation procedures.
+ Integrate with incident management and communication tools.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

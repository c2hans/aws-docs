---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/inspect-adapt-iterate.html
---

# Stage 3: Inspect, adapt and iterate
<a name="inspect-adapt-iterate"></a>

After you implement your observability system, we recommend that you continually review, assess, learn, adapt, and improve your implementation. You can use the [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/) as a tool to assess the maturity of your implementation and to identify and prioritize areas for improvement.

## Implement regular reviews
<a name="reviews"></a>

Observability is an iterative process. It requires regular audits and assessments of existing components, and changes and enhancements to drive continual improvement. We recommend that you perform regular reviews to reevaluate SLOs, alert thresholds, dashboards, metric granularity, retention policies, sampling strategies, and so on to ensure that these are driving value for your teams and business. By connecting observability costs to specific teams and services, you can enable data-driven decisions about coverage and resource allocation.

At Amazon, we conduct weekly [Operational Readiness Reviews (ORRs)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) to audit teams' processes and observability postures against best practices. This is a non-blocking exercise that aligns with the number of services and frequency of releases at Amazon.

Depending on the size of your organization, you can also have a business as usual (BAU) roster, where one member of each team is responsible for reporting on anomalies and trends, uncovering unknown-unknowns, removing unwanted instrumentation and alerts, improving dashboards, and ensuring that the observability solution continues to work for the team and is aligned to the team's objectives and success metrics. This could also be an opportunity to reassess the alerting strategy to be more responsive, proactive, and closer to the user. The goal with these reviews is to create a virtuous cycle, as shown in the following illustration, and to improve the maturity of your observability posture maturity, as described in the [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model).

![Feedback and review cycle in the iterative observability process.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/images/guide-img/81bb2e9d-84eb-4662-8792-f2a3fb2603f4/images/ff32aa65-699d-42ae-b029-224ea468b108.png)

Identify the playbooks that are accessed most frequently and consider improving your application or adding more instrumentation. Identify the runbooks that are executed most frequently and consider automating those runbooks.

The learnings from these reviews are also shared with the observability squad and specialists, to highlight improvements in central programs and the observability platform. For example, depending on the frequency of deployment-triggered events, you might decide to prioritize the improvement of the deployment pipeline over other components. If the MTTR is higher because of monitoring gaps, you can prioritize improving the observability platform and its configuration.

## Celebrate wins
<a name="wins"></a>

Share success stories from teams that use observability tools. For example, highlight the success of a team that used observability metrics to implement an alternative solution that is more efficient and leads to lower latency or cost. Communicating this success underscores the importance of observability and motivates other teams to improve their observability posture and strive for similar success.

## Learn from incidents
<a name="learnings"></a>

Conduct blameless post-incident exercises similar to the [correction of errors (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/) process at Amazon to identify areas for improvement and to prevent future issues. As with wins, the learnings from this exercise can be shared broadly with other teams to reinforce the value of observability and best practices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

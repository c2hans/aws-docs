---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-concept-mapping.html
---

# Concept mapping: AWS Resilience Hub v1 to Next generation Resilience Hub
<a name="next-gen-concept-mapping"></a>

The following table maps concepts from AWS Resilience Hub v1 to their equivalents in the next generation of Resilience Hub.

| AWS Resilience Hub v1 concept | Next generation Resilience Hub concept | Notes |
| --- | --- | --- |
| Application | Service | Your v1 "application" becomes a the next generation of Resilience Hub "service" – the primary unit of assessment |
| Resilience checks | Failure mode assessment findings | Static checks replaced by GenAI-powered findings with reasoning |
| Application assessment | Service failure mode assessment | Same concept, now at service level with richer output |
| Assessment policy (RTO/RPO) | Resilience policy (modular) | Policies are now composable: DR \+ Availability SLO \+ Data recovery |
| Application (as grouping) | System \+ User journeys | The "grouping" aspect of applications maps to systems and user journeys |
| – (not available) | Dependency discovery | New capability in the next generation of Resilience Hub |
| – (not available) | Service functions | Technical workflows within a service; new in the next generation of Resilience Hub |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

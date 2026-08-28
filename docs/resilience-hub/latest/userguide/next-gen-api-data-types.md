---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-data-types.html
---

# Data types
<a name="next-gen-api-data-types"></a>

The following table lists the key data types used by the next generation of Resilience Hub API.

| Type | Description |
| --- | --- |
| SystemEntity | System with ARN, name, description, and creation time. |
| UserJourneyEntity | User journey with name, description, service list, and policy. |
| ServiceEntity | Service with ARN, name, system association, permission model, and input sources. |
| ResiliencePolicyEntity | Policy with name and components (DR, availability, performance). |
| AssessmentEntity | Assessment with ID, status, timestamps, and failure mode findings count. |
| FindingEntity | Failure mode finding with ID, name, description, severity, and recommendations. |
| RecommendationEntity | Recommendation with name, description, cost, and complexity. |
| DependencyDiscoveryConfig | Dependency discovery configuration with status, eligible resource count, message, and last-updated timestamp. Returned by GetService and ListServices. |
| DependencyEntity | Dependency with name, location, criticality, and allowed status. |
| TopologyEntity | Topology with ID, timestamp, resource count, and edges. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

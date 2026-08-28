---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/service-per-team.html
---

# Service per team pattern
<a name="service-per-team"></a>

Instead of decomposing monoliths by business capabilities or services, the service per team pattern breaks them down into microservices that are managed by individual teams. Each team is responsible for a business capability and owns the capability's code base. The team independently develops, tests, deploys, or scales its services, and primarily interacts with other teams to negotiate APIs. We recommend that you assign each microservice to a single team. However, if the team is large enough, multiple subteams could own separate microservices within the same team structure. The following table explains the advantages and disadvantages of using this pattern.

|
|
| Advantages | Disadvantages |
| --- |--- |
| + Teams act independently with minimal coordination.<br />+ Code bases and microservices are not shared by multiple teams.<br />+ Teams can quickly innovate and iterate on product features.<br />+ Different teams can use different technologies, frameworks, or programming languages. : These should be hidden behind a well-defined and stable API. | + It can be difficult to align teams to end-user functionality or business capabilities.<br />+ Additional effort is required to deliver larger, coordinated application increments, especially if there are circular dependencies between teams. |

The following illustration shows how a monolith can be split into microservices that are managed, maintained, and delivered by individual teams.

![Service by team pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/guide-img/8e9fa68d-7532-4c4b-8c7b-74bc6afdb7b9/images/af89a9b9-fcea-4d13-b499-eb85e96bef73.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

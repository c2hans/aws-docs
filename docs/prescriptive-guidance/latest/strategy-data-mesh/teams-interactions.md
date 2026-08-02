---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/teams-interactions.html
---

# Teams and interactions
<a name="teams-interactions"></a>

To implement a data mesh architecture, you must organize your teams and their interaction patterns. [Conway's law](https://www.melconway.com/Home/Committees_Paper.html) states that the design of a system ends up mimicking the communication structure of the organization that implemented it. In other words, the architecture of a software solution reflects the organization of teams that built it. Another implication of Conway's law is that you should seek to match your team structure to the architecture you want to promote. For the data mesh solution, this means promoting a distributed team structure in your organization.

## Teams involved in the data mesh strategy
<a name="teams"></a>

The foundational teams in this journey are core teams that build the data mesh of your organization: the self-service data platform team and the domain teams. In addition, to accelerate the data mesh journey of your organization, the enabler teams can help support where applicable. This section enlists the common teams we've observed at AWS customers. Depending on the data and cloud maturity of your organization, some of these teams might already exist. In this case, gain sponsorship of these teams to support the data mesh initiative. We recommend to designing your teams based on your industry, size of organization, and scope of the data mesh solution.

### Executive leadership team
<a name="executive-leadership-team.84ab3038-c76a-588e-a4dd-563ca21ac44f"></a>

The executive leadership team defines the vision of the data and data management strategy of your organization. Members of these teams are the C-level executives, IT, and business executives of your company. The executive leadership team has the following key responsibilities:
+ Formulate the vision of the data strategy.
+ Sponsor the data mesh strategy.
+ Define and collect metrics to evaluate the health of the program.

### Domain teams
<a name="domain-teams.ab827dec-fb9f-5806-8d64-d062dddfd434"></a>

The domain teams create and maintain data products related to the data domains. Members of these teams possess domain-specific knowledge and own use cases that deliver business value for your organization. The domain teams have the following key responsibilities:
+ Own the data products.
+ Align with the leadership on business use case priorities.
+ Collaborate with the self-service data platform team to deliver business value within the defined time frame.

### Self-service data platform team
<a name="self-service-data-platform-team.5421a96e-7eed-52ea-bf19-254d1ac8d3c6"></a>

The self-service data platform team owns, maintains and drives the roadmap of the self-service data mesh–based data solution. This team has the following responsibilities:
+ Own the data mesh–based data solution.
+ Implement new features of the data solution based on feedback from users and in alignment with the leadership team.
+ Maintain the data mesh–based data solution
+ Serve as the point of contact for business and technical questions related to the data solution.

### Governance team
<a name="governance-team.cce61da5-363c-5b46-9d03-9683f506dd6e"></a>

The governance team ensures that the data products meet industry standards and regulations. This team acts as the gatekeeper for data quality and administration. By having the proper mechanisms in place, the governance team gives data users trust and confidence in the data. The governance team has the following main responsibilities:
+ Define the data governance principles and guardrails by collaborating with the leadership team, domain teams, and the security team. Examples of relevant topics are data quality, data security, data lineage, and data tagging.
+ Support the self-service data platform team in implementing these principles and guardrails.

### Cloud foundation team
<a name="cloud-foundation-team.07f64c0d-0993-59e7-b3b8-a7bdba468307"></a>

The cloud foundation team (also known as the landing zone team) provisions new, configured AWS accounts for the data solution. The cloud foundation team has the following key responsibilities of this team:
+ Configure and provision new AWS accounts for the data solution.
+ Release configuration updates for the AWS accounts that are linked to the data solution.

### Assets team
<a name="assets-team.1fc1e2c0-e2e8-58ed-a6a7-106e1547dd3e"></a>

The assets team collaborates with the domain teams to identify and extract reusable assets. This team enables the self-service data platform team to integrate these reusable assets with the data solution so that is the assets are available to all data users.

You might also require industry-specific teams, such as a [GxP](https://aws.amazon.com/compliance/gxp-part-11-annex-11/) (Good Practices) team for the life sciences industry. If your organization is new to the cloud, a data ingestion team can help you move your data from on-premises to the cloud.

## Interaction between teams
<a name="interaction"></a>

One implication of Conway's law is that not all communication is helpful, and that too much communication can prevent people from doing their work. Ensure that the scope of each team is defined and that the communication is focused. More communication doesn't necessarily lead to fast delivery of the data mesh–based data solution.

The following diagram illustrates the grouping of the teams involved in the data mesh strategy and their interactions. The teams are grouped in concentric circles.

![Diagram of interteam communications.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/images/guide-img/8ee4070d-6c71-44bc-a40f-f010d4d931e6/images/4a1157b6-6996-4e14-aedd-93706ae8f365.png)

1. At the center are the core teams of the data mesh: the self-service data platform team and the domain teams. The self-service data platform team communicates frequently with the domain teams to provide technical support and speed up creation of business value.

1. In the next layer are the three enabler teams: governance, assets, and cloud foundation. The enabler teams communicate frequently with the self-service data platform team. The frequent communication ensures that all cloud resources are available to the data platform team and that the data solution is secure and compliant. The assets team interacts infrequently with the domain teams to extract the reusable assets. The governance team communicates with the self-service data platform team and domain teams to ensure that the data governance principles and guardrails are established. The cloud foundation team interacts with the self-service data platform team to gather requirements on the configuration and cloud resources for the newly provisioned accounts.

1. The outer layer consists of the executive leadership team. The executive leadership team communicates infrequently with the representatives of the teams of the inner layers to monitor status of the program and unblock teams with organizational issues.

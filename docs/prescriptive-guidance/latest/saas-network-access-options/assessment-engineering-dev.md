---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/assessment-engineering-dev.html
---

# Development metrics related to network access for SaaS offerings
<a name="assessment-engineering-dev"></a>

## Deployment frequency, time to deploy, and sprint velocity
<a name="assessment-engineering-dev-velocity"></a>

To optimize the efficiency of the development cycle, it's essential that you understand the influence of network stack provisioning on sprint velocity.

### High-score criteria
<a name="high-score-criteria.d43d9a5e-6174-5cad-a6d6-645ba9e6931f"></a>

Network stack provisioning is streamlined and automated, and it requires minimal manual intervention. It does not significantly impact sprint velocity. Network stack provisioning and redeployment can be performed by any team member. This reduces bottlenecks and dependencies on specialized resources.

### Low-score indicators
<a name="low-score-indicators.9252e9fb-af44-5b8a-a3ad-85443d281079"></a>

A high number of story points are necessary for provisioning the network stack. This suggests a complex and time-consuming process that detracts from the development of new features. Frequent redeployment of the network stack incurs substantial time and cost overheads. Network provisioning tasks require specialized engineering expertise, which creates bottlenecks and slows the development cycle.

### Self-assessment questions
<a name="self-assessment-questions.480c81b8-3407-52a2-a75a-89f9f353b70f"></a>
+ What manual steps, if any, are involved in the deployment process. How do they impact the deployment frequency and time?
+ How are rollbacks handled in case of deployment failures. What is their impact on deployment frequency and recovery time?
+ How many story points are required for provisioning the network stack when you set up new environments?
+ How much additional costs and time overhead are associated with frequent redeployment of the network stack during the development process?
+ Does provisioning the network stack depend on specialized engineering expertise, or is it a task that can be managed by any team member?

## Flexibility and feature delivery
<a name="assessment-engineering-dev-features"></a>

The network access approach can influence the engineering team's ability to innovate and deploy new features efficiently.

### High-score criteria
<a name="high-score-criteria.95120c6d-a11f-51c8-8541-5c505bd9a8c2"></a>

The network access approach offers the flexibility needed for rapid and seamless feature deployment. It supports a wide range of communication protocols, unidirectional and bidirectional communication, and message sizes. It does not impose significant constraints on development processes or innovation.

### Low-score indicators
<a name="low-score-indicators.71514f08-fcde-541d-ae47-a948e65e2d3f"></a>

The network access approach restricts the team's ability to roll out new features due a lack of supported communication protocols, inflexibility in message sizes, or dependency on specific technologies and related expert resources. This can lead to slower development cycles and hinder the service's evolution.

### Self-assessment questions
<a name="self-assessment-questions.5c9f06fb-3ca3-5115-a3ec-345a12afddf9"></a>
+ How does the network access approach impact the team's agility in developing and deploying new features?
+ Are there limitations in the network access approach that restrict the support of certain communication protocols or technologies?
+ How does the approach facilitate or limit the integration of new technologies and innovations into the service?
+ How does the network access approach affect development timelines and the product roadmap?

## Change failure rate
<a name="assessment-engineering-dev-failure-rate"></a>

The network access approach you choose can affect the change failure rate when deploying new services or features. Greater control often means greater flexibility, but it also increases the potential for misconfigurations, such as when managing a complex routing setup.

### High-score criteria
<a name="high-score-criteria.f0883c48-fdb6-5758-8944-66de7a535bd0"></a>

You can implement changes to the network stack with minimal risk of failure. Sufficient testing mechanisms are present, efficient rollback mechanisms exist, and effective monitoring helps you to quickly identify and resolve issues.

### Low-score indicators
<a name="low-score-indicators.5dca0267-b8f5-571e-8c17-079637e956fb"></a>

The network access approach is prone to failures during changes. There are limited testing options, complicated deployment strategies, or insufficient monitoring and troubleshooting capabilities. Multiple parties are required to participate in troubleshooting sessions. This can lead to increased downtime and decrease the availability of the SaaS offering.

### Self-assessment questions
<a name="self-assessment-questions.270b80af-de05-51c2-973e-1d75d24b4568"></a>
+ What measures are in place to mitigate the risk of change failure when updating the network stack?
+ Are there thorough testing and validation processes?
+ How quickly can the system recover from a failed change? Is there an efficient rollback process in place?
+ Are there proactive monitoring and alerting systems to detect and address issues swiftly during and after network stack changes?
+ What is the historical change failure rate for network stack deployments. What lessons have been learned from past incidents?
+ How does the network access approach facilitate or limit change implementation. Does the approach minimize service disruption?
+ What is the risk of impacting the availability of the SaaS offering in the production environment when you deploy changes that involve the network access approach?

## Code quality and engineering team performance
<a name="assessment-engineering-dev-performance"></a>

Network access approaches can indirectly affect code quality for SaaS offerings. A lack of standardization in network access can compel the engineering team to support multiple integration approaches, which can lead to a bloated codebase. This, in turn, can hinder the team's ability to develop the depth and control over code quality that is necessary to maintain high-performing engineering teams.

### High-score criteria
<a name="high-score-criteria.a8e1ee9d-d113-5cf5-a92b-d2ea885d4232"></a>

The engineering team stays focused thanks to code modularity and reusability across supported network access approaches. The network access approaches are compatible with existing deployment pipelines and automated testing strategies.

### Low-score indicators
<a name="low-score-indicators.657c7add-18d9-5b23-9571-06b982b8cd0c"></a>

The engineering team performance is reduced due to overhead that is associated with the integration and maintenance of too many network access approaches. Some approaches significantly increase complexity, generate tech debt, or require development of workarounds to address missing or insufficient capabilities.

### Self-assessment questions
<a name="self-assessment-questions.efa34a94-8aeb-57e6-9a32-879abede32ac"></a>
+ How does the network access approach manage network variability?
+ Do you need to develop additional code for handling disruptions in connectivity?
+ Is a new network access approach seamlessly integrate with existing approaches, or does it require significant custom development?
+ What is the extent of the change needed to adopt a new network access approach? Can the existing codebase and automated tests be used effectively?
+ How easy or difficult is it to deploy or redeploy the service with the selected network access approach? Can this be done frequently? Are there any dependencies on expert resources?
+ Does the network access approach facilitate or complicate adherence to coding standards and best practices?
+ How does the approach affect the time-to-market for new features or fixes?

## Technical debt reduction
<a name="assessment-engineering-dev-debt-reduction"></a>

An evaluation of a network access approach's impact on technical debt should consider its scalability, observability, and security capabilities.

### High-score criteria
<a name="high-score-criteria.160b5229-cc2e-50a6-b0e6-209388fb3be3"></a>

The approach effectively streamlines infrastructure management as the customer base expands. It offers robust observability capabilities out-of-the-box. This promotes efficient monitoring and maintenance.

### Low-score indicators
<a name="low-score-indicators.d8d8a65d-b080-5451-b2a9-e8e82a993fc8"></a>

The network access approach inadequately secures communication channels and lacks sufficient tools for qualitative metric observation. It might also require additional development for infrastructure management as the customer base increases, or it might necessitate workarounds for reliability issues.

### Self-assessment questions
<a name="self-assessment-questions.743efee6-ed41-58ae-90aa-e18058933227"></a>
+ How does the network access approach influence the long-term scalability of the infrastructure? Does it facilitate seamless growth with minimal additional investment?
+ How comprehensive are the included observability tools? Do they allow for proactive monitoring and issue resolution?
+ What is the anticipated impact of the network access approach on the maintenance and evolution of the codebase over time?
+ Does the approach integrate well with existing and planned infrastructure. Does it require significant changes or additions?

## Scalability, capacity, and performance
<a name="assessment-engineering-dev-scalability"></a>

To determine the suitability of a network access approach for a SaaS offering, it's essential to analyze how it maintains optimal performance as demand increases.

### High-score criteria
<a name="high-score-criteria.8375f45e-5507-5391-8c3d-8304d3826ade"></a>

The network access approach seamlessly facilitates expansion. It maintains low latency during request processing, and it efficiently handles traffic spikes. It provides consistent performance regardless of increased traffic levels, and it doesn't impose operational limits on growth.

### Low-score indicators
<a name="low-score-indicators.a24e3905-90e0-5c48-a301-c08130a465e7"></a>

The network access approach doesn't scale effectively, possibly due to inherent bandwidth limitations or insufficient infrastructure capacity. Resource provisioning and management increase the complexity or create dependencies. Service performance is degraded due to increased latency, jitter, and throughput variability, particularly in congested network conditions.

### Self-assessment questions
<a name="self-assessment-questions.84caf2e3-2597-5351-829c-163cde864b99"></a>
+ How does the network access approach accommodate an increasing number of tenants and their data volumes?
+ Is it inherently scalable to meet future demands?
+ What measures are in place to make sure performance is consistent, even during peak traffic periods or rapid scaling events?
+ How does the approach handle network latency and jitter? Are there mechanisms to optimize data throughput and minimize delays?
+ Can the network access approach adapt to varying network conditions? Can it provide a single-tenant experience for every customer?
+ What is the impact of the network access approach on the underlying infrastructure? Does it require significant upgrades or changes to existing systems?

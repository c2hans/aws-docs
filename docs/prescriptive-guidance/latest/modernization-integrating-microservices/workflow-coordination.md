---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/workflow-coordination.html
---

# Coordination options
<a name="workflow-coordination"></a>

Synchronous and asynchronous communication work well for a client that calls a single service or a small number of services. However, in a real-world environment, this communication can quickly become complicated and hard to scale. Accomplishing a unit of work might require several microservices, which might have interdependencies. Often, these interactions are modeled as a workflow. There are two approaches for designing these workflows: orchestration and choreography.

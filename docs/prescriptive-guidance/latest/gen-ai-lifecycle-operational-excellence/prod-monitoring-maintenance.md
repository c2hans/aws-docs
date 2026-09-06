---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-maintenance.html
---

# Scalable maintenance and user support for generative AI applications
<a name="prod-monitoring-maintenance"></a>

Successful production deployment of generative AI applications requires robust maintenance processes and support structures that can scale with increasing usage. This section outlines frameworks for implementing automated maintenance pipelines and establishing comprehensive support systems for both end users and operations teams. It examines strategies for automating routine operational tasks, managing infrastructure at scale, and creating effective support structures through monitoring, ticketing systems, and standardized runbooks. These components form the foundation for maintaining reliable generative AI applications while efficiently supporting a growing user base and increasing system complexity.

## Scalable maintenance
<a name="prod-monitoring-maintenance-scaling"></a>

The key to scalable maintenance is automation. Repetitive operational tasks should be codified and automated through  GenAIOps pipelines. This includes automating the process for retraining or fine-tuning models, upgrading generative AI applications to use the latest models, updating the RAG knowledge base to incorporate new data sources and the latest data, and scaling the underlying cloud infrastructure in response to load. You can achieve this by adopting an infrastructure as code (IaC) and operations as code (OaC) approach. You can use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to automate deployment processes, validate consistent environment setup, and streamline resource management. This reduces manual effort, minimizes human error, and validates that the system can be managed efficiently by a small team even as its complexity and usage grow.

## User support readiness
<a name="prod-monitoring-maintenance-user-support"></a>

As with any production application, the right support structures are essential to make sure that users have a pathway to troubleshoot or escalate. You also need to make sure that business and operations teams have the right tools and mechanisms to respond to an incident.

### End user support
<a name="end-user-support.f44bca5a-f489-57f6-a884-6a9a25e8a085"></a>

The primary goal of end-user support is to help users to effectively use the target application to accomplish their task. This section outlines an example support model that monitors usage and sets up pathways for queries, escalations, and root-cause analysis. You can do the following to establish a robust user support mechanism:

1. Define the end-user support objectives and coverage. Example objectives include support response time, problem resolution time, user downtime, and user feedback. Support issues typically fall into three categories: guidance and queries, application and business function concerns, and technical issues.

1. Define monitoring metrics that map to these objectives. These metrics serve as key indicators of support effectiveness and help identify areas for improvement.

1. Implement monitoring and alerting systems for two primary purposes: to provide agents with the tools necessary for root-cause analysis, and to enable proactive user engagement when issues arise.

1. Integrate with a ticketing system to streamline support operations. This integration should automate the assignment and routing of issues to relevant agents while providing a mechanism to trace and audit overall support health and track application issues.

1. Design runbooks for root-cause analysis and resolution. These runbooks serve multiple purposes. They facilitate knowledge transfer between agents, enable automated resolution of recurring issues, and provide a systematic mechanism to debug problems and reduce response times.

### Business and operations support
<a name="business-and-operations-support.bedf1215-e0da-59e5-8daa-a158be9ec038"></a>

Business and operations support focuses on maintaining system reliability to prevent business disruptions. This section outlines the required support model for monitoring application health and development of runbooks/playbooks for diagnosis and resolution. You can do the following to make sure that you are prepared to support the business and its operations:

1. Define business and operational support objectives. Key metrics typically include mean time to recovery (MTTR), system uptime, and recovery time objectives. These fundamental measures help you establish clear performance targets for the support team.

1. Define operational monitoring metrics that map to these objectives. This alignment focuses monitoring efforts on the most critical aspects of system performance.

1. Implement comprehensive monitoring and alerting systems that support engineers with the necessary tools for system diagnostics. These systems should provide real-time visibility into system health and performance.

1. Integrate with a ticketing system to streamline support operations. This automates the assignment and routing of issues to the appropriate engineers, and it provides a mechanism to trace and audit overall support health while tracking operational issues.

1. Design detailed runbooks for root-cause analysis and resolution. These runbooks serve three essential purposes: to facilitate knowledge transfer between engineers, to enable automated resolution of recurring issues, and to provide a systematic approach to debug errors and reduce response times.

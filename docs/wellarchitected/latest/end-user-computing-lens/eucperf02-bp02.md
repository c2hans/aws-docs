---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp02.html
---

# EUCPERF02-BP02 Scale your EUC environment to accommodate the required number of end users
<a name="eucperf02-bp02"></a>

 The number of users accessing the selected AWS EUC service should not affect the performance of the service itself, as AWS provides both scale and resilience for the components that affect authentication and streaming of user sessions. Many supporting components, however, need to be scaled to support the user numbers you intend to deploy.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-4"></a>

 Understand the backend requirements for your deployment and scale them accordingly. For example, a WorkSpaces compute instance with 2 vCPU and 4Gb of RAM may offer acceptable performance to run a targeted application set, but if access to user data or an application database backend is compromised by server performance or network constraints, then the user may complain that WorkSpaces is performing badly. Ideally, perform end to end testing for each application set using scalability testing tools to be sure that they will deliver acceptable performance in production as the services scale.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

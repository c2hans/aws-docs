---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/business-impact-analysis-and-risk-assessment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Business impact analysis and risk assessment
<a name="business-impact-analysis-and-risk-assessment"></a>

 One of the first steps to perform when planning the implementation of a disaster recovery solution is a business impact analysis for all relevant applications. A business impact analysis should quantify the business impact of a disruption to each application. It should identify the impact your internal and external customers will face from not being able to use your applications and the effect that will have on your business with regards to cost, reputation, and compliance. The analysis should help you determine how quickly the application needs to be made available (RTO) and how much data loss can be tolerated (RPO). However, recovery objectives should not be defined without also considering the likelihood of disruption and the cost of recovery when calculating the business value of providing disaster recovery for an application.

 The business impact of a disaster may not be constant. For example, the impact might be dependent on the timing of the disaster — disruption to your payroll system is likely to have a very high impact to the business just before employees are supposed to be paid, but it may have a low impact just after employees have been paid.

 With all of this information, you can document the threat, risk, and impact of different disaster scenarios and the associated recovery options. This information should be used to choose the best disaster recovery strategy and tools for each application and to match the risk and impact (financial, among other types) of a disaster for each application.

 The following table is a sample risk analysis for disaster recovery planning for determining maximum TCO.

 Table 1 - Sample risk analysis for disaster recovery planning

 Risk analysis for application <APPLICATION NAME>

|  **Disaster type**  |  **Likelihood (per year)**  |  **Consequences**  |  **Risk (likelihood x consequences)**  |
| --- | --- | --- | --- |
|  Weather  |  10% (based on past statistics)  |  $100,000  |  $10,000  |
|  Power outage  |  5% (based on past statistics)  |  $150,000 (includes equipment that would need to be replaced)  |  $7,500  |
|   |   |   |  $17,500  |

 After you have determined your maximum TCO, identify whether there is a disaster recovery solution that has a lower TCO than the cost estimated in the risk analysis (taking the probability of a disaster into account). If such a solution exists, then it makes sense financially to use that solution for that application.

 In addition to the financial calculations, the RTO and RPO for each application need to be considered during this process. The more critical the application is, the more aggressive its RTO and RPO requirements, resulting in a higher TCO of an overall disaster recovery solution. Therefore, solutions that don’t offer the needed RTO and RPO should not be considered, even if they make sense based on the raw financial calculation.

## How to match a disaster recovery solution to an application
<a name="how-to-match-a-disaster-recovery-solution-to-an-application"></a>

 There are a variety of disaster recovery solutions on the market. Currently available disaster recovery solutions have the following main differences:
+  **Source application support limitations** – Different disaster recovery products and services support a different subset of operating systems, central processing unit (CPU) architectures, applications, and hypervisors. For applications that are not supported by a disaster recovery solution, the solution will either not be able to correctly (if at all) copy the data to the disaster recovery site or run a working copy of that application in the disaster recovery site when needed (the latter sometimes can only be discovered during a disaster recovery drill).
+  **Recovery infrastructure support limitations** – Different disaster recovery solutions have different requirements for the disaster recovery site infrastructure. For example, not all recovery infrastructures support all of the operating systems of the source or can run with the required performance.
+  **RPO** – Choose a solution that provides the RPO required for the application.
+  **RTO** – Choose a solution that offers your required RTO.
+  **TCO** – Usually the more features and capabilities a disaster recovery solution has, the higher its TCO will be. For example, more aggressive RTOs and RPOs would increase the TCO.
+  **Compliance** – Applications that are covered by compliance certifications normally require their disaster recovery solutions to be covered by the requirements of the certifications.
+  **Ease of operation** – Choose a solution that does not require significant effort or uncommon skills to operate and manage during normal operation (outside of drills and disasters).
+  **Ease of disaster recovery drills** – Choose a solution that reduces the cost and simplifies the process for disaster recovery drills. This will encourage you to conduct the drills more frequently and improve your readiness for disasters.
+  **Level of automation** – Disaster recovery solutions that offer a higher level of automation (for example, they have application programming interfaces (APIs) for integration with other solutions) can be used to extend their capabilities and meet more of your disaster recovery needs.

 This list of technical criteria should be used when evaluating which disaster recovery solution best meets your needs. Keep in mind that different applications (or groups of applications) are likely to have different requirements. It’s also important to pay attention to the small print and to confirm that the product will work as expected in real life scenarios.

 Lastly, as a general best practice, narrow down your disaster recovery solutions to the ones you actually need. Operationally, each new solution will have separate overhead, an added learning curve, and additional implementation and maintenance efforts (such as monitoring the solution, upgrading versions, and applying security patches). Therefore, AWS recommends selecting a small number of disaster recovery solutions to cover all the required applications.

 After you select the disaster recovery solution for each application, you need to plan the implementation project. Implementing disaster recovery for a large number of applications may be a lengthy and complex project.

 To simplify and accelerate the project, include the following in your planning process:
+  **Mapping** – Map the applications, the resources within the applications, and what needs to be recovered for the application to run. AWS recommends preparing a complete list of such resources, grouped by applications. These resources include servers, appliances (such as NAS appliances and firewalls), and networks. As a part of this mapping, dependencies within and between applications need to be established and documented.

   For each application, go through the risk analysis, define the disaster recovery tier, and determine the RTO and RPO.
+  **Timeline** – For both the planning and the implementation stages, a realistic timeline needs to be defined based on the number of applications and their complexity and also the skillset and experience of the people involved in the project.
+  **People** – The number of people that will be allocated for each stage of the project (including planning and implementation), who these people are, and the skillsets, roles, and responsibilities of each person.
+  **Budget** – How much the entire project is estimated to cost. The budget should take into account the cost of the licenses of the AWS services used as well as other costs, such as data transfer from the source site to AWS.
+  **Solution** – Choose solutions for each disaster recovery tier. Because this paper focuses on using AWS for disaster recovery, the prescribed suggestions are as follows:
  + For servers, use Elastic Disaster Recovery. Edge cases for which Elastic Disaster Recovery cannot be used include [unsupported operating systems](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems.html), non-ACID applications (such as MyISAM-backed MySQL databases), applications using shared storage that multiple nodes write to in parallel (such as Oracle RAC), systems that have distributed databases with multiple nodes that need to be in sync with each other (such as a Hadoop Cluster), and servers that the AWS Replication Agent can’t be installed on (for example, third-party appliances).
  + For NAS appliances, such as NetApp, use DataSync whenever possible.
  + For components of source applications that are not supported by either Elastic Disaster Recovery or DataSync, an application-level solution needs to be used. For example, Oracle has application-level solutions for replicating Oracle RAC databases, NAS appliances can be replicated by periodically copying all the changed files to AWS, and Hadoop clusters may require duplicating each node with another one running in AWS. Application-level disaster recovery solutions have multiple disadvantages, including scope (only relevant for specific applications or application components), cost, and ability to replicate over long distances. Therefore, we recommend trying other disaster recovery solution options prior to opting for an application-level solution.
+  **Success criteria** – For a disaster recovery implementation project, success is normally signified by a disaster recovery drill that achieves a failover according to the requirements of the disaster recovery plan.
+  **Team resources** – Assign team members who are skilled in the resources you mapped for replication. For example, if you have a mix of Linux and Windows operating systems, then you need people who understand both operating systems.
+  **Timelines** – Assign timelines to the implementation phase and to at least a single successful drill per application that will conclude the implementation. The disaster recovery implementation is done when all of the applications have had at least one successful drill.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This solution helps you achieve the following objectives.

## Business benefits
<a name="business-benefits.533f7897-e44a-5933-a38d-2b7f3e651d82"></a>
+ **Seamless migration and workflow orchestration** – Control-M facilitates the smooth transition of mainframe workloads to AWS. It orchestrates complex workflows and ensuring continuity in batch processing during and after migration.
+ **Hybrid operations management** – Control-M enables efficient management of both legacy mainframe processes and new cloud-based applications during the transition to AWS.
+ **Cost reduction and optimized resource use** – Migrating to AWS with Control-M reduces operational costs through optimized cloud-resource use and scaling.
+ **Enhanced agility and innovation** – The move to AWS helps your company to adapt rapidly to market changes and use cloud-native services for innovation.
+ **Compliance, security, and efficient monitoring** – Control-M helps ensure ongoing compliance and security. Control-M also provides enhanced real-time monitoring and reporting capabilities in the cloud environment.
+ **Reducing talent gaps** – The move to AWS addresses the challenges associated with finding and retaining skilled mainframe professionals on a legacy platform.

## Technical benefits
<a name="technical-benefits.ec7e8164-f72a-56b2-a331-35fb0de8eaf7"></a>

This solution helps you achieve the following objectives:
+ Extend your Control-M environment to manage workloads on the AWS Mainframe Modernization service.
+ Support rapid innovations by using wizards to incorporate Control-M REST APIs into processes quickly.
+ Orchestrate, schedule and monitor all your application workload jobs in the Control-M unified view.
+ Increase your organization's scalability and business agility, so that you can respond more effectively to changing market conditions and customer demands.
+ Optimize the cost of running or extending applications by modernizing their mainframe workloads and using the benefits of cloud-native services.

### Terms in this guide
<a name="terms"></a>
+ A *mainframe application* refers to a set of related mainframe programs and subprograms that accomplish and facilitate a set of business processes. Mainframe applications can be batch processing systems or online transaction processing (OLTP) systems.
+ A *batch job* refers to a scheduled program that is configured to run without requiring user interaction. In AWS Replatform with Micro Focus, both batch job JCL files and batch job binaries are prepared in an Amazon Simple Storage Service (Amazon S3) bucket, and the location of both is provided in the application definition file.
+ [AWS Mainframe Modernization](https://aws.amazon.com/mainframe-modernization/) is a cloud-native service for migrating, modernizing, running, and operating mainframe applications.
+ [Amazon S3](https://aws.amazon.com/s3/) is scalable object storage with high durability, availability, and performance.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), IT managers, and product owners.
+ *Control-M* *Web* is a solution for managing enterprise workloads, including mainframe batch jobs, through the entire lifecycle of building, testing, deploying, scheduling, and monitoring business application workflows. An extensive set of graphical and programmatic facilities provide all users with access to Control-M facilities in the way they feel most comfortable.
+ Control-M's *Application Integrator* is a web-based, low-code designer used to create job types that enable integration between applications or cloud services with Control-M. After Application Integrator job types are built, they operate exactly like all other Control-M jobs, exposing all Control‑M features and functions for the target integration. In this guide, the integration is with AWS Replatform with Micro Focus.
+ The *Planning domain* is a set of capabilities for managing the creation and updating of job flows.
+ The *Monitoring domain* is a set of capabilities for managing the job flows. This is where you view all running jobs and their status. If errors occur, alerts are generated. You can perform operational actions to view job status, react to delays or failures, analyze problems, and take corrective actions.
+ *Control-M Agents* are installed on different computers that are managed by Control-M Server. Jobs are assigned to an agent name that identifies a host. The Agent communicates with the server using HTTPS protocol (port 443).

### Assumptions
<a name="assumptions"></a>

The examples and diagrams in this guide reflect the following assumptions:
+ The mainframe application that is being migrated might run a single program or multiple programs. For simplicity, the diagrams in this guide display a single program and multiple subprograms for each application.
+ The mainframe application is migrated and running in an AWS Replatform with Micro Focus managed runtime environment with multiple defined batch jobs. For this pilot, set up the BankDemo example application in AWS Replatform with Micro Focus by following the instructions in [Tutorial: Managed Runtime for Micro Focus](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-runtime.html).
+ A full [Control-M installation](https://www.bmc.com/it-solutions/control-m.html) is available, with all Control-M components, including Application plug-ins and add-ons.
+ The [Control-M Agent](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Control-M_Agents.htm) is responsible for managing jobs. To distribute the workload, Agents can be installed on multiple computers. This can enhance performance and resiliency.
+ The [Control-M Automation API](https://docs.bmc.com/docs/automation-api/9021/control-m-automation-api-home-1123726007.html) exposes Control-M functionality through Restful Web Services (REST API). Artifacts such as jobs, connection profiles, users and roles, and site standards can be written in JSON and provided as input to or are generated as output by various services. Services can be accessed directly through HTTPS requests by using curl or similar facilities or the provided ctm[ command line interface (CLI)](https://documents.bmc.com/supportu/API/Monthly/en-US/Documentation/API_Installation.htm#InstallingtheControlMAutomationCLI).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/introduction.html
---

# Using Control-M workflow orchestrator integration with AWS Mainframe Modernization
<a name="introduction"></a>

*Sunil Bemarkar, Vij Balakrishna, Pablo Alonso Prieto, and Vaidy Sankaran, Amazon Web Services*

*Joe Goldberg, BMC SOFTWARE INC*

**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

To meet the needs of a business and digital transformation, customers are modernizing mainframe applications to achieve increased agility, reduce costs, and innovate faster. At re:Invent 2021, Amazon Web Services (AWS) announced the [AWS Mainframe Modernization](https://aws.amazon.com/mainframe-modernization/) service to help customers modernize their mainframe workloads. AWS Mainframe Modernization provides a cloud-native managed and highly available runtime environment on AWS.

This guide provides detailed information on how [BMC Helix Control-M](https://www.bmc.com/it-solutions/bmc-helix-control-m.html) workflow orchestration can be integrated with the AWS Mainframe Modernization service to give you an additional option for modernizing your batch applications during your mainframe modernization journey. By using the capabilities of Control-M, organizations can rationalize an environment that consists of existing and migrated workloads using a single tool that delivers an end-to-end view.

## Overview
<a name="overview"></a>

The integration of Control-M and AWS Mainframe Modernization Replatform with Micro Focus offers the following benefits:
+ Helps with reducing talent gaps
+ Supports rapid innovation with an agile DevOps approach
+ Provides easier access to applications and data without significant changes
+ Optimizes the costs of running or extending applications
+ Maximizes business agility and reduces costs.

The AWS Replatform with Micro Focus service helps you modernize your mainframe applications to AWS cloud-native managed runtime environments. It provides tools and resources to help you plan and implement migration and modernization. Users can submit or cancel batch jobs and review the details of batch job runs. Each time a user submits a batch job, the AWS Replatform with Micro Focus service creates a separate batch job run, which can be monitored. Using the AWS Mainframe Modernization service web console, you can search for batch jobs by name, provide job control language (JCL), script files, and parameters to batch jobs.

Using Control-M, you can define, schedule, manage, and monitor application and data workflows. This enhances visibility and reliability, which helps with improving service-level agreements (SLAs). Control-M integrates, automates, and orchestrates workflows on premises and in AWS Cloud to help you deliver business services on time. With a single unified graphical view, users can orchestrate all your workflows, including file transfers, applications, data sources and infrastructure, with a rich library of plug-ins. Provisioned in a cloud, Control-M uses the ephemeral capabilities of the AWS Cloud. Because they use a jobs-as-code approach, with REST APIs, JSON, and Python within the continuous integration and continuous delivery (CI/CD) toolchain, Control‑M workflows can be versioned, tested, and maintained, so that developers and DevOps engineers can work collaboratively.

**Note**
AWS Mainframe Modernization Refactor with AWS Blu Age is also supported. For more information, see the [AWS Prescriptive Guidance guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/introduction.html).

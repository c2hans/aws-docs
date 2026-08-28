---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/introduction.html
---

# Running modernized Blu Age mainframe workloads on serverless AWS infrastructure
<a name="introduction"></a>

*Richard Milner-Watts, Amazon Web Services*

Many organizations use older, mainframe computers to run workloads that are key to their operations. However, these legacy mainframe workloads can be problematic to maintain for a number of reasons, including the following:
+ The programming languages being used, such as common business-oriented language (COBOL), are often older and infrequently taught to new developers.
+ The mainframe environments that run the workloads are expensive to operate and maintain, and they commonly require significant on-premises infrastructure for support.
+ Specialized skills are required to operate mainframes, necessitating that your organization retains staff with rare (and often expensive) skills or works with partners who specialize in this space.
+ Parts and support from vendors can be challenging and costly to obtain.

Migrating these legacy mainframe workloads into modern cloud architectures can eliminate the costs of maintaining a mainframe—costs that only increase as the environment ages. By modernizing the mainframe workload and migrating it to the cloud, you can refactor the application, reduce costs, and take advantage of the latest cloud service and offerings.

Migrating jobs from a mainframe can pose unique challenges. Staff might not be familiar with the job logic. Mainframes are designed to handle very high volumes of input and output (I/O), achieving performance that modern generalized CPUs can struggle to match. Rewriting these jobs can be a large undertaking and require significant effort.

[Blu Age](https://www.bluage.com/) is an AWS [mainframe modernization tool](https://aws.amazon.com/mainframe-modernization/patterns/refactor) that converts legacy mainframe workloads, including application code, dependencies, and infrastructure, into modern workloads for the cloud. It converts legacy mainframe workloads into modern Java code. Blu Age reads the code from the legacy mainframe workload and then uses a translation engine to create a modern Java application with equivalent functionality. After you modernize and refactor the workload, you deploy it in the AWS Cloud. The modernized application needs access to the same inputs and outputs as the original mainframe application, and it requires an operating environment. For more information about modernizing your workloads by using Blu Age and AWS services, see these AWS Prescriptive Guidance publications:
+ [Containerize mainframe workloads that have been modernized by Blu Age](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/containerize-mainframe-workloads-that-have-been-modernized-by-blu-age.html)
+ [Deploy an environment for containerized Blu Age applications by using Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-environment-for-containerized-blu-age-applications-by-using-terraform.html)

This guide provides best practices and a reference architecture for deploying and operating the entire modernized workload on cloud-native, serverless infrastructure. The architecture in this guide is designed with the following considerations in mind:
+ Running [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instances 24/7 in order to host these Java applications is not recommended. The proven architecture in this guide is based around [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). These services can orchestrate and run these modernized workloads.
+ After the mainframe tasks have been converted into Java, you confirm that the integrated systems successfully process the task inputs and outputs.
+ The target infrastructure for the modernized workloads should be [well-architected](https://aws.amazon.com/architecture/well-architected) to minimize costs and operational overhead and to maximize performance, availability, security, and sustainability.
+ The architecture covers both batch jobs that run on demand and real-time services that need to run and scale with the incoming load.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The best practices and sample architecture covered in this guide can help you and your organization achieve the following business objectives:
+ Understand the value proposition of the Blu Age mainframe modernization service and how it can be used to reduce the costs of migrating away from existing mainframe implementations.
+ Understand the types of mainframe job types that you can migrate to AWS by using Blu Age.
+ Plan how the target architecture detailed in this guide can be applied to your mainframe workloads.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for enterprise and data architects who are evaluating options to decommission their mainframes by migrating workloads to the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

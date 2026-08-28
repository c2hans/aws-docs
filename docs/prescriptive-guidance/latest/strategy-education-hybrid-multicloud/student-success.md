---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-education-hybrid-multicloud/student-success.html
---

# Predicting student success
<a name="student-success"></a>

A Midwest university in the US discovered that a handful of key activities for incoming first-year students was highly predictive of success, both in the student's first semester of classes and in attaining their degree. The university wanted to implement a system that watched for these activities to be completed, and when key deadlines approached or passed, they wanted to encourage students to complete these steps.

The SaaS learning management system (LMS) data was a key input for this solution, but its data proved to be challenging to access and process with the university IT team's data warehousing tools. In addition, the messages to students had to be sent through the school's cloud-based customer relationship management (CRM) system. To build a functional solution and assess the effectiveness of prompts to students, the university had to initiate messages through the CRM and gather data from it.

The university developed and deployed a solution into a single cloud environment. The solution is a mixture of cloud-native managed services, provisioned cloud servers, and integrations with on-premises systems and cloud-based SaaS applications. As the following diagram shows, the solution ingests data from the student information system (SIS), LMS, and CRM into a data lake. It uses this data to identify students who are in jeopardy of missing key activities, initiates messages to them through the CRM, and provides a dashboard to university leadership.

![System for predicting student success](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-education-hybrid-multicloud/images/guide-img/72d1214e-0148-413e-9e71-1a181ad4845c/images/0aebe4be-56c2-41dc-9a21-edd0f3ab6383.png)

This architecture follows these recommendations:
+ **Select a primary, strategic cloud provider. **The university's strategic cloud provider houses the entire deployed solution. This enables the IT and business staff to focus on developing skills in a single, integrated set of cloud capabilities.
+ **Differentiate between SaaS applications and foundational cloud services. **The university differentiates between SaaS applications and core cloud analytics services, and uses integrations with the SaaS applications to gather data and initiate the appropriate communications.
+ **Establish security and governance requirements for each cloud service provider. **The university ensures that all components of the architecture are secure by enforcing guardrails and controls, including encryption in transit and at rest, to handle student data appropriately.
+ **Adopt cloud-native, managed solutions wherever possible and practical. **Cloud-native managed services are used for data ingestion, storage, database, and extract, transform, and load (ETL) functionality, which reduces the time to develop the end-to-end data processing workflow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

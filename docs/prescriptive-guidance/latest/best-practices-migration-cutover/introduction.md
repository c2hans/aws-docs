---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/introduction.html
---

# Best practices for cutting over network traffic to AWS during a migration
<a name="introduction"></a>

*Damien Renner, Ernest Asare, Martin Fluck, Khurram Mahmood, and Mark Willis, Amazon Web Services*

The cutover phase is one of the most critical stages in a cloud migration. In a cutover, you redirect your network traffic from a source system to a target system hosted on Amazon Web Services (AWS). During the cutover, your systems and users are most likely to experience some level of disruption. To minimize disruption and mitigate cutover risks, we recommend that you develop a cutover plan that aligns with the best practices covered in this guide. This guide is intended for migration consultants, application architects, program managers, application owners, and any other role that's implementing or leading a cloud migration to AWS.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The ultimate goal of this guide is to help you minimize the disruptions and mitigate the risks associated with the cutover phase of a cloud migration. This guide can help you achieve this overall goal by meeting the following targeted business outcomes:
+ Developing an optimal cutover process
+ Developing a communication and governance strategy for your cutover
+ Understanding the different cutover options and choosing the most effective one based on your requirements

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

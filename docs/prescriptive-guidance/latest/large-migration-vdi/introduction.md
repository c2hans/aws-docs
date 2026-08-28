---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/introduction.html
---

# Planning large VDI migrations to the AWS Cloud
<a name="introduction"></a>

*Martin Guenthner, Amazon Web Services*

In the migration space, large-scale migrations of applications are a well-established pattern. Many organizations also need to migrate virtual desktop infrastructures (VDIs). However, because VDIs are end-user facing and have special requirements, in terms of availability, accessibility, and provisioning, this type of migration requires special considerations and planning compared to typical large-scale migrations.

This guide describes multiple architectural decision points for planning a large-scale migration of on-premises VDIs to the AWS Cloud. It also includes some additional recommendations for migrating from a Citrix environment, but these recommendations can also apply to other source technology stacks.

This guide helps you plan a large VDI migration to the AWS Cloud by providing a checklist of decisions that you'll need to make during the migration. As you complete the checklist, you'll be making informed decisions about the migration and the target architecture, which includes [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) instances and [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) file shares.

The technical and non-technical considerations in this guide can also be used to evaluate alternatives to traditional VDI solutions, such as [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) or [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html). As part of your migration planning, we recommend that you do a feasibility assessment to consider migrating to these services.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for VDI platform owners who are considering a platform migration to AWS, storage architects who support the migration approach, and compliance and risk teams who guide the decision-making process for reliability requirements.

## Attachments
<a name="attachments-4216869b-a3c7-4a1b-8529-279b6b36f090"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

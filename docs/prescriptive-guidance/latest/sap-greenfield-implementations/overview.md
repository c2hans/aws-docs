---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/overview.html
---

# Overview
<a name="overview"></a>

This document highlights lessons learned during a greenfield implementation of SAP on AWS.  Most of these recommendations can be applied to standard SAP on AWS migration projects as well. This article shares advice for the planning, design, and build phases of a project.   It includes lessons for the maintenance or operations phase of a project, but that phase isn't the focus of this guide. You can use a waterfall methodology or an iterative, agile, or hybrid approach to apply these best practices.

Here are the key stakeholders of the infrastructure team who are referenced in this guide:
+ The AWS implementation partner – This could be AWS Professional Services or an AWS Partner.  Their role is to build the AWS infrastructure that SAP applications will run on.
+ The SAP Basis team – This team can be supplied by the systems integrator (SI) or vendor company, staffed in house by employees at your organization, or a mix. Their job is to install the SAP software, configure it at a technical level, upgrade it, and generally maintain it.
+ SI infrastructure leader – This individual serves as a product owner. They provide technical requirements that originate from the bigger project team and provide general leadership to the infrastructure team.
+ Customer infrastructure leader – This individual also serves as a product owner. They provide technical requirements that originate from the bigger project team and provide general leadership to the infrastructure team. The SI and customer infrastructure leaders can operate as equals in a joint leadership model, or you might decide to designate a single infrastructure leader.

The focus of this prescriptive guidance is specifically on the AWS aspect of a greenfield SAP project.

When deploying SAP environments on AWS, the infrastructure teams are typically months ahead of the functional and development teams who are configuring and customizing SAP to meet business needs. Because the two teams are on different delivery timelines, what is considered the build phase for the infrastructure team might be the planning phase for the functional teams. Additionally, the work of building SAP environments is very iterative and repetitive. For example, in an N\+2 scenario, you might build three different development environments. Depending on how you structure your project and when the environments are needed, it is possible to have three build phases, unless the environments are all due on the same date. Keep these differences in mind when applying this guidance to the specific phases of your project, so you can communicate and work with the functional and development teams more effectively.

## Intended audience
<a name="intended-audience"></a>

This document is written with project managers in mind, as a guide for project implementation, and as a tool for setting expectations and providing strong IT leadership during an SAP on AWS implementation. In a large-scale SAP implementation, it is likely that all the members of the infrastructure team will participate with their own project managers to manage their piece of work. We recommend that you identify a single, overarching infrastructure project manager to manage the overall cloud journey and to take accountability for ensuring that these best practices are followed.

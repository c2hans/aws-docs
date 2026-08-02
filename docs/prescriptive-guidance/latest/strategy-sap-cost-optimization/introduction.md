---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/introduction.html
---

# Cost optimization strategy for SAP workloads in the AWS Cloud
<a name="introduction"></a>

*Chris Grudzinski and Sergej Trisic, Amazon Web Services*

Migrating [SAP](https://www.sap.com/about/what-is-sap.html) workloads to the AWS Cloud can improve reliability, scalability, and agility and can reduce operational costs associated with running SAP. According to [Business Benefits of Running SAP Workloads on AWS](https://pages.awscloud.com/acq_NAMER_SAP-IDG-MarketPulse-Study-Feb-2019-Registration-Page.html) (IDG whitepaper), "Cost savings are the primary motivator for customers to make the move, with 96% of customers reporting a reduction in total cost of ownership (TCO) and an average overall savings of 26%".

The same IDG whitepaper revealed that most organizations realize their cost savings expectations after two years. 43% of the respondents saved on hardware and software, 37% cited operational savings, and 36% realized savings on ongoing maintenance. From our experiences, SAP workloads consume a large proportion of the typical IT budget. By implementing the strategies in this guide, you can redirect your savings to other initiatives, such as improving IT operations and advancing innovation.

This guide helps you optimize the costs of running SAP on AWS and highlights the AWS services and tools that support this strategy. Generally, there are two levers that allow you to control your spending for AWS services:
+ **Specific pricing models** – You typically select a pricing model at the beginning of your migration journey. This guide briefly discusses pricing models and includes references to additional resources so that you can dive deeper. Because some pricing models are subject to term commitments, this section is most applicable for enterprises at the beginning of their migration journey or enterprises that are revisiting their current models.
+ **AWS services** – Native AWS services and tools can provide detailed analysis and visualization into your actual and projected costs. This guide focuses primary on this lever. Analysis and visualization of costs are critical because you or managed services provider (MSP) can measure, act, and learn in an interactive and agile manner.

|
|
| Important The AWS services mentioned in this guide might make recommendations to optimize your costs. However, these recommendations might not be compatible with operating SAP workloads. Before acting, confirm that the recommendations are compatible with operating SAP on AWS:[SAP Applications on AWS: Supported DB/OS and AWS EC2 products – 1656099](https://launchpad.support.sap.com/#/notes/1656099) (SAP note)[SAP on AWS: Support prerequisites - 1656250](https://launchpad.support.sap.com/#/notes/1656250) (SAP note) |
| --- |

## Intended audience
<a name="intended-audience"></a>

This guide is designed for senior SAP stakeholders, such as chief information officers (CIOs); chief digital officers (CDOs); vice presidents (VPs), cloud financial operations officers; and directors of enterprise application teams, SAP or enterprise resource planning (ERP) competence centers, and IT infrastructure teams. The goal of this guide is to help you select, customize, and deploy AWS services that optimize your spending and balance it against performance, availability, flexibility, and speed objectives. As a result, this document doesn't focus on technical details or implementation. However, it might be helpful for technical consultants, solution architects, IT administrators, and other IT staff responsible for managing costs. The guide includes references to deeper technical content about SAP technologies and cost management on AWS.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>
+ Reduce hardware costs
+ Reduce operating system (OS) costs
+ Minimize maintenance costs for hardware and OSs
+ Reduce software costs
+ Improve cost efficiencies by centralizing cost management
+ Improve organizational learnings

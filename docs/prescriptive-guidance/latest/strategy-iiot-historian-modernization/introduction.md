---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/introduction.html
---

# Modernizing data historians for the manufacturing industry in the AWS Cloud
<a name="introduction"></a>

*Devender Satija, Amazon Web Services*

Industry 4.0 is a revolution in the manufacturing industry, and it's shaped by intelligent computing. Connectivity, data, analytics, artificial intelligence (AI), and machine learning (ML) are driving a digital transformation of the manufacturing industry. The result is the emergence of the industrial Internet of Things (IIoT) and the convergence of operational technology (OT) and information technology (IT) teams. *Historian modernization* is an approach used to modernize and upgrade OT systems to better serve the needs of the manufacturing industry.

Industry objectives haven't changed over the years; the focus remains on continuous quality improvement and reduced downtime. Many organizations have factory assets that are more than 20 years old, and much of the production data is trapped in these aging machines. To optimize operations, manufacturers need to extract that data, enrich it with data from other sources, and gain insights from it. Historically, manufacturers have depended on an on-premises historian. A *manufacturing data historian*, also known as a *historian*, is a type of database that is used to collect and store data from various sources in a factory. This guide provides strategies for modernizing historians in order to take advantage of the connectivity, analytics, and AI/ML benefits of the AWS Cloud.

## Overview
<a name="overview"></a>

Historian modernization strategies focus on the use of data and technology to help organizations make better decisions. These strategies include using existing data, analyzing that data, and uncovering insights by using advanced technologies, such as AI/ML. These strategies can help improve operational efficiency, reduce downtime, and drive innovation.

The following are common drivers for modernization, depending on the size of the organization:
+ **Unprecedented scale and data democratization **– The data might be available, but it is siloed in on-premises historians that provide only local visibility and limited local analytics. As your organization continues to accrue more data, the cost of storing and managing that data in on-premises historians continues to rise.
+ **Relentless innovation or a merger** – It can be challenging to maintain and integrate various on-premises historians as a result of expansion, a merger, or an acquisition.
+ **Performance at the edge **– You might be unable to bring advanced analytics and compute power to on-premises operational data.
+ **Opportunities for scale and savings** – Scalability, performance issues, and prohibitive tag-based licensing models can affect the total cost of ownership (TCO) and can prevent adequate data acquisition to build advanced use cases.
+ **Actionable insights** – IT and OT data aren't sufficiently integrated to provide plant supervisors with timely insights that help them minimize unplanned downtime, improve product quality, and increase asset performance and availability.
+ **Sustainability** – To meet sustainability and energy-saving goals, you need a better understanding of plant operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

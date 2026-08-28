---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/introduction.html
---

# Strategies for building a data mesh-based enterprise solution on AWS
<a name="introduction"></a>

*Dhrubajyoti Mukherjee, Adjoa Taylor, and Siva Venkat, Amazon Web Services*

Amazon Web Services (AWS) customers of all sizes are generating massive quantities and types of data. To manage this data, many organizations have built central data lakes to collect, store, process, and take action to deliver value for their customers and operate their business more effectively. Often, a central data team builds the data pipelines to ingest data into the data lake and manages access to the data. However, as the data volume grows, the data lake-based approach doesn't scale with it. In addition, as the number of data creators and users increase, the data team can't process all requests in time, and it becomes a bottleneck.

To address this issue, your organization can provide autonomy to the teams that generate and use the data. The data creator and user teams can then manage and access the data assets without relying on a central data team. This shift toward a decentralized approach to data ownership requires a decentralized data solution architecture.

A decentralized data solution that uses an architectural and organizational approach such as data mesh helps companies accelerate innovation and drive business value. Data mesh is based on four fundamental principles:
+ Domain ownership
+ Data as a product
+ Self-service data platform
+ Federated governance.

For more information about data mesh concepts and terminology, see the [Resources](resources.md) section.

This document focuses on strategies for building a data mesh–based solution on the AWS Cloud. It's intended for CTOs, CIOs, CDOs, IT and business executives, program managers, and architects. The document discusses the following:
+ How you can accelerate your enterprise data mesh strategy by using the Data Mesh Strategy Framework
+ The teams and personas involved, and their responsibilities
+ The AWS services that you can use to build the data solution

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

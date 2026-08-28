---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/introduction.html
---

# Migrating OpenText TeamSite and Media Management workloads to the AWS Cloud
<a name="introduction"></a>

*Battulga Purevragchaa, Amazon Web Services*

## Overview
<a name="overview"></a>

[OpenText TeamSite](https://www.opentext.com/products-and-solutions/products/customer-experience-management/web-content-management/opentext-teamsite) helps deliver personalized, omnichannel digital experiences through an enterprise web content management system (CMS). OpenText TeamSite also integrates with OpenText digital asset management solutions, such as [OpenText Media Management](https://developer.opentext.com/ce/products/media-management) and [OpenText MediaBin](https://www.opentext.com/products-and-solutions/products/customer-experience-management/digital-asset-management/opentext-mediabin). These solutions offer digital asset management and distribution capabilities, and you can use them to complement OpenText TeamSite.

Many [OpenText Customer Experience ](https://www.opentext.com/products-and-solutions/products/customer-experience-management)workloads are hosted on premises or on traditional hosting solutions with fixed capacity or legacy hosting cost models. Migrating your OpenText Customer Experience platform to the Amazon Web Services (AWS) Cloud provides additional capabilities and value by increasing your business agility and integration capabilities, and reducing the total cost of ownership (TCO). By migrating OpenText TeamSite and Media Management workloads to the AWS Cloud, you can achieve the following three business outcomes:
+ **Improved business agility** – Reduce the cost and time to market for your new campaigns, products, solutions, and functionalities by using improved development and deployment tools, and integrating with the AWS Cloud.
+ **Significant cost reduction** – Benefit from economies of scale and use an infrastructure in the AWS Cloud that quickly scales to your requirements. Typically, hosting OpenText workloads on the AWS Cloud [can reduce your costs by up to 70 percent](https://www.tbscg.com/whitepaper/).
+ **Enable innovation and digital transformation** – Use AWS cloud-native services or integrate with external cloud applications to enable innovative use cases for improving user experience, gaining business insights, or optimizing costs and resources (for example, improved data and customer analytics, custom-made content, or artificial intelligence (AI)-driven customer interactions).

You can achieve these business outcomes by migrating your OpenText TeamSite platform to the AWS Cloud and modernizing it with AWS products and services.

Modernizing an OpenText TeamSite workload depends on the characteristics of your migration's implementation and your specific business requirements. We recommend that you use the [API in the cloud](https://www.tbscg.com/expertise/) approach when modernizing an OpenText Customer Experience platform. This approach enables [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to orchestrate different applications deployed in containers on [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), serverless applications (for example, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)), and commercial-off-the-shelf (COTS) applications. The approach also exposes a consolidated catalog of services and applications to the public internet.

This guide focuses on migrating OpenText TeamSite workloads to the AWS Cloud to reduce costs and enable modernization. For a full overview of the migration steps, see the pattern [Migrate OpenText TeamSite workloads to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-opentext-teamsite-workloads-to-the-aws-cloud.html) on the [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance) website. This guide was created by AWS and [TBSCG](https://www.tbscg.com/), an AWS Partner, and is intended for technical managers, technical executives, and technical engineering and architectural teams that are migrating OpenText TeamSite workloads to the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

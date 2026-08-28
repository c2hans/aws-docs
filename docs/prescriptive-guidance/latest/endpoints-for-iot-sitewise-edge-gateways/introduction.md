---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/introduction.html
---

# Required endpoints for AWS IoT SiteWise Edge gateways
<a name="introduction"></a>

*Anish Kunduru, Hemant Borole, Sudhakar Reddy, and Ayush Sood, Amazon Web Services*

AWS IoT SiteWise is a service for the AWS Cloud that helps you collect, model, analyze, and visualize data from devices at scale. To connect your edge devices and servers to AWS IoT SiteWise, you use a *gateway*. [AWS IoT SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-gateway-ggv2.html) gateways run on AWS IoT Greengrass V2. The AWS IoT SiteWise Edge software is installed alongside an AWS IoT Greengrass core device and collects equipment data. AWS IoT Greengrass requires access to other AWS services, such as Amazon Simple Storage Service (Amazon S3), AWS Secrets Manager, and AWS Systems Manager. Connections to these services are required for AWS IoT SiteWise Edge gateways to function properly. You can optionally connect to other AWS services and features that provide additional business value, such as storing data, analyzing data, optimizing operations, and increasing availability.

However, common firewall configurations in industrial control networks can prevent these AWS IoT services from connecting to their supporting services in the AWS Cloud. A common approach for protecting on-premises systems or operational technology (OT) networks is to restrict Internet access by using an allow list. An *allow list* is an explicit list of trusted domains or IP addresses that users can access. Allow listing is typically configured in a firewall in the internet perimeter zone. This can prevent the AWS IoT SiteWise Edge gateways from accessing AWS services in the cloud.

This guide describes how to configure a network with firewalls to allow access to AWS service endpoints that allow your AWS IoT SiteWise Edge gateways to connect to the required target services. You use an endpoint to connect programmatically to an AWS service in a virtual private cloud (VPC). A *service endpoint* is the URL of the entry point for an AWS service. For more information, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in *AWS General Reference*. Configuring and testing endpoints helps make sure that the firewall permits the requests to those services before you create the gateway.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for, but not limited to, the following audiences:
+ Cloud application architects
+ Cloud infrastructure architects
+ Network engineers
+ DevOps professionals
+ Developers

Before reading this guide, it is helpful to understand the levels of an industrial control network, as defined in the Purdue reference model. For more information about this model and how cloud, Internet of Things (IoT), and edge computing developments are transforming on-premises OT workloads into hybrid workloads for the AWS Cloud, see [Security Best Practices for Manufacturing OT](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/security-best-practices-for-manufacturing-ot.html) (AWS Whitepaper).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

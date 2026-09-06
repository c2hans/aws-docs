---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/introduction.html
---

# Integrating third-party services in the AWS Cloud
<a name="introduction"></a>

*Manuel Marugan Cruz and Giulio Dipace, Amazon Web Services*

In the Amazon Web Services (AWS) Cloud, it's common to interact with third-party providers and integrate third-party services for specific functionalities that you do not want to build in-house, from scratch. The functionalities provided by vendors differ, and there are many different vendors. Each vendor has proprietary solutions that address specific use cases. Independently of the functionality of the third-party solution, the integration must be scalable, secure, and resilient.

There are different ways to integrate third-party services, depending on how they are hosted. Often, third-party services also use the AWS Cloud. In this case, the integration between your resources and the third-party resources can be achieved by using AWS native constructs.

The recommendations in this guide help you standardize your third-party integrations and meet your requirements for networking, security, scalability, and resiliency. This guide discusses four architectures for cloud-native integration of third-party solutions. The architectures in this guide use one of the following AWS services for third-party integration: AWS PrivateLink, Amazon Virtual Private Cloud (Amazon VPC) peering connections, and AWS Transit Gateway. This guide also describes the advantages and disadvantages of each architectures and provides a simple decision chart to help you select an architecture based on integration characteristics.

## Target audience
<a name="target-audience"></a>

This prescriptive guidance is written specifically for application owners, business owners, architects, technical leads, and project managers and is designed to facilitate planning and implementation.

## Attachments
<a name="attachments-80f3a808-d645-486e-82c4-f574fdcf6710"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

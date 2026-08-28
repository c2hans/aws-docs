---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/elpg-overview.html
---

# 1 Overview
<a name="elpg-overview"></a>

An ExpressLink module is a connectivity module connected via serial interface (initially UART based) that uses an abstracted Application Programming Interface (API) to connect any host application to AWS IoT Core and its services. In so doing, an ExpressLink module offloads complex and undifferentiated workloads, such as authentication, device management, connectivity, and messaging, from the application (host) processor. ExpressLink modules were conceived after discussions with microcontroller vendors, OEMs, and module makers regarding the complexity and repetitiveness of migrating existing hardware and software designs to new or different MCUs and RTOSs. They enable a scalable migration for millions of embedded applications to cloud-connected applications.

## 1.1 Goals
<a name="elpg-overview-goals"></a>

The top-level goals are to:
+ Accelerate time to market for IoT devices.
+ Ease the transition to cloud connected solutions:
  + Reduce the skill gap required for cloud-connected embedded applications.
  + Allow OEMs to migrate existing designs by adding ExpressLink to existing applications with minimal modification to the existing application code.
+ Dramatically reduce the resources embedded devices require to connect to AWS IoT Core and publish and subscribe to topics, regardless of the connectivity solution chosen (Wi-Fi, ethernet, or cellular):
  + An abstract API does not reveal (leak) implementation details to the customer application.
  + Configuration parameters (implementation dependent) are easily isolated.
  + Requires minimal hardware connections with defined pinouts (two wire minimum).
  + Provides stateless module communication (command mode only, single configuration).
+ Support a hardware root of trust-based unique identity that allows for an optimal out-of-the-box experience and high-volume quick manufacturing, even when using untrusted Contract Manufacturers, by taking advantage of the AWS Multi Account Registration feature.
+ Provide a quick evaluation experience out-of-the-box without requiring an AWS account.
+ Simplify onboarding with an additional late binding option.
+ Offer easy updates over the air (and over the wire) so the module and host processor can ensure security throughout the life of the product.
+ Connect to standard AWS IoT Core services without additional cost and allow for heterogenous fleets.

## 1.2 Specifications
<a name="elpg-overview-specifications"></a>

The specifications in this document are the minimum set of requirements needed by the ExpressLink module to provide connectivity and basic support for AWS services. The ExpressLink manufacturer (third party) can provide additional pins and commands that can present key differentiators of their unique product or technology within the guidelines provided in this document. Testing and AWS qualification of the device will be based on this specification and not on any additional features or functionality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/understanding-matter.html
---

# Understanding the Matter standard
<a name="understanding-matter"></a>

![Matter administrators managing Matter-compatible devices](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/images/guide-img/b77bbd58-038f-410c-901d-a12fcd0e950b/images/4b747b4c-20c7-4079-8b78-a53c95b60796.png)

## Matter protocol
<a name="matter-protocol"></a>

Matter is an open, smart-home connectivity protocol that enables communication between devices, mobile apps, and cloud services. Developed by the Connectivity Standards Alliance (CSA), Matter simplifies connectivity and interoperability for consumers and manufacturers. Matter supports a wide range of smart-home categories. For consumers, Matter provides onboarding, unified management, and control across ecosystems. For manufacturers, Matter reduces development and support costs through a single certification and through app development. Many large companies, such as Amazon, Apple, and Google, are promoting Matter adoption. CSA offers four [membership levels](https://csa-iot.org/become-member/) depending on the organization involvement - Promoters, Participants, Adopters, and Associates. With strong industry support, Matter aims to provide seamless connectivity across brands for consumers and streamline development for manufacturers.

Matter smart home standard has matured significantly with the introduction of version 1.5 on November 20, 2025. The standard expanded support for camera streaming, energy management systems including solar, batteries, and heat pumps. Advances on protocol level include stability advances for Thread and better TV-device integration.

## Overview of how Matter works
<a name="how-matter-works"></a>

Matter is an IP-based, application-level protocol for smart-home devices across vendor ecosystems. It works on devices that use IPv6. Conceptually, Matter is organized as a collection of network *nodes*, which are Matter endpoints. The following is a brief summary of the Matter terminology:
+ *Matter devices* are smart-home products, such as light bulbs, switches, thermostats, or locks.
+ A *Matter fabric *is the virtual network on which all of the devices are connected. All of the devices share the same trusted root. The fabric forms a star network topology.
+ A *Matter administrator* creates, maintains, and manages security and privileges for all devices on the fabric. An administrator can be a hub or an application. Matter has a Multi-Admin feature, where a Matter device can be part of multiple fabrics simultaneously. For example, a single Matter device can be managed both by an Amazon Alexa device and a Google Home device, both of which could be Matter administrators on the same physical network.
+ A *Matter commissioner* is a device that commissions (or *onboards*) a new Matter device into the fabric. This could be an app on a phone, a smart-home gateway, or a Matter administrator.
+ A *Matter bridge* connects non-IP protocol devices to a Matter fabric.

For information about the different roles that hardware and software can assume in Matter, see [Peeking Under the Hood of Your Matter Smart Home](https://csa-iot.org/newsroom/peeking-under-the-hood-of-your-matter-smart-home/) (CSA blog post). Matter version 1.4 introduced Enhanced multi-admin with improved credential sharing using Home Router Access Protocol (HRAP). Matter version 1.5 introduced camera streaming. Matter versions are released approximately twice a year.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

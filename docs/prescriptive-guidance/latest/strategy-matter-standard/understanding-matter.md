---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/understanding-matter.html
---

# Understanding the Matter standard
<a name="understanding-matter"></a>

![Matter administrators managing Matter-compatible devices](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/images/guide-img/b77bbd58-038f-410c-901d-a12fcd0e950b/images/4b747b4c-20c7-4079-8b78-a53c95b60796.png)

## Matter protocol
<a name="matter-protocol"></a>

Matter is an open, smart-home connectivity protocol that enables communication between devices, mobile apps, and cloud services. Developed by the Connectivity Standards Alliance (CSA), Matter simplifies connectivity and interoperability for consumers and manufacturers. Matter supports a wide range of smart-home categories. For consumers, Matter provides onboarding, unified management, and control across device brands. For manufacturers, Matter reduces development and support costs through a single certification and shared app development. Many large companies, such as Amazon, Apple, and Google, promote Matter adoption. CSA offers four [membership levels](https://csa-iot.org/become-member/) based on the level of an organization's involvement: Promoters, Participants, Adopters, and Associates. With industry support, Matter aims to provide connectivity across brands for consumers and to streamline development for manufacturers.

## Overview of how Matter works
<a name="how-matter-works"></a>

Matter is an IP-based, application-level protocol for smart-home devices from different vendors. It works on devices that use IPv6. A Matter network consists of nodes. Each node can contain one or more endpoints that expose the device's functions. The following list summarizes Matter terminology:
+ *Matter devices* are smart-home products, such as light bulbs, switches, thermostats, or locks.
+ A Matter fabric is a logical security domain containing Matter nodes that share a common root of trust and can communicate securely.
+ A *Matter administrator* creates, maintains, and manages security and privileges for all devices on the fabric. An administrator can be a hub or an application. Matter has a Multi-Admin feature, where a Matter device can be part of multiple fabrics simultaneously. For example, a single Matter device can be managed both by an Amazon Alexa device and a Google Home device, both of which could be Matter administrators on the same physical network.
+ A *Matter commissioner* is a device that commissions (or *onboards*) a new Matter device into the fabric. This could be an app on a phone, a smart-home gateway, or a Matter administrator.
+ A *Matter bridge* connects non-IP protocol devices to a Matter fabric.

For information about the different roles that hardware and software can assume in Matter, see [Peeking Under the Hood of Your Matter Smart Home](https://csa-iot.org/newsroom/peeking-under-the-hood-of-your-matter-smart-home/) (CSA blog post).

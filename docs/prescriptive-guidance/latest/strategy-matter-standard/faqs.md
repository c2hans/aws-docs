---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/faqs.html
---

# FAQs
<a name="faqs"></a>

## What are the membership levels with Matter?
<a name="faq-membership-levels"></a>

The membership information can be found on the [CSA website](https://csa-iot.org/become-member/). The membership level you choose depends on your interest in certifying a product (adopter) or defining the product type within the standard (participant). For more information about the membership levels, see [Impact the Future of the IoT](https://csa-iot.org/become-member/) on the CSA website.

## How do smart-home consumers benefit from Matter?
<a name="faq-consumers-benefit"></a>

Consumers benefit from Matter in the following ways:
+ Simplified onboarding of Matter devices at home, including enhanced setup flow, multi-device QR codes, and NFC onboarding (Matter version 1.4.1)
+ Unified management of all smart-home devices through a single app across major ecosystems (Amazon Alexa, Google Home, Apple HomeKit, Samsung SmartThings)
+ Device control from multiple voice assistants simultaneously through Enhanced Multi-Admin (Matter version 1.4)
+ Access to expanded device types including cameras with streaming, appliances, energy management devices, and robotic vacuums

For more information, see [Benefits of Matter certification for smart-home consumers](consumer-benefits.md) in this guide.

## How do device makers benefit from Matter?
<a name="faq-manufacturer-benefits"></a>

Device makers benefit from Matter in the following ways:
+ Reduced costs for supporting customers who have infrastructure and connectivity issues
+ A single certification for a device instead of multiple certifications with each ecosystem
+ Development of proprietary apps is no longer necessary for basic device functionality
+ Reduced costs of materials due to not having to ship infrastructure elements (such as Thread Border Routers)
+ Reduced costs for supporting customers who have infrastructure and connectivity issues
+ Access to mature SDKs, development tools, and testing infrastructure (significantly improved since initial release)
+ Faster time-to-market with established certification processes and expanded testing provider networks

For more information, see [Benefits of Matter certification for device makers](manufacturer-benefits.md) in this guide.

## Does Matter replace Wi-Fi, Bluetooth, or Thread?
<a name="faq-replacements"></a>

No, Matter is an application-level protocol that runs on IP networks. Devices that use Wi-Fi, Ethernet, or Thread for connectivity can become Matter certified. The following table summarizes how Matter contrasts with Wi-Fi, Bluetooth, and Thread.

|
|
| Feature | Matter | Wi-Fi | Bluetooth | Thread |
| --- |--- |--- |--- |--- |
| Purpose | Smart-home communication | Internet access and data transfer | Short-range wireless communication | Low-power wireless mesh networking |
| Range | Varies depending on the underlying protocol | Up to 300 feet | Up to 30 feet | Up to 300 feet |
| Bandwidth | Varies depending on the underlying protocol | Up to 10 gigabits per second | Up to 2 megabits per second | Up to 250 kilobits per second |
| Power consumption | Varies depending on the underlying protocol | Relatively high | Relatively low | Very low |
| Security | Varies depending on the underlying protocol | WPA2, WPA3 | AES, BLE Secure Connections | AES |
| Cost | Varies depending on the device | Relatively inexpensive | Relatively inexpensive | Relatively expensive |

## What is a vendor ID and product ID?
<a name="faq-ids"></a>

CSA members can apply for a vendor ID that identifies them as a supplier. Products from the company are henceforth assigned to this ID and can be traced back to their origin. In addition, they receive a unique product ID. The 16-digit numerical code accompanies products like a passport number and renders them as unmistakable as the vendor.

## Which devices need to be Matter certified?
<a name="faq-device-certification"></a>

Any devices that need to authenticate and be part of the Matter fabric need to be Matter certified. However, those devices that are designed to interact only with the vendor-specified hub over a non-standard (proprietary) protocol would not benefit from the Matter certification process. For example, a smart home security system hub must be certified as Matter complaint, but a door or window sensor that communicates with the hub doesn't need to be certified as Matter compliant. The choice to getting a product certified for Matter is primarily driven by this consideration.

## My product type is not currently defined in Matter. What additional tasks should I budget time for to get the products Matter certified?
<a name="faq-device-type"></a>

Matter has significantly expanded device type coverage through versions 1.0 to 1.5. The standard now supports over 50 device types, including:
+ **Core devices**: lighting, switches, plugs, door locks, thermostats, window coverings, sensors
+ **Appliances**: refrigerators, air conditioners, dishwashers, robotic vacuums, microwaves, ovens
+ **Energy management**: solar panels, batteries, heat pumps, water heaters, EV chargers
+ **Environmental**: water management devices, air quality sensors, air purifiers
+ **Security**: cameras with streaming support

If your device type is still not supported, the first step is to join the CSA as a participant. Matter releases new versions approximately twice per year, continuously expanding device type coverage. As a participant member, you can lead the definition of new device types and have access to draft specifications that enable a faster go-to-market strategy. For more information about the membership levels, see [Impact the Future of the IoT](https://csa-iot.org/become-member/) on the CSA website.

## Some of my devices connect directly to the home Wi-Fi network. Do these devices need to be Matter certified?
<a name="faq-wifi"></a>

Matter certification can benefit devices that connect directly to the smart-home network because they can connect to the Matter fabric. This enables consumers to control the devices through their virtual assistants on the same Matter fabric. However, consumers must use a device-specific app for any operations that are vendor-specific and not defined in the Matter specification.

## What is the current version of Matter and what's new?
<a name="faq-whats-new"></a>

As of November 2025, Matter 1.5 is the current version. Key additions across recent versions include:
+ Matter 1.5 (November 2025): Camera streaming support via RTSP, stability improvements
+ Matter 1.4.2 (June 2025): Improved BLE commissioning, PSA-based crypto, transport reliability
+ Matter 1.4.1 (November 2024): Enhanced setup flow, multi-device QR codes, NFC onboarding
+ Matter 1.4 (November 2024): Energy management devices, Enhanced Multi-Admin, HRAP
+ Matter 1.3 (May 2024): Appliances, EV chargers, enhanced energy reporting
+ Matter 1.2 (October 2023): Refrigerators, air conditioners, dishwashers, robotic vacuums

Matter versions are released approximately twice per year by the CSA working group.

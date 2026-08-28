---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/introduction.html
---

# Adopting the Matter standard for IoT device makers
<a name="introduction"></a>

*Tushar Patel, Vijay Ujjain, and David Walters, Amazon Web Services*

According to [Statista](https://www.statista.com/forecasts/887613/number-of-smart-homes-in-the-smart-home-market-in-the-world), the number of smart home users worldwide are expected to exceed 1.9 billion by 2029. This rapid growth brings challenges in terms of operations and management. From a consumer's point of view, each device vendor has a different method of on-boarding the smart-home device onto a home network through an app that is specific to that device vendor. This makes it challenging to manage a growing array of diverse types of devices from various vendors. Similarly, from a device maker's point of view, certifying their smart-home products with various ecosystems adds to the cost and complexity of their business processes. For example, this might require different SKUs for the same device model. It is an additional overhead to maintain a compelling user experience app and provide periodic updates, taking resources away from the focus on building and delivering a better product. Both consumers and device makers would benefit from a common smart-home interoperability standard. This standard allows devices from multiple vendors to interoperate with each other in a seamless, secure, and reliable manner. Both consumers and device makers have benefited significantly from the adoption of a common smart-home interoperability standard that enables devices from multiple vendors to interoperate seamlessly, securely, and reliably.

The [Matter](https://csa-iot.org/all-solutions/matter/) standard evolved from an exciting opportunity for Internet of Things (IoT) device manufacturers in the smart-home space to actually deliver on the promise of a single protocol to connect smart-home systems. This standard aims to improve compatibility and interoperability between devices from different manufacturers. Matter is an open, smart-home connectivity protocol that enables communication between IoT devices, mobile apps, and cloud services.

## Objectives
<a name="objectives"></a>

When integrating the Matter standard into their products, IoT device manufacturers must address several challenges before beginning development. Matter offers many advantages over proprietary IoT protocols, including interoperability, security, simplicity, reliability, and future-proofing of devices. However, integrating Matter into both new and existing IoT deployments requires careful planning and strategy. Manufacturers want guidance on the Matter compliance process in order to leverage the benefits while avoiding pitfalls. This guide provides IoT device makers with comprehensive guidance about Matter adoption. It includes a clear roadmap, from strategy to implementation. This guide eases the transition to Matter, helping you build secure, interoperable, and future-ready products that thrive in the smart-home ecosystem. With the right strategic approach, organizations can overcome the hurdles of Matter adoption and develop innovative IoT devices that embrace open standards.

The Matter standard, now in version 1.5, has matured into a proven solution for Internet of Things (IoT) device manufacturers in the smart-home space. This open standard has demonstrated substantial improvements in compatibility and interoperability between devices from different manufacturers. Matter is an open, smart-home connectivity protocol that enables communication between IoT devices, mobile apps, and cloud services across major ecosystems including Amazon Alexa, Google Home, Apple HomeKit, and Samsung SmartThings.

Matter 1.5 introduces expanded device support beyond the initial release, now including enhanced energy management devices, robotic vacuums, air quality sensors, air purifiers, and improved support for cameras and security systems. The standard has also added advanced features such as multi-admin capabilities, improved commissioning flows, and enhanced security protocols. With thousands of certified Matter devices now available in the market, the ecosystem has reached critical mass, making Matter adoption essential rather than optional for device manufacturers seeking market competitiveness.

This guide provides device makers a comprehensive overview of Matter and the steps required to become Matter-compliant. It outlines pros and cons for planning a Matter adoption strategy. The guide also suggests best practices for leveraging Matter while continuing to support existing wireless protocols, in a phased manner. For IoT device manufacturers exploring smart-home solutions, this guide can inform your connectivity strategy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

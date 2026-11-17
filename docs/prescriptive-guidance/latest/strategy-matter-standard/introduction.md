---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/introduction.html
---

# Adopting the Matter standard for IoT device makers
<a name="introduction"></a>

*Tushar Patel, Vijay Ujjain, and David Walters, Amazon Web Services*

According to [Statista](https://www.statista.com/forecasts/887613/number-of-smart-homes-in-the-smart-home-market-in-the-world), the number of smart home users worldwide is expected to exceed 1.9 billion by 2029. This rapid growth brings operational and management challenges. From a consumer's point of view, each device vendor has a different method of onboarding the smart-home device onto a home network through an app that is specific to that vendor. This makes it challenging to manage a growing array of diverse devices from various vendors. Similarly, from a device maker's point of view, certifying smart-home products with various smart-home systems adds cost and complexity to business processes. For example, certification might require different SKUs for the same device model. Maintaining a compelling user experience app and providing periodic updates is additional overhead that takes resources away from building and delivering a better product. Both consumers and device makers would benefit from a common smart-home interoperability standard that enables devices from multiple vendors to interoperate seamlessly, securely, and reliably.

The [Matter](https://csa-iot.org/all-solutions/matter/) standard evolved to give Internet of Things (IoT) device manufacturers in the smart-home space a single protocol to connect smart-home systems. This standard aims to improve compatibility and interoperability between devices from different manufacturers. Matter is an open, smart-home connectivity protocol that enables communication between IoT devices, mobile apps, and cloud services.

## Objectives
<a name="objectives"></a>

When integrating the Matter standard into their products, IoT device manufacturers must address several challenges before beginning development. Matter offers many advantages over proprietary IoT protocols, including interoperability, security, simplicity, reliability, and longer-lasting device support. However, integrating Matter into both new and existing IoT deployments requires careful planning and strategy. Manufacturers want guidance on the Matter compliance process so that they can use the benefits while avoiding pitfalls. This guide provides IoT device makers with guidance about Matter adoption, including a clear roadmap from strategy to implementation. This guide helps you build secure, interoperable products for the smart-home market. With the right strategic approach, organizations can overcome the hurdles of Matter adoption and develop innovative IoT devices that embrace open standards.

The Matter standard continues to evolve through regular updates from the Connectivity Standards Alliance (CSA). Matter supports interoperability across major smart-home ecosystems, including Amazon Alexa, Google Home, Apple Home, and Samsung SmartThings. Updates to the standard expand supported device types and improve commissioning, security, reliability, energy management, and multi-ecosystem operation. Device makers should confirm which Matter features their target ecosystems support because platforms might adopt new capabilities at different times. For current version and release information, see Matter specifications on the CSA website.

This guide provides device makers an overview of Matter and the steps required to become Matter-compliant. It outlines advantages and disadvantages to consider when planning a Matter adoption strategy. The guide also suggests best practices for using Matter while continuing to support existing wireless protocols in phases. If you are an IoT device manufacturer exploring smart-home solutions, this guide can inform your connectivity strategy.
